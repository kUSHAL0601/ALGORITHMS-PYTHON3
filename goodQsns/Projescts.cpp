#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int l=1;l<=t;l++)
	{
		int n,m;
		cin>>n;
		cin>>m;
		unordered_multimap<char, char> mp;
		for(int i=0;i<n;i++)
		{
			char x,y;
			cin>>x;
			cin>>y;
			mp.insert(make_pair(y,x));
		}
		vector<char> v(m);
		for(int i=0;i<m;i++)
			cin>>v[i];
		vector<char> ans;
		for(int i=0;i<v.size();i++)
		{
			char x=v[i];
			ans.push_back(x);
			while(mp.find(x) !=mp.end())
			{
				unordered_multimap<char, char> :: iterator it=mp.find(x);
				ans.push_back(it->second);
				x=it->second;
			}
		}
		sort(ans.begin(), ans.end());
		for(int i=0;i<ans.size();i++)
			cout<<ans[i]<<", ";
		cout<<"\n";
	}
}