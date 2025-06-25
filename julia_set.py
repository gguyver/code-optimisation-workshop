from line_profiler import profile
CONSTVAL = complex(-0.62772, -0.42193)

@profile
def calc_z_serial_python(maxiter, zs, c):
  #' Calculate the Julia set for a given set of complex numbers and a constant c.
  output = [0] * len(zs)
  for i in range(len(zs)):
    z = zs[i]
    n = 0
    while abs(z) <= 2 and n < maxiter:
      z = z * z + c
      n += 1
    output[i] = n
  return output

def calc_complex_numbers(x1, x2, y1, y2, desired_width):
  #' Generate complex numbers to use for the Julia set.
  #' Returns a list of complex numbers and their corresponding constants.
  xstep = (x2 - x1) / desired_width
  ystep = (y1 - y2) / desired_width
  x = []
  y = []
  ycoord = y2
  while ycoord > y1:
    y.append(ycoord)
    ycoord += ystep
  xcoord = x1
  while xcoord < x2:
    x.append(xcoord)
    xcoord += xstep
  zs = []
  cs = []
  for ycoord in y:
      for xcoord in x:
        zs.append(complex(xcoord, ycoord))
  return zs

def run_julia_set(desired_width, max_iterations):
  #' Run the Julia set calculation and return the results.
  print(f"Generating complex numbers to calculate Julia set")
  zs = calc_complex_numbers(-1.8, 1.8, -1.8, 1.8, desired_width)
  print(f"Length of zs: {len(zs)}")
  output = calc_z_serial_python(max_iterations, zs, CONSTVAL)
  
  # expected output sum with max_iterations=300, desired_width=1000
  assert(sum(output) == 33219980), "Output sum does not match expected value."

def visualise_julia_set(desired_width, max_iterations):
  #' Visualise the Julia set using matplotlib.
  import matplotlib.pyplot as plt
  zs = calc_complex_numbers(-1.8, 1.8, -1.8, 1.8, desired_width, max_iterations)
  output = calc_z_serial_python(max_iterations, zs, CONSTVAL)
  
  plt.imshow([output[i:i + desired_width] for i in range(0, len(output), desired_width)], extent=(-1.8, 1.8, -1.8, 1.8), cmap='hot')
  plt.colorbar()
  plt.title('Julia Set')
  plt.show()

if __name__ == "__main__":
  run_julia_set(desired_width = 1000, max_iterations = 300)