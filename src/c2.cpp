// C와 공통점

// #1. 변수의 정의
// 변수 정의
// 변수명은 알파벳, '_', 숫자들로만 사용
// 이름 가장 앞 부분에 숫자는 오면 안됨
// 이름으로 구분할 수 있어야됨, 길더라도 확실하게 이해할 수 있게 짓자
// 모든 변수는 '_'로, 함수이름은 대문자로 띄어쓰기를 구분하자

// #include <iostream>
// int main() {
//     int i;
//     char c;
//     double d;
//     float f;

//     return 0;
// }

// #2. 포인터의 정의
// #include <iostream>
// int main(){
//     int arr[10];
//     int *parr = arr;

//     int i;
//     int *pi = &i;

//     return 0;
// }

// #3. for 문
// #include <iostream>

// int main(){
//     int i, sum = 0;
//     for (i = 1; i <= 10; i++){
//         sum += i;
//     }

//     std::cout << "합은 : " << sum << std::endl;

//     return 0;
// }

// #4. while 문
// #include <iostream>

// int main(){
//     int i = 1, sum = 0;
//     while(i<= 10){
//         sum += i;
//         i++;
//     }

//     std::cout << "합은 : " << sum << std::endl;
//     return 0;
// }

// #5. if-else 문
// #include <iostream>

// int main(){
//     int lucky_num = 3;
//     std::cout << "내 비밀 수를 맞춰 봐" << std::endl;

//     int user_input;

//     while(1){
//         std::cout << "입력 : ";
//         std::cin >> user_input;
//         if (lucky_num == user_input) {
//             std::cout << "맞추셨습니다~.~" << std::endl;
//             break;
//         } else {
//             std::cout << "다시 생각해보세요~" << std::endl;
//         }
//     }
//     return 0;
// }

// #6. switch문
#include <iostream>

using std::cout;
using std::endl;
using std::cin;

int main(){
    int user_input;
    cout << "저의 정보를 표시해줍니다" << endl;
    cout << "1. 이름 " << endl;
    cout << "2. 나이 " << endl;
    cout << "3. 성별 " << endl;
    cin >> user_input;

    switch(user_input){
        case 1:
            cout << "Psi ! " << endl;
            break;

        case 2:
            cout << "99 살" << endl;
            break;
        
        case 3:
            cout << "남자" << endl;
            break;
        
        default:
            cout << "궁금한게 없군요~" << endl;
            break;
    }
    return 0;
}
