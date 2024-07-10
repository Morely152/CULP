#include <stdio.h>  //包含标准输入输出的头文件
#include <stdlib.h> //包含用于生成随机数的rand()函数的头文件
#include <stdbool.h> //包含布尔型的头文件

int main(void)
{
    int m,adds,price_0; //只涉及整数运算，声明整型的变量（下同）
    int i = 1;
    int n = 0;
    bool p_continue;  //p_continue的值为True或False，因此使用布尔型的变量
    
    printf("叫卖人数:");   scanf("%d",&m);
    
    while (i <= m) {
        printf("\n\n第%d位客人开始叫卖，底价为40\n",i);
        
        price_0 = 40;
        p_continue = true;
        
        while (p_continue) {  //目前还没学到C语言函数的声明和调用，直接写到一起…
            adds = rand()%10;
            
            if (adds <=6)
                price_0 += 10;
            else 
                price_0 += 20;
            printf("  抽到了%d，价格变为%d\n",adds,price_0);
            
            if (price_0 == 150) {
                printf("  这位客人叫卖成功\n");
                n += 1;
                p_continue = false;
            }
            else if (price_0 >= 150) {
                printf("  这位客人叫卖失败\n");
                p_continue = false;
            }
        }
        i += 1;
    }
    printf("\n\n一共有%d位客人进行叫卖，其中%d人叫卖成功，成交率为%.2f\n",m,n,(double)n / m);
    
    return 0;
    
}
