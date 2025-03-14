#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *arquivo = fopen("message.txt.cz", "rb");
    char output[25600];
    for(int i = 0; i < 256; output[i] = '\0', ++i);
    for(int i = 0; i < 255; ++i) {
        long long int size = 0;
        fread(&size, sizeof(long long int), 1, arquivo);
        for(int j = 0; j < size; ++j) {
            long long indice;
            fread(&indice, sizeof(long long int), 1, arquivo);
            output[indice] = (char)i;

        }
    }
    fclose(arquivo);
    printf("%s\n", output);
    return 0;
}
