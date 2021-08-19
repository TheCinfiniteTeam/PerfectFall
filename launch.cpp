#include <iostream>
#include <cstdlib>
#include <ctime>
#include <fstream>
#ifdef __WIN32__
#include <direct.h>
#endif


void forWindows();

void forOther();

using namespace std;
void Delay(int time){
    clock_t now = clock();
    while(clock() - now < time);
}
int main() {
#ifdef __WIN32__
    forWindows();
#else
    forOther();
#endif
    return 0;
}

void forWindows() {
    std::cout << "Welcome to the Perfect Fall" << std::endl;
    Delay(2.5*1000);
    system("cls");
    ifstream inFile("./logo.txt");
    string logoline;
    while (inFile.good()){
        getline(inFile, logoline);
        std::cout << logoline << std::endl;
    }
    Delay(2.5*1000);
    char *charPath;
    string proName;
    proName = "PerfectFall.exe";
    if ((charPath = getcwd(NULL, 0)) == NULL){
        std::cout << "\"" << proName << "\"" << std::endl;
        system(proName.data());
    }else{
        std::cout << "\"" << charPath << "\\" << "PerfectFall.exe" << "\"" << std::endl;
        string path;
        path.append(charPath);
        path.append("\\");
        path.append(proName);
        system(path.data());
    }
    delete charPath;
    charPath = NULL;
}

void forOther() {
    std::cout << "Sorry, You System Can't support" << std::endl;
}