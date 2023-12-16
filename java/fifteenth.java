public class fifteenth{
    public static void main(String[] args){
        long matrix[][] = new long[21][21];
        
        for(int i = 0; i < 21; i++){
            matrix[20][i] = 1L;
            matrix[i][20] = 1L;
        }

        for(int i = 19; i >= 0; i--){
            for(int j = 19; j >= 0; j--)
                matrix[i][j] = matrix[i+1][j] + matrix[i][j+1];
        }

        for(int i = 0; i < 21; i++){
            System.out.print("|");
            for(int j = 0; j < 21; j++)
                System.out.printf("%12d|", matrix[i][j]);
            System.out.println();
        }
        System.out.println(matrix[0][0]);
    }
}