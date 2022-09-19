class Solution{
    
public:

bool isIsomorphic(string s, string t) {
    
     if(s.size() != t.size())
     
        return false;
    
     map<char, char>  storage;

     
     std::map<char,char>::iterator it;
     
     for (int i = 0; i < s.size(); i++) {
         
         char first = s[i];
         
         char second = t[i];
         
         it = storage.find(first);
         
         if (it != storage.end()) {
             
             if (it->second != second)
             
                return false;
            
         } else {
             for (it = storage.begin(); it != storage.end(); ++it )
             
                 if (it->second == second)
             
                     return false;
                    
                 storage[first] = second;
         }
    }
    
    return true;
}

};
