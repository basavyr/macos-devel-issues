# Development issues - macOS 
Issues and their solutions (*if any*) that are encountered in a predominantly `C++` oriented development workflow on macOS. 
The solutions for each of the issues are presented in separate documents, together with the documentation that helped into fixing that particular issue.
The repository also contains various files that are required for fixing certain issues. 

Thank you to all the development communities (e.g. [Stack Overflow](https://stackoverflow.com/questions]),[GitHub](https://github.com/) and many more) that have solutions for most of the issues. Even if the solution to a particular issue is missing, a *piece-by-piece* puzzle building procedure can be applied, which will result in eventually getting the problem to stop.


**Disclaimer**: I do not own any rights on this documentation. Everything that is contained in this repository was put together from *open-access* communities and *open-source* official documentation of the respective packages that were used here.

**Important aspects** (to take into consideration if one decides to try these fixes)

* They were all tried/tested on a MacBookPro with at least macOS 10.15 (Catalina)
* The earliest version of XCode which this machine had installed was `11.3`
* The earliest version for the Command Line Tools which was installed on the machine was 11.3
* Compilation of `C++` sources was done with the `clang` compiler that comes with XCode (no additional compiler(s) was(were) installed)
