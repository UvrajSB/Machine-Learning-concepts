# pReLU
What if we can learn that small value during training so that our activation function can better adapt to the other parameters (like weights and biases). This is where PReLU comes in. We can learn the slope parameter using backpropagation at a negligible increase in the cost of training.
## Function
$$
   F(x) = x,\quad x  > 0
$$
$$
	= \alpha( x),\quad  x\leq0
$$
## Graph

![Graph of pReLU](https://github.com/UvrajSB/Machine-Learning-concepts/blob/main/non-linearities/pReLU/pReLU.png)
