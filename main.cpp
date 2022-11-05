// Water usage tracker
// Chris Woo, Justin Jiang, Mark Soliman, Terry Chen
// CutieHack project for sustainability

#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main(){
    const int avgGal = 60;

    ifstream fin;
    fin.open("water.txt");

    if(!fin.is_open()){
        cout << "Error opening file" << endl;
        return 1;
    }

    vector<string> waterUsage;
    vector<int> times;
    string type;
    int amount;

    while(fin >> type){
        fin >> amount;
        waterUsage.push_back(type);
        times.push_back(amount);
    }

    // check if vectors are filled correctly
    // for(unsigned i = 0; i < waterUsage.size(); i++){
    //     cout << waterUsage.at(i) << " ";
    //     cout << times.at(i) << endl;
    // }

    double totalGal = 0;
    for(unsigned  i = 0; i < waterUsage.size(); i++){
        if(i == 0){
            totalGal += times.at(i) * 1.6;
            cout << waterUsage.at(i) << ": " << times.at(i) << " times" << endl;
        }
        if(i == 1){
            totalGal += times.at(i) * 0.1320312;
            cout << waterUsage.at(i) << ": " << times.at(i) << " times" << endl;
        }
        if(i == 2){
            totalGal += times.at(i) * 17;
            cout << waterUsage.at(i) << ": " << times.at(i) << " times" << endl;
        }
        if(i == 3){
            totalGal += times.at(i) * 0.22;
            cout << waterUsage.at(i) << ": " << times.at(i) << " times" << endl;
        }
        if(i == 4){
            totalGal += times.at(i) * 6;
            cout << waterUsage.at(i) << ": " << times.at(i) << " times" << endl;
        }

        if(i == 5){
            totalGal += times.at(i) * 62.3; //fix value
            cout << waterUsage.at(i) << ": " << times.at(i) << " times" << endl;
        }
        if(i == 6){
            totalGal += times.at(i) * 20; //fix value
            cout << waterUsage.at(i) << ": " << times.at(i) << " times" << endl;
        }
    }


    cout << "\nYou used a total of " << totalGal << " gallons" << endl;
    cout << "The average amount of water an American uses daily is " << avgGal << endl;
    if(avgGal < totalGal){
        cout << "Try to lower your water usage." << endl;
    }
    else{
        cout << "You used less than the average." << endl;
    }

    fin.close();
}
