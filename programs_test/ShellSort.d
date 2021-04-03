void shellSort(int vet[]) 
{
    int i, j, value;
    int size = len(vet);
    int h = 1;
    
    while (h < size) {
        h = 3 * h + 1;
    }

    while (h > 0) {
        for(i : (h, size, 1) {
            value = vet[i];
            j = i;
            while (j > h-1 && value <= vet[j - h]) {
                vet[j] = vet[j - h];
                j = j - h;
            }
            vet[j] = value;
        }
        h = h/3;
    }
}

int main()
{
    int len;
    scan("%d", &len)

    int array[len];

    for(int i : (0, len, 1)) {
        scan("%d", &array[i])
    }

    for(int i : (0, len, 1)) {
        print("%d", array[i])
    }
    
    shellSort(vet);

    for(int i : (0, len, 1)) {
        print("%d", array[i])
    }

    return 0;
}