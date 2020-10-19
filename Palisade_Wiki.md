# 欢迎访问Palisade 的Wiki（维基百科）

#### 本页面由陈智罡博士负责翻译更新维护

#### Palisade是一个开源项目。 我们很荣幸的宣布，我们正在接受NumFOCUS.org（专注于开源数据科学软件的非营利基金会）资助。 请参阅我们的PALISADE管理文档，以获取各个PALISADE团队及 其职责的列表。 另请参阅我们制定的行为准则，以了解我们的贡献者和维护者的责任。

#### 该Wiki是服务用户使用PALISADE库的信息汇总。我们欢迎您通过社区提供其他相关材料。如果有任何建议，建议的文档或者类似的建议相关内容，请发送至如下地址：
#### ·PALISADE项目 contact@palisade-crypto.org 
#### 或者
#### ·PALISADE项目负责人: 
#### 　　　　o Kurt Rohloff ：  krohloff@dualitytech.com, rohloff@njit.edu 
#### 　　　　o Yuriy Polyakov： ypolyakov@dualitytech.com 
#### 　　　　o Dave Cousins：  dcousins@njit.edu, dcousins@dualitytech.com


## PALISADE介绍


### PALISADE是一个通用的格密码库，目前包含以下格密码算法的有效实现：
#### ·全同态加密（FHE），包含如下方案 
#### 　·用于整数计算的Brakerski / Fan-Vercauteren（BFV）方案
#### 　·用于整数计算的Brakerski-Gentry-Vaikuntanathan（BGV）方案
#### 　·用于实数计算的Cheon-Kim-Kim-Song（CKKS）方案
#### 　·用于布尔电路计算的Ducas-Micciancio（FHEW）和Chillotti-Gama-Georgieva-Izabachene（TFHE）方案
#### 　·有限整数计算的Stehle-Steinfeld方案
#### ·多方全同态加密，包含如下方案 
#### 　·BGV，BFV和CKKS方案的门限FHE
#### 　·BGV，BFV和CKKS方案的代理重加密
#### ·数字签名
#### ·基于身份的加密
#### ·密文策略基于属性的加密

#### PALISADE是支持Linux，Windows和macOS的跨平台C ++ 11库。支持的编译器是g ++ v6.1或更高版本以及clang ++ v6.0或更高版本。

#### 该库还包括单元测试和示例应用程序演示。

#### PALISADE在BSD-2条款的许可下使用。

#### 该库基于模块化体系结构，包含如下各层：
#### ·数学运算层：支持一些基础计算，例如模算术，数论变换和整数采样。该层支持可移植到多种硬件计算框架下。
#### ·格运算层：支持格运算，环代数和格陷门采样。
#### ·加密层：包含各类格密码方案的有效实现。
#### ·编码层：为各种加密方案提供多种明文编码。
#### PALISADE的重点在于方案的可用性。例如，所有带有密文打包的FHE方案都使用相同的通用API，并使用运行时多态性实现。

#### PALISADE有效实现了的余数系统（RNS）算法，从而大幅提高BGV，BFV和CKKS等方案的性能。PALISADE库被用作全基因组关联研究（GWAS）解决方案的库，在iDASH'18比赛上获奖。

#### 默认情况下，该库的构建没有外部依赖关系。但是如果需要，可以为用户提供添加GMP / NTL和/或tcmalloc（线程敏感内存分配）第三方库的选项。


## PALISADE入门

#### 为了熟悉PALISADE，我们建议您阅读以下Wiki文章：
#### 1.安装方法（不依赖于操作系统）
#### 　(1)在Linux上安装PALISADE 
#### 　(2)在Windows上安装PALISADE  
#### 　(3)在macOS上安装PALISADE 
#### 　(4)使用CMake/make自定义安装
#### 2.在PALISADE库上建立C++项目的方法 
#### 3.介绍PALISADE库的目录结构 
#### 4.使用PALISADE库 

#### 为了熟悉PALISADE的主要API，我们建议您查看以下示例的代码：
#### 1.用于整数运算（BFV）的全同态加密：
#### 　(1)[简单代码示例][1] 
[1]: https://gitlab.com/palisade/palisade-development/blob/master/src/pke/examples/simple-integers.cpp
#### 　(2)[带有序列化的简单代码示例][2]
[2]: https://gitlab.com/palisade/palisade-development/blob/master/src/pke/examples/simple-integers-serial.cpp
#### 2.用于整数运算（BGV）的全同态加密： 
#### 　(1)[简单代码示例][3]
[3]: https://gitlab.com/palisade/palisade-development/blob/master/src/pke/examples/simple-integers-bgvrns.cpp
#### 　(2)[带有序列化的简单代码示例][4]
[4]: https://gitlab.com/palisade/palisade-development/blob/master/src/pke/examples/simple-integers-serial-bgvrns.cpp
#### 3.用于实数运算（CKKS）的全同态加密： 
#### 　(3)[简单代码示例][5]
[5]: https://gitlab.com/palisade/palisade-development/blob/master/src/pke/examples/simple-real-numbers.cpp
#### 　(4)[高级代码示例][6]
[6]: https://gitlab.com/palisade/palisade-development/blob/master/src/pke/examples/advanced-real-numbers.cpp
#### 4.布尔电路的全同态加密（FHEW / TFHE）： 
#### 　(5)[简单代码示例][7]
[7]: https://gitlab.com/palisade/palisade-development/blob/master/src/binfhe/examples/boolean.cpp
#### 　(6)[JSON序列化代码][8]
[8]: https://gitlab.com/palisade/palisade-development/blob/master/src/binfhe/examples/boolean-serial-json.cpp
#### 　(7)[二进制序列化代码][9]
[9]: https://gitlab.com/palisade/palisade-development/blob/master/src/binfhe/examples/boolean-serial-binary.cpp
#### 5.门限全同态加密： 
#### 　(1)[BGV，BFV和CKKS的代码示例][10]
[10]: https://gitlab.com/palisade/palisade-development/blob/master/src/pke/examples/threshold-fhe.cpp

## 更多文档
### 对PALISADE目录中的文件和README.md文件的说明：
#### 1.[PALISADE User Manual（PALISADE使用手册）][11] 包含有关PALISADE库以及如何在应用程序中使用它的详细说明
[11]:https://gitlab.com/palisade/palisade-development/blob/master/doc/palisade_manual.pdf
#### 2.[PALISADE Webinars（PALISADE研讨会）][12] --YouTube视频（每月录制），介绍和讨论有关PALISADE，同态加密以及同态加密的应用的最新新闻
[12]:https://palisade-crypto.org/webinars
#### 3.[PALISADE API（PALISADE库的API接口）][13]--使用Doxygen自动生成的API文档
[13]:https://palisade.gitlab.io/palisade-development/classes.html
#### 4.[PALISADE Release Notes（PALISADE版本更新）][14] 是每个版本的更新，包括大的更新和小的更新
[14]:https://gitlab.com/palisade/palisade-development/blob/master/Release_Notes.md
#### 5.[Benchmarking PALISADE code（基准测试代码）][15] --在benchmark目录中
[15]:https://gitlab.com/palisade/palisade-development/-/blob/master/benchmark/src/README.md
#### 6.[Example Programs for the Public Key Encryption (PKE) Module（公钥加密模块的示例程序）][16] 在src/pke/examples目录下
[16]:https://gitlab.com/palisade/palisade-development/blob/master/src/pke/examples/README.md
#### 7.[The Palisade Lattice Layer（格密码层）][17] 在src/core/include/lattice目录
[17]:https://gitlab.com/palisade/palisade-development/blob/master/src/core/include/lattice/README.md
#### 8.[Various Mathematical Backends for Multiprecision Arithmetic（支持多精度算术的各种数学后端）][18] 在src/core/include/math目录下
[18]:https://gitlab.com/palisade/palisade-development/blob/master/src/core/include/math/README.md
#### 9.[Discrete Gaussian Sampling implemented in PALISADE（PALISADE中的离散高斯取样实现）][19]在src/core/include/math目下
[19]:https://gitlab.com/palisade/palisade-development/blob/master/src/core/include/math/SAMPLING_README.md
### 在doc/wiki目录下的Wiki页面 
#### 1.This [Home page][20] （首页）
[20]:https://gitlab.com/palisade/palisade-development/-/wikis/Home
#### 2.[Publications on Lattice Crypto Scheme Implementations in PALISADE][21]（关于格密码方案实现的相关出版物）
[21]:https://gitlab.com/palisade/palisade-development/-/wikis/Publications
#### 3.[Known Issues][22] （已知的问题）
[22]:https://gitlab.com/palisade/palisade-development/-/wikis/Known-Issues
#### 4.[CI Documentation][23]（CI文档）
[23]:https://gitlab.com/palisade/palisade-development/-/wikis/CI-Documentation
#### 5.[Exception Handling][24]（异常处理）
[24]:https://gitlab.com/palisade/palisade-development/-/wikis/Palisade-Exceptions
#### 6.[Frequently Asked Questions][25]（经常被问到的问题）
[25]:https://gitlab.com/palisade/palisade-development/-/wikis/Frequently-Asked-Questions
#### 7.[How To Rebase a Feature Branch from the Master Branch][26]（如何从主分支建立一个功能分支）
[26]:https://gitlab.com/palisade/palisade-development/-/wikis/How-to-rebase-your-branch-from-the-master-branch

## 修改和改进PALISADE

#### 我们鼓励您对PALISADE进行修改和改进。请参阅Contributing.md文件，以了解有关遵循我们的主要和次要贡献过程的详细信息，以及有关我们编程风格要求的讨论。[Contributing.md][27]。
[27]:https://gitlab.com/palisade/palisade-development/blob/master/Contributing.md
#### 　·如果您计划对PALISADE进行重大修改，请先与我们联系，因为PALISADE正在开发中。这样，您可以确保添加的内容与计划的PALISADE版本保持一致。它还将确保您所做的更改基于开发库的#### 最新版本。
#### 　·[PALISADE][28]发行版本的所有新增内容均需获得PALISADE治理团队的批准，具体见PALISADE管理文档中的规定。
[28]:https://gitlab.com/palisade/palisade-development/blob/master/Governance.md
## 许可证信息

#### PALISADE库使用BSD-2条款许可，这使公司和其他组织更容易使用该软件并将其集成到产品中，而不必担心受到许可问题的阻碍。
#### 　·[可以在此处查看PALISADE许可证。][29]
[29]: https://gitlab.com/palisade/palisade-development/blob/master/License.md
## 感谢我们的贡献者
#### 在https://palisade-crypto.org/community/ 上有贡献或使用过PALISADE的组织和赞助PALISADE开发的组织的最新列表。
Contributors wiki article.提供了为PALISADE贡献代码或算法的核心成员和社区开发人员的最新列表。


## 如何引用PALISADE

#### 要在学术论文中引用PALISADE，请使用以下BibTeX条目。如果使用其他（旧）版本，请使用https://gitlab.com/palisade/palisade-development/blob/master/Release_Notes.md 中的日期去 更新发行版本和月份/年份。

 


## 经常问的问题
#### 请参阅“ PALISADE[常见问题解答][30]”页面，以获取常见问题和解决方案的列表。
[30]: https://gitlab.com/palisade/palisade-development/-/wikis/Frequently-Asked-Questions
