from  torch import tensor
#create tensor
x = tensor(3.)
w = tensor(4., requires_grad=True)
b = tensor(5., requires_grad=True)
x, w, b
# here is the result
#(tensor(3.), tensor(4., requires_grad=True),
# tensor(5., requires_grad=True))

#Arithmetic operations
y = w * x + b

#compute derivatives
y.backward()

#The derivates of y w.r.t the input tensors are stored in
# the .grad property of the respective tensors

#gradient
print('dy/dx:', x.grad)
print('dy/dw:', w.grad)
print('dy/db:', b.grad)