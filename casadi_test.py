import casadi as ca


print("Hello, CasADi!")
print("CasADi version:", ca.__version__)



# Define a scalar variable
x = ca.MX.sym('x')
print("x:", x)

