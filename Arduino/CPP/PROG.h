#include <iostream>

using namespace std;

//Declare a class
/*
class className
   {
   //some private data & function 
   //some public data & function
   };
   */
   
//===================================================   
   class test
   {
       private:
       int tag1;
       float tag2;
       
       public:
       void fun1()
       {
           tag1=2;
           tag2=3.1;
       }
       float fun2();
       
   };
   
   float test::fun2()
   {
    
    return float(tag1)*tag2;
    
   }
   
//=====================================================

// class=====================
class box
{
    public:
    float Height;
    float Length;
    float Width;
    float getVolume(void);
    float getSurfaceArea(void);//Outside surface area
};

float box::getVolume(void)
{
    return Height*Length*Width;
}

float box::getSurfaceArea(void)
{
    return (2*(Height*Width)+2*(Height*Length)+2*(Width*Length));
}
int main()
{
    box b1;
    b1.Height=1;
    b1.Length=2;
    b1.Width=3;
    
    cout <<" volume of Box=" <<b1.getVolume();
    cout <<" Surface Area=" <<b1.getSurfaceArea();
 
   
   return 0;
}