#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main(){
    ifstream fin;
    fin.open("carbon.txt");

    if(!fin.is_open()){
        cout << "Error opening file" << endl;
    }


    vector<string> name;
    vector<int> emission;
    string item;
    int carbon;



    while(fin >> item){
        name.push_back(item);
        fin>>carbon;
        emission.push_back(carbon);
    }

    // for(unsigned i = 0; i < name.size(); i++){
    //     cout << name.at(i) << " " ;
    //     cout << emission.at(i) << endl;
    // }
    fin.close();

    cout << "Daily Carbon Emission Program" << endl;
    cout << "What have you used today" << endl;

    int totalEmission = 0;
    string input;

    while(input != "q"){
        for(unsigned i = 0; i < name.size(); i++){
            if(input == name.at(i)){
                totalEmission += emission.at(i);
            }
        }
        cin >> input; 
        cout << "Your current total carbon emission is: " << totalEmission << endl;
    }

    

}