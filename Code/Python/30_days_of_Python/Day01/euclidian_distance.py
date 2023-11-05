from math import sqrt

def calculate_euclidaian_distace(x1 ,y1, x2, y2):
    co_oridant_x = (x1-x2)
    co_oridante_y = (y1-y2)

    return sqrt(pow(co_oridant_x,2) + pow(co_oridante_y,2))


def main():
    print(calculate_euclidaian_distace(2,3,10,8))

if __name__ == "__main__":
    main()
