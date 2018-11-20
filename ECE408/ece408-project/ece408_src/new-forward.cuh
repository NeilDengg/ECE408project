
#ifndef MXNET_OPERATOR_NEW_FORWARD_CUH_
#define MXNET_OPERATOR_NEW_FORWARD_CUH_

#include <mxnet/base.h>

#define TILE_SIZE 32
#define MASK_WIDTH 5
namespace mxnet
{
namespace op
{

__global__ void forward_kernel(float *y, const float *x, const float *k, const int B, const int M, const int C, const int H, const int W, const int K, const int W_SIZE)
{

    /*
    Modify this function to implement the forward pass described in Chapter 16.
    We have added an additional dimension to the tensors to support an entire mini-batch
    The goal here is to be correct AND fast.
    We have some nice #defs for you below to simplify indexing. Feel free to use them, or create your own.
    */

    const int H_out = H - K + 1;
    const int W_out = W - K + 1;
    (void)H_out; // silence declared but never referenced warning. remove this line when you start working
    (void)W_out; // silence declared but never referenced warning. remove this line when you start working

// An example use of these macros:
// float a = y4d(0,0,0,0)
// y4d(0,0,0,0) = a
#define y4d(i3, i2, i1, i0) y[(i3) * (M * H_out * W_out) + (i2) * (H_out * W_out) + (i1) * (W_out) + i0]
#define x4d(i3, i2, i1, i0) x[(i3) * (C * H * W) + (i2) * (H * W) + (i1) * (W) + i0]
#define k4d(i3, i2, i1, i0) k[(i3) * (C * K * K) + (i2) * (K * K) + (i1) * (K) + i0]
    int IN_TILE_WIDTH=TILE_SIZE+K-1;
    __shared__ float input_tile[IN_TILE_WIDTH][IN_TILE_WIDTH];
    __shared__ float m_tile[5][5];
    int b = blockIdx.x;
    int m = blockIdx.y;
    int tb= threadIdx.x;
    int tm= threadIdx.y;
    int hbase = (blockIdx.z / W_SIZE) * TILE_SIZE;
    int wbase = (blockIdx.z % W_SIZE) * TILE_SIZE; 
    int h = threadIdx.y + hbase;
    int w = threadIdx.x + wbase;
    double acc = 0.0;
    for(int c = 0; c < C; c++){
    	if(tb < K && tm < K)
    		m_tile[tb][tm]=k4d(m,c,tb,tm);
    }
    __syncthreads();
    for(int i=h;i<hbase+IN_TILE_WIDTH;i+=TILE_SIZE)
    	for(int j=w;j<w_base+IN_TILE_WIDTH;j+=TILE_SIZE)
    		input_tile[i-hbase][j-wbase]=x4d(b,c,i,j);
    __syncthreads();
    for(int p = 0; p < K; p++){
 	    for(int q = 0; q < K; q++){
	    	if(h + p < H && w + q < W){
	             acc += input_tile[tm+p][tb+q] * m_tile[p][q];
			}
	    }
	}
    if(b < B && m < M && h < H_out && w < W_out){
    	 y4d(b,m,h,w) = acc;
    }
#undef y4d
#undef x4d
#undef k4d
}

/* 
   This function is called by new-inl.h
   Any code you write should be executed by this function.
   For ECE408, we only expect the float version of the operator to be called, so here we specialize with only floats.
*/
template <>
void forward<gpu, float>(mshadow::Tensor<gpu, 4, float> &y, const mshadow::Tensor<gpu, 4, float> &x, const mshadow::Tensor<gpu, 4, float> &w)
{
    // Use mxnet's CHECK_EQ to do assertions.
    // Remove this assertion when you do your implementation!
    

    // Extract the tensor dimensions into B,M,C,H,W,K
    const int B = x.shape_[0];
    const int M = y.shape_[1];
    const int H = x.shape_[2];
    const int W = x.shape_[3];
    const int K = w.shape_[3];
    const int C = x.shape_[1];
    const int H_out = H - K + 1;
    const int W_out = W - K + 1;

    
    // Set the kernel dimensions
    const int W_SIZE = ceil(W_out*1.0 / TILE_SIZE);
    const int H_SIZE = ceil(H_out*1.0 / TILE_SIZE);
    const int Z = W_SIZE * H_SIZE;

    dim3 DimGrid(B, M, Z);

    dim3 DimBlock(TILE_SIZE, TILE_SIZE, 1);
    // Call the kernel
    cudaStream_t s = y.stream_->stream_;	
    forward_kernel<<<DimGrid, DimBlock, 0, s>>>(y.dptr_, x.dptr_, w.dptr_, B, M, C, H, W, K, W_SIZE);

    // Use MSHADOW_CUDA_CALL to check for CUDA runtime errors.
    MSHADOW_CUDA_CALL(cudaDeviceSynchronize());

}

/* 
    This tells mxnet how to do an op when it's not a float.
    This is not used in the ECE408 project
*/
template <typename gpu, typename DType>
void forward(mshadow::Tensor<gpu, 4, DType> &y, const mshadow::Tensor<gpu, 4, DType> &x, const mshadow::Tensor<gpu, 4, DType> &w)
{
    CHECK_EQ(0,1) << "Remove this line and replace it with your implementation.";
}
}
}

#endif
