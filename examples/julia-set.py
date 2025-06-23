import time

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

def calc_complex_numbers(x1, x2, y1, y2, desired_width, max_iterations):
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
  zs = calc_complex_numbers(-1.8, 1.8, -1.8, 1.8, desired_width, max_iterations)
  print(f"Length of zs: {len(zs)}")
  start_time = time.time()
  output = calc_z_serial_python(max_iterations, zs, complex(-0.62772, -0.42193))
  end_time = time.time()
  print(f"{calc_z_serial_python.__name__} took {end_time - start_time:.2f} seconds")

  # expected output sum with max_iterations=300, desired_width=1000
  assert(sum(output) == 33219980), "Output sum does not match expected value."



if __name__ == "__main__":
  run_julia_set(desired_width = 1000, max_iterations = 300)