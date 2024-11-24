#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <time.h>
#include <array>
#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#define LENGTH 15
#define WIDTH  80
#define LIVE  '*'
#define DEATH ' '
typedef std::array<std::array<char,WIDTH>,LENGTH> WorldMat;

inline void delay_ms(int ms) {
#ifdef _WIN32
    Sleep(ms); // Windows 平台
#else
    usleep(ms * 1000); // Linux/macOS 平台
#endif
}

class Universe {
public:
	Universe() {
		world = new WorldMat;
		(*world)[0].fill(DEATH);
		this->world->fill((*world)[0]);
		this->NullLocation = DEATH;
	}
	~Universe() {
		delete world;
	}
	std::array<char,WIDTH>& operator[] (int x) {
		assert(x>=0 && x<LENGTH);
		return (*world)[x];
	}
	void Show() const {
		for(int i=0;i<LENGTH;i++) {
			for(int j=0;j<WIDTH;j++) 
				printf("%c",(*world)[i][j]);
			printf("\n");
		}
	}
	void Seed() {
		srand(time(0));
		for(int i=0;i<LENGTH;i++)
		for(int j=0;j<WIDTH;j++) 
			if(rand()*4 < RAND_MAX)
				(*world)[i][j] = LIVE;
	}
	void Alive() {
		WorldMat* nworld = new WorldMat;
		for(int i=0;i<LENGTH;i++)
		for(int j=0;j<WIDTH;j++) {
			int s = 0;
			if((*world)[i+1][j  ] == LIVE) s++;
			if((*world)[i-1][j  ] == LIVE) s++;
			if((*world)[i  ][j+1] == LIVE) s++;
			if((*world)[i  ][j-1] == LIVE) s++;
			if((*world)[i+1][j+1] == LIVE) s++;
			if((*world)[i+1][j-1] == LIVE) s++;
			if((*world)[i-1][j+1] == LIVE) s++;
			if((*world)[i-1][j-1] == LIVE) s++;
			if ((*world)[i][j] == LIVE) {
				if (s < 2 || s > 3) (*nworld)[i][j] = DEATH;
				else (*nworld)[i][j] = LIVE;
			} else {
				if (s == 3) (*nworld)[i][j] = LIVE;
				else (*nworld)[i][j] = DEATH;
			}
		}
		delete world;
		world = nworld;
	}
protected:
	WorldMat* world;
	char& loc(int x, int y) {
		if(x>=LENGTH || x<0) return this->NullLocation;
		if(y>=WIDTH  || y<0) return this->NullLocation;
		return (*(this->world))[x][y];
	}
	char NullLocation;
};

int main() {
	Universe universe;
	universe.Seed();
	
	while(1) {
		printf("\033[H");
		universe.Alive();
		universe.Show();
		delay_ms(200);
	}
	printf("Done\n");
}