Measures, Integrals & Martingales
(2nd edition)
Cambridge University Press, Cambridge 2017
ISBN: 9781316620243
Solution Manual
René L. Schilling
Dresden, May 2017
corrected & updated 18th July 2019

R.L. Schilling: Measures, Integrals & Martingales
Acknowledgement. I am grateful for the help of Dr. Franziska Kühn in the preparation of this solution
manual. Dr. Björn Böttcher, Dr. Julian Hollender and Dr. Franziska Kühn contributed problems and
solutions to this collection. Max Ziegenbalg helped to improve the solutions.
Dresden, Mai 2017 René Schilling
2

Contents
1 Prologue.
Solutions to Problems 1.11.5 7
2 The pleasures of counting.
Solutions to Problems 2.12.22 9
3 -Algebras.
Solutions to Problems 3.13.16 21
4 Measures.
Solutions to Problems 4.14.22 31
5 Uniqueness of measures.
Solutions to Problems 5.15.13 49
6 Existence of measures.
Solutions to Problems 6.16.14 59
7 Measurable mappings.
Solutions to Problems 7.17.13 73
8 Measurable functions.
Solutions to Problems 8.18.26 81
9 Integration of positive functions.
Solutions to Problems 9.19.14 95
10 Integrals of measurable functions.
Solutions to Problems 10.110.9 103
11 Null sets and the `almost everywhere'.
Solutions to Problems 11.111.12 111
12 Convergence theorems and their applications.
Solutions to Problems 12.112.37 121
3

R.L. Schilling: Measures, Integrals & Martingales
13 The function spaces p.
Solutions to Problems 13.113.26 151
14 Product measures and Fubini's theorem.
Solutions to Problems 14.114.20 169
15 Integrals with respect to image measures.
Solutions to Problems 15.115.16 189
16 Integrals of images and Jacobi's transformation rule.
Solutions to Problems 16.116.12 201
17 Dense and determining sets.
Solutions to Problems 17.117.9 213
18 Hausdor measure.
Solutions to Problems 18.118.7 223
19 The Fourier transform.
Solutions to Problems 19.119.9 227
20 The RadonNikodým theorem.
Solutions to Problems 20.120.9 237
21 Riesz representation theorems.
Solutions to Problems 21.121.7 245
22 Uniform integrability and Vitali's convergence theorem.
Solutions to Problems 22.122.17 257
23 Martingales.
Solutions to Problems 23.123.16 273
24 Martingale convergence theorems.
Solutions to Problems 24.124.9 281
25 Martingales in action.
Solutions to Problems 25.125.15 289
26 Abstract Hilbert space.
Solutions to Problems 26.126.19 299
27 Conditional expectations.
Solutions to Problems 27.127.19 317
4

Solution Manual. Last update 18th July 2019
28 Orthonormal systems and their convergence behaviour.
Solutions to Problems 28.128.11 333
5



1 Prologue.
Solutions to Problems 1.11.5
Problem 1.1 Solution: Wehavetocalculatetheareaofanisoscelestriangleofside-length r, baseb,
heightℎand opening angle∶=2∕2j. From elementary geometry we know that
cos 
2 = ℎ
r and sin 
2 = b
2r
so that
area (triangle)= 1
2ℎb=r2cos 
2sin 
2 = r2
2 sin.
Since we havelim→0
sin
 =1 we ﬁnd
area (circle)= lim
j→∞
2j r2
2 sin 2
2j
=r2 lim
j→∞
sin 2
2j
2
2j
=r2
just as we had expected.
■■
Problem 1.2 Solution: By construction,
Cn+1=[0,1] ⧵
Hn+1˝
i=1
˝
t1,…,ti∈{0,2}
It1,…,ti
I
and each intervalIt1,…,ti has length2−i. We have used this when calculatingl(Cn+1)
l(Cn+1)= l[0,1]−2 0× 1
31 −21× 1
32 −⋯−2n× 1
3n+1
(note that we have removed2n intervals of length3−n−1). If we letn →∞, we get for all removed
intervals
l
H ∞˝
i=1
˝
t1,…,ti∈{0,2}
It1,…,ti
I
=
∞É
i=1
2i−1× 1
3i =1.
The last line requires-additivity. (Just in case: you will see in the next chapter that the number
of removed intervals is indeed countable).
■■
7

R.L. Schilling: Measures, Integrals & Martingales
Problem 1.3 Solution: We record the lenghts of the removed pieces in each step
1. In Step 1 we remove one(=2 0)piece of length1
2r;
2. In Step 2 we remove two(=2 1)pieces, each of length1
8r;
3. In Step 3 we remove four(=2 2)pieces, each of length1
32r;
n. In Stepnwe remove2n pieces, each of length1
22n−1r;
In each step we remove2n×2−2n+1×r=2 −n+1runits of length, i.e. we remove
∞É
n=1
r
2n−1 =r.
Thus,l(I)= l[0,1]− r=1− r.
This means that the modiﬁed Cantor set does have a length! Consequently it cannot be empty.
■■
Problem 1.4 Solution: In each step the total length is increased by the factor4∕3, since we remove
the middle interval (relative length1∕3) and replace it by two copies constituting the sides of an
equilateral triangle (relative length2∕3). Thus,
l(Kn)= 4
3×l(Kn−1)= ⋯=
4
3
n
l(K0)=
4
3
n
.
In particular,limn→∞l(Kn)=∞ .
Again-additivity comes in in the form of a limit (compare with Problem 1.2).
■■
Problem 1.5 Solution: Ineachstepthetotalareaisdecreasedbythefactor 3∕4,sinceweremovethe
middle triangle (relative area1∕4). Thus,
area(Sn)= 3
4×area(Sn−1)= ⋯=
3
4
n
area(S0)=
3
4
n
√
3
4 .
In particular, area(S)=lim n→∞area(Sn)=0 .
Again-additivity comes in in the form of a limit (compare with Problem 1.2). Notice thatS is
not empty as it contains the vertices of all black triangles (see ﬁgure) of each stage.
■■
8

2 The pleasures of counting.
Solutions to Problems 2.12.22
Problem 2.1 Solution:
(i) We have
x∈A ⧵B ⇐ ⇒x∈Aandx∉B
⇐ ⇒x∈Aandx∈Bc
⇐ ⇒x∈A∩Bc.
(ii) Using (i) and de Morgan’s laws (*) yields
(A ⧵B) ⧵C
(i)
=(A∩Bc)∩ Cc =A∩Bc∩Cc
=A∩(Bc∩Cc)
(∗)
= A∩(B∪C)c =A ⧵(B∪C).
(iii) Using (i), de Morgan’s laws (*) and the fact that(Cc)c =C gives
A ⧵(B ⧵C)
(i)
=A∩(B∩Cc)c
(∗)
= A∩(Bc∪C)
=(A∩Bc)∪( A∩C)
(i)
=(A ⧵B)∪( A∩C).
(iv) Using (i) and de Morgan’s laws (*) gives
A ⧵(B∩C)
(i)
=A∩(B∩C)c
(*)
= A∩(Bc∪Cc)
=(A∩Bc)∪( A∩Cc)
(i)
=(A ⧵B)∪( A ⧵C)
(v) Using (i) and de Morgan’s laws (*) gives
A ⧵(B∪C)
(i)
=A∩(B∪C)c
(*)
= A∩(Bc∩Cc)
=A∩Bc∩Cc
9

R.L. Schilling: Measures, Integrals & Martingales
=A∩Bc∩A∩Cc
(i)
=(A ⧵B)∩( A ⧵C)
(vi) By deﬁnition and the distributive laws for sets we ﬁnd
(A∪B) ⧵C =(A∪B)∩ Cc
=(A∩Cc)∪( B∩Cc)
=(A ⧵C)∪( B ⧵C).
■■
Problem 2.2 Solution: Observe, ﬁrst of all, that
A ⧵C ⊂(A ⧵B)∪( B ⧵C). (*)
This follows easily from
A ⧵C =(A ⧵C)∩ X
=(A∩Cc)∩( B∪Bc)
=(A∩Cc∩B)∪( A∩Cc∩Bc)
⊂(B∩Cc)∪( A∩Bc)
=(B ⧵C)∪( A ⧵B).
Using this and the analogous formula forC ⧵Athen gives
(A∪B∪C) ⧵(A∩B∩C)
= (A∪B∪C)∩( A∩B∩C)c
= [A∩(A∩B∩C)c]∪[ B∩(A∩B∩C)c]∪[ C∩(A∩B∩C)c]
= [A ⧵(A∩B∩C)]∪[ B ⧵(A∩B∩C)]∪[ C ⧵(A∩B∩C)]
= [A ⧵(B∩C)]∪[ B ⧵(A∩C)]∪[ C ⧵(A∩B)]
2.1(iv)
= (A ⧵B)∪( A ⧵C)∪( B ⧵A)∪( B ⧵C)∪( C ⧵A)∪( C ⧵B)
(*)
= (A ⧵B)∪( B ⧵A)∪( B ⧵C)∪( C ⧵B)
= (A▵B)∪( B▵C)
■■
Problem 2.3 Solution: It is clearly enough to prove (2.3) as (2.2) follows ifI contains 2 points.
De Morgan’s identities state that for any index setI (ﬁnite, countable or not countable) and any
collection of subsetsAi⊂X ,i∈I, we have
(a)
H
˝
i∈I
Ai
Ic
=
Ì
i∈I
Ac
i and (b)
H
Ì
i∈I
Ai
Ic
=
˝
i∈I
Ac
i.
10

Solution Manual. Last update 18th July 2019
In order to see (a) we note that
a∈
H
˝
i∈I
Ai
Ic
⇐ ⇒a∉
˝
i∈I
Ai
⇐ ⇒∀i∈I ∶a∉Ai
⇐ ⇒∀i∈I ∶a∈Ac
i
⇐ ⇒a∈
Ì
i∈I
Ac
i,
and (b) follows from
a∈
H
Ì
i∈I
Ai
Ic
⇐ ⇒a∉
Ì
i∈I
Ai
⇐ ⇒∃i0∈I ∶a∉Ai0
⇐ ⇒∃i0∈I ∶a∈Ac
i0
⇐ ⇒a∈
˝
i∈I
Ac
i.
■■
Problem 2.4 Solution:
(i) Theinclusion f(A∩B)⊂f (A)∩f(B)isalwaystruesince A∩B ⊂AandA∩B ⊂Bimply
thatf(A∩B)⊂f (A)andf(A∩B)⊂f (B), respectively. Thus,f(A∩B)⊂f (A)∩ f(B).
Furthermore,y∈f(A)⧵f(B)meansthatthereissome x∈Abutx∉Bsuchthat y=f(x),
that is:y∈f(A ⧵B). Thus,f(A) ⧵f(B)⊂f (A ⧵B).
To see that the converse inclusions cannot hold we consider somenon injectivef. Take
X = [0,2], A = (0,1), B = (1,2), andf ∶ [0,2] → R withx → f(x) =c (c is some
constant). Thenf is not injective and
ç= f(ç)= f((0,1)∩(1 ,2)) ≠f((0,1))∪ f((1,2))={ c}.
Moreover,f(X)= f(B)={ c}= f(X ⧵B)butf(X) ⧵f(B)=ç .
(ii) Recall, ﬁrst of all, the deﬁnition off−1 for a mapf ∶X →Y andB ⊂Y
f−1(B)∶={ x∈X∶f(x)∈ B}.
Observe that
x∈f−1(∪i∈ICi) ⇐ ⇒f(x)∈∪ i∈ICi
⇐ ⇒∃i0∈I ∶f(x)∈ Ci0
⇐ ⇒∃i0∈I ∶x∈f−1(Ci0)
⇐ ⇒x∈∪ i∈If−1(Ci),
11

R.L. Schilling: Measures, Integrals & Martingales
and
x∈f−1(∩i∈ICi) ⇐ ⇒f(x)∈∩ i∈ICi
⇐ ⇒∀i∈I ∶f(x)∈ Ci
⇐ ⇒∀i∈I ∶x∈f−1(Ci)
⇐ ⇒x∈∩ i∈If−1(Ci),
and, ﬁnally,
x∈f−1(C ⧵D) ⇐ ⇒f(x)∈ C ⧵D
⇐ ⇒f(x)∈ C and f(x)∉ D
⇐ ⇒x∈f−1(C) and x∉f−1(D)
⇐ ⇒x∈f−1(C) ⧵f−1(D).
■■
Problem 2.5 Solution:
(i), (vi) For everyx we have
1A∩B(x)=1 ⇐ ⇒x∈A∩B
⇐ ⇒x∈A, x∈B
⇐ ⇒ 1A(x)=1= 1B(x)
⇐ ⇒
⎧
⎪
⎨
⎪⎩
1A(x)⋅ 1B(x)=1
min{1A(x), 1B(x)}=1
(ii), (v) For everyxwe have
1A∪B(x)=1 ⇐ ⇒x∈A∪B
⇐ ⇒x∈Aorx∈B
⇐ ⇒ 1A(x)+ 1B(x) ⩾1
⇐ ⇒
⎧
⎪
⎨
⎪⎩
min{1A(x)+ 1B(x),1}=1
max{1A(x), 1B(x)}=1
(iii) SinceA=(A∩B)⊍(A ⧵B)weseethat 1A∩B(x)+ 1A⧵B(x)canneverhavethevalue 2,thus
part (ii) implies
1A(x)= 1(A∩B)⊍(A⧵B)(x)=min{ 1A∩B(x)+ 1A⧵B(x),1}
= 1A∩B(x)+ 1A⧵B(x)
and all we have to do is to subtract1A∩B(x)on both sides of the equation.
12

Solution Manual. Last update 18th July 2019
(iv) With the same argument that we use in (iii) and with the result of (iii) we get
1A∪B(x)= 1(A⧵B)⊍(A∩B)⊍(B⧵A)(x)
= 1A⧵B(x)+ 1A∩B(x)+ 1B⧵A(x)
= 1A(x)− 1A∩B(x)+ 1A∩B(x)+ 1B(x)− 1A∩B(x)
= 1A(x)+ 1B(x)− 1A∩B(x).
(vii) We have
∀i∶ 1Ai ⩽ 1⋃
iAi - ⇒sup
i
1Ai ⩽ 1⋃
iAi.
On the other hand,
x0∈
˝
i
Ai - ⇒∃i0∶x∈Ai0.
Thus,
1⋃
iAi(x0)=1 - ⇒ 1Ai0
(x0)=1 - ⇒sup
i
1Ai(x0)=1
and we getsupi 1Ai ⩾ 1⋃
iAi.
(viii) Onepossibilityistomimictheproofof(vii). Weprefertoarguelikethis: using(iii)andde
Morgan’s identities we get
1⋂
iAi
(iii)
=
de Morgan
1X− 1⋃
iAc
i
(vii)
= 1−sup
i
1Ac
i
=inf
i
(1− 1Ac
i
)
(iii)
= inf
i
1Ai.
■■
Problem 2.6 Solution:
(i) Using 2.5(iii), (iv) we see that
1A▵B(x)= 1(A⧵B)⊍(B⧵A)(x)
= 1A⧵B(x)+ 1B⧵A(x)
= 1A(x)− 1A∩B(x)+ 1B(x)− 1A∩B(x)
= 1A(x)+ 1B(x)−2 1A∩B(x)
and this expression is1 if, and only if,xis either inAorB but not in both sets. Thus
1A▵B(x) ⇐ ⇒ 1A(x)+ 1B(x)=1 ⇐ ⇒ 1A(x)+ 1B(x)mod2=1 .
It is also possible to show that
1A▵B = ð1A− 1Bð.
13

R.L. Schilling: Measures, Integrals & Martingales
This follows from
1A(x)− 1B(x)=
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪⎩
0, if x∈A∩B;
0, if x∈Ac∩Bc;
+1, if x∈A ⧵B;
−1, if x∈B ⧵A.
Thus,
ð1A(x)− 1B(x)ð=1 ⇐ ⇒x∈(A ⧵B)∪( B ⧵A)= A▵B.
(ii) From part (i) we see that
1A▵(B▵C)= 1A+ 1B▵C−2 1A1B▵C
= 1A+ 1B+ 1C−2 1B1C−2 1A
 1B+ 1C−2 1B1C

= 1A+ 1B+ 1C−2 1B1C−2 1A1B−2 1A1C+4 1A1B1C
and this expression treatsA,B,C in a completely symmetric way, i.e.
1A▵(B▵C)= 1(A▵B)▵C.
(iii) Step 1: (P(X),▵,ç)is an abelian group.
Neutral element:A▵ç=ç ▵A=A;
Inverse element:A▵A=(A ⧵A)∪( A ⧵A)=ç , i.e. each element is its own inverse.
Associativity: see part (ii);
Commutativity: A▵B=B▵A.
Step 2: For the multiplication∩ we have
Associativity:A∩(B∩C)=( A∩B)∩ C;
Commutativity: A∩B=B∩A;
One-element: A∩X=X∩A=A.
Step 3: Distributive law:
A∩(B▵C)=( A∩B)▵(A∩C).
For this we use again indicator functions and the rules from (i) and Problem 2.5:
1A∩(B▵C)= 1A1B▵C = 1A(1B+ 1C mod 2)
= 1A(1B+ 1C) mod 2
= 1A1B+ 1A1C
 mod 2
= 1A∩B+ 1A∩C
 mod 2
= 1(A∩B)▵(A∩C).
14

Solution Manual. Last update 18th July 2019
■■
Problem 2.7 Solution: Letf ∶X →Y. One has
f surjective ⇐ ⇒∀B ⊂Y ∶f◦f−1(B)= B
⇐ ⇒∀B ⊂Y ∶f◦f−1(B)⊃B.
This can be seen as follows: by deﬁnitionf−1(B)={ x∶f(x)∈ B} so that
f◦f−1(B)= f {x∶f(x)∈ B}={f(x)∶ f(x)∈ B}⊂{y∶y∈B}
andwehaveequalityinthelaststepif,andonlyif,wecanguaranteethatevery y∈Bisoftheform
y=f(x)forsome x. Sincethismustholdforallsets B,thisamountstosayingthat f(X)= Y,i.e.
thatf is surjective. The second equivalence is clear since our argument shows that the inclusion
‘⊂’ always holds.
Thus, we can construct a counterexample by settingf ∶ R → R,f(x) ∶=x2 andB = [−1,1].
Then
f−1([−1,1])=[0 ,1] and f◦f−1([−1,1])= f([0,1])=[0 ,1] a[−1,1].
On the other hand
f injective ⇐ ⇒∀A⊂X ∶f−1◦f(A)= A
⇐ ⇒∀A⊂X ∶f−1◦f(A)⊂A.
To see this we observe that because of the deﬁnition off−1
f−1◦f(A)={ x∶f(x)∈ f(A)}⊃{x∶x∈A}= A (*)
sincex ∈ A always entailsf(x) ∈f(A). The reverse is, for non-injectivef, wrong since then
there might be somex0∉A but withf(x0)= f(x)∈ f(A) i.e.x0∈f−1◦f(A) ⧵A. This means
that we have equality in(∗) if, and only if,f is injective. The second equivalence is clear since
our argument shows that the inclusion ‘⊃’ always holds.
Thus, we can construct a counterexample by settingf ∶ R → R,f ≡1. Then
f([0,1])={1} and f−1◦f([0,1])= f−1({1})= R b[0,1].
■■
Problem 2.8 Solution: Assume that forx,y we havef◦g(x) =f◦g(y). Since f is injective, we
conclude that
f(g(x))= f(g(y)) - ⇒g(x)= g(y),
15

R.L. Schilling: Measures, Integrals & Martingales
and, sinceg is also injective,
g(x)= g(y) - ⇒x=y
showing thatf◦g is injective.
■■
Problem 2.9 Solution:
• Call the set of odd numbersO. Every odd number is of the form2k−1 wherek∈ N. We
are done, if we can show that the mapf ∶ N →O,k →2k−1 is bijective. Surjectivity is
clear asf(N)= O. For injectivity we takei,j ∈ N such thatf(i)= f(j). The latter means
that2i−1=2 j−1, soi=j, i.e. injectivity.
• The quickest solution is to observe thatN× Z = N× N∪ N×{0}∪ N×(− N) where
−N∶={−n∶n∈ N}arethestrictlynegativeintegers. WeknowfromExample2.5(iv)that
N×Niscountable. Moreover,themap ∶ N×N → N×(−N),((i,k))=( i,−k)isbijective,
thus#N×(− N) = #N× N is also countable and so isN×{0} since ∶ N → N×{0} ,
(n)∶=( n,0) is also bijective.
Therefore, N× Zis a union of three countable sets, hence countable.
Analternativeapproach wouldbetowriteout Z× N(theswapof Zand Nisfornotational
reasons—since the map((j,k))∶=( k,j)from Z× Nto N× Zis bijective, the cardinality
does not change) in the following form
… (−3,1) (−2,1) (−1,1) (0,1) (1,1) (2,1) (3,1) …
… (−3,2) (−2,2) (−1,2) (0,2) (1,2) (2,2) (3,2) …
… (−3,3) (−2,3) (−1,3) (0,3) (1,3) (2,3) (3,3) …
… (−3,4) (−2,4) (−1,4) (0,4) (1,4) (2,4) (3,4) …
… (−3,5) (−2,5) (−1,5) (0,5) (1,5) (2,5) (3,5) …
… (−3,6) (−2,6) (−1,6) (0,6) (1,6) (2,6) (3,6) …
⋮ ⋮ ⋮ ⋮ ⋮ ⋮ ⋮
and going through the array, starting with(0,1), then(1,1) →(1,2) →(0,2) →(−1,2) →
(−1,1), then(2,1) →(2,2) →(2,3) →(1,3) → ... in clockwise oriented⨆-shapes down,
left, up.
• In Example 2.5(iv) we have shown that#Q ⩽ #N. Since N ⊂ Q, we have a canonical
injection | ∶ N → Q,i → i so that#N ⩽ #Q. Using Theorem 2.7 we conclude that
#Q=# N.
The proof of#(N× N)=# N can be easily adapted—using some pretty obvious notational
changes—toshowthattheCartesianproductofanytwocountablesetsofcardinality #Nhas
again cardinality#N. Applying thism−1 times we see that#Qn=# N.
• ⋃
m∈N Qm is a countable union of countable sets, hence countable, cf. Theorem 2.6.
16

Solution Manual. Last update 18th July 2019
■■
Problem 2.10 Solution: Following the hint it is clear that∶ N → N×{1},i →(i,1)is a bijection
and that|∶ N×{1} → N× N,(i,1) →(i,1) is an injection. Thus,#N ⩽#(N× N).
On the other hand,N× N = ⋃
j∈N N×{j} which is a countable union of countable sets, thus
#(N× N) ⩽#N.
Applying Theorem 2.7 ﬁnally gives#(N× N)=# N.
■■
Problem 2.11 Solution: SinceE ⊂F the map|∶E →F,e →e is an injection, thus#E ⩽#F.
■■
Problem 2.12 Solution: Assumethattheset {0,1}N wereindeedcountableandthat {sj}j∈N wasan
enumeration: eachsj would be a sequence of the form(dj
1,dj
2,dj
3,...,d j
k,...)withdj
k∈{0,1}. We
could write these sequences in an inﬁnite list of the form:
s1 = d1
1 d1
2 d1
3 d1
4 … d1
k …
s2 = d2
1 d2
2 d2
3 d2
4 … d2
k …
s3 = d3
1 d3
2 d3
3 d3
4 … d3
k …
s4 = d4
1 d4
2 d4
3 d4
4 … d4
k …
⋮ ⋮ ⋮ ⋮ ⋮ ⋮ ⋱ ⋮ ⋱
sk = dk
1 dk
2 dk
3 dk
4 … dk
k …
⋮ ⋮ ⋮ ⋮ ⋮ ⋮ ⋱ ⋮ ⋱
and produce a new0-1-sequenceS =(e1,e2,e3,…)by setting
em∶=
⎧
⎪
⎨
⎪⎩
0, if dm
m =1
1, if dm
m =0
.
SinceS diﬀersfromsl exactlyatposition l,S cannotbeintheabovelist, thus, theabovelistdid
not contain all0-1-sequences, hence a contradiction.
■■
Problem 2.13 Solution: Consider the functionf ∶(0,1) → R given by
f(x)∶= 1
1− x− 1
x.
This function is obviously continuous and we havelimx→0f(x) = −∞andlimx→1f(x) = +∞.
By the intermediate value theorem we have thereforef((0,1))= R, i.e. surjectivity.
Sincef is also diﬀerentiable andf‡(x)= 1
(1− x)2 + 1
x2 >0, we see thatf is strictly increasing,
hence injective, hence bijective.
■■
17

R.L. Schilling: Measures, Integrals & Martingales
Problem 2.14 Solution: SinceA1 ⊂ ⋃
i∈NAi it is clear thatc = #A1 ⩽ #⋃
i∈NAi. On the other
hand,#Ai = c means that we can mapAi bijectively ontoR and, using Problem 2.13, we mapR
bijectivelyonto (0,1)or(i−1,i). Thisshowsthat #⋃
i∈NAi ⩽#⋃
i∈N(i−1,i) ⩽#R= c. Using
Theorem 2.7 ﬁnishes the proof.
■■
Problem 2.15 Solution: Since we can write eachx ∈ (0,1) as an inﬁnite dyadic fraction (o.k. if it
is ﬁnite, ﬁll it up with an inﬁnite tail of zeroes !), the proof of Theorem 2.8 shows that#(0,1) ⩽
#{0,1}N.
On the other hand, thinking in base-4 expansions, each element of{1,2}N can be interpreted
as a unique base-4 fraction (having no0 or3 in its expansion) of some number in(0,1). Thus,
#{1,2}N ⩽#N.
But#{1,2}N=#{0,1}N and we conclude with Theorem 2.7 that#(0,1)=#{0 ,1}N.
■■
Problem 2.16 Solution: Just as before, expandx ∈ (0,1) as ann-adic fraction, then interpret each
elementof {1,2,…,n +1} N asaunique (n+1)-adicexpansionofanumberin (0,1)andobserve
that#{1,2,…,n +1} N={0,1,…,n}N.
■■
Problem 2.17 Solution: Take a vector(x,y) ∈ (0,1)×(0 ,1) and expand its coordinate entriesx,y
as dyadic numbers:
x=0.x1x2x3…, y =0.y1y2y3….
Thenz∶=0.x1y1x2y2x3y3…isanumberin (0,1). Conversely,wecan‘zip’eachz=0.z1z2z3z4…∈
(0,1) into two numbersx,y ∈(0,1) by setting
x∶=0.z2z4z6z8…, y ∶=0.z1z3z5z7…
This is obviously a bijective operation.
Since we have a bijection between(0,1) ↔ R it is clear that we have also a bijection between
(0,1)×(0 ,1) ↔ R× R.
■■
Problem 2.18 Solution: We have seen in Problem 2.18 that#{0,1}N = #{1,2}N = c. Obviously,
{1,2}N ⊂ NN ⊂ RN and since we have a bijection between(0,1) ↔ R one extends this (using
coordinates) to a bijection between(0,1)N ↔ RN. Using Theorem 2.9 we get
c=#{1,2}N ⩽#NN ⩽#RN= c,
and, because of Theorem 2.7 we have equality in the above formula.
■■
18

Solution Manual. Last update 18th July 2019
Problem 2.19 Solution: LetF ∈ℱ with#F =nThenwecanwrite F asatupleoflength n(having
n pairwise diﬀerent entries...) and therefore we can interpretF as an element of⋃
m∈N Nm. In
this sense,ℱ  →⋃
m∈N Nm and#ℱ ⩽ ⋃
m∈N Nm=# Nsince countably many countable sets are
again countable. SinceN⊂ℱ we get#ℱ =# N by Theorem 2.7.
Alternative: Deﬁne a map∶ℱ → N by
ℱ ∋A →(A)∶=
É
a∈A
2a
. It is clear that increases ifA gets bigger:A ⊂ B - ⇒ (A) ⩽ (B). LetA,B ∈ℱ be two
ﬁnite sets, sayA = {a1,a2,…,aM} and{b1,b2,…,bN} (ordered according to size witha1,b1
being the smallest andaM,bN the biggest) such that(A)= (B). Assume, to the contrary, that
A ≠B. IfaM ≠bN, sayaM >b N, then
(A) ⩾({aM}) ⩾2aM > 2aM −1
2−1 =
aM−1É
j=1
2j
=({1,2,3,…aM−1})
⩾(B),
which cannot be the case since we assumed(A) = (B). Thus, aM = bN. Now consider
recursively the next elements,aM−1 andbN−1 and the same conclusion yields their equality etc.
The process stops aftermin{M,N} steps. But ifM ≠N, sayM >N, thenA would contain at
least one more element thanB, hence(A) > (B), which is also a contradiction. This, ﬁnally
shows thatA=B, hence that is injective.
On the other hand, each natural number can be expressed in terms of ﬁnite sums of powers of
base-2, so thatis also surjective.
Thus,#ℱ =# N.
■■
Problem 2.20 Solution: (Letℱ be as in the previous exercise.) Observe that the inﬁnite sets from
P(N),ℐ ∶=P(N) ⧵ℱ can be surjectively mapped onto{0,1}N: if{a1,a2,a3,…} =A ⊂N,
thendeﬁneaninﬁnite0-1-sequence(b1,b2,b3,…)bysetting bj =0 orbj =1 accordingtowhether
aj is even or odd. This is a surjection ofP(N) onto{0,1}N and so#P(N) ⩾#{0,1}N. Call this
map and consider the family−1(s),s∈{0,1}N inℐ, consisting of obviously disjoint inﬁnite
subsets of N which lead to the same0-1-sequence s. Now choose from each family−1(s) a
representative,callit r(s)∈ ℐ. Thenthemap s →r(s)isabijectionbetween {0,1}N andasubset
ofℐ, the set of all representatives. Hence,ℐ has at least the same cardinality as{0,1}N and as
such a bigger cardinality thanN.
■■
19

R.L. Schilling: Measures, Integrals & Martingales
Problem 2.21 Solution: DenotebyΘthemapP(N)∋ A → 1A∈{0,1}N. Let=(d1,d2,d3,…)∈
{0,1}N anddeﬁneA()∶={ j∈ N∶dj =1} . Then=( 1A()(j))j∈N showingthat Θissurject-
ive.
On the other hand,
1A= 1B ⇐ ⇒ 1A(j)= 1B(j) ∀j∈ N ⇐ ⇒A=B.
This shows the injectivity ofΘ, and#P(N)=#{0 ,1}N follows.
■■
Problem 2.22 Solution: Since forA,A‡,B,B ‡⊂X we have the ‘multiplication rule’
(A∩B)∪( A‡∩B‡)=( A∪A‡)∩( A∪B‡)∩( B∪A‡)∩( B∪B‡)
and since this rule carries over to the inﬁnite case, we get the formula from the problem by ‘mul-
tiplying out’ the countable union
(A0
1∩A1
1)∪( A0
2∩A1
2)∪( A0
3∩A1
3)∪( A0
4∩A1
4)∪ ⋯.
More formally, one argues as follows:
x∈
˝
n∈N
(A0
n∩A1
n) ⇐ ⇒∃n0∶x∈A0
n0
∩A1
n0
(*)
while
x∈
Ì
i=(i(k))k∈N∈{0,1}N
˝
k∈N
Ai(k)
k
⇐ ⇒∀i=(i(k))k∈N∈{0,1}N∶x∈
˝
k∈N
Ai(k)
k
⇐ ⇒∀i=(i(k))k∈N∈{0,1}N∃k0∈ N∶x∈Ai(k0)
k0
(**)
Clearly, (*) implies (**). On the other hand, assume that (**) holds but that (*) is wrong, i.e.
suppose that for everyn we have that eitherx∈A0
n orx∈A1
n orx is in neither ofA0
n,A1
n. Thus
we can construct a uniquely deﬁned sequencei(n)∈{0 ,1},n∈ N, by setting
i(n)=
⎧
⎪
⎪
⎨
⎪
⎪⎩
0 ifx∈A0
n;
1 ifx∈A1
n;
0 ifx∉A0
n andx∉A1
n.
Deﬁne byi‡(n)∶=1− i(n)the ‘complementary’0-1-sequence. Then
x∈
˝
n
Ai(n)
n but x∉
˝
n
Ai‡(n)
n
contradicting our assumption (**).
■■
20

3 -Algebras.
Solutions to Problems 3.13.16
Problem 3.1 Solution:
(i) It is clearly enough to show thatA,B ∈ A - ⇒ A∩B ∈ A, because the case ofN sets
follows from this by induction, the induction step being
A1∩…∩ AN
«››››››ﬂ››››››‹
=∶B∈A
∩AN+1=B∩AN+1∈A.
LetA,B ∈A. Then, by (Σ2) alsoAc,Bc ∈A and, by (Σ3) and (Σ2)
A∩B=(Ac∪Bc)c =(Ac∪Bc∪ç∪ç∪…) c ∈A.
Alternative: Of course, the last argument also goes through forN sets:
A1∩A2∩…∩ AN =(Ac
1∪Ac
2∪…∪ Ac
N)c
=(Ac
1∪…∪ Ac
N∪ç∪ç∪…) c ∈A.
(ii) By (Σ2) we haveA∈A - ⇒ Ac ∈A. UseAc instead ofA and observe that(Ac)c =A to
see the claim.
(iii) ClearlyAc,Bc ∈A and so, by part (i),A ⧵B=A∩Bc ∈A as well asA▵B=(A ⧵B)∪
(B ⧵A)∈ A.
■■
Problem 3.2 Solution:
(iv) Let us assume thatB ≠ç andB ≠X. ThenBc ∉{ç,B,X }. Since withB alsoBc must be
contained in a-algebra, the family{ç,B,X }cannot be one.
(vi) SetAE ∶={E∩A∶A∈A}. The key observation is that all set operations inAE are now
relative toE and not toX. This concerns mainly the complementation of sets! Let us check
(Σ1)–(Σ3).
Clearlyç= E∩ç∈ AE. IfB∈A, thenB=E∩A for someA∈A and the complement
ofB relative toE isE ⧵B=E∩Bc =E∩(E∩A)c =E∩(Ec∪Ac)= E∩Ac ∈AE as
Ac ∈A. Finally, let(Bj)j∈N ⊂AE. Then there are(Aj)j∈N ⊂A such thatBj = E∩Aj.
SinceA= ⋃
j∈NAj ∈A weget ⋃
j∈NBj = ⋃
j∈N(E∩Aj)= E∩⋃
j∈NAj =E∩A∈AE.
21

R.L. Schilling: Measures, Integrals & Martingales
(vii) Note thatf−1 interchanges with all set operations. LetA,Aj,j ∈ N be sets inA. We know
that thenA=f−1(A‡),Aj =f−1(A‡
j) for suitableA,A‡
j ∈A‡. SinceA‡is, by assumption
a-algebra, we have
ç= f−1(ç)∈ A as ç∈ A‡
Ac =  f−1(A‡)c
=f−1(A‡c)∈ A as A‡c ∈A‡
˝
j∈N
Aj =
˝
j∈N
f−1(A‡
j)= f−1
H
˝
j∈N
A‡
j
I
∈A as
˝
j∈N
A‡
j ∈A‡
which proves (Σ1)–(Σ3) forA.
■■
Problem 3.3 Solution: Denote byΣ = ({x},x ∈ R). Let A be the-algebra deﬁned in Ex-
ample 3.3(v). It is clear that{x}∈ A, and soΣ⊂A. On the other hand, ifA∈A, then eitherA
orAc is countable. Wlog assume thatA is countable. ThenA is a countable union of singletons,
as suchA∈Σ as well asAc ∈Σ . This meansA ⊂Σ.
■■
Problem 3.4 Solution:
(i) SinceG is a-algebra,G ‘competes’ in the intersection of all-algebrasC ⊃G appearing
in the deﬁnition ofA in the proof of Theorem 3.4(ii). Thus,G ⊃ (G) whileG ⊂ (G) is
always true.
(ii) Without loss of generality we can assume thatç ≠ A ≠ X since this would simplify the
problem. Clearly{ç,A,A c,X} is a-algebra containingA and no element can be removed
without losing this property. Thus{ç,A,A c,X} is minimal and, therefore,=({A}).
(iii) Assume thatℱ ⊂ G. Then we haveℱ ⊂ G ⊂ (G). Now C ∶= (G) is a potential
‘competitor’ in the intersection appearing in the proof of Theorem 3.4(ii), and as suchC ⊃
(ℱ), i.e.(G)⊃(ℱ).
■■
Problem 3.5 Solution:
(i) {ç,(0, 1
2),{0}∪[ 1
2,1],[0,1]}.
We have 2atoms(see the explanations below):(0, 1
2),(0, 1
2)c.
(ii) {ç,[0, 1
4),[1
4, 3
4],(3
4,1],[0, 3
4],[1
4,1],[0, 1
4)∪( 3
4,1],[0,1]}.
We have 3atoms(see below):[0, 1
4),[1
4, 3
4],(3
4,1].
(iii) —same solution as (ii)—
Parts(ii)and(iii)arequitetedioustodoandtheyillustratehowdiﬃcultitcanbetoﬁnda -algebra
containing two distinct sets.... imagine how to deal with something that is generated by 10, 20,
or inﬁnitely many sets. Instead of giving a particular answer, let us describe the method to ﬁnd
({A,B})practically, and then we are going to prove it.
22

Solution Manual. Last update 18th July 2019
1. Start with trivial sets and given sets:ç,X,A,B .
2. now add their complements:Ac,Bc
3. now add their unions and intersections and diﬀerences:A∪B,A ∩B,A ⧵B,B ⧵A
4. now add the complements of the sets in 3.:Ac∩Bc,Ac∪Bc,(A ⧵B)c,(B ⧵A)c
5. ﬁnally,addunionsofdiﬀerencesandtheircomplements: (A⧵B)∪(B ⧵A),(A⧵B)c∩(B ⧵A)c.
All in all one should have 16 sets (some of them could be empty orX or appear several times,
dependingonhowmuch AdiﬀersfromB). That’sit,butthetroubleis: isthisconstructioncorrect?
Here is a somewhat more systematic procedure:
Deﬁnition:An atom of a-algebraA is a non-void setç ≠A∈A that contains no other set of
A.
SinceA is stable under intersections, it is also clear that all atoms are disjoint sets! Now we can
make up every set fromA as union (ﬁnite or countable) of such atoms. The task at hand is to
ﬁnd atoms ifA,B are given. This is easy: the atoms of our future-algebra must be:A ⧵B,
B ⧵A,A∩B,(A∪B)c. (Test it: if you make a picture, this is a tesselation of our spaceX using
disjointsetsandwecangetback A,B asunion! Itisalsominimal,sincethesesetsmustappearin
({A,B})anyway.) The crucial point is now:
Theorem. If A is a-algebra withN atoms (ﬁnitely many!), thenA consists of exactly2N
elements.
Proof. The question is how many diﬀerent unions we can make out ofN sets. Simple answer:
we ﬁnd N
j
,0 ⩽j ⩽N diﬀerent unions involving exactlyj sets (j =0 will, of course, produce
the empty set) and they are all diﬀerent as the atoms were disjoint. Thus, we get∑N
j=0
 N
j
 =
(1+1) N =2 N diﬀerent sets.
It is clear that they constitute a-algebra.
Thisanswerstheabovequestion. Thenumberofatomsdependsobviouslyontherelativeposition
ofA,B: do they intersect, are they disjoint etc. Have fun with the exercises and do not try to ﬁnd
-algebras generated by three or more sets..... (By the way: can you think of a situation in[0,1]
with two subsets given and exactlyfour atoms? Can there be more?)
■■
Problem 3.6 Solution:
(i) See the solution to Problem 3.5.
(ii) IfA1,…,AN ⊂X are given, there are at most2N atoms. This can be seen by induction. If
N =1 ,thenthereare #{A,Ac}=2 atoms. Ifweaddafurtherset AN+1,thentheworstcase
would be thatAN+1 intersects with each of the2N atoms, thus splitting each atom into two
sets which amounts to saying that there are2⋅2N =2 N+1 atoms.
23

R.L. Schilling: Measures, Integrals & Martingales
■■
Problem 3.7 Solution: We follow the hint. Since#A = #N, the following set is a countable inter-
section of measurable sets, hence itself inA:
∀x∈X∶A(x)∶=
Ì
A∈A,A∋x
A∈A. (*)
WriteA0 for the atoms ofA. Then
• A(x)∈ A is an atom which containsx.
Indeed: Otherwise, there is someB ⊂ A(x) such thatB ∈ A,B ≠ ç,B ≠ A(x). We can
assume thatx∈B, or we would takeB‡∶=A(x) ⧵B instead ofB. Sincex∈B,B is part
of the intersection appearing in (*) so thatB ⊃A(x), henceB=A(x), which is impossible.
• Every atomA ≠ç ofA is of the form (*).
Indeed: By assumption,x0∈Aso thatA=A(x0).
• A has#N many atoms.
Indeed: Since#A = #N, there are countably inﬁnitely many disjoint sets inA, thus the
procedure(*)yieldsatleast #Nmanyatoms. Ontheotherhand,therecannotbemoreatoms
than members ofA, and the claim follows.
SinceA contains all countable unions of sets fromA0, and since there are more than countably
many such unions, it is clear that#A >#N.
Remark: A-algebra may have no non-empty atoms at all! Here is an example (which I learned
fromJulianHollender). Let I beanuncountableset,e.g. I =[0,1],andconsider Ω={0 ,1}I. We
canconstructa -algebraonΩinthefollowingway: Let K ⊂IanddeﬁnePK ∶{0,1}I →{0,1}K
the coordinate projection. Acylinder setorﬁnitely based setwith basisK ⊂I is a set of the form
P−1
K (B) where#K <∞ andB ⊂{0,1}K. Now consider the-algebraA ∶= ({cylinder sets})
on{0,1}I. Intuitively,A ∈ A is of the formP−1
L (B) whereL is countable. (The proof as such
is not obvious, a possible source is Lemma 4.5 in Schilling & Partzsch:Brownian Motion. De
Gruyter, Berlin 2012.) Assume thatA0 ∈ A were an atom. ThenA0 has the basisL. Take
i ∈ I ⧵L, considerL‡= L∪{i} and construct a setP−1
L‡(B‡) whereB‡= B×{0} , say. Then
P−1
L‡(B‡)⊂A 0 andP−1
L‡(B‡)∈ A.
■■
Problem 3.8 Solution: We begin with anexample: LetX = (0,1] andA = ℬ(0,1] be the Borel
sets. Deﬁne
An∶= ((j−1)2−n,j2−n], j=1,2,…,2n
the dyadic-algebra of step2−n. Clearly,#An=2 n. Moreover,
An⊊An+1 and A∞∶=
˝
n
An.
24

Solution Manual. Last update 18th July 2019
However,A∞ is NOT a-algebra.
Argument 1:I ∈ A∞ ⇐ ⇒ I ∈ An for somen, i.e.I is a ﬁnite union of intervals with dyadic
end-points. (More precisely: the topological boundaryI ⧵I◦ consists of dyadic points).
On the other hand, every open set(a,b)⊂[0,1]is a countable union of sets fromA∞:
(a,b)=
˝
I∈A∞,I⊂(a,b)
I
which follows from the fact that the dyadic numbers are dense in(0,1]. (If you want it more
elementary, then approximatea and b from the right and left, respectively, by dyadic numbers
and construct the approximating intervals by hand....). If, for example,aandbare irrational, then
(a,b)∉ A∞. This shows thatA∞ cannot be a-algebra.
In fact, our argument shows that(A∞)= ℬ(0,1].
Argument 2: Since#An=2 n we see that#A∞=# N. But Problem 3.7 tells us thatA∞ can’t be a
-algebra.
Let us now turn to the general case. We follow the note by
A.BroughtonandB.W.Huﬀ: Acommentonunionsofsigma-ﬁelds. Am.Math.Monthly 84(1977)
553–554.
Since theAn are strictly increasing, we may assume thatA1 ≠{ç,X}. Recall also the notion of a
trace-Algebra
B∩An∶={B∩A∶A∈An}.
Step 1. Claim: There exists a setE∈A1 such that(E∩An+1) ⧵(E∩An) ≠çfor inﬁnitely many
n∈ N.
To see this, assume – to the contrary – that for somenand someB∈A1 we have
B∩An=B∩An+1 and Bc∩An=Bc∩An+1.
IfU ∈An+1 ⧵An, then
U = ( B∩U)
«ﬂ‹
∈B∩An+1=B∩An⊂An
∪ ( Bc∩U)
«›ﬂ›‹
∈Bc∩An+1=Bc∩An⊂An
leading to the contradictionU ∈An. Thus the claim holds with eitherE=B orE=Bc.
Step 2. LetE be the set from Step 1 and denote byn1,n2,… a sequence for which the assertion
in Step 1 holds. Then
ℱk∶=E∩Ank, k ∈ N
25

R.L. Schilling: Measures, Integrals & Martingales
is a strictly increasing sequence of-Algebras over the setE. Again we may assume thatℱ1 ≠
{ç,E} As in Step 1, we ﬁnd someE1 ∈ℱ1 such thatE1 is not trivial (i.e.E1 ≠ç andE1 ≠ E)
and(E1∩ℱk+1) ⧵(E1∩ℱk) ≠ç holds for inﬁnitely manyk.
Step 3. Now we repeat Step 2 and construct recursively a sequence of-algebrasAi1 ⊂ Ai2 ⊂
Ai3… and a sequence of setsE1⊃E 2⊃E 3… such that
Ek∈Aik and Ek+1∈(Ek∩Aik+1) ⧵(Ek∩Aik).
Step 4. The setsFk ∶= Ek ⧵Ek+1 have the property that they are disjoint andFk ∈Aik+1 ⧵Aik.
Since the-algebras are increasing, we have
˝
n∈N
An=
˝
k∈N
Aik
which means that we can restrict ourselves to a subsequence. This means that we can assume that
ik=k.
Step 5. Without loss of generality we can identifyFk with{k} and assume that theAn are -
algebras onN such that{k}∈ Ak+1 ⧵Ak. LetBn the smallest set inAn such thatn∈Bn. Then
n∈Bn⊂{n,n +1,n +2,…}andBn ≠{n}. Moreover
m∈Bn - ⇒Bm⊂B n since m∈Bn∩Bm∈Am.
Now deﬁnen1=1 and picknk+1 recursively:nk+1∈Bnk such thatnk+1 ≠nk. ThenBn1 ⊃B n2 ⊃
…. SetE={n2,n4,n6,…}. IfA∞ were a-algebra, thenE∈An for somen, thusE∈An2k for
somek. Then{n2k,n2k+2,…}∈ An2k and thusBn2k ⊂{n2k,n2k+2,…}. This contradicts the fact
n2k+1∈Bn2k.
■■
Problem 3.9 Solution:
O1 Sinceç contains no element, every elementx ∈ çadmits certainly some neighbourhood
B(x)and soç∈ O. Since for allx∈ Rn alsoB(x)⊂ Rn, Rn is clearly open.
O2 LetU,V ∈O. IfU∩V =ç , we are done. Else, we ﬁnd somex∈U∩V. SinceU,V are
open, we ﬁnd some1,2 >0 such thatB1(x)⊂U andB2(x)⊂V . But then we can take
ℎ∶=min{1,2}>0 and ﬁnd
Bℎ(x)⊂B 1(x)∩ B2(x)⊂U ∩V,
i.e.U∩V ∈O. Forﬁnitelymany,sayN,sets,thesameargumentworks. Noticethatalready
for countably many sets we will get a problem as the radiusℎ ∶= min{j ∶ j ∈ N} is not
necessarily any longer>0.
26

Solution Manual. Last update 18th July 2019
O2 LetI be any (ﬁnite, countable, not countable) index set and(Ui)i∈I ⊂O be a family of open
sets. SetU ∶= ⋃
i∈IUi. Forx∈U weﬁndsomej∈I withx∈Uj,andsince Uj wasopen,
we ﬁnd somej >0such thatBj(x)⊂U j. But then, trivially,Bj(x)⊂U j ⊂ ⋃
i∈IUi=U
proving thatU is open.
The familyOn cannot be a-algebra since the complement of an open setU ≠ç, ≠ Rn is closed.
■■
Problem 3.10 Solution: LetX = R and setUk∶=(− 1
k, 1
k) which is an open set. Then⋂
k∈NUk=
{0}but a singleton like{0} is closed and not open.
■■
Problem 3.11 Solution: WeknowalreadythattheBorelsets ℬ=ℬ(R)aregeneratedbyanyofthe
following systems:
{[a,b)∶ a,b ∈ Q}, {[a,b)∶ a,b ∈ R},
{(a,b)∶ a,b ∈ Q}, {(a,b)∶ a,b ∈ R}, O1, orC1
Here is just an example (with the dense setD = Q) how to solve the problem. Letb > a. Since
(−∞,b) ⧵(−∞,a)=[ a,b)we get that
{[a,b)∶ a,b ∈ Q}⊂({(−∞,c)∶ c∈ Q})
- ⇒ ℬ=({[a,b)∶ a,b ∈ Q})⊂({(−∞,c)∶ c∈ Q}).
On the other hand we ﬁnd that(−∞,a)= ⋃
k∈N[−k,a)proving that
{(−∞,a)∶ a∈ Q}⊂({[c,d)∶ c,d ∈ Q})= ℬ
- ⇒ ({(−∞,a)∶ a∈ Q})⊂ℬ
and we get equality.
The other cases are similar.
■■
Problem 3.12 Solution: Let B∶={Br(x)∶ x∈ Rn, r >0} and letB‡∶={Br(x)∶ x∈ Qn, r∈
Q+}. Clearly,
B‡⊂ B⊂On
- ⇒ (B‡)⊂(B)⊂(On)= ℬ(Rn).
On the other hand, any open setU ∈On can be represented by
U =
˝
B∈B‡,B⊂U
B. (*)
27

R.L. Schilling: Measures, Integrals & Martingales
Indeed,U ⊃⋃
B∈B‡,B⊂U B follows by the very deﬁnition of the union. Conversely, ifx∈U we
usethefactthat U isopen,i.e.thereissome B(x)⊂U . Withoutlossofgeneralitywecanassume
that is rational, otherwise we replace it by some smaller rational. Since Qn is dense inRn we
can ﬁnd someq ∈ Qn with ðx−qð < ∕3 and it is clear thatB∕3(q) ⊂ B(x) ⊂ U. This shows
thatU ⊂⋃
B∈B‡,B⊂U B.
Since#B‡=#( Qn× Q)=# N, formula(∗)entails that
On⊂(B‡) - ⇒(On)= (B‡) and, therefore, (On)= (B)
and we are done.
■■
Problem 3.13 Solution:
(i) O1: We haveç=ç∩ A∈OA,A=X∩A∈OA.
O1: LetU‡=U∩A∈OA,V‡=V∩A∈OAwithU,V ∈O. ThenU‡∩V‡=(U∩V)∩A∈
OA sinceU∩V ∈O.
O2: LetU‡
i =Ui∩A∈OA withUi∈O. Then⋃
iU‡
i =  ⋃
iUi
∩A∈OA since⋃
iUi∈O.
(ii) We use for a setA and a familyℱ ⊂P(X)the shorthandA∩ℱ ∶={A∩F ∶F ∈ℱ}.
Clearly,A∩O ⊂A ∩(O)= A∩ℬ(X). Since the latter is a-algebra, we have
(A∩O)⊂A ∩ℬ(X) i.e. ℬ(A)⊂A ∩ℬ(X).
For the converse inclusion we deﬁne the family
Σ∶={ B ⊂X∶A∩B∈(A∩O)}.
It is not hard to see thatΣ is a-algebra and thatO ⊂ Σ. Thusℬ(X) =(O) ⊂ Σ which
means that
A∩ℬ(X)⊂(A∩O).
Notice that this argument does not really need thatA∈ℬ(X). If, however,A∈ℬ(X) we
have in addition toA∩ℬ(X)= ℬ(A)that
ℬ(A)={ B ⊂A∶B∈ℬ(X)}
■■
Problem 3.14 Solution:
(i) We see, as in the proof of Theorem 3.4, that the intersection of arbitrarily many mono-
tone classes (MC, for short) is again a MC. Thus,
m(ℱ)∶=
Ì
ℱ⊂G
G MC
G,
28

Solution Manual. Last update 18th July 2019
isitselfaMC.Note,thattheintersectionisnon-voidasthepowerset P(X)is(trivially)
aMCwhichcontains ℱ. Byconstruction,seealsotheargumentofTheorem3.4, m(ℱ)
is a minimal MC containingℱ.
(ii) Deﬁne
D ∶={F ∈ m(ℱ)∶ Fc ∈ m(ℱ)}.
By assumption,ℱ ⊂D. We are done, if we can show thatD is a MC.
(MC1) Let(Mn)n∈N⊂D beanincreasingfamily Mn ↑M = ⋃
n∈NMn. Sincem(ℱ)
is a MC,M ∈ m(ℱ)and
Mc =
H
˝
n∈N
Mn
Ic
=
Ì
n∈N
Mc
n
«ﬂ‹
∈m(ℱ)
∈ m(ℱ).
Hereweusethat Mn ↑ - ⇒Mc
n ↓andso ⋂
n∈NMc
n ∈ m(ℱ)becauseof (MC2)
for the systemm(ℱ). This provesM ∈D.
(MC2) Let(Nn)n∈N ⊂D be a decreasing familyNn ↓N = ⋂
n∈NNn. As in the ﬁrst
part we get fromN ∈ m(ℱ) andNc
n ↑Nc thatNc ∈ m(ℱ) due to (MC1) for
the familym(ℱ). Consequently,N ∈D.
(iii) Wefollowthehint. Becauseofthe ∩-stabilityof ℱ weget ℱ ⊂Σ. Letuscheckthat Σ
is a MC:
(MC1) Let(Mn)n∈N ⊂ Σ be an increasing sequenceMn ↑ M and F ∈ ℱ. Then
M ∈ m(ℱ) and fromm(ℱ)∋ Mn∩F ↑M∩F we get (using (MC1) for the
system m(ℱ)), thatM∩F ∈ m(ℱ), hence,M ∈Σ .
(MC2) This is similar to(MC1).
Therefore,Σ is a MC andℱ ⊂ Σ. This proves m(ℱ) ⊂ Σ andℱ ⊂ Σ‡. Since Σ‡
is also a MC (the proof is very similar to the one forΣ; just replace “F ∈ ℱ” with
“F ∈ m(ℱ)”) we getm(ℱ)⊂Σ‡, too. This proves our claim.
(iv) Sinceℳ⊃ℱ, we get
ℳ= m(ℳ)⊃ m(ℱ);
so it is enough to show thatm(ℱ)is a-algebra containingℱ. Clearly,ℱ ⊂ m(ℱ).
(Σ1) By assumption,X∈ℱ ⊂ m(ℱ).
(Σ2) This follows immediately from (ii).
(Σ3) First we show thatm(ℱ)is∪-stable: sincem(ℱ)is∩-stable – by (iii) – we get
C,D ∈ m(ℱ) - ⇒C ⧵D=C∩Dc ∈ m(ℱ)
and so
C,D ∈ m(ℱ)
(Σ2)
- - - - - - - - - - - - - ⇒
(Σ1)
C∪D=X ⧵(X ⧵C) ⧵D∈ m(ℱ).
29

R.L. Schilling: Measures, Integrals & Martingales
If(An)n∈N ⊂ m(ℱ) is any sequence, the new sequenceBn ∶= A1∪⋯∪An is
increasing and⋃
n∈NAn= ⋃
n∈NBn. Thus, (Σ3) follows from (MC1).
■■
Problem 3.15 Solution: Clearly,ℳ= m(O),i.e.itisthemonotoneclassgeneratedbytheopensets.
Since(O)is itself a monotone class, the minimality ofm(O)yields
m(O)⊂(O).
On the other hand, the monotone class theorem (Problem 3.14(iv)) shows
m(O)= ℳ⊃O - ⇒ m(O)= ℳ⊃(O).
This ﬁnishes the ﬁrst part of the problem.
Theanswertotheadditionalquestionis: yes,wecanomitthemonotonicityinthecountableinter-
sectionandunion. Theargumentisasfollows: Problem3.14stillworkswithoutthemonotonicity
(giving a slightly diﬀerent notion of monotone class), and so the above proof goes through!
■■
Problem 3.16 Solution: WriteΣ∶= ⋃{(C) ∶C ⊂ℱ, C is a countable sub-family}.
IfC ⊂ℱ we get(C)⊂(ℱ), and soΣ⊂(ℱ).
Conversely, it is clear thatℱ ⊂Σ, just takeC ∶=CF ∶={F} for eachF ∈ℱ. If we can show
thatΣis a-algebra we get(ℱ)⊂(Σ)=Σ and equality follows.
• Clearly,ç∈Σ .
• IfS ∈Σ , thenS ∈(CS) for some countableCS ⊂ℱ. Moreover,Sc ∈(CS), i.e. Sc ∈
Σ.
• If(Sn)n⩾0 ⊂Σ are countably many sets, thenSn ∈ (Cn) for some countableCn ⊂ ℱ and
eachn ⩾0. SetC ∶= ⋃
nCn. This isagain countable andwe getSn∈(C)for alln, hence
⋃
nSn∈(C)and so⋃
nSn∈Σ .
■■
30

4 Measures.
Solutions to Problems 4.14.22
Problem 4.1 Solution:
(i) Wehavetoshowthatforameasure andﬁnitelymany,pairwisedisjointsets A1,A2,…,AN ∈
A we have
(A1⊍A2⊍…⊍AN)= (A1)+ (A2)+…+ (AN).
We use induction inN ∈ N. The hypothesis is clear, for the start(N = 2)see Proposition
4.3(i). Inductionstep: takeN+1disjointsets A1,…,AN+1∈A,set B∶=A1⊍…⊍AN ∈A
and use the induction start and the hypothesis to conclude
(A1⊍…⊍AN ⊍AN+1)= (B⊍A N+1)
=(B)+ (AN+1)
=(A1)+…+ (AN)+ (AN+1).
(iv) Togetanideawhatisgoingonweconsiderﬁrstthecaseofthreesets A,B,C . Applyingthe
formula for strong additivity thrice we get
(A∪B∪C)= (A∪(B∪C))
=(A)+ (B∪C)− (A∩(B∪C)
«››››ﬂ››››‹
=(A∩B)∪(A∩C)
)
=(A)+ (B)+ (C)− (B∩C)− (A∩B)
−(A∩C)+ (A∩B∩C).
As an educated guess it seems reasonable to suggest that
(A1∪…∪ An)=
nÉ
k=1
(−1)k+1 É
⊂{1,…,n}
#=k
  ∩
j∈
Aj
.
Weprovethisformulabyinduction. TheinductionstartisjusttheformulafromProposition
4.3(iv), the hypothesis is given above. For the induction step we observe that
É
⊂{1,…,n+1}
#=k
=
É
⊂{1,…,n,n+1}
#=k,n+1∉
+
É
⊂{1,…,n,n+1}
#=k,n+1∈
=
É
⊂{1,…,n}
#=k
+
É
‡⊂{1,…,n}
#‡=k−1,∶=‡∪{n+1}
(∗)
31

R.L. Schilling: Measures, Integrals & Martingales
Having this in mind we get forB∶=A1∪…∪ An andAn+1 using strong additivity and the
induction hypothesis (forA1,…,An resp.A1∩An+1,…,An∩An+1)
(B∪An+1)= (B)+ (An+1)− (B∩An+1)
=(B)+ (An+1)−   n
∪
j=1
(Aj∩An+1)
=
nÉ
k=1
(−1)k+1 É
⊂{1,…,n}
#=k
  ∩
j∈
Aj
+(An+1)
+
nÉ
k=1
(−1)k+1 É
⊂{1,…,n}
#=k
 An+1 ∩
j∈
Aj
.
Because of(∗)the last line coincides with
n+1É
k=1
(−1)k+1 É
⊂{1,…,n,n+1}
#=k
  ∩
j∈
Aj

and the induction is complete.
(v) We have to show that for a measure and ﬁnitely many setsB1,B2,…,BN ∈A we have
(B1∪B2∪…∪ BN) ⩽(B1)+ (B2)+…+ (BN).
We use induction inN ∈ N. The hypothesis is clear, for the start(N = 2)see Proposition
4.3(v). Inductionstep: takeN+1 setsB1,…,BN+1∈A,set C ∶=B1∪…∪ BN ∈A and
use the induction start and the hypothesis to conclude
(B1∪…∪ BN∪BN+1)= (C∪BN+1)
⩽(C)+ (BN+1)
⩽(B1)+…+ (BN)+ (BN+1).
■■
Problem 4.2 Solution:
(i) The Dirac measure is deﬁned on an arbitrary measurable space(X,A)by
x(A)∶=
⎧
⎪
⎨
⎪⎩
0, ifx∉A
1, ifx∈A
,
whereA∈A andx∈X is a ﬁxed point.
(M1)Sinceç contains no points,x∉ç and sox(ç)=0 .
(M2) Let(Aj)j∈N ⊂ A a sequence of pairwise disjoint measurable sets. Ifx ∈ ⋃
j∈NAj,
there is exactly onej0 withx∈Aj0, hence
x
H
˝
j∈N
Aj
I
=1=1+0+0+…
32

Solution Manual. Last update 18th July 2019
=x(Aj0)+
É
j≠j0
x(Aj)
=
É
j∈N
x(Aj).
Ifx∉ ⋃
j∈NAj, thenx∉Aj for everyj∈ N, hence
x
H
˝
j∈N
Aj
I
=0=0+0+0+…=
É
j∈N
x(Aj).
(ii) The measure is deﬁned on(R,A) by(A)∶=
⎧
⎪
⎨
⎪⎩
0, if#A ⩽#N
1, if#Ac ⩽#N
whereA ∶={A⊂ R∶
#A ⩽#N or #Ac ⩽#N}. (Note that#A ⩽#N if, and only if,#Ac =# R ⧵A> #N.)
(M1)Sinceç contains no elements, it is certainly countable and so(ç)=0 .
(M2)Let(Aj)j∈N bepairwisedisjoint A-sets. Ifallofthemarecountable,then A∶= ⋃
j∈N
is countable and we get

H
˝
j∈N
Aj
I
=(A)=0=
É
j∈N
(Aj).
Ifatleastone Aj isnotcountable,sayfor j=j0,then A⊃A j0 isnotcountableandtherefore
(A) =(Aj0) = 1. Assume we could ﬁnd some otherj1 ≠ j0 such thatAj0,Aj1 are not
countable. SinceAj0,Aj1 ∈A weknowthattheircomplements Ac
j0
,Ac
j1
arecountable,hence
Ac
j0
∪Ac
j1
iscountableand,atthesametime, ∈A. Becauseofthis,(Ac
j0
∪Ac
j1
)c =Aj0∩Aj1 =ç
cannot be countable, which is absurd! Therefore there is at most one indexj0∈ Nsuch that
Aj0 is uncountable and we get then

H
˝
j∈N
Aj
I
=(A)=1=1+0+0+…= (Aj0)+
É
j≠j0
(Aj).
(iii) Wehaveanarbitrarymeasurablespace (X,A)andthemeasure ðAð=
⎧
⎪
⎨
⎪⎩
#A, ifAis ﬁnite
∞, else
.
(M1)Sinceç contains no elements,#ç=0 andðçð=0 .
(M2)Let(Aj)j∈N be a sequence of pairwise disjoint sets inA. Case 1: AllAj are ﬁnite and
only ﬁnitely many, say the ﬁrstk, are non-empty, thenA = ⋃
j∈NAj is eﬀectively a ﬁnite
union ofkﬁnite sets and it is clear that
ðAð= ðA1ð+…+ ðAkð+ðçð+ðçð+…=
É
j∈N
ðAjð.
33

R.L. Schilling: Measures, Integrals & Martingales
Case 2: AllAj are ﬁnite and inﬁnitely many are non-void. Then their unionA= ⋃
j∈NAj
is an inﬁnite set and we get
ðAð=∞=
É
j∈N
ðAjð.
Case 3: At least oneAj is inﬁnite, and so is then the unionA= ⋃
j∈NAj. Thus,
ðAð=∞=
É
j∈N
ðAjð.
(iv) Onacountableset Ω={ !1,!2,…}wedeﬁneforasequence(pj)j∈N⊂[0,1]with∑
j∈Npj =
1 the set function
P(A)=
É
j∶!j∈A
pj =
É
j∈N
pj!j(A), A⊂ Ω.
(M1)P(ç)=0 is obvious.
(M2)Let(Ak)k∈N be pairwise disjoint subsets ofΩ. Then
É
k∈N
P(Ak)=
É
k∈N
É
j∈N
pj!j(Ak)
=
É
j∈N
É
k∈N
pj!j(Ak)
=
É
j∈N
pj
0 É
k∈N
!j(Ak)
1
=
É
j∈N
pj!j
 ∪
k
Ak

=P ∪
k
Ak
.
The change in the order of summation needs justiﬁcation; one possibility is the argument
used in the solution of Problem 4.7(ii). (Note that the reordering theorem for absolutely
convergent series is not immediately applicable since we deal with a double series!)
(v) This is obvious.
■■
Problem 4.3 Solution:
• On(R,ℬ(R)) the function is not be a measure, since we can take the setsA = (1,∞),
B=(−∞,−1)which are disjoint, not countable andboth have non-countable complements.
Hence,(A)= (B)=1 . On the other hand,A⊍B is non-countable and has non-countable
complement,[−1,1]. So,(A⊍B ) = 1. This contradicts the additivity:(A⊍B ) = 1≠
2= (A)+ (B). Notice that the choice of the-algebraA avoids exactly this situation.ℬ
is the wrong-algebra for.
34

Solution Manual. Last update 18th July 2019
• On Q (and, actually, any possible-algebra thereon) the problem is totally diﬀerent: ifA
is countable, thenAc = Q ⧵A is also countable and vice versa. This means that(A) is,
according to the deﬁnition, both1 and0 which is, of course, impossible. This is to say: is
not well-deﬁned. makes only sense on a non-countable setX.
■■
Problem 4.4 Solution:
(i) IfA ={ç, R}, then is a measure.
But as soon asA contains one setA which is trivial (i.e. eitherç orX), we have actually
Ac ∈A which is also non-trivial. Thus,
1= (X)= (A⊍A c) ≠(A)+ (Ac)=1+1=2
and cannot be a measure.
(ii) If we equipR with a-algebra which contains sets such that bothA andAc can be inﬁnite
(the Borel-algebra would be such an example:A= (−∞,0) - ⇒Ac = [0,∞)), then is
not well-deﬁned. The only type of sets where is well-deﬁned is, thus,
A ∶={A⊂ R∶#A< ∞ or #Ac <∞}.
But this is no-algebra as the following example shows:Aj ∶= {j} ∈A, j ∈ N, are
pairwise disjoint sets but⋃
j∈NAj = N is not ﬁnite and its complement isR ⧵ N not ﬁnite
either! Thus, N∉A, showing thatA cannot be a-algebra. We conclude that can never
beameasureifthe -algebracontainsinﬁnitelymanysets. Ifwearehappywithﬁnitelymany
sets only, then here is an example that makes into a measureA ={ç,{69}, R ⧵{69}, R}
and similar families are possible, but the point is that they all contain only ﬁnitely many
members.
■■
Problem 4.5 Solution: Denote by one-dimensional Lebesgue measure and consider the Borel sets
Bk∶=(k,∞). Clearly⋂
kBk=ç ,k∈ N, so thatBk ↓ç. On the other hand,
(Bk)=∞ - ⇒inf
k
(Bk)=∞ ≠0= (ç)
which shows that the ﬁniteness condition is indeed essential.
■■
Problem 4.6 Solution: Mind the typo in the problem: it should read “inﬁnite mass” – otherwise the
problem is pointless.
Solution 1:Deﬁne a measure which assigns every pointn− 1
2k,n∈ Z,k∈ N the mass 1
2k:
=
É
n∈Z
É
k∈N
1
2kn− 1
2k
.
35

R.L. Schilling: Measures, Integrals & Martingales
(Since Z×Niscountable,Problem4.7showsthatthisobjectisindeedameasure!) Obviously,any
interval[a,b)oflength b−a> 2containssomeinteger,say m∈[a,b)sothat [m−1∕2,m)⊂[a,b),
thus
[a,b) ⩾[m−1∕2,m)=
É
k∈N
1
2k =∞.
On the other hand, the sequence of sets
Bn∶=
n˝
k=−n
k−1,k − 1
2n

satisﬁes(Bn)<∞and⋃
nBn= R.
Solution 2:Set(B) ∶= #(B∩ Q),B ∈ ℬ(R), i.e. the counting measure of the rationals inR.
Clearly,[a,b) = ∞for every (non-empty) interval witha < b. On the other hand, if(qk)k∈N
is an enumeration ofQ, the setsBn∶=( R ⧵ Q)∪{ q1,…,qn} satisfy
Bn ↑ R and (Bn)= n,
i.e. is-ﬁnite.
■■
Problem 4.7 Solution:
(i) Clearly,∶=a+b∶A →[0,∞] (sincea,b ⩾0!). We check(M1),(M2).
(M1)Clearly,(ç)= a(ç)+ b(ç)= a⋅0+ b⋅0=0 .
(M2)Let(Aj)j∈N⊂A be mutually disjoint sets. Then we can use the-additivity of, to
get

0 ˝
j∈N
Aj
1
=a
0 ˝
j∈N
Aj
1
+b
0 ˝
j∈N
Aj
1
=a
É
j∈N
(Aj)+ b
É
j∈N
(Aj)
=
É
j∈N
 a(Aj)+ b(Aj)
=
É
j∈N
(Aj).
Since all quantities involved are positive and since we allow the value+∞ to be attained,
there are no convergence problems.
(ii) Sinceall j arepositive,thesum ∑
j∈Njj(A)isasumofpositivequantitiesand,allowing
the value+∞ to be attained, there is no convergence problem. Thus, ∶ A → [0,∞] is
well-deﬁned. Before we check(M1),(M2)we prove the following
Lemma. Letij,i,j ∈ N, be real numbers. Then
sup
i∈N
sup
j∈N
ij =sup
j∈N
sup
i∈N
ij.
36

Solution Manual. Last update 18th July 2019
Proof. Observe that we havemn ⩽supj∈Nsupi∈Nij for allm,n ∈ N. The right-hand side
is independent ofmandnand we may take thesup over alln
sup
n∈N
mn ⩽sup
j∈N
sup
i∈N
ij ∀m∈ N
and then, with the same argument, take thesupover allm
sup
m∈N
sup
n∈N
mn ⩽sup
j∈N
sup
i∈N
ij ∀m∈ N.
Theoppositeinequality,‘⩾’,followsfromthesameargumentwith iandj interchanged.
(M1)We have(ç)= ∑
j∈Njj(ç)= ∑
j∈Nj⋅0=0 .
(M2) Take pairwise disjoint sets(Ai)i∈N ⊂A. Then we can use the-additivity of each of
thej’s to get

0˝
i∈N
Ai
1
=
É
j∈N
jj
0˝
i∈N
Ai
1
= lim
N→∞
NÉ
j=1
j
É
i∈N
j
 Ai

= lim
N→∞
NÉ
j=1
j lim
M→∞
MÉ
i=1
j
 Ai

= lim
N→∞
lim
M→∞
NÉ
j=1
MÉ
i=1
jj
 Ai

= sup
N∈N
sup
M∈N
NÉ
j=1
MÉ
i=1
jj
 Ai

where we use that the limits are increasing limits, hence suprema. By our lemma:

0˝
i∈N
Ai
1
= sup
M∈N
sup
N∈N
MÉ
i=1
NÉ
j=1
jj
 Ai

= lim
M→∞
lim
N→∞
MÉ
i=1
NÉ
j=1
jj
 Ai

= lim
M→∞
MÉ
i=1
É
j∈N
jj
 Ai

= lim
M→∞
MÉ
i=1
 Ai

=
É
i∈N
 Ai
.
■■
37

R.L. Schilling: Measures, Integrals & Martingales
Problem 4.8 Solution: Finite additivity implies monotonicity:A⊂B - ⇒B=A⊍ (B ⧵A)and so
(B)= (A⊍ (B ⧵A))= (A)+ (B ⧵A) ⩾(A).
LetBn ↑B andDn∶=Bn ⧵Bn−1 withB0∶=ç . This gives

0 ∞˝
n=1
Bn
1
⩾sup
n∈N
(Bn)= sup
n∈N

0 nÓ
i=1
Di
1
(1)
= sup
n∈N
nÉ
i=1
(Di)=
∞É
i=1
(Di)
(2)
⩾ 
0 ∞˝
i=1
Di
1
=
0 ∞˝
n=1
Bn
1
.
where we use ﬁnite additivity for (1) and-subaddtitivity for (2).
■■
Problem 4.9 Solution: Set(A) ∶=(A∩F). We know, by assumption, that is a measure on
(X,A). We have to show that is a measure on(X,A). SinceF ∈A, we haveF ∩A∈A for
allA∈ A, so is well-deﬁned. Moreover, it is clear that(A) ∈ [0,∞]. Thus, we only have to
check
(M1)(ç)= (ç∩ F)= (ç)=0 .
(M2) Let(Aj)j∈N ⊂A be a sequence of pairwise disjoint sets. Then also(Aj∩F)j∈N ⊂A are
pairwise disjoint and we can use the-additivity of to get

0 ˝
j∈N
Aj
1
=
0
F ∩
˝
j∈N
Aj
1
=
0 ˝
j∈N
(F ∩Aj)
1
=
É
j∈N
(F ∩Aj)
=
É
j∈N
(Aj).
■■
Problem 4.10 Solution: SinceP isaprobabilitymeasure, P(Ac
j)=1− P(Aj)=0 . By-subadditivity,
P
0 ˝
j∈N
Ac
j
1
⩽
É
j∈N
P(Ac
j),=0
and we conclude that
P
0 Ì
j∈N
Aj
1
=1− P
04 Ì
j∈N
Aj
5c1
=1− P
0 ˝
j∈N
Ac
j
1
=1−0=0 .
■■
38

Solution Manual. Last update 18th July 2019
Problem 4.11 Solution: Note that
˝
j
Aj ⧵
˝
k
Bk=
˝
j
0
Aj ⧵
˝
k
Bk
«ﬂ‹
⊃Bj ∀j
1
⊂
˝
j
 Aj ⧵Bj

Since⋃
jBj ⊂ ⋃
jAj we get from-subadditivity

0˝
j
Aj
1
−
0˝
j
Bj
1
=
0˝
j
Aj ⧵
˝
k
Bk
1
⩽
0˝
j
 Aj ⧵Bj
1
⩽
É
j
(Aj ⧵Bj).
■■
Problem 4.12 Solution:
(i) We haveç∈ A and(ç)=0 , thusç∈ N.
(ii) SinceM ∈ A (this is essential in order to apply toM!) we can use the monotonicity of
measures to get0 ⩽(M) ⩽(N)=0 , i.e.(M)=0 andM ∈N follows.
(iii) Since allNj ∈ A, we getN ∶= ⋃
j∈NNj ∈ A. By the-subadditivity of a measure we
ﬁnd
0 ⩽(N)= 
0 ˝
j∈N
Nj
1
⩽
É
j∈N
(Nj)=0 ,
hence(N)=0 and soN ∈N.
■■
Problem 4.13 Solution:
(i) Theone-dimensionalBorelsets ℬ∶=ℬ(R)aredeﬁnedasthesmallest -algebracontaining
the open sets. Pickx ∈ R and observe that the open intervals(x− 1
k,x + 1
k),k ∈ N, are
all open sets and therefore(x− 1
k,x + 1
k)∈ ℬ. Since a-algebra is stable under countable
intersections we get{x}= ⋂
k∈N(x− 1
k,x + 1
k)∈ ℬ.
Using the monotonicity of measures and the deﬁnition of Lebesgue measure we ﬁnd
0 ⩽({x}) ⩽((x− 1
k,x + 1
k))=( x+ 1
k)−( x− 1
k)= 2
k , , , , , , , , , , , , , , , , , , , , →
k→∞
0.
[Following the hint leads to a similar proof with[x− 1
k,x + 1
k)instead of(x− 1
k,x + 1
k).]
(ii) a) Since Q is countable, we ﬁnd an enumeration{q1,q2,q3,…} and we get triviallyQ =
⋃
j∈N{qj}whichisadisjointunion. (Thisshows,bytheway,that Q∈ℬas{qj}∈ ℬ.)
Therefore, using part (i) of the problem and the-additivity of measures,
(Q)= 
0 ˝
j∈N
{qj}
1
=
É
j∈N
({qj})=
É
j∈N
0=0 .
39

R.L. Schilling: Measures, Integrals & Martingales
b) Take again an enumerationQ = {q1,q2,q3,…}, ﬁx >0 and deﬁneC() as stated in
the problem. Then we haveC() ∈ℬ and Q ⊂ C(). Using the monotonicity and
-subadditivity ofwe get
0 ⩽(Q) ⩽ C()
=
0 ˝
k∈N
[qk−2−k,qk+2−k)
1
⩽
É
k∈N
 [qk−2−k,qk+2−k)
=
É
k∈N
2⋅⋅2−k
=2
1
2
1− 1
2
=2.
As >0 was arbitrary, we can make →0 and the claim follows.
(iii) Since⋃
0⩽x⩽1{x} is a disjoint union, only the countability assumption is violated. Let’s see
what happens if we could use ‘-additivity’ for such non-countable unions:
0=
É
0⩽x⩽1
0=
É
0⩽x⩽1
({x})= 
0 ˝
0⩽x⩽1
{x}
1
=([0,1])=1
which is impossible.
■■
Problem 4.14 Solution: Without loss of generality we may assume thata ≠ b; set ∶= a+b.
Then(B)=0 if, and only if,a∉B andb∉B. Since{a},{b} and{a,b} are Borel sets, all null
sets of are given by
N= B ⧵{a,b}∶ B∈ℬ(R).
(This shows that, in some sense, null sets can be fairly large!).
■■
Problem 4.15 Solution: Let us writeN for the family of all (proper and improper) subsets of null
sets. We note that sets inNcan be measurable (that is:N ∈A) but need not be measurable.
(i) Sinceç∈ N, weﬁndthatA=A∪ç∈ A forevery A∈A; thus,A ⊂A. Letuscheckthat
A is a-algebra.
(Σ1) Sinceç∈ A ⊂A, we haveç∈ A.
(Σ2) LetA∗∈A. ThenA∗=A∪N forA∈A andN ∈ N. By deﬁnition,N ⊂M ∈A
where(M)=0 . Now
A∗c =(A∪N)c =Ac∩Nc
=Ac∩Nc∩(Mc∪M)
40

Solution Manual. Last update 18th July 2019
=(Ac∩Nc∩Mc)∪( Ac∩Nc∩M)
=(Ac∩Mc)∪( Ac∩Nc∩M)
where we use thatN ⊂M, henceMc ⊂N c, henceMc∩Nc =Mc. But now we see
thatAc∩Mc ∈A andAc∩Nc∩M ∈ N sinceAc∩Nc∩M ⊂M andM ∈A is a
 null set:(M)=0 .
(Σ3) Let (A∗
j)j∈N be a sequence ofA-sets. From its very deﬁnition we know that each
A∗
j =Aj∪Nj for some (not necessarily unique!)Aj ∈A andNj ∈ N. So,
˝
j∈N
A∗
j =
˝
j∈N
(Aj∪Nj)=
0 ˝
j∈N
Aj
1
∪
0 ˝
j∈N
Nj
1
=∶A∪N.
SinceA is a-algebra,A∈A. All we have to show is thatNj is inN. Since eachNj
is a subset of a (measurable!) null set, say,Mj ∈ A, we ﬁnd thatN = ⋃
j∈NNj ⊂
⋃
j∈NMj =M ∈A and all we have to show is that(M)=0 . But this follows from
-subadditivity,
0 ⩽(M)= 
0 ˝
j∈N
Mj
1
⩽
É
j∈N
(Mj)=0 .
Thus,A∪N ∈A.
(ii) As already mentioned in part (i),A∗ ∈ A could have more than one representation, e.g.
A∪N =A∗ =B∪M withA,B ∈A andN,M ∈ N. If we can show that(A)= (B)
then the deﬁnition of̄ is independent of the representation ofA∗. Since M,N are not
necessarily measurable but, by deﬁnition, subsets of (measurable) null setsM‡,N ‡∈A we
ﬁnd
A⊂A ∪N =B∪M ⊂B∪M‡,
B ⊂B∪M =A∪N ⊂A∪N‡
andsince A,B,B ∪M‡,A∪N‡∈A,wegetfrommonotonicityandsubadditivityofmeasures
(A) ⩽(B∪M‡) ⩽(B)+ (M‡)= (B),
(B) ⩽(A∪N‡) ⩽(A)+ (N‡)= (A)
which shows(A)= (B).
(iii) We check (M1) and (M2)
(M1) Sinceç=ç∪ç∈ A,ç∈ A,ç∈ N, we havē (ç)= (ç)=0 .
(M2) Let(A∗
j)j∈N⊂A beasequenceofpairwisedisjointsets. Then A∗
j =Aj∪Nj forsome
Aj ∈A andNj ∈ N. These sets are also mutually disjoint, and with the arguments in
(i) we see thatA∗ = A∪N whereA∗ ∈ A,A ∈ A,N ∈ N stand for the unions of
41

R.L. Schilling: Measures, Integrals & Martingales
A∗
j,Aj andNj, respectively. Sincē does not depend on the special representation of
A-sets, we get
̄ 
0 ˝
j∈N
A∗
j
1
= ̄ (A∗)= (A)= 
0 ˝
j∈N
Aj
1
=
É
j∈N
(Aj)
=
É
j∈N
̄ (A∗
j)
showing that̄ is-additive.
(iv) LetM∗ be ā null set, i.e.M∗∈A and ̄ (M∗)=0 . Take anyB ⊂M∗. We have to show
that B ∈ A and ̄ (B) = 0. The latter is clear from the monotonicity of̄ once we have
shown thatB∈A which means, once we know that we may plugB into ̄ .
Now,B ⊂ M∗ andM∗ = M∪N for someM ∈A andN ∈ N. As ̄ (M∗) = 0we also
know that(M) = 0. Moreover, we know from the deﬁnition ofN thatN ⊂ N‡for some
N‡∈A with(N‡)=0 . This entails
B ⊂M∗=M∪N ⊂M∪N‡∈A
and (M∪N‡) ⩽(M)+ (N‡)=0 .
HenceB∈ Nas well asB=ç∪ B∈A. In particular,̄ (B)= (ç)=0 .
(v) SetC ={A∗⊂X ∶∃A,B ∈A, A⊂A ∗A⊂B,  (B ⧵A)=0} . We have to show that
A =C.
TakeA∗ ∈A. ThenA∗ =A∪N withA∈A,N ∈ N and chooseN‡∈A,N ⊂N‡and
(N‡)=0 . This shows that
A⊂A ∗=A∪N ⊂A∪N‡=∶B∈A
andthat (B ⧵A)= ((A∪N‡)⧵A) ⩽(N‡)=0 . (Notethat(A∪N‡)⧵A=(A∪N‡)∩Ac =
N‡∩Ac ⊂N ‡and that equality need not hold!).
Conversely,takeA∗∈C. Then,bydeﬁnition,A⊂A ∗⊂B withA,B ∈A and(B⧵A)=0 .
Therefore,N ∶=B ⧵A is a null set and we see thatA∗ ⧵A⊂B ⧵A, i.e.A∗ ⧵A∈ N. So,
A∗=A∪(A∗ ⧵A)whereA∈A andA∗ ⧵A∈ Nshowing thatA∗∈A.
■■
Problem 4.16 Solution: Set
Σ∶= F▵N ∶F ∈ℱ, N∈N.
anddenote,withoutfurthermentioning,by F,F j resp.N,N j setsfrom ℱ resp.N. SinceF▵ç=
F,ç▵N =N andF▵N ∈(ℱ,N)we get
ℱ, N ⊂Σ⊂(ℱ,N) (*)
42

Solution Manual. Last update 18th July 2019
and the ﬁrst assertion follows if we can show thatΣ is a-algebra. In this case, we can apply the
-operation to the inclusions (*) and get
(ℱ,N)⊂(Σ)⊂((ℱ,N))
which is just
(ℱ,N)⊂Σ⊂(ℱ,N).
To see thatΣ is a-algebra, we check conditions (Σ1)–(Σ3).
(Σ1): Clearly,X∈ℱ andN ∈N so thatX=X▵ç∈Σ ;
(Σ2): We have, using de Morgan’s identities over and over again:
[F▵N]c =[(F ⧵N)∪( N ⧵F)]c
=(F ∩Nc)c∩(N∩Fc)c
=(Fc∪N)∩( Nc∪F)
=(Fc∩Nc)∪( Gc∩G)∪( N∩Nc)∪( N∩F)
=(Fc∩Nc)∪( N∩F)
=(Fc ⧵N)∪( N ⧵Fc)
= Fc
«ﬂ‹
∈ℱ
▵N
∈Σ;
(Σ3): We begin by a few simple observations, namely that for allF ∈ℱ andN,N ‡∈N
F ∪N =F▵(N ⧵F)
«›ﬂ›‹
∈N
∈Σ; (a)
F ⧵N =F▵(N∩F)
«›ﬂ›‹
∈N
∈Σ; (b)
N ⧵F =N▵(F ∩N)
«›ﬂ›‹
∈N
∈Σ; (c)
(F▵N)∪ N‡=  F▵N▵ N‡ ⧵(F▵N)
=F▵

N▵(N‡ ⧵(F▵N))

«››››››››››››››ﬂ››››››››››››››‹
∈N
∈Σ, (d)
where we use Problem 2.6(ii) and part (a) for (d).
Now let(Fj)j∈N ⊂ ℱ and(Nj)j∈N ⊂ N and setF ∶= ⋃
jFj ∈ ℱ and, because of-
subadditivity of measuresN ∶= ⋃
jNj ∈N. Then
F ⧵N =
˝
j∈N
(Fj ⧵N)⊂
˝
j∈N
(Fj ⧵Nj)⊂
˝
j∈N
Fj =F
43

R.L. Schilling: Measures, Integrals & Martingales
as well as
ç⊂
˝
j∈N
(Nj ⧵Fj)⊂
˝
j∈N
Nj =N
which shows that
F ⧵N ⊂
˝
j∈N
(Fj▵Nj)⊂F ∪N. (**)
Sinceℱ,N ⊂A, and consequently⋃
j∈N(Fj▵Nj)∈ A, and sinceA-measurable subsets
of null sets are again inN, the inclusions (**) show that there exists someN‡∈N so that
˝
j∈N
(Fj▵Nj)=( F ⧵N)
«›ﬂ›‹
∈Σ,cf. (b)
∪N‡∈Σ
where we use (d) for the last inclusion.
■■
Problem 4.17 Solution: By deﬁnition,
A = A∪N ∶A∈A, N∈N.
Since
A∪N =A▵(N ⧵A)
«ﬂ‹
∈N
and since by an application of Problem 4.16 to(X,A, ̄ ),A,N (instead of(X,A,),G,N) we
get
(A,N)= A▵N ∶A∈A, N∈N
and we conclude that
A ⊂(A,N).
On the other hand,
A ⊂A and N ⊂A
so that, sinceA is a-algebra,
(A,N)⊂(A)= A ⊂(A,N).
Finally, assume thatA∗∈A andA∈A. ThenA=A∗▵N and we get
A∗▵A=A▵N▵A=(A▵A)▵N =N.
Notethatthisresultwouldalsofollowdirectlyfrom4.15sinceweknowfromtherethat A∗=A∪N
so that
A∗▵A=(A∪N)▵A=A▵(N ⧵A)▵A=N ⧵A
■■
44

Solution Manual. Last update 18th July 2019
Problem 4.18 Solution: Denotethecompletionby ℬ∗ andwrite Nx forallsubsetsofBorelnullsets
ofx. Clearly,
Nx={A⊂ Rn∶x∉A}.
RecallfromProblem4.15(i)that ℬ∗containsallsetsoftheform B∪N withB∈ℬandN ∈Nx.
Now letC ⊂Rn be any set. Ifx∈C, then write
C = {x}
«ﬂ‹
∈ℬ
∪(C ⧵{x})
«››ﬂ››‹
∈Nx
∈ℬ∗;
Otherwise,x∉C and
C =C ⧵{x}= ç
«ﬂ‹
∈ℬ
∪(C ⧵{x})
«››ﬂ››‹
∈Nx
∈ℬ∗.
This shows thatℬ∗=P(Rn)is the power set ofRn.
■■
Problem 4.19 Solution:
(i) Sinceℬ is a-algebra, it is closed under countable (disjoint) unions of its elements, thus
inherits the properties (M1), (M2) directly from.
(ii) Yes [yes], since the full spaceX∈ℬ so that(X)= (X)is ﬁnite [resp.=1 ].
(iii) No,-ﬁniteness is also a property of the-algebra. Take, for example, Lebesgue measure
on the Borel sets (this is-ﬁnite) and consider the-algebraC ∶={ç,(−∞,0),[0,∞), R}.
ThenóóóC
isnot -ﬁnitesincethereisnoincreasingsequenceof C-setshavingﬁnitemeasure.
■■
Problem 4.20 Solution: By deﬁnition, is-ﬁnite if there is anincreasingsequence(Bj)j∈N ⊂A
suchthat Bj ↑X and(Bj)<∞. Clearly,Ej ∶=Bj satisﬁestheconditioninthestatementofthe
problem.
Conversely, let(Ej)j∈N be as stated in the problem. ThenBn ∶= E1∪…∪ En is measurable,
Bn ↑X and, by subadditivity,
(Bn)= (E1∪…∪ En) ⩽
nÉ
j=1
(Ej)<∞.
Remark: A small change in the above argument allows to take pairwise disjoint setsEj.
■■
Problem 4.21 Solution:
45

R.L. Schilling: Measures, Integrals & Martingales
(i) Fix >0andchoosefor A∈Σ setsU ∈O,F ∈ℱ suchthat F ⊂A⊂U and(U ⧵F)< .
SetU‡∶=Fc ∈O andF‡∶=Uc ∈ℱ. Then we have
F‡⊂A c ⊂U ‡andU‡ ⧵F‡=Fc ⧵Uc =Fc∩U =U ⧵F
and so(U‡ ⧵F‡)= (U ⧵F)< . This means thatAc ∈Σ .
Denote byd(x,y) the distance of two pointsx,y ∈ X and writeB1∕n(0) for the open ball
{y∈X∶d(y,0)< 1
n}. AsinthesolutionofProblem3.14(ii)weseethat Un∶=F+B1∕n(0)
is a sequence of open sets such thatUn ↓ F. Because of the continuity of measures we get
(Un ⧵F) , , , , , , , , , , , , , , , , , , , , →
n→∞
0 and sinceℱ ∋F ⊂F ⊂Un∈O, this means thatℱ ⊂Σ.
(ii) Fix >0 and pick forAj ∈ Σ,j = 1,2, open setsUj and closed setsFj such thatFj ⊂
A⊂U j and(Uj ⧵Fj)< . ThenF1∩F2 andU1∩U2 are again closed resp. open, satisfy
F1∩F2⊂A 1∩A2⊂U 1∩U2 as well as
 (U1∩U2) ⧵(F1∩F2)= (U1∩U2)∩( Fc
1 ∪Fc
2)
= [(U1∩U2) ⧵F1]∪[( U1∩U2) ⧵F2]
⩽ (U1∩U2) ⧵F1
+ (U1∩U2) ⧵F2

<2.
This shows thatΣis∩-stable.
(iii) Fix and pick for a given sequence(Aj)j∈N⊂Σ open setsUj and closed setsFj such that
Fj ⊂A j ⊂U j and(Uj ⧵Fj)<2−j.
SetA∶= ⋃
jAj. ThenU ∶= ⋃
jUj ⊃A is an open set wileF ∶= ⋃
jFj is contained inA
but it is only an increasing limit of closed setsΦn∶=F1∪…∪ Fn. Using Problem 4.11 we
get
(U ⧵F) ⩽
É
j
(Uj ⧵Fj) ⩽
É
j
2−j ⩽.
SinceΦn⊂A⊂U andU ⧵Φn ↓U ⧵F, we can use the continuity of measures to conclude
thatinfn(U ⧵Φn) =(U ⧵F) ⩽ , i.e.(U ⧵ΦN) ⩽2 ifN = N is suﬃciently large.
This shows thatΣcontains all countable unions of its members. Because of part (i) it is also
stable under complementation and contains the empty set. Thus,Σis a-algebra.
Asℱ ⊂Σandℬ=(ℱ), we haveℬ⊂Σ.
(iv) For any Borel setB∈Σ and any >0we can ﬁnd open and closed setsU andF, respect-
ively, such thatF ⊂B ⊂U and
(B ⧵F) ⩽(U ⧵F)< - ⇒(B) ⩽+(F),
(U ⧵B) ⩽(U ⧵F)< - ⇒(B) ⩾(U)− .
46

Solution Manual. Last update 18th July 2019
Thus,
sup
F⊂B,F ∈ℱ
(F) ⩽(B) ⩽+(F) ⩽+ sup
F⊂B,F ∈ℱ
(F)
inf
U⊃B,U ∈O
(U)−  ⩽(U)−  ⩽(b) ⩽ inf
U⊃B,U ∈O
(U).
(v) For every closedF ∈ℱ the intersectionsKj∩F,j∈ N, will be compact andKj∩F ↑F.
By the continuity of measures we get
(F)=sup
j
(Kj∩F) ⩽ sup
K⊂F,K cpt
(K) ⩽(F).
Thus,
(F)= sup
K⊂F,K cpt
(K) ∀ F ∈ℱ. (*)
Combining (iv) and (*) we get
(B)
(iv)
= sup
F⊂B,F ∈ℱ
(F)
(*)
= sup
F⊂B,F ∈ℱ
sup
K⊂F,K cpt
(K)
⩽ sup
F⊂B,F ∈ℱ
sup
K⊂B,K cpt
(K)
«››››››ﬂ››››››‹
note: independent ofF⊂B
= sup
K⊂B,K cpt
(K)
and since(K) ⩽ (B) forK ⊂ Band supK⊂B,K cpt(K) ⩽ (B) are obvious, we are
ﬁnished.
(vi) Assume now that is-ﬁnite. Let(Bn)n∈N ⊂ ℬ be an exhausting sequence forX such
that (Bn) < ∞. Then the measuresn(B) ∶= (B ∩Bn) deﬁned onℬ are ﬁnite and
regular according to part (iv). Since we may interchange any two suprema (cf. the solution
of Problem 4.7) we get
(B)=sup
n
n(B)=sup
n
sup
F⊂B,F ∈ℱ
n(F)
= sup
F⊂B,F ∈ℱ
sup
n
n(F)
= sup
F⊂B,F ∈ℱ
(F).
■■
Problem 4.21 Solution: First of all, Problem 4.21(iv) shows that
(B)= sup
F⊂B,F closed
(F). (*)
47

R.L. Schilling: Measures, Integrals & Martingales
Let(dk)k beanenumerationofthedenseset D⊂X andwrite forthemetricin X andKr(x)∶=
{y∈X∶(x,y) ⩽r} for the closed ball with centrex and radiusr.
Since, for any ﬁxedn∈ N the sets
K1∕n(d1)∪ ⋯∪K1∕n(dm) ↑X for m →∞
we get from (*)
∀ >0 ∃ k(n)∈ N∶(Fn)+ 
2n ⩾(X)
ifFn∶=K1∕n(d1)∪ ⋯∪K1∕n(dk(n)). Setting
K ∶=K ∶=
Ì
n
Fn
it is clear thatK is closed. Moreover, sinceK is, for every1∕n, covered by ﬁnitely many balls of
radius1∕n, to wit,
K ⊂K1∕n(d1)∪ ⋯∪K1∕n(dk(n)),
we see thatK is compact. Indeed, if(xj)j ⊂K is a sequence, there is a subsequence(xn
j)j which
is completely contained in one of the ballsK1∕n(d1),…,K1∕n(dk(n)). Passing iteratively to sub-
sub-etc.sequencesweﬁndasubsequence (yj)j ⊂(xj)j whichiscontainedinasequenceofclosed
ballsK1∕n(cn) (cn is a suitable element fromD). Thus(yj)j is a Cauchy sequence and converges,
becauseofcompleteness,toanelement x∗ whichis, asthe Fn areclosed, inevery Fn,hencein K.
ThusK is (sequentially) compact.
Since
(X ⧵K)= 
0˝
n
X ⧵Fn
1
⩽
É
n
(X ⧵Fn) ⩽
É
n

2n =,
we have found a sequence of compact setsKn such that(Kn) →(X)(note that theKn need not
‘converge’X asaset!). Obviously,Kn∩F iscompactforeveryclosed F andwehave (Kn∩F) →
(F), hence
(F)= sup
K⊂F,K cpt
(K) ∀ F ∈ℱ.
Now we can use the argument from the proof of Problem 4.22(v).
■■
48

5 Uniqueness of measures.
Solutions to Problems 5.15.13
Problem 5.1 Solution: SinceX∈D and since complements are again inD, we haveç= Xc ∈D.
IfA,B ∈ D are disjoint, we setA1 ∶= A,A2 ∶= B,Aj ∶= ç ∀j ⩾ 3. Then(Aj)j∈N ⊂ D is a
sequence of pairwise disjoint sets, and by (D3) we ﬁnd that
A⊍B =
Ó
j∈N
Aj ∈D.
Since (Σ1)= (D3), (Σ2)= (D2) and since (Σ3) - ⇒ (D3), it is clear that every-algebra is also a
Dynkin system; that the converse is, in general, wrong is seen in Problem 5.2.
■■
Problem 5.2 Solution: Consider (D3) only, as the other two conditions coincide:(Σj) = (Δj), j=
1,2. Weshowthat( Σ3)breaksdownevenforﬁniteunions. If A,B ∈D aredisjoint,itisclearthat
A,B and alsoA⊍B contain an even number of elements. But ifA,B have non-void intersection,
and if this intersection contains an odd number of elements, thenA∪B contains an odd number
of elements. Here is a trivial example:
A={1,2}∈ D, B ={2,3,4,5}∈ D,
whereas
A∪B={1,2,3,4,5}∉ D.
This means that (D3) holds, but (Σ3) fails.
■■
Problem 5.3 Solution: We verify the hint ﬁrst. Using de Morgan’s laws we get
R ⧵Q=R ⧵(R∩Q)= R∩(R∩Q)c =(Rc∪(R∩Q))c =(Rc⊍(R∩Q))c
where the last equality follows sinceRc∩(R∩Q)=ç .
Now we takeA,B ∈D such thatA⊂B . In particularA∩B=A. Taking this into account and
settingQ=A,R =B we get from the above relation
B ⧵A=   Bc
«ﬂ‹
∈D
⊍A
«›››ﬂ›››‹
∈D
c
∈D
49

R.L. Schilling: Measures, Integrals & Martingales
where we repeatedly use (D2) and (D2).
■■
Problem 5.4 Solution:
(i) Since the-algebraA is also a Dynkin system, it is enough to prove(D) =D for any
Dynkin systemD. By deﬁnition,(D) is the smallest Dynkin system containingD, thus
D ⊂ (D). On the other hand,D is itself a Dynkin system, thus, because of minimality,
D ⊃(D).
(ii) Clearly,G ⊂ℋ ⊂ (ℋ). Since(ℋ) is a Dynkin system containingG, the minimality of
(G)implies that(G)⊂(ℋ).
(iii) Since(G) is a-algebra, it is also a Dynkin system. SinceG ⊂ (G) we conclude (again,
by minimality) that(G)⊂(G).
Combining both deﬁnitions, i.e. (D1)–(D‡
3) and (D1)–(D3), we see thatX ∈ D. Stability under
incrasinglimitsfollowsfrom(D ‡
3)andif Dn ↓Dweget Dc
n ↑Dc,i.e.thestabilityunderdecreasing
limits follows from (D2), (D‡
3) and deMorgan’s laws.
■■
Problem 5.5 Solution: Clearly,({A,B})⊂({A,B}) is always true.
By Theorem 5.5,({A,B}) =({A,B}) if{A,B} is∩-stable, i.e. ifA = B orA = Bc or if at
least one ofA,B isX orç.
Let us exclude these cases. IfA∩B=ç , then
({A,B})= ({A,B})= ç,A,A c,B,B c,A⊍B,A c∩Bc,X.
IfA∩B ≠ç, then
({A,B})= ç,A,A c,B,B c,X}
while({A,B}) is much larger containing, for example,A∩B.
■■
Problem 5.6 Solution: Someauthorscallfamiliesofsetssatisfying(D 1),(D‡
2),(D‡
3)monotoneclasses
(this is not the standard deﬁnition!). We will use this conventionlocally for this solution only.
Clearly, such a monotone classℱ is a Dynkin system:
C,D ∈ℱ, C ∩D=ç
(D1)
- - - - - - - - - - - - - - ⇒
(D‡
2)
C⊍D =E ⧵ (E ⧵C) ⧵D
«››››ﬂ››››‹
E⧵C⊃D asC∩D=ç
∈ℱ,
i.e.,ℱ is⊍-stable. This and (D‡
3) yield (D3); (D2) is a special case of (D‡
2).
Converselyevery Dynkin systemD is a monotone class in the sese of this problem:
M,N ∈D, M ⊂N
(D2)
- - - - - - - - - - - - - - ⇒
(D3)
Nc∩M =M ⧵N =ç and N ⧵M =(Nc⊍M)c ∈D,
50

Solution Manual. Last update 18th July 2019
i.e. (D‡
2) holds. Thus, (D3) immediately implies (D‡
3).
■■
Problem 5.7 Solution: We prove the hint ﬁrst. Let(Gj)j∈N ⊂ G as stated in the problem, i.e.
satisfying (1) and (2), and deﬁne the setsFN ∶= G1 ∪…∪ GN. As G ⊂ A, it is clear that
FN ∈A (but not necessarily inG...). Moreover, it is clear thatFN ↑X.
We begin with a more general assertion:For any ﬁnite union ofG-setsA1∪…∪ AN we have
(A1∪…∪ AN)= (A1∪…∪ AN).
Proof. Induction Hypothesis:(A1∪…∪ AN) =(A1∪…∪ AN) for someN ∈ N and any
choice ofA1,…,AN ∈G.
Induction Start(N =1) : is obvious.
Induction StepN ⇝N+1: By the induction assumption we know that
 (A1∪⋯∪AN)∩ AN+1
= (A1∩AN)∪ ⋯∪(AN∩AN+1)
= (A1∩AN)∪ ⋯∪(AN∩AN+1)
= (A1∪⋯∪AN)∩ AN+1
.
If (A1∪⋯∪AN)∩AN+1
<∞,hence  (A1∪⋯∪AN)∩AN+1
<∞,wehavebythestrong
additivity of measures and the∩-stability ofG that
 A1∪…∪ AN∪AN+1

= (A1∪…∪ AN)∪ AN+1

= A1∪…∪ AN
+(AN+1)−  (A1∪…∪ AN)∩ AN+1

= A1∪…∪ AN
+(AN+1)−  (A1∩AN+1
«›››ﬂ›››‹
∈G
)∪…∪( AN∩AN+1
«››››ﬂ››››‹
∈G
)
= A1∪…∪ AN
+(AN+1)−  (A1∩AN+1)∪…∪( AN∩AN+1)
⋮
= A1∪…∪ AN∪AN+1

whereweusetheinductionhypothesistwice,namelyfortheunionofthe NG-setsA1,…,AN as
well as for theNG-setsA1∩AN+1,…,AN∩AN+1. The induction is complete.
If (A1∪⋯∪AN)∩ AN+1
=∞ , hence (A1∪⋯∪AN)∩ AN+1
=∞ , there is nothing to
show since the monotinicity of measures entails
(A1∪⋯∪AN)∩ AN+1⊂(A1∪⋯∪AN)∪ AN+1
- ⇒ (A1∪⋯∪AN)∪ AN+1
=∞=  (A1∪⋯∪AN)∪ AN+1
.
In particular we see that(FN) =(FN),(FN) ⩽ (G1)+…+ (GN) < ∞ by subadditivity,
and that (think!)(G∩FN)= (G∩FN) for anyG∈G (just work out the intersection, similar
51

R.L. Schilling: Measures, Integrals & Martingales
to the step in the induction....). This shows that on the∩-stable system
G ∶={ all ﬁnite unions of sets inG}
andcoincide. Moreover,G ⊂ G ⊂A sothat,byassumption A =(G)⊂( G)⊂(A)⊂A,
sothatequalityprevailsinthischainofinclusions. Thismeansthat G isageneratorof A satisfying
all the assumptions of Theorem 5.7, and we have reduced everything to this situation.
Remark. Thelaststepshowsthatweonlyneedtheinductionforsetsfrom G withﬁnite-,hence
-measure. Therefore,theextendeddiscussiononﬁnitenessisactuallynotneeded,iftheinduction
is only used for the sequences(Gi)i and(Fn)n.
■■
Problem 5.8 Solution: Intuition: in two dimensions we have rectangles. TakeI,I ‡∈ J. Call the
lowerleftcornerof Ia =(a1,a2),theupperrightcorner b=(b1,b2),anddothesamefor I‡using
a‡,b‡. This deﬁnes a rectangle uniquely. We are done, ifI∩I‡=ç . If not (draw a picture!) then
wegetanoverlapwhichcanbedescribedbytakingtheright-and-upper-mostofthetwolowerleft
cornersa,a‡and the left-and-lower-most of the two upper right cornersb,b‡. That does the trick.
Now rigorously:sinceI,I ‡∈J, we have for suitableaj,bj,a‡
j,b‡
j’s:
I =
n
×
j=1
aj,bj
 and I‡=
n
×
j=1
a‡
j,b‡
j
.
We want to ﬁndI∩I‡, or, equivalently the condition under whichx∈I∩I‡. Now
x=(x1,…,xn)∈ I ⇐ ⇒xj ∈[aj,bj) ∀j=1,2,…,n
⇐ ⇒aj ⩽xj <b j ∀j=1,2,…,n
and the same holds forx∈I‡(samex, butI‡—no typo). Clearlyaj ⩽xj <b j, and, at the same
timea‡
j ⩽xj <b ‡
j holds exactly if
max(aj,a‡
j) ⩽xj <min(bj,b‡
j) ∀j=1,2,…,n
⇐ ⇒x∈
n
×
j=1
max(aj,a‡
j),min(bj,b‡
j).
Thisshowsthat I∩I‡isindeeda‘rectangle’,i.e.inJ. Thiscouldbeanemptyset(whichhappens
ifI andI‡do not meet).
■■
Problem 5.9 Solution: First we must make sure thatt⋅B is a Borel set ifB∈ℬ. We consider ﬁrst
rectanglesI =[[a,b))∈ J wherea,b ∈ Rn. Clearly,t⋅I =[[ta,tb))whereta,tb arejustthescaled
vectors. So,scaledrectanglesareagainrectangles,andthereforeBorelsets. Nowﬁx t> 0andset
ℬt∶={B∈ℬ(Rn)∶ t⋅B∈ℬ(Rn)}.
52

Solution Manual. Last update 18th July 2019
It is not hard to see thatℬt is itself a-algebra and thatJ ⊂ℬt⊂ℬ(Rn). But then we get
ℬ(Rn)= (J)⊂(ℬt)= ℬt⊂ℬ(Rn),
showing thatℬt=ℬ(Rn), i.e. scaled Borel sets are again Borel sets.
Now deﬁne a new measure(B)∶= n(t⋅B)for Borel setsB∈ℬ(Rn)(which is, because of the
above, well-deﬁned). For rectangles[[a,b))we get, in particular,
[[a,b))= n (t⋅[[a,b))=n[[ta,tb))
=
n˙
j=1
 (tbj)−( taj)
=
n˙
j=1
t⋅ bj−aj

=tn⋅
n˙
j=1
 bj−aj

=tnn[[a,b))
which shows that andtnn coincide on the∩-stable generatorJ ofℬ(Rn), hence they’re the
same everywhere. (Mind the small gap: we should make the mental step that for any measure
 a positive multiple, say,c⋅, is again a measure—this ensures thattnn is a measure, and we
need this in order to apply Theorem 5.7. Mind also that we need that is ﬁnite on all rectangles
(obvious!) and that we ﬁnd rectangles increasing toRn, e.g.[−k,k)×…×[− k,k)as in the proof
of Theorem 5.8(ii).)
■■
Problem 5.10 Solution: Deﬁne(A)∶= ◦−1(A). Obviously,isagainaﬁnitemeasure. Moreover,
since−1(X)= X, we have
(X)= (X)<∞ and, by assumption,(G)= (G) ∀ G∈G.
Thus, =  onG‡∶= G ∪{X}. SinceG‡is a∩-stable generator ofA containing the (trivial)
exhaustingsequence X,X,X, …,theassertionfollowsfromtheuniquenesstheoremformeasures,
Theorem 5.7.
■■
Problem 5.11 Solution: The necessity of the condition is trivial sinceG ⊂ (G)= ℬ, resp.,ℋ ⊂
(ℋ)= C.
FixH ∈ℋ and deﬁne
(B)∶= P(B∩H) and (B)∶= P(B)P(H).
Obviously, and are ﬁnite measures onℬ having massP(H) such that and coincide on
the∩-stable generatorG ∪{X} ofℬ. Note that this generator contains the exhausting sequence
53

R.L. Schilling: Measures, Integrals & Martingales
X,X,X, …. By the uniqueness theorem for measures, Theorem 5.7, we conclude
= on the whole ofℬ.
Now ﬁxB∈ℬ and deﬁne
(C)∶= P(B∩C) and (C)∶= P(B)P(C).
Then the same argument as before shows that =  onC and, sinceB ∈ ℬ was arbitrary, the
claim follows.
■■
Problem 5.12 Solution:
(i) Following the hint we check that
D ∶={A∈A ∶∀  >0∃ G∈G ∶(A▵G) ⩽}
is a Dynkin system.
(D1) By assumption,G∶=X∈G and so(X▵G)= (ç)=0 , henceX∈D.
(D2) Assume thatA ∈ D. For every >0 there is someG ∈ G such that(A▵G) ⩽ .
From
Ac▵Gc =(Gc ⧵Ac)∪( Ac ⧵Gc)
=(Gc∩A)∪( Ac∩G)
=(A ⧵G)∪( G ⧵A)
=A▵G
we conclude that(Ac▵Gc) ⩽; consequently,Ac ∈D (observe thatGc ∈G!).
(D3) Let(Aj)j∈N⊂D be a sequence of mutually disjoint sets and >0. Since is a ﬁnite
measure, we get
É
j∈N
(Aj)= 
H
Ó
j∈N
Aj
I
<∞,
and, in particular, we can pickN ∈ N so large, that
∞É
j=N+1
(Aj) ⩽.
Forj ∈ {1,…,N} there is someGj ∈ G such that(Aj▵Gj) ⩽ . Thus, G ∶=
⋃N
j=1Gj ∈G satisﬁes
H
Ó
j∈N
Aj
I
⧵G=
H
Ó
j∈N
Aj
I
∩Gc
=
H
Ó
j∈N
Aj
I
∩
H NÌ
j=1
Gc
j
I
54

Solution Manual. Last update 18th July 2019
=
Ó
j∈N
H
Aj∩
NÌ
k=1
Gc
k
I
⊂
NÓ
j=1
(Aj∩Gc
j)∪
∞Ó
j=N+1
Aj.
In the same way we get
G ⧵
H
˝
j∈N
Aj
I
⊂G ⧵
H NÓ
j=1
Aj
I
=G∩
NÌ
j=1
Ac
j
⊂
N˝
j=1
(Gj∩Ac
j).
Thus,

HH
Ó
j∈N
Aj
I
▵G
I
⩽
H N˝
j=1
(Aj▵Gj)∪
∞Ó
j=N+1
Aj
I
⩽
NÉ
j=1
(Aj▵Gj)+ 
H ∞É
j=N+1
Aj
I
⩽N +.
Since >0 is arbitrary, we conclude that⨃
j∈NAj ∈D.
Obviously,G ⊂D (takeG=A∈G). SinceG is∩-stable, we get
A =(G)= (G)⊂D.
(ii) Using the family
D‡∶={A∈A ∶∀  >0∃ G∈G ∶(A▵G) ⩽,(A▵G) ⩽},
we ﬁnd, just as in (i), thatD‡is a Dynkin system. The rest of the proof is as before.
(iii) “⇐”: LetA∈A suchthat A⊂ ⋃
n∈NInand ⋃
n∈NIn
 ⩽. Becauseofthemonotonicity
of measures we get
(A) ⩽
H
˝
n∈N
In
I
⩽,
and so(A)=0 .
“⇒”: SetK ∶={A⊂ Rn ∶∃(Ik)k∈N ⊂J ∶A= ⋃
kIk orAc = ⋃
kIk} and observe that
I ∈K ⇒Ic ∈K. Deﬁne, furthermore,
D ∶={A⊂ Rn∶∀ ∃J,K ∈K, J ⊂A⊂K, (K ⧵J) ⩽}.
We claim thatD is a Dynkin system.
55

R.L. Schilling: Measures, Integrals & Martingales
(D1) Clearly,X= Rn∈D (takeJ =K = Rn).
(D2) Pick A ∈ D and  > 0. Then there areJ,K ∈ K such thatJ ⊂ A ⊂ Kand
(K ⧵J) ⩽. FromJc,K c ∈K,(Kc ⧵Jc)= (J ⧵K) ⩽ andJc ⊃A c ⊃K c we
get immediatelyAc ∈D.
(D3) Let(Aj)j∈N⊂D be a sequence of mutually disjoint sets and >0. PickJj ∈K and
Kj ∈K such thatJj ⊂A j ⊂K j,(Kj ⧵Jj) ⩽2−j and set
J ∶=
˝
j∈N
Aj K ∶=
˝
j∈N
Kj.
SinceK is stable under countable unions, we getJ ∈ K,K ∈ K. Moreover,J ⊂
⨃
jAj ⊂K and
(K ⧵J)= 
HH
˝
j∈N
Kj
I
∩
H
˝
j∈N
Jj
IcI
=
HH
˝
j∈N
Kj
I
∩
H
Ì
j∈N
Jc
j
II
=
HL
˝
j∈N
H
Kj∩
Ì
k∈N
Jc
k
IMI
⩽
H
˝
j∈N
(Kj∩Jc
j)
I
⩽
É
j∈N
(Kj∩Jc
j)
«›››ﬂ›››‹
(Kj ⧵Jj)⩽2−j
⩽.
Thus,⨃
jAj ∈D.
Finally,J ⊂D entails thatℬ(Rn)= (J)⊂D.
Now letA be a set satisfying(A) = 0. Therefore, for every >0 there is a setK = K ∈ K
such thatA ⊂ Kand(K)< . IfK = ⋃
iIi, we are done. IfKc = ⋃
iIi we have to argue like
this: LetJ ∶=JR∶=[−R,R)d ∈J. Then
K =
Ì
i
Ic
i and J∩K =
Ì
i
Ic
i ∩J =
Ì
i
J ⧵Ii=
Ì
k
kÌ
i=1
J ⧵Ii
and each setJ ⧵Ii is a ﬁnite union of sets fromJ (sinceJ is a semiring), hence⋂k
i=1J ⧵Ii is a
ﬁniteunionofsetsfrom J. Since(J∩K) ⩽(K) ⩽,acontinuity-of-measureargumentshows
that there exists someksuch thatJ∩K ⊂⋂k
i=1J ⧵Ii and(⋂k
i=1J ⧵Ii) ⩽2.
If we pick=∕2R, we see that we can coverA∩[−R,R)d by a countable union ofJ-sets, call
their unionUR, such that(UR) ⩽∕2R. Finally,
(A) ⩽
É
R∈N
(UR) ⩽
56

Solution Manual. Last update 18th July 2019
and we can combine all covers which make up theUR,R∈ N.
■■
Problem 5.13 Solution:
(i) mind the misprint: we also need stability ofℳ under ﬁnite intersections.Clearly, any
-algebra is also a monotone class. Conversely, ifℳ is a monotone class such thatM ∈
ℳ - ⇒Mc ∈ℳ,thenthecondition( Σ2)holds,while( Σ1)issatisﬁedbytheverydeﬁnition
of a monotone class. Ifℳ is also stable under ﬁnite intersections, we getM,N ∈ ℳ - ⇒
M∪N =(Mc∩Nc)c ∈ℳ, so (Σ3) follows from the stability under ﬁnite unions and the
stability of monotone classes under increasing limits of sets.
(ii) Since(G)isamonotoneclasscontaining G,wehave–byminimality–that m(G)⊂(G).
On the other hand, by the monotone class theorem, we getG ⊂ m(G) - ⇒(G) ⊂ m(G)
which means thatm(G)= (G).
■■
57



6 Existence of measures.
Solutions to Problems 6.16.14
Problem 6.1 Solution:
(i) Monotonicity: Ifx ⩽0 ⩽y, thenF(x) ⩽0 ⩽F(y).
If0<x ⩽y, we have[0,x)⊂[0,y)and so0 ⩽F(x)= [0,x) ⩽[0,y)= F(y).
Ifx ⩽y< 0, we have[y,0)⊂[x,0) and so0 ⩽−F(y)= [y,0) ⩽[x,0)=− F(x), i.e.
F(x) ⩽F(y) ⩽0.
Left-continuity: Let us deal with the casex ⩾ 0 only, the casex <0 is analogous (and
even easier). Assume ﬁrst thatx >0. Take any sequencexk < xandxk ↑ x ask → ∞.
Without loss of generality we can assume that0 < xk < x. Then[0,xk) ↑[0,x) and using
Proposition 4.3 (continuity of measures) implies
lim
k→∞
F(xk)= lim
k→∞
[0,xk)= [0,x)= F(x).
Ifx = 0we must take a sequencexk < 0 and we have then[xk,0) ↓ [0,0) = ç. Again by
Proposition 4.3, now(iii‡), we get
lim
k→∞
F(xk)=− lim
k→∞
[xk,0)= (ç)=0= F(0).
which shows left-continuity at this point, too.
We remark that, since for a sequenceyk ↓y,yk > ywe have[0,yk) ↓[0,y], and not[0,y),
we cannot expect right-continuity in general.
(ii) SinceJ ={[a,b),a ⩽b}isasemi-ring(cf.theremarkprecedingProposition6.3orPropos-
ition6.5)itisenoughtocheckthat F isapremeasureon J. Thisagainamountstoshowing
(M1) and (M2) relative toJ (mind you:F is not ameasureasJ is not a-algebra....).
(i) F(ç)= F[a,a)= F(a)− F(a)=0 for anya.
(ii) Leta ⩽b ⩽c so that[a,b),[b,c)∈ J are disjoint sets and[a,c)=[ a,b)⊍[b,c)∈ J
(the latter is crucial). Then we have
F[a,b)+ F[b,c)= F(b)− F(a)+ F(c)− F(b)
=F(c)− F(a)
=F[a,c)
=F
 [a,b)⊍[b,c).
59

R.L. Schilling: Measures, Integrals & Martingales
(iii) We mimick the proof of existence of Lebesgue measure. LetIn = [an,bn) ∈J be
disjoint such thatI = [a,b) =⨃∞
n=1[an,bn) ∈J. Fixn, >0 (these values will be
chosen later) and observe that
∞˝
n=1
(an−n,bn)⊃[a,b −]
is an open cover of the compact interval[a,b −]. Thus, there exists a ﬁnite open
subcover, hence someN ∈ N such that
N˝
n=1
(an−n,bn)⊃[a,b −] - ⇒
N˝
n=1
[an−n,bn)⊃[a,b −).
We have to show that
F[a,b)−
NÉ
n=1
F[an,bn) , , , , , , , , , , , , , , , , , , , , , , , , →
N→∞
0.
First note that we can de- and increasean ⩾a‡
n andbn ⩽b‡
n such that
NÓ
n=1
[an,bn)⊂
NÓ
n=1
[a‡
n,b‡
n)=[ a,b)
so that by the ﬁnite additivity ofF we get
0= F[a,b)−
NÉ
n=1
F[a‡
n,b‡
n) ⩽F[a,b)−
NÉ
n=1
F[an,bn).
Thus, using only the ﬁnite additivity and sub-additivity ofF
0 ⩽F[a,b)−
NÉ
n=1
F[an,bn)
=F[a,b −)−
NÉ
n=1
F[an−n,bn)
⩽0 ﬁnite covering & subadditivity
+F[b−,b)+
NÉ
n=1
F[an−n,an)
⩽F[b−,b)+
NÉ
n=1
F[an−n,an).
Now we choose andn. For any given >0 we can ﬁnd >0 andn>0 such that
F[b−,b)= F(b)− F(b−) ⩽ 
2
and F[an−n,an)= F(an)− F(an−n) ⩽2−n
2
here we use the left-continuity ofF. Thus,
0 ⩽F[a,b)−
NÉ
n=1
F[an,bn) ⩽ 
2+
NÉ
n=1
2−n
2 ⩽.
Letting ﬁrstN →∞and then →0 proves the claim.
60

Solution Manual. Last update 18th July 2019
Note thatF takes on only positive values becauseF increases.
This means that we ﬁndat least oneextension. Uniqueness follows since
F[−k,k)= F(k)− F(−k)<∞ and [−k,k) ↑ R.
(iii) Now let be a measure with[−n,n) < ∞. The latter means that the functionF(x),
as deﬁned in part (i), is ﬁnite for everyx ∈ R. Now take thisF and deﬁne, as in (ii) a
(uniquely deﬁned) measureF. Let us see that = F. For this, it is enough to show
equality on the sets of type[a,b) (since such sets generate the Borel sets and the uniqueness
theorem applies....)
If0 ⩽a ⩽b,
F[a,b)= F(b)− F(a)= [0,b)− [0,a)
= [0,b) ⧵[0,a)
=[a,b) ✓
Ifa ⩽b ⩽0,
F[a,b)= F(b)− F(a)=− [b,0)−(− [a,0))
=[a,0)− [b,0)
= [a,0) ⧵[b,0)
=[a,b) ✓
Ifa ⩽0 ⩽b,
F[a,b)= F(b)− F(a)= [0,b))−(− [a,0))
=[a,0))+ [0,b)
= [a,0)⊍[0,b)
=[a,b) ✓
(iv) F ∶ R → R withF(x)= x, since[a,b)= b−a=F(b)− F(a).
(v) F ∶ R → R, with, say,F(x) =
⎧
⎪
⎨
⎪⎩
0, x ⩽0
1, x> 0
= 1(0,∞)(x) since0[a,b) = 0whenever
a,b< 0ora,b> 0. This means thatF must be constant on(−∞,0)and(0,∞)Ifa ⩽0<b
we have, however,0[a,b) = 1which indicates thatF(x) must jump by1 at the point0.
Given the fact thatF must be left-continuous, it is clear that it has, in principle, the above
form. The only ambiguity is, that ifF(x) does the job, so doesc+F(x) for any constant
c∈ R.
61

R.L. Schilling: Measures, Integrals & Martingales
(vi) Assume thatF is continuous at the pointx. Then
({x})= 
0 Ì
k∈N

x,x + 1
k
1
4.3
= lim
k→∞


x,x + 1
k

def
= lim
k→∞

F

x+ 1
k

−F(x)

= lim
k→∞
F

x+ 1
k

−F(x)
(∗)
= F(x)− F(x)=0
where we use (right-)continuity ofF atxin the step marked(∗).
Now, let conversely({x}) = 0. A similar calculation as above shows, that forevery se-
quencek>0 withk →∞
F(x+)− F(x)= lim
k→∞
F  x+k
−F(x)
def
= lim
k→∞
[x,x +k)
4.3
= 
0 Ì
k∈N
[x,x +k)
1
=({x})=0
which means thatF(x)= F(x+) (x+ indicates the right limit), i.e.F is right-continuous at
x, hence continuous, asF is left-continuous anyway.
■■
Problem 6.2 Solution: Using the notion of measurability we get
∗
H
Q∩
∞˝
i=1
Ai
I
=∗
HH
Q∩
∞˝
i=1
Ai
I
∩A1
I
+∗
HH
Q∩
∞˝
i=1
Ai
I
∩Ac
1
I
=∗(Q∩A1)+ ∗
H
Q∩
∞˝
i=2
Ai
I
=…
=
n−1É
i=1
∗(Q∩Ai)+ ∗(Q∩(∪∞
i=nAi))
(6.1)
for anyn∈ N. Thus,∗(Q∩⋃∞
i=1Ai) ⩾ ∑n−1
i=1 ∗(Q∩Ai)for alln∈ N. Ifn →∞we obtain
∗
H
Q∩
∞˝
i=1
Ai
I
⩾
∞É
i=1
∗(Q∩Ai).
Case 1:∑∞
i=1∗(Q∩Ai)=∞ . Nothing to show.
Case 2:∑∞
i=1∗(Q∩Ai)<∞. Using the sub-additivity of outer measures we get
∗
H
Q∩
∞˝
i=n
Ai
I
⩽
∞É
i=n
∗(Q∩Ai)
n→∞
, , , , , , , , , , , , , , , , , , , , →0
62

Solution Manual. Last update 18th July 2019
and the claim follows from (6.1) asn →∞.
■■
Problem 6.3 Solution: Weknowalreadythat ℬ[0,∞)isa -algebra(itisatrace -algebra)and, by
deﬁnition,
Σ= B∪(−B)∶ B∈ℬ[0,∞)
if we write−B∶={−b∶b∈ℬ[0,∞)}.
Sincethestructure B∪(−B)isstableundercomplementationandcountableunionsitisclearthat
Σis indeed a-algebra.
Onepossibilitytoextend deﬁnedonΣwouldbetotake B∈ℬ(R)anddeﬁneB+∶=B∩[0,∞)
andB−∶=B∩(−∞,0) and to set
(B)∶= (B+∪(−B+))+ ((−B−)∪ B−)
which is obviously a measure. We cannot expect uniqueness of this extension sinceΣ does not
generateℬ(R)—not all Borel sets are symmetric.
■■
Problem 6.4 Solution: By deﬁnition we have
∗(Q)=inf
<É
j
(Bj)∶( Bj)j∈N⊂A, ∪
j∈N
Bj ⊃Q
=
.
(i) Assume ﬁrst that∗(Q) < ∞. By the deﬁnition of the inﬁmum we ﬁnd for every >0 a
sequence(B
j)j∈N⊂A such thatB ∶= ⋃
jB
j ⊃Q and, because of-subadditivity,
(B)− ∗(Q) ⩽
É
j
(B
j)− ∗(Q) ⩽.
SetB∶= ⋂
kB1∕k∈A. ThenB ⊃Qand(B)= ∗(B)= ∗(Q).
Now letN ∈A andN ⊂B ⧵Q. Then
B ⧵N ⊃B ⧵(B ⧵Q)= B∩[(B∩Qc)c]= B∩[Bc∪Q]
=B∩Q
=Q.
So,
∗(Q)− (N)= (B)− (N)= (B ⧵N)= ∗(B ⧵N) ⩾∗(Q)
which means that(N)=0 .
If∗(Q)=∞ , we take the exhausting sequence(Ak)k∈N⊂A withAk ↑X and(Ak)<∞
and setQk ∶= Ak∩Q for everyk ∈ N. By the ﬁrst part we can ﬁnd setsBk ∈ A with
63

R.L. Schilling: Measures, Integrals & Martingales
Bk ⊃ Qk,(Bk)= ∗(Qk) and(N)=0 for allN ∈A withN ⊂ Bk ⧵Qk. Without loss
of generality we can assume thatBk ⊂ Ak, otherwise we replaceBk byAk∩Bk. Indeed,
Bk∩Ak⊃Q k,Bk∩Ak∈A,
∗(Qk)= (Bk) ⩾(Ak∩Bk) ⩾∗(Qk)
andBk ⧵Qk ⊃(Bk∩Ak) ⧵Qk, i.e. we have again that all measurableN ⊂(Bk∩Ak) ⧵Qk
satisfy(N)=0 .
Assume now thatN ⊂B ⧵Q,B= ⋃
kBk andN ∈A. ThenNk∶=N∩Bk∈A and we
haveN = ⋃
kNk as well as
Nk=N∩Bk⊂(B ⧵Q)∩ Bk=Bk ⧵Q=Bk ⧵Qk.
Thus(Nk)=0 and, by-subadditivity,(N) ⩽ ∑∞
k=1(Nk)=0 .
(ii) Deﬁnē ∶=∗óóóA∗. We know from Theorem 6.1 that̄ is a measure onA∗ and, because of
the monotonicity of∗, we know that for allN∗∈A∗ with ̄ (N∗)we have
∀M ⊂N∗∶∗(M) ⩽∗(N∗)= ̄ (N∗)=0 .
It remains to show thatM ∈A∗. Because of (6.2) we have to show that
∀Q⊂X ∶∗(Q)= ∗(Q∩M)+ ∗(Q ⧵M).
Since∗ is subadditive we ﬁnd for allQ⊂X
∗(Q)= ∗ (Q∩M)∪( Q ⧵M)
⩽∗(Q∩M)+ ∗(Q ⧵M)
=∗(Q ⧵M)
⩽∗(Q),
which means thatM ∈A∗.
(iii) Obviously,(X,A∗, ̄ ) extends(X,A,) sinceA ⊂ A∗ and ̄ óóóA
= . In view of Problem
4.15 we have to show that
A∗={A∪N ∶A∈A, N ∈ N} (*)
with N={N ⊂X∶N is subset of anA-measurable null set or, alternatively,
A∗={A∗⊂X ∶∃ A,B ∈A, A⊂A ∗⊂B, (B ⧵A)=0} . (**)
We are going to use both equalities and show ‘⊃’ in(∗) and ‘⊂’ in(∗∗) (which is enough
since, cf. Problem 4.15 asserts the equality of the right-hand sides of(∗),(∗∗)!).
‘⊃’:By part (ii), subsets ofA-null sets are inA∗ so that every set of the formA∪N with
A∈A andN being a subset of anA null set is inA∗.
64

Solution Manual. Last update 18th July 2019
‘⊂’:Bypart(i)weﬁndforevery A∗∈A∗someA∈A suchthat A⊃A ∗andA⧵A∗isan A∗
nullset. Bythesameargumentweget B∈A,B ⊃(A∗)c andB ⧵(A∗)c =B∩A∗=A∗ ⧵Bc
is anA∗ null set. Thus,
Bc ⊂A ∗⊂A
and
A ⧵Bc ⊂  A ⧵A∗∪ A∗ ⧵Bc=  A ⧵A∗∪ B ⧵(A∗)c
which is the union of twoA∗ null sets, i.e.A ⧵Bc is anA null set.
■■
Problem 6.5 Solution: Since, by assumption,m is an additive set function such that0 ⩽ m(X) ⩽
(X)<∞, it is enough to show (cf. Lemma 4.9) thatmis continuous atçandm(ç)=0 .
• m(ç)=0 : This follows immediately fromm(ç) ⩽(ç)=0 . (Note:ç= Xc ∈ℬ.)
• m is continuous atç: Let(Bk)k∈N⊂ℬ,Bk ↓ç. Since(Bk) →0 we get
m(Bk) ⩽(Bk)
k→∞
, , , , , , , , , , , , , , , , , , , , →0.
This shows thatmis continuous atç.
Remark. In order to be self-contained, let us check that any additive set functionm on a Boolean
algebraℬ is a pre-measure (i.e. sigma-additive) if it is continuous atç:
Let (Bn)n∈N ⊂ ℬ be a sequence of mutually disjoint sets andB ∶= ⋃
n∈NBn ∈ ℬ. From
B1⊍…⊍Bn∈ℬ we get
An∶=B ⧵(B1⊍…⊍Bn)= B∩(B1⊍…⊍Bn)c
«›››››››ﬂ›››››››‹
∈ℬ
∈ℬ.
SinceAn ↓ç, continuity atç provesm(An) →0. Sincem is additive,
m(B)= m(B ⧵(B1⊍…⊍Bn))+ m(B1⊍…⊍Bn)
=m(An)+
nÉ
j=1
m(Bj)
n→∞
, , , , , , , , , , , , , , , , , , , , →0+
∞É
j=1
m(Bj).
■■
Problem 6.6 Solution:
(i) A little geometry ﬁrst: a solid, open disk of radiusr, centre0 is the setBr(0) ∶= {(x,y) ∈
R2∶x2+y2<r 2}. Then-dimensionalanalogueisclearly {x∈ Rn∶x2
1+x2
2+…+x2
n<r 2}
(includingn=1 where it reduces to an interval). We want to inscribe a box into a ball.
65

R.L. Schilling: Measures, Integrals & Martingales
Claim: Q(0)∶=
n
×××
j=1
4
− √
n, √
n
1
⊂B 2(0). Indeed,
x∈Q(0) - ⇒x2
1+x2
2+…+ x2
n ⩽ 2
n + 2
n +…+ 2
n <(2)2
- ⇒x∈B2(0),
and the claim follows.
Observe thatn(Q(0)) =∏n
j=1
2√
n > 0. Now take some open setU. By translating it we
canachievethat 0∈ U and,asweknow,thismovementdoesnotaﬀect n(U). As0∈ U we
ﬁnd some >0 such thatB(0)⊂U , hence
n(U) ⩾n(B(0)) ⩾(Q(0))>0.
(ii) Forclosedsetsthisis, ingeneral,wrong. Trivialcounterexample: thesingleton{0}isclosed,
it is Borel (take a countable sequence of nested rectangles, centered at0 and going down to
{0}) and the Lebesgue measure is zero.
TogetstrictlypositiveLebesguemeasure,onepossibilityistohaveinteriorpoints,i.e.closed
sets which have non-empty interior do have positive Lebesgue measure.
■■
Problem 6.7 Solution:
(i) Without loss of generality we can assume thata<b . We have[a+ 1
k,b) ↑(a,b) ask →∞.
Thus, by the continuity of measures, Proposition 4.3, we ﬁnd (write=1, for short)
(a,b)= lim
k→∞


a+ 1
k,b

= lim
k→∞

b−a− 1
k

=b−a.
Since[a,b)= b−a, too, this proves again that
({a})= ([a,b) ⧵(a,b))= [a,b)− (a,b)=0 .
(ii) The hint says it all:H is contained in the uniony+ ⋃
k∈NAk for somey and we have
2(Ak)=(2 2−k)⋅(2k)=4 ⋅⋅k2−k. Usingthe-subadditivityandmonotonicityofmeasures
(the Ak’s are clearly not disjoint) as well as the translational invariance of the Lebesgue
measure we get
0 ⩽2(H) ⩽2
0 ∞
∪
k=1
Ak
1
⩽
∞É
k=1
(Ak)=
∞É
k=1
4⋅⋅k2−k=C
whereC is the ﬁnite (!) constant4∑∞
k=1k2−k (check convergence!). As was arbitrary, we
can let it→0 and the claim follows.
(iii) n-dimensionalversionof(i): WehaveI =
n
×××
j=1
(aj,bj). SetIk∶=
n
×××
j=1
[aj+1
k,bj). ThenIk ↑I
ask →∞and we have (write=n, for short)
(I)= lim
k→∞
(Ik)= lim
k→∞
n˙
j=1

bj−aj− 1
k

=
n˙
j=1
 bj−aj
.
66

Solution Manual. Last update 18th July 2019
n-dimensional version of (ii):The changes are obvious:Ak = [−2−k,2−k)×[− k,k)n−1
andn(Ak) = 2n⋅⋅2−k⋅kn−1. The rest stays as before, since the sum∑∞
k=1kn−12−k still
converges to a ﬁnite value.
■■
Problem 6.8 Solution:
(i) All we have to show is that1({x})=0 for anyx∈ R. But this has been shown already in
problem 6.6(i).
(ii) Take the Dirac measure:0. Then{0}is an atom as0({0})=1 .
(iii) LetC be countable and let{c1,c2,c3,…} be an enumeration (could be ﬁnite, ifC is ﬁnite).
Sincesingletonsarein A,sois C asacountableunionofthesets {cj}. Usingthe-additivity
of a measure we get
(C)= (∪j∈N{cj})=
É
j∈N
({cj})=
É
j∈N
0=0 .
(iv) Ify1,y2,…,yN are atoms of massP({yj}) ⩾ 1
k we ﬁnd by the additivity and monotonicity
of measures
N
k ⩽
NÉ
j=1
P({xj})
=P
0 N
∪
j=1
{yj}
1
=P({y1,…,yN}) ⩽P(R)=1
so N
k ⩽1,i.e. N ⩽k,andtheclaiminthehint(aboutthemaximalnumberofatomsofgiven
size) is shown.
Now denote, as in the hint, the atoms with measure of size[1
k, 1
k−1) byy(k)
1 ,…y(k)
N(k) where
N(k) ⩽kis their number. Since
˝
k∈N

1
k, 1
k−1

=(0,∞)
we exhaust all possible sizes for atoms.
There are at most countably many (actually: ﬁnitely many) atoms in each size range. Since
the number of size ranges is countable and since countably many countable sets make up a
countableset,wecanrelabeltheatomsas x1,x2,x3,…(couldbeﬁnite)and,aswehaveseen
in exercise 4.7(ii), the set function
∶=
É
j
P({xj})⋅xj
(nomatterwhetherthesumisoveraﬁniteorcountablyinﬁnitesetof j’s)isindeedameasure
on R. But more is true: for any Borel setA
(A)=
É
j
P({xj})⋅xj(A)
67

R.L. Schilling: Measures, Integrals & Martingales
=
É
j∶xj∈A
P({xj})
=P(A∩{x1,x2,…}) ⩽P(A)
showing that(A) ∶=P(A)− (A) is a positive number for each Borel setA ∈ ℬ. This
meansthat ∶ℬ →[0,∞]. Letuscheck M1 andM2. UsingM1,M2 forP and (forthem
they are clear, asP, are measures!) we get
(ç)= P(ç)− (ç)=0−0=0
and for a disjoint sequence(Aj)j∈N⊂ℬ we have

0˝
j
Aj
1
=P
0˝
j
Aj
1
−
0˝
j
Aj
1
=
É
j
P(Aj)−
É
j
(Aj)
=
É
j
 P(Aj)− (Aj)
=
É
j
(Aj)
which isM2 for.
■■
Problem 6.9 Solution:
(i) Fix a sequence of numbersk > 0,k ∈ N0 such that∑
k∈N0
k < ∞. For example we
couldtakeageometricserieswithgeneralterm k∶=2 −k. NowdeﬁneopenintervalsIk∶=
(k−k,k +k), k∈ N0 (these are open sets!) and call their unionI ∶= ⋃
k∈N0
Ik. As
countableunionofopensets I isagainopen. Usingthe -(sub-)additivityof =1 weﬁnd
(I)= 
0 ˝
k∈N0
Ik
1 (∗)
⩽
É
k∈N0
(Ik)=
É
k∈N0
2k=2
É
k∈N0
k<∞.
By 6.7(i),(I)>0.
Notethatinstep (∗)equalityholds(i.e.wewoulduse -additivityratherthan -subadditivity)
if theIk are pairwise disjoint. This happens, if allk < 1
2 (think!), but to be on the safe side
and in order not to have to worry about such details we use sub-additivity.
(ii) Take the open interior of the setsAk, k ∈ N, from the hint to 6.7(ii). That is, take the
open rectanglesBk ∶= (−2−k,2−k)×(− k,k),k ∈ N, (we choose = 1since we are after
ﬁnitenessandnotnecessarily smallness). Thattheseareopensetswillbeseenbelow. Nowset
B= ⋃
k∈NBk and observe that the union of open sets is always open.B is also unbounded
anditisgeometricallyclearthat Bispathwiseconnectedasitissomekindoflozenge-shaped
‘staircase’ (draw a picture!) around they-axis. Finally, by-subadditivity and using 6.7(ii)
we get
2(B)= 2
0 ˝
k∈N
Bk
1
⩽
É
k∈N
2(Bk)
68

Solution Manual. Last update 18th July 2019
=
É
k∈N
2⋅2−k⋅2⋅k
=4
É
k∈N
k⋅2−k<∞.
It remains to check that an open rectangle is an open set. For this take any open rectangle
R= (a,b)×( c,d) and pick(x,y) ∈R. Then we know thata < x < bandc < y < dand
sincewehavestrictinequalities,wehavethatthesmallestdistanceofthispointtoanyofthe
fourboundaries(drawapicture!) ℎ∶=min{ ða−xð,ðb−xð,ðc−yð,ðd−yð}>0. Thismeans
that a square around(x,y) with side-length2ℎ is insideR and what we’re going to do is to
inscribe into this virtual square an open disk with radiusℎand centre(x,y). Since the circle
is again inR, we are done. The equation for this disk is
(x‡,y‡)∈ Bℎ(x,y) ⇐ ⇒(x−x‡)2+(y−y‡)2<ℎ 2
Thus,
ðx‡−xð ⩽
√
ðx−x‡ð2+ðy−y‡ð2<ℎ
and ðy‡−yð ⩽
√
ðx−x‡ð2+ðy−y‡ð2<ℎ
i.e.x−ℎ<x ‡<x +ℎ andy−ℎ<y ‡<y +ℎ or(x‡,y‡)∈( x−ℎ,x +ℎ)×( y−ℎ,y +ℎ),
which means that(x‡,y‡)is in the rectangle of sidelength2ℎcentered at(x,y). since(x‡,y‡)
was an arbitrary point ofBℎ(x,y), we are done.
(iii) No, this is impossible. Since we are in one dimension, pathwise connectedness forces us to
go between points in a straight, uninterrupted line. Since the set is unbounded, this means
that we must have a line of the sort(a,∞) or(−∞,b) in our set and in both cases Lebesgue
measureisinﬁnite. Inalldimensionsn> 1,seepart(ii)fortwodimensions,wecan,however,
construct pathwise connected, unbounded open sets with ﬁnite Lebesgue measure.
■■
Problem 6.10 Solution: Fix >0and let{qj}j∈N be an enumeration ofQ∩[0,1]. Then
U ∶=U ∶=
˝
j∈N
 qj−2−j−1,qj+2−j−1∩[0,1]
is a dense open set in[0,1] and, because of-subadditivity,
(U) ⩽
É
j∈N
 qj−2−j−1,qj+2−j−1=
É
j∈N

2j =.
■■
Problem 6.11 Solution: Assume ﬁrst that for every >0 there is some open setU ⊃ Nsuch that
(U) ⩽. Then
(N) ⩽(U) ⩽ ∀ >0,
69

R.L. Schilling: Measures, Integrals & Martingales
which means that(N)=0 .
Conversely, let∗(N) = inf
$∑
j(Uj) ∶Uj ∈ O, ∪j∈NUj ⊃ N
%
. Since for the Borel setN
we have∗(N)= (N)=0 , the deﬁnition of the inﬁmum guarantees that for every >0there is
asequenceofopensets (U
j)j∈N coveringN,i.e.suchthat U ∶= ⋃
jU
j ⊃N . SinceU isagain
open we ﬁnd because of-subadditivity
(N) ⩽(U)= 
0˝
j
U
j
1
⩽
É
j
(U
j) ⩽.
Attention: A construction along the lines of Problem 3.15, hint to part (ii), using open setsU ∶=
N+B(0) is, in general not successful:
• itisnotclearthat U hasﬁniteLebesguemeasure(o.k.onecanovercomethisbyconsidering
N∩[−k,k]and then lettingk →∞...)
• U ↓ ̄N and notN (unlessN is closed, of course). If, say,N is a dense set of[0,1], this
approach leads nowhere.
■■
Problem 6.12 Solution: Observe that the setsCk ∶= ⋃∞
j=kAj,k ∈ N, decrease ask → ∞—we
admit less and less sets in the union, i.e. the union becomes smaller. SinceP is a probability
measure,P(Ck) ⩽1and therefore Lemma 4.9 applies and shows that
P
0 ∞⋂
k=1
∞⋃
j=k
Aj
1
=P
0 ∞⋂
k=1
Ck
1
= lim
k→∞
P(Ck).
On the other hand, we can use-subadditivity of the measureP to get
P(Ck)= P
0 ∞⋃
j=k
Aj
1
⩽ ∑∞
j=kP(Aj)
but this is the tail of the convergent (!) sum∑∞
j=1P(Aj) and, as such, it goes to zero ask →∞.
Putting these bits together, we see
P
0 ∞⋂
k=1
∞⋃
j=k
Aj
1
= lim
k→∞
P(Ck) ⩽ lim
k→∞
∞É
j=k
P(Aj)=0 ,
and the claim follows.
■■
Problem 6.13 Solution:
(i) We can work out the ‘optimal’A-cover of(a,b):
Case1: a,b ∈[0,1). Then[0,1)isthebestpossiblecoverof (a,b),thus ∗(a,b)= [0,1)=
1
2.
Case2: a,b ∈[1,2). Then[1,2)isthebestpossiblecoverof (a,b),thus ∗(a,b)= [1,2)=
1
2.
70

Solution Manual. Last update 18th July 2019
Case 3:a ∈ [0,1),b ∈ [1,2). Then[0,1)⊍[1,2) is the best possible cover of(a,b), thus
∗(a,b)= [0,1)+ [1,2)=1 .
And in the case of a singleton{a} the best possible cover is always either[0,1) or[1,2) so
that∗({a})= 1
2 for alla.
(ii) Assumethat (0,1)∈ A∗. SinceA ⊂A∗, wehave[0,1)∈ A∗, hence{0}=[0 ,1) ⧵(0,1)∈
A∗. Since∗(0,1)= ∗({0})= 1
2, and since∗ is a measure onA∗ (cf. Step 4 in the proof
of Theorem 6.1), we get
1
2 =[0,1)= ∗[0,1)= ∗(0,1)+ ∗{0}= 1
2+1
2 =1
leading to a contradiction. Thus neither(0,1) nor{0}are elements ofA∗.
■■
Problem 6.14 Solution: SinceA ⊂A∗, the only interesting sets (to which one could extend) are
thoseB ⊂R where bothB andBc are uncountable. By deﬁnition,
∗(B)=inf
$É
j
(Aj)∶ Aj ∈A,
˝
j
Aj ⊃B
%
.
The inﬁmum is obviously attained forAj = R, so that∗(B) =∗(Bc) = 1. On the other hand,
since∗ is necessarily additive onA∗, the assumption thatB∈A∗ leads to a contradiction:
1= (R)= ∗(R)= ∗(B)+ ∗(Bc)=2 .
Thus,A =A∗.
■■
71



7 Measurable mappings.
Solutions to Problems 7.17.13
Problem 7.1 Solution: We have−1
x (z)= z+x. According to Lemma 7.2 we have to check that
−1
x ([a,b))∈ ℬ(Rn) ∀[ a,b)∈ J
since the rectanglesJ generateℬ(Rn). Clearly,
−1
x ([a,b))=[ a,b)+ x=[a+x,b +x)∈ J ⊂ℬ(Rn),
and the claim follows.
■■
Problem 7.2 Solution: Wehad Σ‡={A‡⊂X ‡∶T−1(A‡)∈ A}whereA wasa -algebraofsubsets
ofX. Let us check the properties (Σ1)–(Σ3).
(Σ1) Takeç⊂X ‡. ThenT−1(ç)=ç∈ A, henceç∈Σ ‡.
(Σ2) Take anyB ∈ Σ‡. ThenT−1(B) ∈A and thereforeT−1(Bc) = T−1(B)c
∈ A since all
set operations interchange with inverse maps and sinceA is a-algebra. This shows that
Bc ∈Σ ‡.
(Σ3) Takeanysequence (Bj)j∈N⊂Σ‡. Then,usingagainthefactthat A isa -algebra,T−1(∪jBj)=
⋃
jT−1(Bj)∈ A which proves that⋃
jBj ∈Σ ‡.
■■
Problem 7.3 Solution:
(i) (Σ1) ç∈ A is clear.
(Σ2) LetA∈A. If2n∈Ac, then2n+1∈ Ac – this follows straight from the deﬁnition
ofA: if2n+1∈ A,then 2n∈A. Inthesamewayweget 2n+1∈ Ac - ⇒2n∈Ac.
Consequently,Ac ∈A.
(Σ3) Let(Aj)j∈N ⊂ A. If2n ∈ ⋃
jAj, then there is some indexj0 such that2n ∈ Aj0.
Since Aj0 ∈ A, we get2n+1 ∈ Aj0 ⊆ ⋃
jAj. In the same way we ﬁnd that
2n+1∈ ⋃
jAj - ⇒2n∈ ⋃Aj.
(ii) It is clear that the mapT is bijective asT−1(n)= n−2. Pick any setA∈A. In order to
verify the measurability ofT, we have to show thatT−1(A)∈ A, i.e.
2n∈T−1(A) ⇔2n+1∈ T−1(A) for alln> 0.
73

R.L. Schilling: Measures, Integrals & Martingales
If2n ∈ T−1(A),n >0, then we see that2n+2 = 2(n+1) ∈A. AsA ∈ A this yields
2n+3∈ Aand so2n+1= T−1(2n+3)∈ T−1(A). Therefore,T is measurable.
On the other hand,T−1 is not measurable: the setA={k;k ⩽0} is contained inA, but
T(A)={ k∶k ⩽2}∉ A (use2=2 ⋅1∈ A, but2⋅1+1=3∉ A).
■■
Problem 7.4 Solution:
(i) First of all we remark thatT−1
i (Ai)is itself a-algebra, cf. Example 3.3(vii).
IfC is a-algebra of subsets ofX such thatTi ∶ (X,C) →(Xi,Ai) becomes measurable,
we know from the very deﬁnition thatT−1(Ai) ⊂ C. From this, however, it is clear that
T−1(Ai)is the minimal-algebra that rendersT measurable.
(ii) From part (i) we know that(Ti,i ∈I) necessarily containsT−1
i (Ai) for everyi∈I. Since
⋃
iT−1
i (Ai) is, in general, not a-algebra, we have
⋃
iT−1
i (Ai)

⊂ (Ti,i ∈I). On the
other hand, eachTi is, because ofT−1
i (Ai) ⊂ ⋃
iT−1
i (Ai) ⊂ (Ti,i ∈ I) measurable w.r.t.

⋃
iT−1
i (Ai)

and this proves the claim.
■■
Problem 7.5 Solution:
(i), (ii)
1T−1(A‡)(x)=1 ⇔ x∈T−1(A‡) ⇔ T(x)∈ A‡
⇔ 1A‡(T(x))=1 ⇔(1A‡◦T)(x)=1
Since an indicatior function can only assume the values0 and1, the claimed equality
follows for the value0 by negating the previously shown equivalence.
(iii) “⇒”: Assume thatT is measurable. We haveT−1(A‡)∈ A ∀A‡∈A‡and sinceA is
a-algebra, we conclude
(T)= ({T−1(A‡)ðA‡∈A‡})⊂(A)= A.
“⇐”:(T)⊂A implies, in particular,
T−1(A‡)∈ A ∀A‡∈A‡,
i.e.,T is measurable.
(iii) Theorem7.6showsthatimagemeasuresaremeasures. Bythedeﬁnitionof T,wehave
T−1(E‡) =E and◦T−1(E‡) < ∞, resp.,◦T−1(E‡) = 1follows from the deﬁnition
of image measures.
The image measure obtained from a-ﬁnite measure need not be-ﬁnite!
Counterexemple: Let  be the counting measure onZ2 and deﬁneT((x,y)) = x.
While is-ﬁnite, the image measureT()isn’t.
74

Solution Manual. Last update 18th July 2019
■■
Problem 7.6 Solution: We have
T−1(G)⊂ T −1((G))
«›››ﬂ›››‹
is itself a-algebra
- ⇒(T−1(G))⊂T −1((G)).
Fortheconverseconsider T ∶(X,(T−1(G))) →(Y, (G)). Bytheverychoiceofthe -algebras
and sinceT−1(G) ⊂ (T−1(G)) we ﬁnd thatT is(T−1(G))∕(G) measurable—mind that we
only have to check measurability at a generator (here:G) in the image region. Thus,
T−1((G))⊂(T−1(G)).
Alternative: We have
T−1(G)⊂ T −1((G))
«›››ﬂ›››‹
is itself a-algebra
- ⇒(T−1(G))⊂T −1((G)).
For the converse, setΣ ∶= {G ∈ (G) ∶T−1(G) ∈(T−1(G))}. It is not hard to see thatΣ is
itself a-algebra and thatG ⊂Σ⊂(G). Thus,(G)=Σ and soT−1((G))⊂(T−1(G)).
■■
Problem 7.7 Solution: We have to show that
f ∶(F,ℱ) →(X,(Ti, i∈I)) measurable
⇐ ⇒ ∀i∈I ∶Ti◦f ∶(F,ℱ) →(Xi,Ai) measurable.
Now
∀i∈I ∶(Ti◦f)−1(Ai)⊂ℱ ⇐ ⇒∀i∈I ∶f−1 T−1
i (Ai)⊂ℱ
⇐ ⇒f−1
˝
i∈IT−1
i (Ai)

⊂ℱ
(∗)
⇐ ⇒
4
f−1
˝
i∈IT−1
i (Ai)
5
⊂ℱ
(∗∗)
⇐ ⇒f−1


˝
i∈IT−1
i (Ai)

⊂ℱ.
Only(*)and(**)arenotimmediatelyclear. Thedirection‘ ⇐ -’in(*)istrivial,while‘ - ⇒’follows
if we observe that the right-hand side,ℱ, is a-algebra. The equivalence (**) is another case of
Problem 7.6 (see there for the solution!).
■■
Problem 7.8 Solution: Using the notation of the foregoing Problem 7.7 we put
I ={1,2,…,m} and Tj ∶=j ∶ Rm → R, j(x1,…,xm)∶= xj
i.e.j is the coordinate projection,Aj ∶=ℬ(R).
75

R.L. Schilling: Measures, Integrals & Martingales
Since eachj is continuous, we have(1,…,m) ⊂ ℬ(Rm) so that Problem 7.7 applies and
proves
f isℬ(Rm)-measurable ⇐ ⇒
fj =j◦f isℬ(R)-measurable for allj=1,2,…,m.
Remark. We will see, in fact, in Chapter 14 (in particular in Theorem 14.17) that we have the
equality(1,…,m)= ℬ(Rm).
■■
Problem 7.9 Solution: Ingeneralthedirectimage T(A)ofa -algebraisnotanylongera -algebra.
(Σ1) and (Σ3) hold, but (Σ2) will, in general, fail. Here is an example: TakeX = X‡= N, take
any-algebraA otherthan {ç, N}in N,andlet T ∶ N → N,T(j)=1 betheconstantmap. Then
T(ç)=ç butT(A)={1} wheneverA ≠ç. Thus,{1}= T(Ac) ≠[T(A)]c = N ⧵{1}butequality
would be needed ifT(A)were a-algebra. This means thatΣ2 fails.
Necessary and suﬃcient forT(A) to be a-algebra is, clearly, thatT−1 is a measurable map
T−1∶X‡ →X.
Warning. Direct images of measurable sets behave badly – even if the mapping is good. For
example, the continuous (direct) image of a Borel set need not be Borel! (It is, however, analytic
or Souslin).
■■
Problem 7.10 Solution: Consider fort >0 the dilationmt ∶ Rn → Rn, x → t⋅x. Since mt is
continuous, it is Borel measurable. Moreover,m−1
t =m1∕t and so
t⋅B=m−1
1∕t(B)
which shows thatn(t⋅B)= n◦m−1
1∕t(B)= m1∕t(n)(B)is actually an image measure ofn. Now
show the formula ﬁrst for rectanglesB=
n
×××
j=1
[aj,bj)(as in Problem 5.9) and deduce the statement
from the uniqueness theorem for measures.
■■
Problem 7.11 Solution:
(i) The hint is indeed already the proof. Almost, that is... Let be some measure as speciﬁed
in the problem. From Problam 6.1(iii) we know that the Stieltjes functionF ∶= F then
satisﬁes
[a,b)= F(b)− F(a)= 1[F(a),F(b))
(#)
= 1(F([a,b)))
(##)
= 1◦F([a,b)).
The crunching points in this argument are the steps(#) and(##).
76

Solution Manual. Last update 18th July 2019
(#) This is o.k. sinceF was continuous, and the intermediate value theorem for continuous
functionstellsusthatintervalsaremappedtointervals. So,noproblemhere,justalittle
thinking needed.
(##) This is more subtle. We have deﬁned image measuresonly for inverse maps, i.e. for
expressionsofthetype 1◦G−1 whereGwasmeasurable. Soourjobistoseethat F can
be obtained in the formF = G−1 whereG is measurable. In other words, we have to
invertF. Theproblemisthatweneedtounderstandthat,if F(x)isﬂatonsomeinterval
(a,b) inversion becomes a problem (since thenF−1 has a jump—horizontals become
verticals in inversions, as inverting is somehow the mirror-image w.r.t. the 45-degree
line in the coordinate system.).
So, if there are no ﬂat bits, then this means thatF is strictly increasing, and it is clear
thatG exists and is even continuous there.
If we have a ﬂat bit, let’s say exactly ifx ∈ [a,b] and callF(x) =F(a) =F(b) =C
forthose x; clearly,F−1 jumpsat C andwemustseetoitthatwetakeaversionof F−1,
say one which makesF−1 left-continuous atC—note that we could assign any value
from[a,b] toF−1(C)—which is accomplished by settingF−1(C) =a. (Draw a graph
to illustrate this!)
There is A canonical expression for such a ‘generalized’ left-continuous inverse of an
increasing function (which may have jumps and ﬂat bits—jumps ofF become just ﬂat
bits in the graph ofF−1, think!) and this is:
G(y)=inf{ x∶F(x) ⩾y}
Let us check measurability:
y0∈{G ⩾} ⇐ ⇒G(y0) ⩾
def
⇐ ⇒inf{F ⩾y0} ⩾
(‡)
- ⇒F() ⩽y0
⇐ ⇒y0∈[F(),∞).
SinceF is monotonically increasing, we ﬁnd also ‘⇐ -’ in step(‡), hence
{G ⩾}=[ F(),∞)∈ ℬ(R)
which shows thatG is measurable. Even more: it shows thatG−1(x)∶=inf{ G ⩾}=
F(x). Thus,1◦F =1◦G−1= is indeed an image measure of1.
(ii) We haveF(x)= F0(x)= 1(0,∞)(x) and its left-continuous inverseG(y) in the sense of part
77

R.L. Schilling: Measures, Integrals & Martingales
(i) is given by
G(y)=
⎧
⎪
⎪
⎨
⎪
⎪⎩
+∞, y> 1
0, 0<y ⩽1
−∞, y ⩽0
.
This function is clearly measurable (usēℬ to accommodate±∞) and so the claim holds in
this case. Observe that in this caseF is not any longer continuous but only left-continuous.
■■
Problem 7.12 Solution:
(i) See Figure 1.4 on page 4.
(ii) EachCn is a ﬁnite union of2n closed and bounded intervals. As such,Cn is itself a closed
andboundedset,hencecompact. Theintersectionofclosedandboundedsetsisagainclosed
and bounded, so compact. This shows thatC is compact. ThatC is non-empty follows from
the intersection principle: if one has a nested sequence of non-empty compact sets, their
intersection is not empty. (This is sometimes formulated in a somewhat stronger form and
called: ﬁnite intersection property. The general version is then: Let(Kn)n∈N be a sequence
of compact sets such thateach ﬁnitesub-family has non-void intersection, then⋂
nKn ≠
ç). This is an obvious generalization of the interval principle: nested non-void closed and
bounded intervals have a non-void intersection.
(iii) At stepn we remove open middle-third intervals of length3−n. To be precise, we partition
Cn−1 in pieces of length3−n and remove every other interval. The same eﬀect is obtained if
we partition[0,∞) in pieces of length3−n and remove every other piece. Call the taken out
piecesFn andset Cn=Cn−1 ⧵Fn, i.e.weremovefrom Cn−1 evenpieceswhichwerealready
removedinprevioussteps. Itisclearthat Fn exactlyconsistsofsetsoftheform (3k+1
3n , 3k+2
3n ),
k∈ N0 which comprises exactly ‘every other’ set of length3−n. Since we do this for every
n, the setC is disjoint to the union of these intervals overk∈ N0 andn∈ N.
(iv) SinceCn consistsof 2n intervalsJ1⊍…⊍J2n, eachofwhichhaslength 3−n (provethisbya
trivial induction argument!), we get
(Cn)= (J1)+…+ (J2n)=2 n⋅3−n=
2
3
n
where we also use (somewhat pedantically) that
[a,b]= ([a,b)⊍{b})= [a,b)+ {b}= b−a+0= b−a.
Now using Proposition 4.3 we conclude that(C)=inf n(Cn)=0 .
(v) Fix >0andchoose nsobigthat 3−n< . ThenCnconsistsof 2ndisjointintervalsoflength
3−n< andcannotpossiblycontainaballofradius . SinceC ⊂Cn,thesameappliesto C.
Since wasarbitrary,wearedone. (Remark: anopenballin Rwithcentre xisobviouslyan
open interval with midpointx, i.e.(x−,x +).)
78

Solution Manual. Last update 18th July 2019
(vi) Fixn and letk= 0,1,2,…,3n−1−1. We saw in (c) that at stepn we remove the intervals
Fn, i.e. the intervals of the form
0
3k+1
3n ,3k+2
3n
1
=
0
0.∗∗∗…∗1«›››ﬂ›››‹
n
000… , 0.∗∗∗…∗2«›››ﬂ›››‹
n
000…
1
where we use the ternary representation ofx. These are exactly the numbers in[0,1]whose
ternary expansion has a1 at thenth digit. As0.∗∗∗ … ∗ 1 = 0.∗∗∗ … ∗ 022222…has
two representations, the left endpoint stays in. Since we do this for every stepn ∈ N, the
claim follows.
(vii) Taket ∈ C with ternary representationt = 0.t1t2t3…tj…,tj ∈ {0,2} and map it to the
binarynumber b=0.t1
2
t2
2
t3
2 …
tj
2 withdigits bj =
tj
2 ∈{0,1}. Thisgivesabijectionbetween
C and[0,1], i.e. both have ‘as inﬁnitely many’ points, i.e.#C =#[0,1]. Despite of that
(C)=0 ≠1= ([0,1])
which is, by the way, another proof for the fact that-additivity for the Lebesgue measure
does not extend to general uncountable unions.
■■
Problem 7.13 Solution:
(i) Sinceç∈ ℰ andç∈ ℱ we get
∀E∈ℰ ∶E∪ç∈ ℰ ⋓ℱ - ⇒ℰ ⊂ℰ ⋓ℱ
and
∀F ∈ℱ ∶ç∪ F ∈ℰ ⋓ℱ - ⇒ℱ ⊂ℰ ⋓ℱ
so thatℰ ∪ℱ ⊂ ℰ ⋓ℱ. A similar argument, using thatX ∈ ℰ and X ∈ ℱ, shows
ℰ∪ℱ ⊂ℰ ⋒ℱ.
(ii) LetA,B ⊂ Xsuch thatA∩B ≠ç,A∪B ≠X and thatA ⊄ B,B ⊄ A. Then we ﬁnd for
ℰ ∶={ç,A,A c,X}andℱ ∶={ç,B,B c,X}that
ℰ∪ℱ ={ç,A,B,A c,Bc,X}
while
ℰ ⋓ℱ={ç,A,B,A c,Bc,A ∪B,Ac∪Bc,A ∪Bc,Ac∪B,X}.
A similar example works forℰ ⋒ℱ.
(iii) Part (i) shows immediately that
(ℰ ⋓ℱ)⊃(ℰ∪ℱ) and (ℰ ⋒ℱ)⊃(ℰ∪ℱ).
79

R.L. Schilling: Measures, Integrals & Martingales
Conversely, it is obvious that
ℰ ⋓ℱ ⊂(ℰ∪ℱ) and ℰ ⋒ℱ ⊂(ℰ∪ℱ)
so that
(ℰ ⋓ℱ)⊂(ℰ∪ℱ) and (ℰ ⋒ℱ)⊂(ℰ∪ℱ)
which proves
(ℰ ⋓ℱ)= (ℰ∪ℱ)= (ℰ ⋒ℱ).
■■
80

8 Measurable functions.
Solutions to Problems 8.18.26
Problem 8.1 Solution: We remark, ﬁrst of all, that{u ⩾ } =u−1([x,∞)) and, similarly, for the
other sets. Now assume that{u ⩾}∈ A for all. Then
{u> }= u−1((,∞))= u−1
0 ˝
k∈N

+ 1
k,∞
1
=
˝
k∈N
u−1

+ 1
k,∞

=
˝
k∈N
{u ⩾+ 1
k}
«››››ﬂ››››‹
by assumption∈A
∈A
sinceA is a-algebra.
Conversely, assume that{u> }∈ A for all. Then
{u ⩾}= u−1([,∞))= u−1
0 Ì
k∈N

− 1
k,∞
1
=
Ì
k∈N
u−1

− 1
k,∞

=
Ì
k∈N
{u> − 1
k}
«››››ﬂ››››‹
by assumption∈A
∈A.
sinceA is a-algebra. Finally, as
{u> }c ={u ⩽} and {u ⩾}c ={u< }
we have that{u > } ∈A if, and only if,{u ⩽ } ∈A and the same holds for the sets{u ⩾
},{u< }.
■■
Problem 8.2 Solution: Recallthat B∗∈ℬ if,andonlyif B∗=B∪C whereB∈ℬ andC isanyof
the following sets:ç,{−∞},{∞},{−∞,∞}. Using the fact thatℬ is a-algebra and using this
notation (that is:ℬ-sets carry an asterisk∗) we see
(Σ1) TakeB=ç∈ ℬ,C =ç to see thatç∗=ç∪ç∈ ℬ;
(Σ2) LetB∗∈ℬ. Then (complements are to be taken inℬ
(B∗)c =(B∪C)c
81

R.L. Schilling: Measures, Integrals & Martingales
=Bc∩Cc
=( R ⧵B)∩( R ⧵C)
=( R ⧵B∪{−∞,+∞})∩( R ⧵C)
=(( R ⧵B)∩( R ⧵C))∪({−∞ ,+∞}∩( R ⧵C))
=( R ⧵B)∪({−∞ ,+∞}∩( R ⧵C))
which is again of the typeℬ-set union a set of the listç,{−∞},{∞},{−∞,∞}, hence it is
inℬ.
(Σ3) LetB∗
n ∈ℬ andB∗
n =Bn∪Cn. Then
B∗=
˝
n∈N
B∗
n =
˝
n∈N
(Bn∪Cn)=
˝
n∈N
Bn∪
˝
n∈N
Cn=B∪C
withB∈ℬ andC from the listç,{−∞},{∞},{−∞,∞}, henceB∗∈ℬ.
A problem is the notationℬ = ℬ(R). While the left-hand side can easily be deﬁned by (8.5),
ℬ(R) has a well-deﬁned meaning as the (topological) Borel-algebra over the setR, i.e. the-
algebra in R which is deﬁned via the open sets inR. To describe the open setsO(R) of R we
use require, that each pointx ∈ U∗ ∈ O(R) admits an open neighbourhoodB(x) insideU∗. If
x ≠ ±∞, we takeB(x) as the usual open-interval aroundx with >0 suﬃciently small. If
x= ±∞we take half-lines[−∞,a) or(b,+∞] respectively withðað,ðbð suﬃciently large. Thus,
O(R) adds toO(R) a few extra sets and open sets are therefore of the formU∗ = U ∪C with
U ∈O(R)andC being of the form[−∞,a)or(b,+∞]orçor R or unions thereof.
Thus,O(R)= R∩O(R)and therefore
ℬ(R)= R∩ℬ(R)
(this time in the proper topological sense).
■■
Problem 8.3 Solution:
(i) Notice that the indicator functions1A and 1Ac are measurable. By Corollary 8.11 sums and
productsofmeasurablefunctionsareagainmeasurable. Since ℎ(x)canbewrittenintheform
ℎ(x)= 1A(x)f(x)+ 1Ac(x)g(x), the claim follows.
(ii) Thecondition fjðAj∩Ak =fkðAj∩Ak justguaranteesthat f(x)iswell-deﬁnedifweset f(x)=
fj(x)forx∈Aj. Using⋃
jAj =X we ﬁnd forB∈ℬ(R)
f−1(B)=
˝
j∈N
Aj∩f−1(B)=
˝
j∈N
Aj∩f−1
j (B)
«›››››ﬂ›››››‹
∈A
∈A.
Analternativesolution wouldbetomakethe Aj’sdisjoint,e.g.bysettingC1∶=A1,Ck∶=
Ak ⧵(A1∪⋯∪Ak−1). Then
f =
É
j
1Cjf =
É
j
1Cjfj
82

Solution Manual. Last update 18th July 2019
and the claim follows from Corollaries 8.11 and 8.10.
■■
Problem 8.4 Solution: Since 1B isℬ-measurableif,andonlyif, B∈ℬ theclaimfollowsbytaking
B∈ℬ such thatB∉A (this is possible asℬ aA.
■■
Problem 8.5 Solution: Bydeﬁnition,f ∈  ifitisastep-functionoftheform f = ∑N
j=0aj1Aj with
someaj ∈ R andAj ∈A. Since
f+=
É
0⩽j⩽N
aj ⩾0
aj1Aj and f−=
É
0⩽j⩽N
aj ⩽0
aj1Aj,
f± are again of this form and therefore simple functions.
Theconverseisalsotruesince f+
f−f−—see(8.8)orProblem8.6—andsincesumsanddiﬀerences
of simple functions are again simple.
■■
Problem 8.6 Solution: By deﬁnition
u+(x)=max{ u(x),0} and u−(x)=−min{ u(x),0}.
Now the claim follows from the elementary identities that for any two numbersa,b ∈ R
a+0=max{ a,0}+min{ a,0} and ðað=max{a,0}−min{ a,0}
which are easily veriﬁed by considering all possible casesa ⩽0 resp.a ⩾0.
■■
Problem 8.7 Solution: If we show that{u > } is an open set, it is also a Borel set, henceu is
measurable.
Letusﬁrstunderstandwhatopennessmeans: {u> }isopenmeansthatfor x∈{u> }weﬁnd
some (symmetric) neighbourhood (a ‘ball’) of the type(x−ℎ,x +ℎ)⊂{u> }. What does this
mean? Obviously,thatu(y)> forany y∈(x−ℎ,x+ℎ)and,inotherwords, u(y)> whenever
y is such thatðx−yð<ℎ . And this is the hint of how to use continuity: we use it in order to ﬁnd
the value ofℎ.
ubeing continuous atxmeans that
∀ >0 ∃  >0 ∀y∶ ðx−yð< ∶ ðu(x)− u(y)ð<.
Sinceu(x)> we know that for a suﬃciently small we still haveu(x) ⩾+. Take this and
ﬁnd the corresponding. Then
u(x)− u(y) ⩽ ðu(x)− u(y)ð< ∀ðx−yð<
83

R.L. Schilling: Measures, Integrals & Martingales
and since+ ⩽u(x)we get
+−u(y)< ∀ðx−yð<
i.e.u(y)> fory such thatðx−yð< . This means, however, thatℎ= does the job.
■■
Problem 8.8 Solution: Theminimum/maximumoftwonumbers a,b ∈ Rcanbewrittenintheform
min{a,b}= 1
2
 a+b−ða−bð
max{a,b}= 1
2
 a+b+ða−bð
whichshowsthatwecanwrite min{x,0}andmax{x,0}asacombinationofcontinuousfunctions.
As such they are again continuous, hence measurable. Thus,
u+=max{u,0}, u −=−min{ u,0}
are compositions of measurable functions, hence measurable.
■■
Problem 8.9 Solution:
(i) From the deﬁnition of the supremum we get
sup
i
fi(x)> ⇐ ⇒∃i0∈I ∶fi0(x)>
⇐ ⇒∃i0∈Ifi0(x)>
⇐ ⇒x∈
˝
i
{fi>}.
(ii) Letx∈{sup ifi <}. Then we havefj(x) ⩽supi∈Ifi(x)< for allj ∈I; this
meansx∈{fj <}for allj∈I and sox∈ ⋂
j∈I{fj <}.
(Note: ‘⊃’ is, in general, wrong. To see this, use e.g.fi(x) ∶= −1
i,i ∈ N, and
=0 . Then we have{supifi<0}=ç ≠E= ⋂
i{fi<0}.)
(iii) Letx∈ ⋃
i{fi ⩾}. Then there is somei0∈I such thatx∈{fi0 ⩾}, hence
sup
i∈I
f(x) ⩾fi0(x) ⩾.
(iv) This follows from
sup
i∈I
fi(x) ⩽ ⇐ ⇒∀i∈I ∶fi(x) ⩽
⇐ ⇒∀i∈I ∶x∈{fi ⩽}
⇐ ⇒x∈
Ì
i∈I
{fi ⩽}.
(v)–(viii) can be proved like parts (i)–(iv).
84

Solution Manual. Last update 18th July 2019
■■
Problem 8.10 Solution: Thefj are step-functions where the bases of the steps are the setsAj
k and
Aj. Since they are of the form, e.g.k2−j ⩽u< (k+1)2−j= k2−j ⩽u∩u< (k+1)2−j,
it is clear that they are not only inA but in(u).
■■
Problem 8.11 Solution:
Corollary 8.12 Ifu± are measurable, it is clear thatu=u+−u− is measurable since diﬀerences
of measurable functions are measurable.
(FortheconversewecouldusethepreviousProblem8.10,butwegiveanalternativeproof...)
Conversely, letube measurable. Thensn ↑u(this is short for:limn→∞sn(x)= u(x)and this
isanincreasinglimit)forsomesequenceofsimplefunctions sn. Nowitisclearthat s+
n ↑u+,
ands+
n issimple,i.e. u+ ismeasurable. Asu=u+−u− weconcludethat u−=u+−uisagain
measurable as diﬀerence of two measurable functions. (Notice that in no case ‘∞−∞ ’ can
occur!)
Corollary 8.13 This is trivial if the diﬀerenceu−v is deﬁned. In this case it is measurable as
diﬀerence of measurable functions, so
{u<v }={0 <u −v}
etc. is measurable.
Let us be a bit more careful and consider the case where we could encounter expressions of
the type ‘∞−∞ ’. Sincesn ↑ufor simple functions (they are alwaysR-valued...) we get
{u ⩽v}={sup
n
sn ⩽u}
(∗)
=
Ì
n
{sn ⩽u}=
Ì
n
{0 ⩽u−sn}
andthelatterisaunionofmeasurablesets,hencemeasurable. Now {u<v }={ u ⩾v}c and
wegetmeasurabilityafterswitchingtherolesof uandv. Finally{u=v}={ u ⩽v}∩{u ⩾v}
and{u ≠v}={ u=v}c.
Let me stress the importance of ‘⩽’ in(∗)above: we use here
x∈{sup
n
sn ⩽u} ⇐ ⇒sup
n
sn(x) ⩽u(x)
(∗∗)
⇐ ⇒sn(x) ⩽u(x) ∀ n
⇐ ⇒x∈
Ì
{sn ⩽u}
and this would be incorrect if we had had ‘<’, since the argument would break down at(∗∗)
(only one implication would be valid: ‘- ⇒’).
■■
Problem 8.12 Solution: SinceXis-ﬁnite,thereisanexhaustingsequence An ↑Xwith(An)<∞.
Letu∈ (A).
85

R.L. Schilling: Measures, Integrals & Martingales
• It is clearly enough to consideru ⩾ 0, otherwise we consider positive and negative parts
separately. By the Sombrero lemma (Theorem 8.8) there is a sequence(un)n ⊂ (A) with
0 ⩽ un(x) ↑ u(x) for allx∈ X. SinceAn ↑ X, we also getun1An ↑ u, i.e. we can without
loss of generality assume that the standard representation of eachun is of the form
un=
M(n)É
m=1
n,m1An,m,  n,m ⩾0, An,m∈A, (An,m)<∞.
• From (an obvious variant of) Problem 5.12 we know that we can approximateAn,m having
ﬁnitemeasure by someGn,m ∈G in such a way that{1Gn,m ≠ 1An,m} ⩽2−n∕M(n) (note:
ð1A− 1Bð= 1A▵B).
Moreover,
fn(x)∶=
M(n)É
m=1
n,m1Gn,m(x)
and since{fn ≠un}⊂ ⋃
mGn,m▵An,m, we get{fn ≠un} ⩽2−n.
Aslimn→∞un(x)= u(x)for allx, we ﬁnd from the continuity of the measure (from above)
(lim
n→∞
fn ≠u) ⩽
H
Ì
k∈N
˝
n⩾k
{fn ≠un}
I
⩽ lim
k→∞
∞É
n=k
{fn ≠un}
⩽ lim
k→∞
∞É
n=k
2−n=0.
This shows that(G)∋ fn(x) →u(x)for allx∉N with(N)=0 .
An alternative proof can be based on the monotone class theorem. We sketch the steps below
(notation as above and in Theorem 8.15):
• Set n∶= u∈ (An∩A)∶∃( fi)i⊂ (An∩G), ∃Nn∈A,(Nn)=0 , ∀x∉Nn∶fi(x) →u(x).
Obviously n isavectorspacewhichisstableunderboundedsuprema(useadiagonalargu-
ment and the fact that the union of countably many null sets is again a null set).
• Observe that1An, 1An∩A∈ n for allA∈A by the result of Problem 5.12.
• Use the monotone class theorem.
• Gluetogetherthesets nbyconsidering u=lim nu1An. Thisleadsagaintoacountableunion
of null sets.
■■
Problem 8.13 Solution: Ifuisdiﬀerentiable,itiscontinuous,hencemeasurable. Moreover,since u‡
exists, we can write it in the form
u‡(x)= lim
k→∞
u x+ 1
k
−u(x)
1
k
86

Solution Manual. Last update 18th July 2019
i.e. as limit of measurable functions. Thus,u‡is also measurable.
■■
Problem 8.14 Solution: Itissometimesnecessarytodistinguishbetweendomainandrange. Weuse
the subscriptx to signal the domain, the subscriptyfor the range.
(i) Since f ∶ Rx → Ry is f(x) =x, the inverse function is clearlyf−1(y) =y. So if we
take any Borel setB ∈ℬ(Ry) we getB = f−1(B) ⊂ Rx. Since, as we have seen,(f) =
f−1(ℬ(Ry)),theaboveargumentshowsthat f−1(ℬ(Ry))= ℬ(Rx),hence (f)= ℬ(Rx).
(ii) The inverse map ofg(x) =x2 is multi-valued, i.e. ify = x2, theny = ±
√
x. So g−1 ∶
[0,∞) → R, g−1(y) = ±√y. Let us take someB ∈ ℬ(Ry). Since g−1 is only deﬁned
for positive numbers (squares yield positive numbers only!) we have thatg−1(B)= g−1(B∩
[0,∞))=
√
B∩[0,∞)∪(−
√
B∩[0,∞))(whereweusetheobviousnotation
√
A={
√
a∶
a∈A} and−A={−a∶a∈A} wheneverAis a set). This shows that
(g)={
√
B∪(−
√
B)∶ B∈ℬ,B ⊂[0,∞)}
={
√
B∪(−
√
B)∶ B∈[0,∞)∩ ℬ}
where we use the notation of trace-algebras in the latter identity.
(Itisaninstructiveexercisetocheckthat (g)isindeeda -algebra. Thisis, ofcourse, clear
from the general theory since(g) =g−1([0,∞)∩ ℬ), i.e. it is the pre-image of the trace
-algebra and pre-images of-algebras are always-algebras.
(iii) A very similar calculation as in part (ii) shows that
(ℎ)={ B∪(−B)∶ B∈ℬ,B ⊂[0,∞)}
={B∪(−B)∶ B∈[0,∞)∩ ℬ}.
(iv) As warm-up we follow the hint. The set{(x,y) ∶x+y = } is the liney = −x in the
x-y-plane, i.e. a line with slope−1 and shift. So{(x,y)∶ x+y ⩾} would be the points
above this line and{(x,y)∶  ⩾x+y ⩾}={( x,y)∶ x+y∈[,]}would be the points
in the strip which has the linesy=−xandy=−xas boundaries.
More general, take a Borel setB∈ℬ(R)and observe that
F−1(B)={( x,y)∶ x+y∈B}.
This set is, in an abuse of notation,y = B−x, i.e. these are all lines with slope−1 (135
degrees) andevery possible shift from the setB—it gives a kind of stripe-pattern. To sum
up:
(F)={ all 135-degree diagonal stripes inR2 with ‘base’B∈ℬ(R)}.
87

R.L. Schilling: Measures, Integrals & Martingales
(v) Again follow the hint to see that{(x,y)∶ x2+y2=r} is a circle, radiusr, centre(0,0). So
{(x,y) ∶x2+y2 ⩽ r} is the solid disk, radiusr, centre(0,0) and{(x,y) ∶R ⩾ x2+y2 ⩾
r} = {(x,y) ∶x2+y2 ∈ [r,R]} is the annulus with exterior radiusR and interior radiusr
about(0,0).
More general, take a Borel setB ⊂[0,∞),B ∈ ℬ(R), i.e.B ∈ [0,∞)∩ ℬ(R) (negative
radii don’t make sense!) and observe that the set{(x,y)∶ x2+y2∈B}gives a ring-pattern
which is ‘supported’ by the setB (i.e. we take all circles passing throughB...). To sum up:
(G)={ a set consists of all circles inR2 about(0,0)
passing throughB∈ℬ[0,∞)∩ B(R)}.
■■
Problem 8.15 Solution: Assume ﬁrst thatu is injective. This means that every point in the range
u(R) comes exactly from one uniquely deﬁnedx ∈ R. This can be expressed by saying that
{x} = u−1({u(x)}) — but the singleton{u(x)} is a Borel set in the range, so{x} ∈ (u) as
(u)= u−1(u(R)∩ ℬ).
Conversely, assume that for eachx we have{x} ∈(u). Fix anx0 and callu(x0) =. Sinceu
is measurable, the set{u = } = {x ∶ u(x) =} is measurable and, clearly,{x0} ⊂ {u = }.
But if we had anotherx0 ≠x1∈{u=}this would mean that we could never ‘produce’{x0}on
its own as a pre-image of some set, but we must be able to do so as{x0}∈ (u), by assumption.
Thus,x1 = x0. To sum up, we have shown that{u = } consists of one point only, i.e. we have
shown thatu(x0)= u(x1)impliesx0=x1 which is just injectivity.
■■
Problem 8.16 Solution: Clearly u ∶ R → [0,∞). So let’s takeI = (a,b) ⊂ [0,∞). Then
u−1((a,b))=(− b,−a)∪( a,b). This shows that for∶=◦u−1
(a,b)= ◦u−1((a,b))=  (−b,−a)∪( a,b)=(−b,−a)+ (a,b)
=(−a−(−b))+( b−a)=2( b−a)=2 ((a,b)).
This shows that=2if we allow only intervals from[0,∞), i.e.
(I)=2  I∩[0,∞) for any intervalI ⊂R.
Since a measure on the Borel sets is completely described by (either: open or closed or half-open
or half-closed) intervals (the intervals generate the Borel sets!), we can invoke the uniqueness
theorem to guarantee that the above equality holds for all Borel sets.
■■
Problem 8.17 Solution:
88

Solution Manual. Last update 18th July 2019
(i) Because of Lemma 7.2 it is enough to check measurability for some generator. LetB =
[a,b)∈J,a<b . We have
Q−1(B)= E∩
⎧
⎪
⎪
⎨
⎪
⎪⎩
çifa,b ⩽0
(−
√
b,+
√
b)ifa ⩽0,b> 0

−
√
b,−
√
a

∪
√
a,
√
b

ifa,b> 0
These sets are inℬ(E), thereforeQisℬ(E)∕ℬ(R)-measurable.
(ii) Denote byT the embedding ofE into R, i.e.T ∶x →x. Formally, we get
(T2∈B)= (±T ∈
√
B).
More precisely: we have already seen that◦Q−1 is a measure (Theorem 7.6). SinceJ
is∩-stable and◦Q−1 a ﬁnite measure ( comes from a ﬁnite Lebesgue measure), we get
uniqueness from Theorem 5.7, and it enough to consider sets of the formB=[a,b)∈J,
a ⩽b.
• Part (i) gives
(Q−1(B))=
⎧
⎪
⎪
⎨
⎪
⎪⎩
0, b ⩽0ora> 1
([0,
√
b)), a< 0,b> 0
([
√
a,
√
b∧1)), 0<a< 1
=
⎧
⎪
⎨
⎪⎩
0, b ⩽0ora> 1
√
b∧1−
√
0∨ a∧1, otherwise.
• Again by part (i)
(Q−1(B))=
⎧
⎪
⎪
⎨
⎪
⎪⎩
0, b ⩽0ora> 1
([(−
√
b)∨(−1) ,
√
b∧1)), a< 0,b> 0
1
2([(−
√
b)∨(−1) ,
√
a)∪[
√
a,
√
b∧1)), 0<a< 1
=
⎧
⎪
⎨
⎪⎩
0, b ⩽0ora> 1
21
2([0∨
√
a∧1,
√
b∧1)), otherwise
=
⎧
⎪
⎨
⎪⎩
0, b ⩽0ora> 1
(
√
b∧1))−(0∧
√
a∧1), otherwise
■■
Problem 8.18 Solution:
89

R.L. Schilling: Measures, Integrals & Martingales
• clear,since u(x−2) isacombinationofthemeasurableshift 2 andthemeasurablefunction
u.
• thisistrivialsince u →euisacontinuousfunction,assuchitismeasurableandcombinations
of measurable functions are again measurable.
• this is trivial sinceu → sin(u+8) is a continuous function, as such it is measurable and
combinations of measurable functions are again measurable.
• iterate Problem 8.13
• obviously,sgnx=(−1) ⋅ 1(−∞,0)(x)+0 ⋅ 1{0}(x)+1 ⋅ 1(0,∞)(x), i.e. a measurable function.
Using the ﬁrst example, we see now thatsgnu(x−7) is a combination of three measurable
functions.
■■
Problem 8.19 Solution: BetrachtezumBeispiel T ∶[0,1) →[0,1)mitT(x)= x
2 undwn∶[0,1) →
R mitwn(x)=(−1) n1[1∕2,1)(x).
■■
Problem 8.20 Solution: LetA⊂ Rbesuchthat A∉ℬ. Thenitisclearthat u(x)= 1A(x)−1Ac(x)is
NOT measurable (take, e.g.A={f =1} which should be measurable for measurable functions),
but clearly,ðf(x)ð=1 and as constant function this IS measurable.
■■
Problem 8.21 Solution: We want to show that the sets{u ⩽ } are Borel sets. We will even show
that they are intervals, hence Borel sets. Imagine the graph of an increasing function and the line
y= cutting through. Essentially we have three scenarios: the cut happens at a point where (a)u
iscontinuousandstrictlyincreasingor(b) uisﬂator(c) ujumps—i.e.hasagap;thesethreecases
are shown in the following pictures: From the three pictures it is clear that we get in any case an
✻
✲
/u1D6FC
/u1D6FD
/u1D44E/u1D44F
✻
✲
/u1D6FC
/u1D6FD
/u1D450 /u1D44F /u1D44E
✻
✲
/u1D6FC
/u1D6FD
/u1D44E/u1D44F
1
interval for the sub-level sets{u ⩽} where is some level (in the pic’s = or=), you can
read oﬀ the intervals on the abscissa where the dotted lines cross the abscissa.
Nowlet’slookattheadditionalconditions: Firsttheintuition: Fromtheﬁrstpicture,thecontinuous
and strictly increasing case, it is clear that we can produce any interval(−∞,b] to(−∞,a] by
looking at{u ⩽ } to{u ⩽ } my moving up the-line to level. The point is here that we get
all intervals, so we get a generator of the Borel sets, so we should get all Borel sets.
90

Solution Manual. Last update 18th July 2019
Thesecondpictureisbad: thelevelset {u ⩽}is(−∞,b]andalllevelsetsbelowwillonlycome
up to the point(−∞,c], so there is no chance to get any set contained in(c,b), i.e. we cannot get
all Borel sets.
The third picture is good again, because the vertical jump does not hurt. The only ‘problem’ is
whether{u ⩽ } is(−∞,b] or(−∞,b) which essentially depends on the property of the graph
whetheru(b) = or not, but this is not so relevant here, we just must make sure that we can get
more or less all intervals. The reason, really, is that jumps as we described them here can only
happen countably often, so this problem occurs only countably often, and we can overcome it
therefore.
Sothepointis: wemustdisallowﬂatbits,i.e. (u)istheBorel -algebraif,andonly,if uisstrictly
increasing, i.e. if, and only if,u is injective. (Note that this would have been clear already from
Problem 8.15, but our approach here is much more intuitive.)
■■
Problem 8.22 Solution: For everyn∈ N the function
gn(x)∶=
nÉ
i=1
2−i1Gi(x), x ∈X,
isA∕ℬ(R)-measurable. Therefore,g = limn→∞gn isA∕ℬ(R)-measurable (pointwise limit of
measurable functions), and so(g)⊂A. For the inclusionA ⊂(g)we deﬁne
Σ∶={ A∈A ∶A∈(g)}.
Σist a-Algebra:
(Σ1) X∈Σ sinceX∈A andX∈(g).
(Σ2) ForA ∈ Σwe haveA ∈ (g); since(g) is a-algebra, we see thatAc ∈ (g); hence,
Ac ∈Σ .
(Σ3) For(An)n∈N⊂Σwe see⋃
n∈NAn∈(g), thus⋃
nAn∈Σ .
SinceGi={g=2 −i}∈ (g)we see thatG ⊂Σ. Consequently,A =(G)⊂(g).
■■
Problem 8.23 Solution: Withoutlossofgenerality,assumethat uisright-continuous(left-continuity
works analogously). Approximateu with simple functions:
un(x)∶=
2n2
É
i=1
u(xn
i+1)1[xn
i,xn
i+1)(x)
wherexn
i ∶=−n+ i
n. The functionsun are obviously Borel measurabl. We claim:
u(x)= lim
n→∞
un(x).
91

R.L. Schilling: Measures, Integrals & Martingales
Indeed: For eachx∈ R there is someN ∈ N such thatx∈[−N,N]. By deﬁnition, we ﬁnd for
alln ⩾N,
un(x)= u
0⌊nx⌋+1
n
1
(⌊nx⌋+1
n is the smallest number of the formk
n, k ∈ Z, which exceedsx.) Because of the right-
continuity ofu we getun(x) →u(x) asn →∞. Therefore,u is Borel-measurable (pointwise limit
of measurable functions).
■■
Problem 8.24 Solution: Every linear map on a ﬁnite-dimensional vector space is continuous, hence
Borel measurable.
Note thatf ∶ R → R2,f(x) ∶= (x,0)⊤, is continuous, hence Borel measurable. This map is,
however,notmeasurable with respect to the completed Borel-algebras:
To see this, letA ⊂ R, A ∉ ℬ(R), be a subset of a Lebesgue null set. ForA×{0} we see
that A×{0} ∈ ℬ(R2); this follows fromA×{0} ⊂ N ∶= R×{0} and 2(N) = 0(cf.
Problem 4.15, Problem 6.7). On the other hand,f−1(A×{0}) = A ∉ ℬ(R) ⊂ ℬ(R), i.e.
f ∶( R,ℬ(R)) →(R2,ℬ(R2)) is not measurable.
■■
Problem 8.25 Solution: Without loss of generality we consider the right-continuous situation. The
left-continuous counterpart is very similar.
• Fix!∈Ω . Notethatitisenoughtoshowthat t →(t,!)1[a,b](t)=∶ a,b(t,!)ismeasurable
for alla<b .
Indeed: Because of
(t,!)= lim
R→∞
−R,R(t,!)
the mapt → (t,!) is measurable (pointwise limit of measurable functions, cf. Corol-
lary 8.10.
Inordertokeepnotationsimple,weassumethat a=0 andb=1 ;thegeneralcaseissimilar.
Deﬁne
n(t,!)∶=
2n−1É
i=0


i+1
2n ,!

14 i
2n,i+1
2n ∧1
1(t).
For anyt∈[0,1]we have⌊2nt⌋+1
2n ↓t, and because of right-continuity,
n(t,!)= 
0⌊2nt⌋+1
2n ,!
1
, , , , , , , , , , , , , , , , , , , , →
n→∞
(t,!)
t∈[0,1]
= 0,1(t,!).
Fort∉[0,1]we haven(t,!)=0= 0,1(t,!)and, thus,
0,1(t,!)= lim
n→∞
n(t,!) ∀t∈ R,! ∈Ω.
92

Solution Manual. Last update 18th July 2019
Consequently, it is enough to show (by Corollary 8.10) that eacht →n(t,!)is measurable.
For∈ R we get
{t∶n(t,!) ⩽}=
˝
i∈I
4
i
2n,i+1
2n
1
«››››ﬂ››››‹
∈ℬ(R)
∈ℬ(R)
where
I ∶=
$
i∈{0,…,2n−1}; 
i+1
2n ,!

⩽
%
.
This proves thatt →n(t,!)is measurable.
• Sincet →(t,!)is right-continuous, we have
sup
t∈R
(t,!)=sup
t∈Q
(t,!). (⋆)
Indeed: The estimate ‘⩾’ is clear, i.e. we only have to show ‘⩽’. Using the deﬁnition of the
supremum, there is for each >0 somes∈ R such that
(s,!) ⩾sup
t∈R
(t,!)− .
Because of right-continuity we ﬁnd somer ∈ Q,r > s, such thatð(r,!)− (s,!)ð ⩽ .
Therefore,
sup
t∈Q
(t,!) ⩾(r,!) ⩾(s,!)−  ⩾sup
t∈R
(t,!)−2 .
Since >0 is arbitrary, the claim follows.
From (⋆) we get that the map! →supt∈R(t,!) is measurable (as supremum of countably
many measurable functions, cf. Corollary 8.10).
■■
Problem 8.26 Solution: ‘⇐’: Assume that there areA∕ℬ(R)-measurable functionsf,g ∶X → R
satisfyingf ⩽ ⩽g and{f ≠g}=0 . For anyx∈ R we get
{ ⩽x}={  ⩽x,f =g}∪{  ⩽x,f ≠g}
={g ⩽x,f =g}
«›››››››ﬂ›››››››‹
=∶A
∪{ ⩽x,f ≠g}
«›››››››ﬂ›››››››‹
=∶N
.
Sincef andg are measurable, we see thatA∈A. ForN we only getN ⊂{f ≠g}, i.e.N is a
subset of a-null set. By the deﬁnition ofA (see Problem 4.15) we ﬁnd{ ⩽x}∈ A.
‘⇒’: Assume, ﬁrst, thatis a simple function, i.e.
(x)=
NÉ
i=1
ci1Ai(x), x ∈X,
withci∈ R,Ai∈A (i=1,…,n). From the deﬁnition ofA we get that theAi are of the form
Ai=Bi+Ni
93

R.L. Schilling: Measures, Integrals & Martingales
withBi∈A andNi being a subset of a-null setMi∈A. Deﬁne
f(x)∶=
nÉ
i=1
ci1Bi(x), g (x)∶=
nÉ
i=1
ci1Bi∪Mi(x), x ∈X.
These are clearlyA∕ℬ(R)-measurable functions andf ⩽ ⩽g. Moreover,
(f ≠g) ⩽
H n˝
i=1
Mi
I
⩽
nÉ
i=1
(Mi)=0 .
This proves that the claim holds for simple functions.
Let be anyA∕ℬ(R)-measurable function. Using Corollary 8.9, we get a sequence(n)n∈N of
A∕ℬ(R)-measurable simple functions such thatn(x) →(x) for allx∈X. By the ﬁrst part of
this proof, there areA∕ℬ(R)-messbare Funktionenfn,gn,n ∈ N, such that mitfn ⩽ n ⩽ gn
and(fn ≠gn)=0 . Set
f(x)∶=liminf
n→∞
fn(x), g (x)∶=liminf
n→∞
gn(x), x ∈X.
The functionsf andg are againA∕ℬ(R)-measurable (Corollary 8.10) and we havef ⩽ ⩽g.
Moreover,
(f ≠g) ⩽
H
˝
n∈N
{fn ≠gn}
I
⩽
É
n∈N
(fn ≠gn)=0 .
■■
94

9 Integration of positive functions.
Solutions to Problems 9.19.14
Problem 9.1 Solution: We know that for any two simple functionsf,g ∈ + we haveI(f +g)=
I(f)+ I(g) (= additivity), and this is easily extended to ﬁnitely many, say,m diﬀerent positive
simple functions. Observe now that eachn1An is a positive simple function, hence
I
H mÉ
n=1
n1An
I
=
mÉ
n=1
I

n1An

=
mÉ
n=1
nI

1An

=
mÉ
n=1
n An
.
Put in other words: we have used the linearity ofI.
■■
Problem 9.2 Solution: We use indicator functions. Note that any ﬁxedx can be contained ink ∈
{0,1,…,N} of the setsAn. Thenx is contained inA1∪⋯∪AN as well as in k
2
 of the pairs
An∪Ak wheren<k ; as usual: m
n
=0 ifm<n . This gives
É
n
1An =k ⩽1+
0
k
2
1
= 1A1∪⋯∪AN +
É
n<k
1An1Ak
= 1A1∪⋯∪AN +
É
n<k
1An∩Ak.
Integrating this inequality w.r.t. yields the result.
■■
Problem 9.3 Solution: We check Properties 9.8(i)–(iv).
(i) This follows from Properties 9.3 and Lemma 9.5 since∫ 1Ad =I(1A)= (A).
(ii) This follows again from Properties 9.3 and Corollary 9.7 since forun∈ + withu=sup nun
(note: thesup’s are increasing limits!) we have
˚ ud = ˚ sup
n
und =sup
n
I(un)
=sup
n
I(un)
=sup
n
I(un)
= ˚ ud.
95

R.L. Schilling: Measures, Integrals & Martingales
(iii) This follows again from Properties 9.3 and Corollary 9.7 since forun,vn ∈ + with u =
supnun,v =sup nvn (note: thesup’s are increasing limits!) we have
˚ (u+v)d = ˚ lim
n→∞
(un+vn)d = lim
n→∞
I(un+vn)
= lim
n→∞
 I(un)+ I(vn)
= lim
n→∞
I(un)+ lim
n→∞
I(vn)
= ˚ ud + ˚ vd.
(iv) This was shown in Step 1 of the proof of the Beppo Levi theorem 9.6
■■
Problem 9.4 Solution: Consideronthespace ([−1,0],),(dx)= dx isLebesguemeasureon [0,1],
the sequence of ‘tent-type’ functions
fk(x)=
⎧
⎪
⎨
⎪⎩
0, −1 ⩽x ⩽−1
k,
k3 x+ 1
k), −1
k ⩽x ⩽0,
(k∈ N),
(draw a picture!). These are clearly monotonically increasing functions but, as a sequence, we do
nothave fk(x) ⩽fk+1(x)foreveryx! Notealsothateachfunctionisintegrable(withintegral 1
2k)
but the pointwise limit is not integrable.
■■
Problem 9.5 Solution: Theﬁrstpartistrivialsinceitjustsaysthatthesequencebecomesincreasing
only from indexK onwards. ThisK does not depend onxbut is uniform for the whole sequence.
Since we are anyway only interested inu=lim n→∞un =sup n⩾Kun, we can neglect the elements
u1,…,uK and consider only the then increasing sequence(un+K)n. Then we can directly apply
Beppo Levi’s theorem, Theorem 9.6.
Theotherconditionsaysthatthesequence un+K(x)isincreasingforsome K =K(x). ButsinceK
maydependon x,wewillnevergetsomeoverallincreasingbehaviourofthesequenceoffunctions.
Take, for example, on(R,ℬ(R), ∶=1),
un(x)= n2(x+ 1
n)1(−1∕n,0)(x)− n2(x− 1
n)1(0,1∕n)(x).
This is a sequence of symmetric tent-like functions of tents with base(−1∕n,1∕n) and tip atn2
(which we take out and replace by the value0). Clearly:
un(x) , , , , , , , , , , , , , , , , , , , , →
n→∞
0 and ˚ un(x)dx=1 ∀ n.
Moreover, ifn ⩾K =K(x) withK(x) deﬁned to be the smallest integer>1∕ðxð, thenun(x)=0
so that the second condition is clearly satisﬁed, but∫ un(x)dx = 1cannot converge to∫ 0dx =
∫ u(x)dx=0 .
■■
96

Solution Manual. Last update 18th July 2019
Problem 9.6 Solution: Followingthehintweset sm=u1+u2+…+ um. Asaﬁnitesumofpositive
measurablefunctionsthisisagainpositiveandmeasurable. Moreover, smincreasesto s= ∑∞
n=1un
asm →∞. Using the additivity of the integral (9.8 (iii)) and the Beppo Levi theorem 9.6 we get
˚
∞É
n=1
und = ˚ sup
m
smd =sup
m ˚ smd
=sup
m ˚ (u1+…+ um)d
=sup
m
mÉ
n=1 ˚ und
=
∞É
n=1 ˚ und.
Conversely,assumethat9.9istrue. WewanttodeducefromitthevalidityofBeppoLevi’stheorem
9.6. So let(wn)n∈N be an increasing sequence of measurable functions with limitw = supnw.
For ease of notation we setw0 ≡0. Then we can write eachwn as a partial sum
wn=(wn−wn−1)+ ⋯+(w1−w0)
of positive measurable summands of the formuk∶=wk−wk−1. Thus,
wm=
mÉ
k=1
uk and w=
∞É
k=1
uk
and, using the additivity of the integral,
˚ wd
9.9
=
∞É
k=1 ˚ ukd =sup
m ˚
mÉ
k=1
ukd =sup
m ˚ wmd.
■■
Problem 9.7 Solution: Set(A) ∶= ∫ 1Aud . Then is a[0,∞]-valued set function deﬁned for
A∈A.
(M1) Since 1ç ≡0 we have clearly(ç)= ∫ 0⋅ud =0 .
(M1) LetA= ⨃
n∈NAn a disjoint union of setsAn∈A. Then
∞É
n=1
1An = 1A
and we get from Corollary 9.9
(A)= ˚
0 ∞É
n=1
1An
1
⋅ud = ˚
∞É
n=1
 1An⋅ud
=
∞É
n=1 ˚ 1An⋅ud
=
∞É
n=1
(An).
97

R.L. Schilling: Measures, Integrals & Martingales
■■
Problem 9.8 Solution: This is actually trivial: since our-algebra isP(N), all subsets ofN are
measurable. Now the sub-level sets{u ⩽}={ k∈ N∶u(k) ⩽} are always⊂ N and as such
they are∈P(N), henceuis always measurable.
■■
Problem 9.9 Solution: We have seen in Problem 4.7 that is indeed a measure. We follow the
instructions. First, forA∈A we get
˚ 1Ad =(A)=
É
j∈N
j(A)=
É
j∈N ˚ 1Adj.
By the linearity of the integral, this easily extends to functions of the form1A +1B where
A,B ∈A and, ⩾0:
˚ (1A+1B)d = ˚ 1Ad+ ˚ 1Bd
=
É
j∈N ˚ 1Adj+
É
j∈N ˚ 1Bdj
=
É
j∈N ˚ (1A+1B)dj
and this extends obviously to simple functions which are ﬁnite sums of the above type.
˚ fd =
É
j∈N ˚ fd j ∀f ∈ +.
Finally,take u∈ + andtakeanapproximatingsequence un∈ + withsupnun=u. Thenweget
by Beppo Levi (indicated by an asterisk∗)
˚ ud
∗
=sup
n ˚ und =sup
n
∞É
j=1 ˚ undj
=sup
n
sup
m
mÉ
j=1 ˚ undj
=sup
m
sup
n
mÉ
j=1 ˚ undj
=sup
m
lim
n
mÉ
j=1 ˚ undj
=sup
m
mÉ
j=1
lim
n ˚ undj
∗
=sup
m
mÉ
j=1 ˚ lim
n
undj
=
∞É
j=1 ˚ udj
98

Solution Manual. Last update 18th July 2019
where we repeatedly use that all sup’s are increasing limits and that we may swap any two sup’s
(this was the hint to the hint to Problem 4.7.)
■■
Problem 9.10 Solution: Set wn ∶= u−un. Then thewn are a sequence of positive measurable
functions. By Fatou’s lemma we get
˚ liminf
n
wnd ⩽liminf
n ˚ wnd
=liminf
n
0
˚ ud − ˚ und
1
= ˚ ud −limsup
n ˚ und
(see, e.g. the rules forliminf andlimsup in Appendix A). Thus,
˚ ud −limsup
n ˚ und ⩾ ˚ liminf
n
wnd
= ˚ liminf
n
(u−un)d
= ˚
 u−limsup
n
un
d
and the claim follows by subtracting theﬁnitevalue ∫ ud on both sides.
Remark. Theuniformdominationof unbyanintegrablefunction uisreallyimportant. Havealook
atthefollowingsituation: (R,ℬ(R),),(dx)= dx denotesLebesguemeasure,andconsiderthe
positive measurable functionsun(x)= 1[n,2n](x). Thenlimsupnun(x)=0 butlimsupn ∫ und =
limsupnn=∞ ≠ ∫ 0d.
■■
Problem 9.11 Solution:
(i) Have a look at Appendix A, Lemma A.2.
(ii) You have two possibilities: the set-theoretic version:
 liminf
n
An
=
0˝
k
Ì
n⩾k
An
1
∗
=sup
k

0Ì
n⩾k
An
1
«››››ﬂ››››‹
⩽(An)∀ n⩾k
hence, ⩽infn⩾k(An)
⩽sup
k
inf
n⩾k
(An)
=liminf
n
(An)
99

R.L. Schilling: Measures, Integrals & Martingales
which uses at the point∗ the continuity of measures, Proposition 4.3.
The alternativewould be (i) combined with Fatou’s lemma:
 liminf
n
An
= ˚ 1liminf nAnd
= ˚ liminf
n
1And
⩽liminf
n ˚ 1And
(iii) Again, you have two possibilities: the set-theoretic version:
 limsup
n
An
=
0Ì
k
˝
n⩾k
An
1
#
=inf
k

0˝
n⩾k
An
1
«››››ﬂ››››‹
⩾(An)∀ n⩾k
hence, ⩾supn⩾k(An)
⩾inf
k
sup
n⩾k
(An)
=limsup
n
(An)
which uses at the point# the continuity of measures, Proposition 4.3. This step uses the
ﬁniteness of.
The alternativewould be (i) combined with the reversed Fatou lemma of Problem 9.10:
 limsup
n
An
= ˚ 1limsupnAnd
= ˚ limsup
n
1And
⩾limsup
n ˚ 1And
(iv) TaketheexampleintheremarktothesolutionforProblem9.10. Wewilldiscussithereinits
set-theoretic form: take(R,ℬ(R),) with denoting Lebesgue measure(dx) =dx. Put
An=[n,2n]∈ ℬ(R). Then
limsup
n
An=
Ì
k
˝
n⩾k
[n,2n]=
Ì
k
[k,∞)=ç
But0 =(ç) ⩾ limsupn(An) = limsupnn = ∞is a contradiction. (The problem is that
[k,∞)=∞ !)
■■
Problem 9.12 Solution: We use the fact that, because of disjointness,
1= 1X =
∞É
n=1
1An
100

Solution Manual. Last update 18th July 2019
so that, because of Corollary 9.9,
˚ ud = ˚
0 ∞É
n=1
1An
1
⋅ud = ˚
∞É
n=1
 1An⋅ud
=
∞É
n=1 ˚ 1An⋅ud.
Assume now that(X,A,) is-ﬁnite with an exhausting sequence of sets(Bn)n ⊂ A such that
Bn ↑X and(Bn)<∞. Then we make theBn’s pairwise disjoint by setting
A1∶=B1, A k∶=Bk ⧵(B1∪⋯∪Bk−1)= Bk ⧵Bk−1.
Nowtakeanysequence (ak)k⊂(0,∞)with∑
kak(Ak)<∞—e.g.ak∶=2 −k∕((Ak)+1)—and
put
w(x)∶=
∞É
n=1
ak1Ak.
Thenw is integrable and, obviously,w(x)>0 everywhere.
■■
Problem 9.13 Solution:
(i) We check(M1),(M2). Using the fact thatN(x,⋅)is a measure, we ﬁnd
N(ç)= ˚ N(x,ç)(dx)= ˚ 0(dx)=0 .
Further, let(An)n∈N⊂A be a sequence of disjoint sets and setA= ⨃
nAn. Then
N(A)= ˚ N

x,
Ó
nAn

(dx) =˚
É
n
N(x,An)(dx)
9.9
=
É
n ˚ N(x,An)(dx)
=
É
n
N(An).
(ii) We have forA,B ∈A and, ⩾0,
N(1A+1B)(x)= ˚
 1A(y)+ 1B(y)N(x,dy)
= ˚ 1A(y)N(x,dy)+  ˚ 1B(y)N(x,dy)
=N 1A(x)+ N 1B(x).
ThusN(f+g)(x)= Nf(x)+Ng(x)forpositivesimple f,g ∈ +(A). Moreover,sinceby
Beppo Levi (marked by an asterisk∗) for an increasing sequencefk ↑u
sup
k
Nfk(x)=sup
k ˚ fk(y)N(x,dy)
∗
= ˚ sup
k
fk(y)N(x,dy)
101

R.L. Schilling: Measures, Integrals & Martingales
= ˚ u(y)N(x,dy)
=Nu(x)
andsincethe supisactuallyanincreasinglimit,weseeforpositivemeasurable u,v ∈ +(A)
and the corresponding increasing approximations via positive simple functionsfk,gk:
N(u+v)(x)=sup
k
N(fk+gk)(x)
=sup
k
Nfk(x)+sup
k
Ngk(x)
=Nu(x)+ Nv(x).
Moreover,x → N1A(x) =N(x,A) is a measurable function, thusNf(x) is a measurable
function for all simplef ∈ +(A) and, by Beppo Levi (see above)Nu(x),u∈ +(A), is
for everyx an increasing limit of measurable functionsNfk(x). Therefore,Nu ∈ +(A).
(iii) Ifu= 1A,A∈A, we have
˚ 1A(y)N(dy)= N(A)= ˚ N(x,A)(dx)
= ˚ N1A(x)(dx).
Bylinearitythiscarriesoverto f ∈ +(A)and,byaBeppoLevi-argument,to u∈ +(A).
■■
Problem 9.14 Solution: Put
(A)∶= ˚ u⋅ 1A+
 d+ ˚ (1− u)⋅ 1A−

d.
IfA is symmetric w.r.t. the origin,A+=−A− andA±
 =A. Therefore,
(A)= ˚ u⋅ 1Ad+ ˚ (1− u)⋅ 1Ad = ˚ 1Ad =(A).
Thismeansthat  extends. Italsoshowsthat (ç)=0 . Since isdeﬁnedforallsetsfrom ℬ(R)
and since has values in[0,∞], it is enough to check-additivity.
For this, let(An)n⊂ℬ(R) be a sequence of pairwise disjoint sets. From the deﬁnitions it is clear
that the sets(An)±
 are again pairwise disjoint and that⨃
n(An)±
 =  ⨃
nAn
±
. Since each of the
set functions
B → ˚ u⋅ 1Bd, C → ˚ (1− u)⋅ 1Cd
is-additive, it is clear that their sum will be-additive, too.
The obvious non-uniqueness of the extension does not contradict the uniqueness theorem for ex-
tensions, sinceΣdoes not generateℬ(R)!
■■
102

10 Integrals of measurable functions.
Solutions to Problems 10.110.9
Problem 10.1 Solution: Letu,v be integrable functions anda,b ∈ R. Assume that eitheru,v are
real-valued or thatau+bv makes sense (i.e. avoiding the case ‘∞−∞ ’). Then we have
ðau+bvð ⩽ ðauð+ðbvð= ðað⋅ðuð+ðbð⋅ðvð ⩽K(ðuð+ðvð)
withK = max{ðað,ðbð}. Since the RHS is integrable (because of Theorem 10.3 and Properties
9.8) we have thatau+bv is integrable by Theorem 10.3. So we get from Theorem 10.4 that
˚ (au+bv)d = ˚ aud + ˚ bvd =a ˚ ud +b ˚ vd
and this is what was claimed.
■■
Problem 10.2 Solution: Without loss of generality we consideru on(0,1] (otherwise we have to
single out the pointx = 1, and this is just awkward in the notation...) We follow the hint and
show ﬁrst thatu(x)∶= x−1∕2,0< x⩽1, is Lebesgue integrable. The idea here is to construct a
sequence of simple functions approximatingufrom below. Setxi=

i
n
2
,i=0,1,…,n and
un(x)∶=
n−1É
i=0
u(xi+1)1(xi,xi+1](x)=
n−1É
i=0
n
i+1 1(xi,xi+1](x)
This is clearly a simple function. Alsoun ⩽uandlimn→∞un(x)=sup nun(x)= u(x)for allx.
SinceP(A)is just(A∩(0,1]), the integral ofun is given by
˚ undP =IP(un)=
n−1É
i=0
n
i+1
4i+1
n
2
−
i
n
25
= 1
n
n−1É
i=0
1
i+1
(i+1)2−i2= 1
n
n−1É
i=0
1
i+1 [2i+1]
⩽ 1
n
n−1É
i=0
1
i+1 [2i+2]= 1
n⋅2n=2
and is thus ﬁnite, even uniformly inn. So, Beppo Levi’s theorem tells us that
˚ udP =sup
n ˚ undP ⩽sup
n
2=2 <∞
103

R.L. Schilling: Measures, Integrals & Martingales
showing integrability.
Nowuis clearly not bounded but integrable.
■■
Problem 10.3 Solution: Clearly, isdeﬁnedonA andtakesvaluesin [0,∞]. Since1ç ≡0wehave
(ç)= ˚ 1ç⋅ud = ˚ 0d =0.
If(An)n∈N⊂A are mutually disjoint measurable sets, we get

 ∞Ó
n=1
An

= ˚ 1⨃∞
n=1An⋅ud
= ˚
∞É
n=1
1An⋅ud
=
∞É
n=1 ˚ 1An⋅ud =
∞É
n=1
(An)
which proves-additivity.
■■
Problem 10.4 Solution: ‘- ⇒’: since theAj are disjoint we get the identities
1⨃
jAj =
∞É
k=1
1Aj and so u⋅ 1⨃
jAj =
∞É
k=1
u⋅ 1Aj,
henceðu1Anð= ðuð1An ⩽ ðuð1⨃
jAj = ðu1⨃
jAjðshowingtheintegrabilityofeach u1An byTheorem
10.3. By a Beppo Levi argument (Theorem 9.6) or, directly, by Corollary 9.9 we get
∞É
j=1 ˚Aj
ðuðd =
∞É
j=1 ˚ ðuð1Ajd = ˚
∞É
j=1
ðuð1Ajd
= ˚ ðuð1⨃
jAjd < ∞.
The converse direction ‘⇐ -’ follows again from Corollary 9.9, now just the other way round:
˚ ðuð1⨃
jAjd = ˚
∞É
j=1
ðuð1Ajd =
∞É
j=1 ˚ ðuð1Ajd
=
∞É
j=1 ˚Aj
ðuðd < ∞
showing thatu1⨃
jAj is integrable.
■■
Problem 10.5 Solution: For any measurable functionu we haveu∈ 1() ⇐ ⇒ðuð∈ 1(). This
means that we may assume thatu ⩾0. Since
kÉ
n=−k
1{2n⩽u<2n+1}u ↑u1{u>0}
104

Solution Manual. Last update 18th July 2019
we can use Beppo Levi’s theorem to conclude
˚ ud = ˚{u>0}
ud =
É
n∈Z ˚{2n⩽u<2n+1}
ud.
Because of the monotonicity of the integral,
C ∶=
É
n∈Z ˚{2n⩽u<2n+1}
2nd ⩽
É
n∈Z ˚{2n⩽u<2n+1}
ud ⩽
É
n∈Z ˚{2n⩽u<2n+1}
2n+1d,
i.e.
C ⩽
É
n∈Z ˚{2n⩽u<2n+1}
ud ⩽2C.
Therefore the following assertions are equivalent:
u∈ 1() ⇐ ⇒
É
n∈Z ˚{2n⩽u<2n+1}
ud< ∞
⇐ ⇒C =
É
n∈Z
2n{2n ⩽u< 2n+1}<∞.
■■
Problem 10.6 Solution: Let us show the following inequalities:
∞É
i=1
1{ðuð⩾i}(x) ⩽ ðu(x)ð ⩽
∞É
i=0
1{ðuð⩾i}(x) ∀x∈X.
First proof:
∞É
i=1
1{ðuð⩾i}=
∞É
i=1
∞É
k=i
1{k+1>ðuð⩾k}=
∞É
k=1
kÉ
i=1
1{k+1>ðuð⩾k}=
∞É
k=1
k1{k+1>ðuð⩾k}
and
∞É
k=1
k1{k+1>ðuð⩾k} ⩽
∞É
k=1
ðuð1{k+1>ðuð⩾k}= ðuð1{ðuð⩾1}
and
∞É
k=1
k1{k+1>ðuð⩾k} ⩾
∞É
k=1
(ðuð−1) 1{k+1>ðuð⩾k}=( ðuð−1) 1{ðuð⩾1} ⩾ ðuð1{ðuð⩾1}− 1{ðuð⩾0}.
So,
∞É
i=1
1{ðuð⩾i} ⩽ ðuð1{ðuð⩾1} ⩽ ðuð ⩽1+
∞É
i=1
1{ðuð⩾i}=
∞É
i=0
1{ðuð⩾i}.
Second proof:Forx∈X, there is somek∈ N0 such thatk ⩽ ðu(x)ð<k +1. Therefore,
x∈{ ðuð ⩾i} ∀i∈{0,…,k}
and
x∉{ ðuð ⩾i} ∀i ⩾k+1.
105

R.L. Schilling: Measures, Integrals & Martingales
Thus,
É
i∈N0
1{ðuð⩾i}(x)= k+1.
Sincek ⩽ ðu(x)ð ⩽k+1 we get
É
i∈N0
1{ðuð⩾i}(x)= k+1 ⩾ ðu(x)ð ⩾k=(k+1)−1=
H
É
i∈N0
1{ðuð⩾i}(x)
I
−1.
As1= 1{ðuð⩾0} (u ⩾0, by assumption) we get the claimed estimates.
Integrating these inequalities we get
∞É
i=1
{ðuð ⩾i} ⩽ ˚ ðuðd ⩽
∞É
i=0
{ðuð ⩾i},
and (ii) follows. Ifu ∈ 1(), then we get∑
i⩾1(ðuð ⩾ 1) < ∞. On the other hand, ifu is
measurable, and∑
i(ðuð ⩾i)<∞, then we get∫ ðuðd< ∞, i.e.u∈ 1()and (i) follows.
Theﬁnitenessofthemeasure  wasonlyusedfor ∫ 1d< ∞or{ðuð ⩾0}<∞–whichisonly
needed for the second estimate in (ii). Hence, the lower estimate in (ii) holds for all measures!
■■
Problem 10.7 Solution: One possibility to solve the problem is to follow the hint. We provide an
alternative (and shorter) solution.
(i) Observethat uj−v ⩾0isasequenceofpositiveandintegrablefunctions. ApplyingFatou’s
lemma (in the usual form) yields (observing the rules forliminf ,limsup from Appendix A,
compare also Problem 9.10):
˚ liminf
j
ujd− ˚ vd = ˚ liminf
j
(uj−v)d
⩽liminf
j ˚ (uj−v)d
=liminf
j ˚ ujd− ˚ vd
and the claim follows upon subtraction of theﬁnite (!)number ∫ vd .
(ii) Verysimilarto(i)byapplyingFatou’slemmatothepositive,integrablefunctions w−uj ⩾0:
˚ wd − ˚ limsup
j
ujd = ˚ liminf
j
(w−uj)d
⩽liminf
j ˚ (w−uj)d
= ˚ wd −limsup
j ˚ ujd
Now subtract the ﬁnite number∫ wd on both sides.
106

Solution Manual. Last update 18th July 2019
(iii) We had the counterexample, in principle, already in Problem 9.10. Nevertheless...
Consider Lebesgue measure onR. Putfj(x)=− 1[−2j,−j](x)andgj(x)= 1[j,2j](x).
Thenliminf fj(x) = 0andlimsup gj(x) = 0for everyx and neither admits an integrable
minorant resp. majorant.
Remark. HereisanevenstrongerversionofFatou’sLemma. Forthisweintroducedtheextended
integrable functions
1()∶=
<
u∈ (A)∶ ˚ u+d< ∞, ˚ u−d< ∞
=
1,e()∶=
<
u∈ (A)∶ ˚ u+d ∈[0,∞], ˚ u−d< ∞
=
.
Foru ∈ 1() oru ∈ 1,e() we may deﬁne∫ ud = ∫ u+d − ∫ u−d in R or R∪{+∞} ,
respectively. Notethat 1,e()isnotavectorspace,butitisstilladditiveandpositivelyhomogen-
eous. Then we have
Let(un)n∈N⊂ (A)such thatun ⩾ufor someu∈ 1,e().
i) liminf n→∞un∈ 1,e();
ii) liminf n→∞ ∫ und ⩾ ∫ liminf n→∞und;
iii) ifliminf n→∞ ∫ und< ∞, thenliminf n→∞un∈ 1().
Proof. i) We have
un ⩾u - ⇒liminf
n
un ⩾u - ⇒
⎧
⎪
⎨
⎪⎩
 liminf nun
+
⩾u+
 liminf nun
−
⩽u−
and so∫  liminf nun
−
d ⩽ ∫ u−d< ∞, i.e.liminf nun∈ 1,e().
ii) Note thatun−u ⩾0. By (the ordinary) Fatou’s lemma,
liminf
n ˚ (un−u)d ⩾ ˚ liminf
n
(un−u)d.
Adding on both sides∫ ud – this is possible since we do not get an expression of type
“∞−∞ ”, we get
liminf
n ˚ und ⩾ ˚ liminf
n
und.
iii) We have
˚

liminf
n
un
+
d = ˚ liminf
n
un+

liminf
n
un
−
d
⩽ ˚ liminf
n
un+u−d
= ˚ liminf
n
und+ ˚ u−d
⩽liminf
n ˚ und+ ˚ u−d< ∞.
107

R.L. Schilling: Measures, Integrals & Martingales
Thisprovestheclaim. (Notethatintheinequality-stepinthelastformulawecouldhaveused
directly the ordinary Fatou lemma, and not step ii), asun+u− ⩾0).
■■
Problem 10.8 Solution: Foru= 1B andv= 1C we have, because of independence,
˚ uvdP =P(A∩B)= P(A)P(B)= ˚ udP ˚ vdP.
For positive, simple functionsu= ∑
jj1Bj andv= ∑
kk1Ck we ﬁnd
˚ uvdP =
É
j,k
jk ˚ 1Aj 1BkdP
=
É
j,k
jkP(Aj∩Bk)
=
É
j,k
jkP(Aj)P(Bk)
=
0É
j
jP(Aj)
10É
k
kP(Bk)
1
= ˚ udP ˚ vdP.
For measurableu ∈ +(ℬ) and v ∈ +(C) we use approximating simple functionsuk ∈
+(ℬ),uk ↑u, andvk∈ +(C),vk ↑v. Then, by Beppo Levi,
˚ uvdP =lim
k ˚ ukvkdP =lim
k ˚ ukdP lim
j ˚ vjdP
= ˚ udP ˚ vdP.
Integrable independent functions:Ifu ∈ 1(ℬ) andv ∈ 1(C), the above calculation when
applied toðuð,ðvðshows thatu⋅vis integrable since
˚ ðuvðdP ⩽ ˚ ðuðdP ˚ ðvðdP <∞.
Considering positive and negative parts ﬁnally also gives
˚ uvdP = ˚ udP ˚ vdP.
Counterexample: Just takeu = v which are integrable but not square integrable, e.g.u(x) =
v(x)= x−1∕2. Then∫(0,1)x−1∕2dx< ∞but ∫(0,1)x−1dx=∞ , compare also Problem 10.2.
■■
Problem 10.8 Solution:
(i) Since the mapg∶ C → R2 is continuous, we haveg−1(ℬ(R2))⊂ℬ(C).
On the other hand, forz∈ Cand >0we haveB(z)= g−1(Bg(z)())∈ g−1(ℬ(R2));
thus, (OC) ⊂ g−1(ℬ(R2)) (Note that the-algebra(OC) is generated by the open
ballsB(z),z∈ C, >0, cf. the proof of Problem 3.12.)
108

Solution Manual. Last update 18th July 2019
(ii) Part(i)showsthatamap ℎ∶E → CisA∕C-measurableif,andonlyif, g◦ℎ∶E → R2
isA∕ℬ(R2)-measurable.
Indeed: Themap ℎ∶(E,A) →(C,C)is,bydeﬁnition,measureableif ℎ−1(A)∈ A for
allA∈C. SinceC =g−1(ℬ(R2)),thisisthesameas ℎ−1(g−1(B))=( g◦ℎ)−1(B)∈ A
for allB∈ℬ(R2), hence it is the same as the measurability ofg◦ℎ.
"⇒": Assume thatℎ∶E → C isA∕C-measurable. Then we have that
(g◦ℎ)=
H
Reℎ
Imℎ
I
isA∕ℬ(R2)-measurable. Since the projectionsj ∶ R2 ∋ (x1,x2) → xj ∈ R are
Borelmeasurable(duetocontinuity!),wegetthat Reℎ=1(g◦ℎ)andImℎ=2(g◦ℎ)
are measurable (composition of measurable functions).
"⇐": Assume thatReℎ andImℎ areA∕ℬ(R)-measurable. Then the map(g◦ℎ) =
(Reℎ,Imℎ) is A∕ℬ(R2)-measurable. With the above arguments we conclude that
ℎ∶(E,A) →(C,C)is measurable.
(iii) We show ﬁrst additivity: letg,ℎ ∈ 1
C(). From
ðRe(g+ℎ)ð ⩽ ðRegð+ðReℎð∈ 1(), ðIm(g+ℎ)ð ⩽ ðIm(g)ð+ðIm(ℎ)ð∈ 1()
we conclude thatg+ℎ∈ 1(). SinceRe(g+ℎ) = Re(g)+Re( ℎ) andIm(g+ℎ) =
Im(g)+Im( ℎ), we get from the deﬁnition of the integral
˚ (g+ℎ)d = ˚ Re(g+ℎ)d+i ˚ Im(g+ℎ)d
= ˚ (Re(g)+Re( ℎ))d+i(Im(g)+Im( ℎ))d
= ˚ Re(g)d+ ˚ Re(ℎ)d+i ˚ Im(g)d+i ˚ Im(ℎ)d
=
0
˚ Re(g)d+i ˚ Im(g)d
1
+
0
˚ Re(ℎ)d+i ˚ Im(ℎ)d
1
= ˚ gd + ˚ ℎd.
Note that we have used theR-linearity of the integral for real-valued functions. The
homogeneity of the complex integral is shown in a very similar way.
(iv) SinceReℎ andImℎare real, we get∫ Reℎd ∈ R and ∫ Imℎd ∈ R. Therefore,
Re
0
˚ ℎd
1
=Re
0
˚ Reℎd +i ˚ Imℎd
1
= ˚ Reℎd.
Similarly, we see
Im
0
˚ ℎd
1
=Im
0
˚ Reℎd +i ˚ Imℎd
1
= ˚ Imℎd.
109

R.L. Schilling: Measures, Integrals & Martingales
(v) Wefollowthehint: as ∫ ℎd ∈ Cwecanpicksome ∈(−,]suchthat ei ∫ ℎd ⩾
0. Thus, (iii) and (iv) entail
óóóó˚ ℎdóóóó
=ei
˚ ℎd
=Re
0
ei
˚ ℎd
1
= ˚ Re(eiℎ)d
⩽ ˚ ðeiℎðd
= ˚ ðℎðd.
(vi) We know from (ii) thatℎ ∶ (E,A) → (C,C) is measurable if, and only if,Reℎ and
ImℎareA∕ℬ(R2)-measurable. IfReℎ andImℎ are-integrable, then so is
ðℎð=
√
(Reℎ)2+(Im ℎ)2 ⩽ ðReℎð+ðImℎð.
If ðℎð∈ 1
R(), then we conclude fromðReℎð ⩽ ðℎð and ðImℎð ⩽ ðℎð, thatReℎ and
Imℎare-integrable.
■■
110

11 Null sets and the `almost everywhere'.
Solutions to Problems 11.111.12
Problem 11.1 Solution: True,wecanchangeanintegrablefunctiononanullset,evenbysettingitto
thevalue +∞or−∞onthenullset . ThisisjusttheassertionofTheorem11.2anditsCorollaries
11.3, 11.4.
■■
Problem 11.2 Solution: We have seen that a single point is a Lebesgue null set:{x} ∈ℬ(R) for
all x ∈ R and ({x}) = 0, see e.g. Problems 4.13 and 6.7. IfN is countable, we know that
N ={xj ∶j∈ N}= ⨃
j∈N{xj} and by the-additivity of measures
(N)= 
H
Ó
j∈N
{xj}
I
=
É
j∈N
 {xj}=
É
j∈N
0=0 .
The Cantor setC from Problem 7.12 is, as we have seen, uncountable but has measure(C)=0 .
This means that there are uncountable sets with measure zero.
In R2 and for two-dimensional Lebesgue measure2 the situation is even easier: every lineL in
the plane has zero Lebesgue measure andL contains certainly uncountably many points. That
2(L) = 0is seen from the fact thatL diﬀers from the ordinate{(x,y) ∈ R2 ∶ x = 0}only
by a rigid motionT which leaves Lebesgue measure invariant (see Chapter 4, Theorem 4.7) and
2({x=0})=0 as seen in Problem 6.7.
■■
Problem 11.3 Solution:
(i) Since{ðuð > c} ⊂ {ðuð ⩾ c} and, therefore,({ðuð > c}) ⩽ ({ðuð ⩾ c}), this follows
immediately from Proposition 11.5. Alternatively, one could also mimic the proof of this
Proposition or use part (iii) of the present problem with(t)= t,t ⩾0.
(ii) This will follow from (iii) with(t) =tp, t ⩾ 0, since({ðuð > c}) ⩽ ({ðuð ⩾ c}) as
{ðuð>c}⊂{ðuð ⩾c}.
(iii) We have, sinceis increasing,
({ðuð ⩾c})= ({(ðuð) ⩾(c)})
= ˚ 1{x∶(ðu(x)ð)⩾(c)}(x)(dx)
111

R.L. Schilling: Measures, Integrals & Martingales
= ˚
(ðu(x)ð)
(ðu(x)ð) 1{x∶(ðu(x)ð)⩾(c)}(x)(dx)
⩽ ˚
(ðu(x)ð)
(c) 1{x∶(ðu(x)ð)⩾(c)}(x)(dx)
⩽ ˚
(ðu(x)ð)
(c) (dx)
= 1
(c) ˚ (ðu(x)ð)(dx)
(iv) Let us setb= ∫ ud . Then we follow the argument of (iii), where we use thatuandbare
strictly positive.
({u ⩾b})= ˚ 1{x∶u(x)⩾b}(x)(dx)
= ˚
u(x)
u(x) 1{x∶u(x)⩾b}(x)(dx)
⩽ ˚
u(x)
b 1{x∶u(x)⩾b}(x)(dx)
⩽ ˚
u
bd
= 1
b ˚ ud
and substituting ∫ ud forb shows the inequality.
(v) Using the fact that is decreasing we get{ðuð< c}={  (ðuð)>  (c)}—mind the change
of the inequality sign—and going through the proof of part (iii) again we use there that
increasesonlyintheﬁrststepinasimilarroleasweusedthedecreaseof  here! Thismeans
that the argument of (iii) is valid after this step and we get, altogether,
({ðuð<c})= ({ (ðuð)> (c)})
= ˚ 1{x∶ (ðu(x)ð)> (c)}(x)(dx)
= ˚
 (ðu(x)ð)
 (ðu(x)ð) 1{x∶ (ðu(x)ð)>(c)}(x)(dx)
⩽ ˚
 (ðu(x)ð)
 (c) 1{x∶ (ðu(x)ð)> (c)}(x)(dx)
⩽ ˚
 (ðu(x)ð)
 (c) (dx)
= 1
 (c) ˚  (ðu(x)ð)(dx)
(vi) This follows immediately from (ii) by taking = P,c = 
√
V,u = − E andp = 2.
Then
P(ð− Eð ⩾E) ⩽ 1
(
√
V)2 ˚ ð− Eð2dP
= 1
2V V = 1
2.
112

Solution Manual. Last update 18th July 2019
■■
Problem 11.4 Solution: We mimic the proof of Corollary 11.6. SetN ={ ðuð=∞}={ ðuðp=∞} .
ThenN = ⋂
k∈N{ðuðp ⩾k}andusingMarkov’sinequality(MI)andthe‘continuity’ofmeasures,
Proposition 4.3(vii), we ﬁnd
(N)= 
H
Ì
k∈N
{ðuðp ⩾k}
I
4.3(vii)
= lim
k→∞
({ðuðp ⩾k})
MI
⩽ lim
k→∞
1
k ˚ ðuðpd
«››ﬂ››‹
<∞
= 0.
Forarctan this is not any longer true for several reasons:
• ...arctan is odd and changes sign, so there could be cancelations under the integral.
• ... even if we had no cancelations we have the problem that the points whereu(x) = ∞are
now transformed to points wherearctan(u(x)) = 
2 and we do not know how the measure
 acts under this transformation. A simple example: Take to be a measure of total ﬁnite
mass (that is:(X) < ∞), e.g. a probability measure, and take the functionu(x) which is
constantlyu ≡+∞. Thenarctan(u(x))= 
2 throughout, and we get
˚ arctanu(x)(dx)= ˚

2d = 
2 ˚ d = 
2(X)<∞,
butuis nowhereﬁnite!
■■
Problem 11.5 Solution:
(i) Assume thatf∗ is A-measurable. The problem at hand is to constructA-measurable up-
per and lower functionsg and f. For positive simple functions this is clear: iff∗(x) =
∑N
j=0j1B∗
j
(x) withj ⩾0 andB∗
j ∈A, then we can use Problem 4.15(v) to ﬁndBj,Cj ∈
A with(Cj ⧵Bj)=0
Bj ⊂B ∗
j ⊂C j - ⇒j1Bj ⩽j1B∗
j
⩽j1Cj
and summing overj = 0,1,…,N shows thatf ⩽ f∗ ⩽ g wheref,g are the appropriate
lower and upper sums which are clearlyA measurable and satisfy
({f ≠g}) ⩽(C0 ⧵B0∪⋯∪CN ⧵BN)
⩽(C0 ⧵B0)+ ⋯+(CN ⧵BN)
=0+ ⋯+0 = 0.
Moreover, since by Problem 4.15(Bj)= (Cj)= ̄ (B∗
j), we have
É
j
j(Bj)=
É
j
j̄ (B∗
j)=
É
j
j(Cj)
113

R.L. Schilling: Measures, Integrals & Martingales
which is the same as
˚ fd = ˚ f∗d̄ = ˚ gd.
(ii), (iii) Assume thatu∗ isA∗-measurable; without loss of generality (otherwise consider pos-
itive and negative parts) we can assume thatu∗ ⩾0. Because of Theorem 8.8 we know that
f∗
k ↑ u∗ forf∗
k ∈ +(A∗). Now choose the correspondingA-measurable lower and upper
functionsfk,gk constructed in part (i). By considering, if necessary,max{f1,…,fk} we
can assume that thefk are increasing.
Setu ∶= supkfk andv ∶= liminfkgk. Thenu,v ∈ (A),u ⩽ u∗ ⩽ v, and by Fatou’s
lemma
˚ vd = ˚ liminf
k
gkd ⩽liminf
k ˚ gkd
=liminf
k ˚ f∗
kd̄ 
= ˚ u∗d̄ 
⩽ ˚ vd.
Sincefk ↑uwe get by Beppo Levi and Fatou
˚ ud =sup
k ˚ fkd =liminf
k ˚ fkd
=liminf
k ˚ gkd
⩾ ˚ liminf
k
gkd
= ˚ vd
⩾ ˚ ud
This provesthat ∫ ud = ∫ vd = ∫ u∗d. Thisanswers part (iii)by consideringpositive
and negative parts.
Itremainstoshowthat {u ≠v}isa -nullset. (Thisdoesnotfollowfromtheaboveintegral
equality, cf. Problem 11.10!) Clearly,{u ≠ v} = {u < v}, i.e. ifx ∈ {u < v} is ﬁxed, we
deduce that, for suﬃciently large values ofk,
fk(x)<g k(x), k large
sinceu=sup fk andv=liminf kgk. Thus,
{u ≠v}⊂
˝
k
{fk ≠gk}
but the RHS is a countable union of-null sets, hence a null set itself.
114

Solution Manual. Last update 18th July 2019
Conversely,assume ﬁrst thatu ⩽ u∗ ⩽ v for twoA-measurable functionsu,v withu = v
a.e. We have to show that{u∗>}∈ A∗. Using thatu ⩽u∗ ⩽v we ﬁnd that
{u> }⊂{u∗>}⊂{v> }
but{v > },{u > } ∈A and{u > } ⧵{v > } ⊂ {u ≠ v} is a-null set. Because of
Problem 4.15 we conclude that{u∗>}∈ A∗.
■■
Problem 11.6 Solution: Throughout the solution the lettersA,B are reserved for sets fromA.
(i) a) Let A ⊂ E ⊂ B. Then (A) ⩽ (B) and going to thesupA⊂E and infE⊂B proves
∗(E) ⩽∗(E).
b) By the deﬁnition of∗ and∗ we ﬁnd someA⊂E such that
ð∗(E)− (A)ð ⩽.
SinceAc ⊃E c we can enlargeA, if needed, and achieve
ð∗(Ec)− (Ac)ð ⩽.
Thus,
ð(X)− ∗(E)− ∗(Ec)ð
⩽ ð∗(E)− (A)ð+ð∗(Ec)− (Ac)ð
⩽2,
and the claim follows as →0.
c) LetA⊃E andB ⊃F be arbitrary majorizingA-sets. ThenA∪B ⊃E∪F and
∗(E∪F) ⩽(A∪B) ⩽(A)+ (B).
Now we pass on the right-hand side, separately, to theinfA⊃E andinfB⊃F, and obtain
∗(E∪F) ⩽∗(E)+ ∗(F).
d) LetA⊂E andB ⊂F be arbitrary minorizingA-sets. ThenA⊍B ⊂E⊍F and
∗(E⊍F ) ⩾(A⊍B )= (A)+ (B).
Now we pass on the right-hand side, separately, to thesupA⊂E andsupB⊂F, where we
stipulate thatA∩B=ç , and obtain
∗(E⊍F ) ⩾∗(E)+ ∗(F).
115

R.L. Schilling: Measures, Integrals & Martingales
(ii) By the deﬁnition of the inﬁmum/supremum we ﬁnd setsAn⊂E ⊂An such that
ð∗(A)− (An)ð+ð∗(A)− (An)ð ⩽ 1
n.
Withoutlossofgeneralitywecanassumethatthe An increaseandthatthe An decrease. Now
A∗ ∶= ⋃
nAn,A∗ ∶= ⋂
nAn areA-sets withA∗ ⊂ A ⊂ A∗. Now,(An) ↓ (A∗) as well
as(An) → ∗(E) which proves(A∗) =∗(E). Analogously,(An) ↑ (A∗) as well as
(An) →∗(E)which proves(A∗)= ∗(E).
(iii) In view of Problem 4.15 and (i), (ii), it is clear that
E ⊂X∶∗(E)= ∗(E)=
E ⊂X∶∃ A,B ∈A, A⊂E ⊂B, (B ⧵A)=0 
but the latter is the completed-algebraA∗. That∗óóóA∗ = ∗
óóóA∗ = ̄ is now trivial since
∗ and∗ coincide onA∗.
■■
Problem 11.7 Solution: LetA∈A and assume that there are non-measurable sets, i.e.P(X) bA.
Take someN ∉ A which is a-null set. Assume also thatN ∩A = ç. Then u = 1A and
w∶= 1A+2 ⋅ 1N are a.e. identical, butw is not measurable.
This means thatw is only measurable if, e.g. all (subsets of) null sets are measurable, that is if
(X,A,)is complete.
■■
Problem 11.8 Solution: The function1Q is nowhere continuous butu=0 Lebesgue almost every-
where. That is
{x∶ 1Q(x) is discontinuous}= R
while
{x∶ 1Q ≠0}= Q is a Lebesgue null set,
that is1Q coincides a.e. with a continuous function but is itself at no point continuous!
The same analysis for1[0,∞) yields that
{x∶ 1[0,∞)(x) is discontinuous}={0}
which is a Lebesgue null set, but1[0,∞) cannot coincide a.e. with a continuous function! This,
namely, would be of the formw = 0on(−∞,−) andw = 1on(,∞) while it ‘interpolates’
somehow between0 and1 if− <x< . But this entails that
{x∶w(x) ≠ 1[0,∞)(x)}
cannot be a Lebesgue null set!
■■
116

Solution Manual. Last update 18th July 2019
Problem 11.9 Solution: Let(Aj)j∈N⊂A be an exhausting sequenceAj ↑X such that(Aj)<∞.
Set
f(x)∶=
∞É
j=1
1
2j((Aj)+1) 1Aj(x).
Thenf is measurable,f(x)>0everywhere, and using Beppo Levi’s theorem
˚ fd = ˚
0 ∞É
j=1
1
2j((Aj)+1) 1Aj
1
d
=
∞É
j=1
1
2j((Aj)+1) ˚ 1Ajd
=
∞É
j=1
(Aj)
2j((Aj)+1)
⩽
∞É
j=1
2−j = 1.
Thus, setP(A)∶= ∫Afd . We know from Problem 9.7 thatP is indeed a measure.
IfN ∈N, then, by Theorem 11.2,
P(N)= ˚N
fd
11.2
= 0
so thatN ⊂NP.
Conversely, ifM ∈ P, we see that
˚M
fd =0
but sincef >0everywhere, it follows from Theorem 11.2 that1M⋅f =0 -a.e., i.e.(M)=0 .
Thus,NP ⊂N.
Remark. Wewillseelater(cf.Chapter20orChapter25,Radon–Nikodýmtheorem)that N=NP
if and only ifP =f⋅ (i.e., ifP has a density w.r.t.) such thatf >0.
■■
Problem 11.10 Solution: Well, the hint given in the text should be good enough.
■■
Problem 11.11 Solution: Observe that
˚C
ud = ˚C
wd ⇐ ⇒ ˚C
(u++w−)d = ˚C
(u−+w+)d
holds for allC ∈ C. The right-hand side can be read as the equality of two measuresA →
∫A(u++w−)d,A → ∫A(u−+w+)d,A∈A which coincide on a generatorC which satisﬁes
the conditions of the uniqueness theorem of measures (Theorem 5.7). This shows that
˚A
ud = ˚A
wd ∀A∈A.
117

R.L. Schilling: Measures, Integrals & Martingales
Now the direction ‘⇒’ follows from Corollary 11.7 whereℬ=A.
The converse implication ‘⇐’ follows directly from Corollary 11.6 applied tou1C andw1C.
■■
Problem 11.12 Solution:
(i) “⊂”: Letx∈Cf, i.e.f(x)=lim n→∞fn(x)exists; in particular,(fn(x))n∈N is Cauchy:
for allk∈ N there is somel∈ N such that
ðfn(x)− fm(x)ð ⩽ 1
k ∀m,n ⩾l.
This shows thatx∈ ⋂
k∈N
⋃
l∈N
⋂∞
n,m=l{ðfn(x)− fm(x)ð ⩽ 1
k}.
“⊃”: Assume that⋂
k∈N
⋃
l∈N
⋂∞
n,m=l{ðfn(x)− fm(x)ð ⩽ 1
k}. This means that for
everyk∈ N there is somel∈ N with
ðfn(x)− fm(x)ð ⩽ 1
k ∀m,n ⩾l.
This shows that(fn(x))n∈N is a Cauchy sequence inR. The claim follows sinceR is
complete.
(ii) From the deﬁnition of limits we get (as in part (i))
Cf =
Ì
k∈N
˝
l∈N
∞Ì
m=l
{ðfm(x)− f(x)ð ⩽ 1
k};
Observe that
Ak
n ↑
∞˝
l=1
∞Ì
m=l
{ðfm(x)− f(x)ð ⩽ 1
k}⊃C f
asn →∞. Using the continuity of measures, we get
(Ak
n) ↑
H ∞˝
l=1
∞Ì
m=l
$
ðfm(x)− f(x)ð ⩽ 1
k
%I
=(X).
(Note: ifA ⊂ Bis measurable and(A) =(X), then we have(B) =(X).) In
particular we can pickn=n(k,)in such a way that(Ak
n) ⩾(X)− 2−k. Therefore,
(X ⧵Ak
n(k,))= (X)− (Ak
n(k,)) ⩽2−k.
(iii) Fix >0, pickn=n(k,)as in part (ii), and deﬁne
A ∶=
Ì
k∈N
Ak
n(k,)∈A.
Using the sub-additivity of we get
(X ⧵A)= 
H
˝
k∈N

X ⧵Ak
n(k,)
I
⩽
É
k∈N
(X ⧵Ak
n(k,)) ⩽
É
k∈N
2−k ⩽.
118

Solution Manual. Last update 18th July 2019
It remains to show thatfn converges uniformly tof on the setA. By deﬁnition,
A =
Ì
k∈N
n(k,)˝
l=1
∞Ì
m=l
{ðf−fmð ⩽ 1
k},
i.e. for allx∈A andk∈ N there is somel(x) ⩽n(k,)such that
ðf(x)− fm(x)ð ⩽ 1
k ∀m ⩾l(x).
Sincel(x) ⩽n(k,)we get, in particular,
ðf(x)− fm(x)ð ⩽ 1
k ∀x∈A, m⩾n(k,).
Sincek∈ N is arbitrary, the uniform convergenceA follows.
(iv) Considerone-dimensionalLebesguemeasure,set f(x)∶= ðxðandfn(x)∶= ðxð1[−n,n].
Then we havefn(x) ↑ f(x) for everyx, but the set{ðfn−fð > } = [−n,n]c has
inﬁnite measure for any >0.
■■
119



12 Convergence theorems and their
applications.
Solutions to Problems 12.112.37
Problem 12.1 Solution: We start with the simple remark that
ða−bðp ⩽(ðað+ðbð)p
⩽(max{ðað,ðbð}+max{ ðað,ðbð})p
=2 pmax{ðað,ðbð}p
=2 pmax{ðaðp,ðbðp}
⩽2p(ðaðp+ðbðp).
Because of this we ﬁnd thatðuj−uðp ⩽2pgp and the right-hand side is an integrable dominating
function.
Proof alternative 1:Apply Theorem 12.2 on dominated convergence to the sequencej ∶= ðuj−
uðpofintegrablefunctions. Notethat j(x) →0andthat 0 ⩽j ⩽ΦwhereΦ=2 pgpisintegrable
and independent ofj. Thus,
lim
j→∞ ˚ ðuj−uðpd = lim
j→∞ ˚ jd = ˚ lim
j→∞
jd
= ˚ 0d = 0.
Proof alternative 2:Mimic the proof of Theorem 12.2 on dominated convergence. To do so we
remark that the sequence of functions
0 ⩽ j ∶=2 pgp−ðuj−uðp , , , , , , , , , , , , , , , , , , , , →
j→∞
2pgp
Since the limitlimj j exists, it coincides withliminf j j, and so we can use Fatou’s Lemma to
get
˚ 2pgpd = ˚ liminf
j→∞
 jd
⩽liminf
j→∞ ˚  jd
=liminf
j→∞ ˚
 2pgp−ðuj−uðpd
121

R.L. Schilling: Measures, Integrals & Martingales
= ˚ 2pgpd+liminf
j→∞
0
− ˚ ðuj−uðpd
1
= ˚ 2pgpd−limsup
j→∞ ˚ ðuj−uðpd
where we use thatliminf j(−j) = −limsupjj. This shows thatlimsupj ∫ ðuj −uðpd = 0,
hence
0 ⩽liminf
j→∞ ˚ ðuj−uðpd ⩽limsup
j→∞ ˚ ðuj−uðpd ⩽0
showing that lower and upper limit coincide and equal to0, hencelimj ∫ ðuj−uðpd =0 .
■■
Problem 12.2 Solution: Assume that, as in the statement of Theorem 12.2,uj → u and thatðujð ⩽
f ∈ 1(). In particular,
−f ⩽uj and uj ⩽f
(j∈ N) is an integrable minorant resp. majorant. Thus, using Problem 10.7 at∗ below,
˚ ud = ˚ liminf
j→∞
ujd
∗
⩽liminf
j→∞ ˚ ujd
⩽limsup
j→∞ ˚ ujd
∗
⩽ ˚ limsup
j→∞
ujd = ˚ ud.
This proves∫ ud =lim j ∫ ujd.
Addition: since0 ⩽ ðu−ujð ⩽ ðlimjujð+ ðujð ⩽ 2f ∈ 1(), the sequenceðu−ujð has an
integrable majorant and using Problem 10.7 we get
0 ⩽limsup
j→∞ ˚ ðuj−uðd ⩽ ˚ limsup
j→∞
ðuj−uðd = ˚ 0d =0
and also (i) of Theorem 12.2 follows...
■■
Problem 12.3 Solution: By assumption we have
0 ⩽fk−gk , , , , , , , , , , , , , , , , , , , , →
k→∞
f−g,
0 ⩽Gk−fk , , , , , , , , , , , , , , , , , , , , →
k→∞
G−f.
Using Fatou’s Lemma we ﬁnd
˚ (f−g)d = ˚ lim
k
(fk−gk)d
122

Solution Manual. Last update 18th July 2019
= ˚ liminf
k
(fk−gk)d
⩽liminf
k ˚ (fk−gk)d
=liminf
k ˚ fkd− ˚ gd,
and
˚ (G−f)d = ˚ lim
k
(Gk−fk)d
= ˚ liminf
k
(Gk−fk)d
⩽liminf
k ˚ (Gk−fk)d
= ˚ Gd −limsup
k ˚ fkd.
Adding resp. subtracting∫ gd resp. ∫ Gd therefore yields
limsup
k ˚ fkd ⩽ ˚ fd ⩽liminf
k ˚ fkd
and the claim follows.
■■
Problem 12.4 Solution: Using Beppo Levi’s theorem in the form of Corollary 9.9 we ﬁnd
˚
∞É
j=1
ðujðd =
∞É
j=1 ˚ ðujðd< ∞, (*)
whichmeansthatthepositivefunction ∑∞
j=1ðujðisﬁnitealmosteverywhere,i.e.theseries ∑∞
j=1uj
converges (absolutely) almost everywhere.
In order to show the second part, we want to apply dominated convergence. Setvk ∶= ∑k
n=1un
and notte that
ðvkð=
óóóóóó
kÉ
n=1
un
óóóóóó
⩽
kÉ
n=1
ðunð ⩽
∞É
n=1
ðunð ⩽w∈ℒ1().
Clearly,vk →u= ∑∞
n=1un ask →∞. Thus, we get with dominated convergence
˚
∞É
n=1
und = ˚ ud = ˚ lim
k→∞
vkd = lim
k→∞ ˚ vkd = lim
k→∞
kÉ
n=1 ˚ und
=
∞É
n=1 ˚ und.
■■
Problem 12.5 Solution: Since 1() ∋uj ↓ 0 we ﬁnd by monotone convergence, Theorem 12.1,
that ∫ ujd ↓0. Therefore,
=
∞É
j=1
(−1)juj and S =
∞É
j=1
(−1)j
˚ ujd converge
123

R.L. Schilling: Measures, Integrals & Martingales
(conditionally, in general). Moreover, for everyN ∈ N,
˚
NÉ
j=1
(−1)jujd =
NÉ
j=1 ˚ (−1)jujd , , , , , , , , , , , , , , , , , , , , , , , , →
N→∞
S.
All that remains is to show that the right-hand side converges to∫ d . Observe that forSN ∶=
∑N
j=1(−1)juj we have
S2N ⩽S2N+2 ⩽… ⩽S
and we ﬁnd, asSj ∈ 1(), by monotone convergence that
lim
N→∞ ˚ S2Nd = ˚ d.
■■
Problem 12.6 Solution: Consideruj(x)∶= j⋅ 1(0,1∕j)(x),j∈ N. Itisclearthat uj ismeasurableand
Lebesgue integrable with integral
˚ ujd=j1
j =1 ∀ j∈ N.
Thus,limj ∫ ujd=1 . On the other hand, the pointwise limit is
u(x)∶=lim
j
uj(x) ≡0
so that0= ∫ ud = ∫ limjujd ≠1.
Theexampledoesnotcontradictdominatedconvergenceasthereisnouniformdominatinginteg-
rable function.
Alternative: asimilarsituationcanbefoundfor vk(x)∶= 1
k 1[0,k](x)andthepointwiselimit v ≡0.
Note that in this case the limit is even uniform and stilllimk ∫ vkd = 1≠ 0 =∫ vd. Again
there is no contradiction to dominated convergence as there does not exist a uniform dominating
integrable function.
■■
Problem 12.7 Solution: Using the majorant (e−rx ⩽ 1 ∈1(),r,x ⩾ 0) we ﬁnd with dominated
convergence
lim
r→∞ ˚[0,∞)
e−rx(dx)= ˚[0,∞)
lim
r→∞
e−rx(dx)= ˚[0,∞)
1{0}(dx)= {0}.
■■
Problem 12.8 Solution:
124

Solution Manual. Last update 18th July 2019
(i) Let >0. Asu∈ 1(), monotone convergence shows that
lim
R→∞ ˚BR(0)c
ðuðd=0.
In particular, we can pick anR> 0such that
˚BR(0)c
ðuðd ⩽.
SinceK is compact (in fact: bounded), there is somer = r(R) > 0, such thatx+K ⊂
BR(0)c for allx satisfyingðxð ⩾r. Thus, we have
˚x+K
ðuðd ⩽ ˚BR(0)c
ðuðd ⩽ ∀x∈ Rn, ðxð ⩾r.
(ii) Fix >0. Byassumption,uisuniformlycontinuous. Therefore,thereissome  >0such
that
ðu(y)− u(x)ð ⩽ ∀x∈ Rn, y∈x+K ∶=x+B(0)= B(x).
Hence,
ðu(x)ðp= 1
(K+x) ˚K+x
ðu(x)ðpd(y)
⩽ 1
(K) ˚K+x
 ðu(y)− u(x)ð
«››››ﬂ››››‹
⩽
+ðu(y)ðp
d(y).
Using the elementary inequality
(a+b)p ⩽(2max{a,b})p ⩽2p(ap+bp), a,b ⩾0 (⋆)
we get forC =2 p
ðu(x)ðp ⩽ C
(K)
0
˚K+x
pd(y)+ ˚K+x
ðu(y)ðd(y)
1
⩽Cp(K+x)
(K)
«››ﬂ››‹
1
+ C
(K) ˚K+x
ðu(y)ðd(y).
Part (i) now implies
limsup
ðxð→∞
ðu(x)ðp ⩽Cp →0
, , , , , , , , , , , , , , , , , →0
and this is the same as to saylimðxð→∞ðu(x)ð=0 .
■■
Problem 12.9 Solution:
125

R.L. Schilling: Measures, Integrals & Martingales
(i) Fix >0,R >0 and considerB ∶= {ðuð ⩽ R}. By deﬁnition,supx∈Bðu(x)ð <∞. On
the other hand, dominated convergence and Corollary 11.6 show that
lim
R→∞ ˚ðuð>R
ðu(x)ðdx= ˚ðuð=∞
ðu(x)ðdx=0.
In particular, we can chooseRso large, that∫Bðu(x)ðdx< . Using Markov’s inequality
(Proposition 11.5) yields
(B)= {ðuð ⩾R} ⩽ 1
R ˚ ðu(x)ðdx< ∞.
(ii) Fix >0 and letB ∈ℬ(Rn) be as in (i). Further, letA∈ℬ(Rn) with(A)< . Then
we have
˚A
ðuðd= ˚A∩B
ðuðd+ ˚A∩Bc
ðuðd
⩽sup
x∈B
ðu(x)ð⋅(A∩B)
«›ﬂ›‹
⩽(A)
+ ˚Bc
ðuðd
⩽sup
x∈B
ðu(x)ð⋅+.
(Observe thatsupx∈Bðu(x)ð<∞.) This proves
lim
(A)→0 ˚A
ðuðd=0.
■■
Problem 12.10 Solution:
(i) Fromun∈ 1()and‖un−u‖∞ ⩽1 (for all suﬃciently largen) we infer
˚ ðuðd ⩽ ˚ ðun−uðd+ ˚ ðunðd ⩽ ‖un−u‖∞(X)+ ˚ ðunðd< ∞,
i.e.u∈ 1(). A very similar argument gives
óóóó˚ und− ˚ udóóóó
= óóóó˚ (un−u)dóóóó
⩽ ˚ ðun−uðd ⩽ ‖un−u‖∞(X).
Since(X)<∞, uniform convergence‖un−u‖∞ →0 implies that
lim
n→∞
óóóó˚ und− ˚ ud
óóóó
=0.
(ii) False. Counterexample:(R,ℬ(R),1)andun(x)∶= 1
2n 1[−n,n](x),x∈ R. Clearly,un →0
uniformly,un∈ 1(1), but
lim
n→∞ ˚ und =1 ≠0= ˚ ud.
■■
126

Solution Manual. Last update 18th July 2019
Problem 12.11 Solution: Without loss of generality we assume thatu is increasing. Because of the
monotonicity ofu, we ﬁnd for every sequence(an)n∈N⊂(0,1) such thatan ↓0, that
u(an) →u(0+)∶=inf
t>0
u(t).
Ifan∶=tn,t∈(0,1), we getu(tn) ↓0 and by monotone convergence
lim
n→∞ ˚
1
0
u(tn)dt= inf
n∈N ˚
1
0
u(tn)dt= ˚
1
0
inf
n∈N
u(tn)dt= ˚
1
0
u(0+)dt=u(0+).
■■
Problem 12.12 Solution: Setun(t)∶= tnu(t),t∈(0,1). Sinceðtnð ⩽1 fort∈(0,1), we have
ðun(t)ð= ðtnð⋅ðf(t)ð ⩽ ðf(t)ð∈ 1(0,1).
Sincetn , , , , , , , , , , , , , , , , , , , , →
n→∞
0 for allt∈ (0,1) and ðf(t)ð <∞ a.e. (Corollary 11.6), we haveðun(t)ð →0 a.e.
An application of dominated convergence (Theorem 12.2 and Remark 12.3) yields
lim
n→∞ ˚
1
0
tnu(t)dt= lim
n→∞ ˚
1
0
un(t)dt= ˚
1
0
lim
n→∞
un(t)
«›ﬂ›‹
0
dt=0.
■■
Problem 12.13 Solution: From the geometric series we know that1
1−x = ∑
n⩾0xn forx ∈ [0,1).
This implies that for allt> 0
1
et−1 = 1
et
1
1− e−t =e−tÉ
n⩾0
(e−t)n=
É
n⩾1
e−nt
(observe thate−t<1fort> 0!). Setuk(t)∶=sin( t)⋅∑k
n=1e−nt, then we get the estimate
ðuk(t)ð ⩽ ðsintð⋅
óóóóóó
kÉ
n=1
e−nt
óóóóóó
= ðsintð
kÉ
n=1
e−nt ⩽ ðsintð
É
n⩾1
e−nt= ðsintð
et−1 (∗)
for allk ∈ N undt >0. Using the elementary inequalitieset−1 ⩾ t (t ⩾ 0) andet−1 ⩾ et∕2
(t ⩾1) we see
ðuk(t)ð ⩽ 1[0,1](t)+ e−t∕21(1,∞)(t)=∶ w(t).
Let us now show thatw∈ 1(0,∞). This can be done with Beppo Levi’s theorem:
˚
∞
0
w(t)dt= ˚
1
0
w(t)
«ﬂ‹
1
dt+ ˚
∞
1
w(t)
«ﬂ‹
e−t∕2
dt
=1+sup
n∈N ˚
n
1
e−t∕2dt=1+sup
n∈N
−2e−t∕2n
t=1<∞.
127

R.L. Schilling: Measures, Integrals & Martingales
We use here that every Riemann-integrable functionf ∶ [a,b] → C, −∞ < a < b <∞,
is Lebesgue integrable and that Riemann and Lebesgue intgrals coincide (in this case, see The-
orem 12.8). By dominated convergence,
˚
∞
0
sin(t)
et−1 dt= lim
k→∞ ˚
∞
0
uk(t)dt= lim
k→∞
kÉ
n=1 ˚
∞
0
sin(t)e−ntdt.
WithImeit =sin t we get
˚
∞
0
sin(t)e−ntdt=Im
0
˚
∞
0
et(i−n)dt
1
,
(cf. Problem 10.9). Again by dominated convergence,
˚
∞
0
sin(t)e−ntdt=Im
0
lim
R→∞ ˚
R
1∕R
et(i−n)dt
1
=Im
H
lim
R→∞
4
et(i−n)
i−n
5R
t=1∕R
I
=Im
 1
n−i

= 1
n2+1 .
■■
Problem 12.14 Solution: Weknowthattheexponentialfunctionisgivenby ezx= ∑
n⩾0
(zx)n
n! . Thus,
uk(x)∶= u(x)
kÉ
n=0
(zx)n
n! , , , , , , , , , , , , , , , , , , , , →
k→∞
u(x)ezx.
By the triangle inequality,
ðuk(x)ð ⩽ ðu(x)ð
kÉ
n=0
óóóó
(zx)n
n!
óóóó
⩽ ðu(x)ð
É
n⩾0
ðzxðn
n! = ðu(x)ðeðzððxð.
Asx →exu(x)is integrable for ﬁxed=± ðzð, we get
ðuk(x)ð ⩽ ðu(x)ðe−ðzðx1(−∞,0)(x)+ ðu(x)ðeðzðx1[0,∞)(x)∈ 1(R).
An application of dominated convergence and the linearity of the integral give
˚ u(x)ezxdx= ˚ lim
k→∞
uk(x)dx
= lim
k→∞ ˚ uk(x)dx
= lim
k→∞
kÉ
n=0
1
n! ˚ (zx)nu(x)dx
=
∞É
n=0
zn
n! ˚ xnu(x)dx.
■■
128

Solution Manual. Last update 18th July 2019
Problem 12.15 Solution: We getóó∫Audóó ⩽ ∫Aðuðd straight from the triangle inequality. There-
fore, it is enough to prove the second estimate. Fix >0.
Solution1: TheSombrerolemmaensuresthatthereisasequence (un)n∈N⊂ (A)withðunð ⩽ ðuð
andlimn→∞un =u (Corollary 8.9). From dominated convergence we get∫ ðun−uðd , , , , , , , , , , , , , , , , , , , , →
n→∞
0;
inparticular, wecanchoose n∈ Nsuchthat ∫ ðun−uðd ⩽. Sinceeachun isbounded(b/o the
deﬁnition of a simple function) we get
˚A
ðunðd ⩽ ‖un‖∞⋅(A)<
for anyA∈A with(A)< ∶=∕‖un‖∞. Using the triangle inequality we get
˚A
ðuðd ⩽ ˚A
ðun−uðd+ ˚A
ðunðd ⩽ ˚ ðun−uðd+ ˚A
ðunðd ⩽2
for anyA∈A with(A)< .
Solution 2:Obviously,
˚A
ðuðd = ˚A∩{ðuð⩾R}
ðuðd+ ˚A∩{ðuð<R}
ðuðd (⋆)
We estimate each term by itself. For the ﬁrst expression on the RHS we use Beppo Levi:
˚A∩{ðuð⩾R}
ðuðd , , , , , , , , , , , , , , , , , , , , , , →
R→∞ ˚A∩{ðuð=∞}
ðuðd.
By assumption,u∈ 1(), we get(ðuð=∞)=0 (see the proof of Corollaryr 11.6) and we get
with Theorem 11.2,
˚A∩{ðuð=∞}
ðuðd =0.
Therefore, we can pick someR> 0 with
˚A∩{ðuð⩾R}
ðuðd ⩽.
For the second expression in (⋆) we have
˚A∩{ðuð<R}
ðuðd ⩽R ˚A∩{ðuð<R}
1d ⩽R(A).
IfA∈A satisﬁes(A) ⩽∶=∕R, then
˚A
ðuðd = ˚A∩{ðuð⩾R}
ðuðd+ ˚A∩{ðuð<R}
ðuðd ⩽+R(A) ⩽2.
■■
Problem 12.16 Solution: Let be an arbitrary Borel measure on the lineR and deﬁne the integral
function for someu∈ 1()through
I(x)∶= Iu
(x)∶= ˚(0,x)
u(t)(dt)= ˚ 1(0,x)(t)u(t)(dt).
129

R.L. Schilling: Measures, Integrals & Martingales
For any sequence0<l j →x,lj <x from the left andrk →x,rk>x from the right we ﬁnd
1(0,lj)(t) , , , , , , , , , , , , , , , , , , , , →
j→∞
1(0,x)(t) and 1(0,rk)(t) , , , , , , , , , , , , , , , , , , , , →
k→∞
1(0,x](t).
Since ð1(0,x)uð ⩽ ðuð∈ 1 is a uniform dominating function, Lebesgue’s dominated convergence
theorem yields
I(x+)− I(x−)=lim
k
I(rk)−lim
j
I(lj)
= ˚ 1(0,x](t)u(t)(dt)− ˚ 1(0,x)(t)u(t)(dt)
= ˚
 1(0,x](t)− 1(0,x)(t)u(t)(dt)
= ˚ 1{x}(t)u(t)(dt)
=u(x)({x}).
ThusI(x)is continuous atxif, and only if,xis not an atom of.
Remark: the proof shows, by the way, thatIu
(x) is alwaysleft-continuous at everyx, no matter
what orulook like.
■■
Problem 12.17 Solution:
(i) We have
˚
1
x 1[1,∞)(x)dx
= lim
n→∞ ˚
1
x 1[1,n)(x)dx by Beppo Levi’s thm.
= lim
n→∞ ˚[1,n)
1
xdx usual shorthand
= lim
n→∞
(R) ˚
n
1
1
xdx Riemann-˚
n
1
exists
= lim
n→∞
logxn
1
= lim
n→∞
[log(n)−log(1)]=∞
which means that1
x is not Lebesgue-integrable over[1,∞).
(ii) We have
˚
1
x2 1[1,∞)(x)dx
= lim
n→∞ ˚
1
x2 1[1,n)(x)dx by Beppo Levi’s thm.
= lim
n→∞ ˚[1,n)
1
x2dx usual shorthand
= lim
n→∞
(R) ˚
n
1
1
x2dx Riemann-˚
n
1
exists
130

Solution Manual. Last update 18th July 2019
= lim
n→∞

−1
x
n
1
= lim
n→∞
[1− 1
n]=1 <∞
which means that1
x2 is Lebesgue-integrable over[1,∞).
(iii) We have
˚
1√
x
1(0,1](x)dx
= lim
n→∞ ˚
1√
x
1(1∕n,1](x)dx by Beppo Levi’s thm.
= lim
n→∞ ˚(1∕n,1]
1√
x
dx usual shorthand
= lim
n→∞
(R) ˚
1
1∕n
1√
x
dx Riemann-˚
1
1∕n
exists
= lim
n→∞

2
√
x
1
1∕n
= lim
n→∞
4
2−2
t
1
n
5
=2 <∞
which means that1√
x is Lebesgue-integrable over(0,1].
(iv) We have
˚
1
x 1(0,1](x)dx
= lim
n→∞ ˚
1
x 1(1∕n,1](x)dx by Beppo Levi’s thm.
= lim
n→∞ ˚(1∕n,1]
1
xdx usual shorthand
= lim
n→∞
(R) ˚
1
1∕n
1
xdx Riemann-˚
1
1∕n
exists
= lim
n→∞
logx1
1∕n
= lim
n→∞

log(1)−log 1
n

=∞
which means that1
x is not Lebesgue-integrable over(0,1].
■■
Problem 12.18 Solution: We construct a dominating integrable function.
Ifx ⩽1, we have clearlyexp(−x) ⩽1, and∫(0,1] 1dx=1 <∞is integrable.
Ifx ⩾ 1, we haveexp(−x) ⩽ Mx−2 for some suitable constantM = M < ∞. This function
is integrable in[1,∞), see e.g. Problem 12.17. The estimate is easily seen from the fact that
x →x2exp(−x)is continuous in[1,∞) withlimx→∞x2exp(−x)=0 .
131

R.L. Schilling: Measures, Integrals & Martingales
This shows thatexp(−x) ⩽ 1(0,1)+Mx−21[1,∞) with the right-hand side being integrable.
■■
Problem 12.19 Solution: Take ∈(a,b) where0<a<b< ∞ are ﬁxed (but arbitrary). We show
that the function is continuous for these. This shows the general case since continuity is a local
property and we can ‘catch’ any given0 by some choice ofa andb’s.
WeusetheContinuitylemma(Theorem12.4)andhavetoﬁnduniform(for ∈(a,b))dominating
boundsontheintegrandfunction f(,x)∶=

sinx
x
3
e−x. Firstofall,weremarkthat óóó
sinx
x
óóó ⩽M
which follows from the fact thatsinx
x is a continuous function such thatlimx→∞
sinx
x = 0and
limx↓0
sinx
x = 1. (Actually, we could chooseM = 1...). Moreover,exp(−x) ⩽ 1 forx ∈ (0,1)
andexp(−x) ⩽ Ca,bx−2 forx ⩾ 1—use for this the continuity ofx2exp(−x) and the fact that
limx→∞x2exp(−x)=0 . This shows that
ðf(,x)ð ⩽M 1(0,1)(x)+ Ca,bx−21[1,∞)(x)
andtheright-handsideisanintegrabledominatingfunctionwhichdoesnotdependon —aslong
as ∈ (a,b). But since → f(,x) is obviously continuous, the Continuity lemma applies and
proves that∫(0,∞)f(,x)dx is continuous.
■■
Problem 12.20 Solution: Fix some numberN >0 and takex ∈ (−N,N). We show thatG(x) is
continuous on this set. SinceN was arbitrary, we ﬁnd thatG is continuous for everyx∈ R.
Setg(t,x)∶= sin(tx)
t(1+t2) =x sin(tx)
(tx)
1
1+t2. Then, using thatóóó
sinu
u
óóó ⩽M, we have
ðg(t,x)ð ⩽x⋅M⋅ 1
1+ t2 ⩽M⋅N⋅

1(0,1)(t)+ 1
t2 1[1,∞)(t)

and the right-hand side is a uniformly dominating function, i.e.G(x) makes sense and we ﬁnd
G(0) =∫t≠0g(t,0)dt = 0. To see diﬀerentiability, we use the Diﬀerentiability lemma (Theorem
12.5) and need to prove thatð)xg(t,x)ð exists (this is clear) and is uniformly dominated forx ∈
(−N,N). We have
ð)xg(t,x)ð= óóóó
)x
sin(tx)
t(1+ t2)
óóóó
= óóóó
cos(tx)
(1+ t2)
óóóó
⩽ 1
1+ t2
⩽

1(0,1)(t)+ 1
t2 1[1,∞)(t)

and this allows us to apply the Diﬀerentiability lemma, so
G‡(x)= )x ˚t≠0
g(t,x)dt= ˚t≠0
)xg(t,x)dt
= ˚t≠0
cos(tx)
1+ t2 dt
= ˚R
cos(tx)
1+ t2 dt
132

Solution Manual. Last update 18th July 2019
(use in the last equality that{0} is a Lebesgue null set). Thus, by a Beppo Levi-argument (and
using that Riemann=Lebesgue whenever the Riemann integral over a compact interval exists...)
G‡(0)= ˚R
1
1+ t2dt= lim
n→∞
(R) ˚
n
−n
1
1+ t2dt
= lim
n→∞
[tan−1(t)]n
−n
=.
Now observe that
)xsin(tx)= tcos(tx)= t
xxcos(tx)= t
x)tsin(tx).
Since the integral deﬁningG‡(x) exists we can use a Beppo Levi-argument, Riemann=Lebesgue
(whenever the Riemann integral over an interval exists) and integration by parts (for the Riemann
integral) to ﬁnd
xG‡(x)= ˚R
xcos(tx)
1+ t2 dt
= lim
n→∞
(R) ˚
n
−n
x)xsin(tx)
t(1+ t2) dt
= lim
n→∞
(R) ˚
n
−n
t)tsin(tx)
t(1+ t2) dt
= lim
n→∞
(R) ˚
n
−n
)tsin(tx)
1+ t2 dt
= lim
n→∞
(R) ˚
n
−n
)tsin(tx)⋅ 1
1+ t2dt
= lim
n→∞
4sin(tx)
1+ t2
5n
t=−n
− lim
n→∞
(R) ˚
n
−n
sin(tx)⋅)t
1
1+ t2dt
= lim
n→∞
(R) ˚
n
−n
sin(tx)⋅ 2t
(1+ t2)2dt
= ˚R
2tsin(tx)
(1+ t2)2 dt.
■■
Problem 12.21 Solution:
(i) Note that for0 ⩽a,b ⩽1
1−(1− a)b= ˚
1
1−a
btb−1dt ⩾ ˚
1
1−a
bdt =ba
so that we get for0 ⩽x ⩽kanda∶=x∕k,b∶=k∕(k+1)

1− x
k
 k
k+1
⩽1− x
k+1 , 0 ⩽x ⩽k
or,

1− x
k
k
1[0,k](x) ⩽

1− x
k+1
k+1
1[0,k+1](x).
133

R.L. Schilling: Measures, Integrals & Martingales
Therefore we can appeal to Beppo Levi’s theorem to get
lim
k→∞ ˚(1,k)

1− x
k
k
lnx1(dx)= sup
k∈N ˚ 1(1,k)(x)

1− x
k
k
lnx1(dx)
= ˚ sup
k∈N

1(1,k)(x)

1− x
k
k
lnx1(dx)
= ˚ 1(1,∞)(x)e−x lnx1(dx).
Thate−xlnxis integrable in(1,∞)follows easily from the estimates
e−x ⩽CNx−N and lnx ⩽x
which hold for allx ⩾1andN ∈ N.
(ii) Note thatx →lnx is continuous and bounded in[,1], thus Riemann integrable. It is easy
to see thatxlnx−xis a primitive forlnx. The improper Riemann integral
˚
1
0
lnxdx =lim
→0
[xlnx−x]1
 =−1
existsand,since lnxisnegativethroughout (0,1),improperRiemannandLebesgueintegrals
coincide. Thus,lnx∈L1(dx,(0,1)).
Therefore,
óóóó

1− x
k
k
lnxóóóó
⩽ ðlnxð, ∀x∈(0,1)
is uniformly dominated by an integrable function and we can use dominated convergence to
get
lim
k ˚(0,1)

1− x
k
k
lnxdx = ˚(0,1)
lim
k

1− x
k
k
lnxdx
= ˚(0,1)
e−x lnxdx
■■
Problem 12.22 Solution: Since the integrand ofF(t) is continuous and bounded by the integrable
functione−x,x> 0, it is clear thatF(t)exists. With the usual approximation argument,
˚(0,∞)
e−x t
t2+x2(dx)= lim
n→∞ ˚
n
1∕n
e−x t
t2+x2dx
(the right-hand side is a Riemann integral) we can use the classical (Riemann) rules to evaluate
the integral. Thus, a change of variablesx=t⋅y - ⇒dx=tdy yields
F(t)= ˚(0,∞)
e−x t
t2+x2(dx)
= ˚(0,∞)
e−ty t
t2+(ty)2t(dy)
134

Solution Manual. Last update 18th July 2019
= ˚(0,∞)
e−ty 1
1+ y2(dy).
Observe that
óóóó
e−ty 1
1+ y2
óóóó
⩽ 1
1+ y2 uniformly for allt> 0,
and that the right-hand side is Lebesgue integrable (the primitive is the arctan). Therfore, we can
use dominated convergence to conclude
F(0+)=lim
t↓0 ˚(0,∞)
e−ty 1
1+ y2(dy)
= ˚(0,∞)
lim
t↓0
e−ty 1
1+ y2(dy)
= ˚(0,∞)
1
1+ y2(dy)
= lim
n→∞ ˚
n
1∕n
1
1+ y2dy
= lim
n→∞
arctanyn
1∕n= 
2.
■■
Problem 12.23 Solution: For the existence of the integrals we needðe−i⋅ð ∈ 1() and ðe−i⋅ð⋅
ðu(⋅)ð∈ 1(dx). Sinceðe−i⋅ð=1 , it is reasonable to require that is a ﬁnite measure (such that
theconstant 1isintegrable)or u∈ 1(dx). Undertheseassumptions,thecontinuityoftheFourier
transform follows directly from the continuity lemma: set
f(,x)∶= 1
2e−ix,  ∈ R,x ∈ R.
By assumption,ðf(x,)ð ⩽(2)−1∈ 1() and →f(,x) is continuous. Using Theorem 12.4,
we get the continuity of the map
 → ˚ f(,x)(dx)=  ().
The argument for̂ uis similar.
Suﬃcient conditions forn-fold diﬀerentiability can be obtained from the diﬀerentiability lemma.
Since
d
df(,x)= (−ix)
2 e−ix
we get
óóóó
d
df(,x)óóóó
⩽ ðxð
2.
By the diﬀerentiabiliy lemma the derivatived
d ̂ () exists, if ∫ ðxð(dx) < ∞. Iterating this
argument, we get that̂ isntimes diﬀerentiable, if
˚ ðxðn(dx)<∞.
Similarly one shows that̂ uisntimes diﬀerentiable, if∫ ðxðnðu(x)ðdx< ∞.
■■
135

R.L. Schilling: Measures, Integrals & Martingales
Problem 12.24 Solution:
(i) Let t ∈ (−R,R) for someR >0. Since ð(x)− tð ⩽ ð(x)ð+ ðtð ⩽ ð(x)ð+R ∈
1([0,1],dx)andsince t → ð(x)−tðiscontinuous,thecontinuitylemma,Theorem12.4,
shows that the mapping
(−R,R)∋ t →f(t)= ˚[0,1]
ð(x)− tðdx
is continuous. SinceR> 0 is arbitrary, the claim follows.
Alternative solution:Using the lower triangle inequality we get that
ðf(t)− f(s)ð ⩽ ˚[0,1]
óóóð(x)− tð−ð(x)− sðóóódx ⩽ ˚[0,1]
ðs−tðdx= ðs−tð,
i.e.f is Lipschitz continuous.
(ii) ‘⇐’: Lett∈ R and assume that{=t}=0 . Forℎ∈ R we deﬁne
f(t+ℎ)− f(t)
ℎ = ˚⩽t−ℎ
ð(x)−( t+ℎ)ð−ð(x)− tð
ℎ dx
+ ˚t−ℎ<<t+ℎ
ð(x)−( t+ℎ)ð−ð(x)− tð
ℎ dx
+ ˚⩾t+ℎ
ð(x)−( t+ℎ)ð−ð(x)− tð
ℎ dx
=∶I1(ℎ)+ I2(ℎ)+ I3(ℎ).
and we consider the three integrals separately. We have
I1(ℎ)= ˚⩽t−ℎ
−((x)−( t+ℎ))+( (x)− t)
ℎ dx
= ˚⩽t−ℎ
dx=( ⩽t−ℎ) , , , , , , , , , , , , , , , , , →
ℎ→0
{<t }.
Similarly,
I3(ℎ)= ˚⩾t−ℎ
((x)−( t+ℎ)−( (x)− t)
ℎ dx
=( ⩾t+ℎ) , , , , , , , , , , , , , , , , , →
ℎ→0
{>t }.
By our assumptions,{t−ℎ <  < t+ℎ} , , , , , , , , , , , , , , , , , →
ℎ→0
{ = t} = 0, and using dominated
convergence we arrive at
I2(ℎ)= ˚t−ℎ<<t+ℎ
ð(x)−( t+ℎ)ð−ð(x)− tð
ℎ dx , , , , , , , , , , , , , , , , , →
ℎ→0
0
(notice that ðð(x)−(t+ℎ)ð−ð(x)−tðð
ℎ ⩽ 2 b/o the lower triangle inequality!). Putting together
all calculations, we get
lim
ℎ→0
f(x+ℎ)− f(x)
ℎ ={>t }+ {<t }.
136

Solution Manual. Last update 18th July 2019
‘⇒’: We use the notation introduced in the direction ‘⇐’. Iff is diﬀerentiable att∈ R,
we ﬁnd as in the ﬁrst part of the proof that
lim
ℎ→0
I2(ℎ)= f‡(t)−lim
ℎ→0
I1(ℎ)−lim
ℎ→0
I3(ℎ)
exists. We splitI2 once again:
I2(ℎ)= ˚{t−ℎ<<t+ℎ}⧵{=t}
ð(x)−( t+ℎ)ð−ð(x)− tð
ℎ dx
+ ˚{=t}
ð(x)−( t+ℎ)ð−ð(x)− tð
ℎ dx
=∶I1
2(ℎ)+ I2
2(ℎ)
Obviously, we have
I2
2(ℎ)= ðℎð
ℎ ˚{=t}
1dx= ðℎð
ℎ {=t}
and with dominated convergence we get
lim
ℎ→0
I1
2(ℎ)=0 .
Therefore,limℎ→0I2(ℎ)can only exist, if
lim
ℎ→0
I2
2(ℎ)= (=t)lim
ℎ→0
ðℎð
ℎ
exists, and this is the case if(=t)=0 .
■■
Problem 12.25 Solution:
(i) The mapt → u(t,x) ∶=x−2sin2(x)e−tx is continuous on[0,∞) and diﬀerentiable on
(0,∞) diﬀerenzierbar. Because of the continuity and diﬀerentiability lemmas (The-
orem 12.4 and 12.5) it is enough to ﬁnd suitable majorants for the function and its
derivatives. Fixt ⩾0. Using the elementary inequalitiessinx
x ⩽1 ande−tx ⩽1 we get
ðu(t,x)ð ⩽ 1[0,1](x)+ 1
x2 1(1,∞)(x)=∶ w(x).
Since w ∈ 1([0,∞)) (cf. Beispiel 12.14), continuity follows from the continuity
lemma. Assume now thatt∈(r,∞) for somer> 0. Then we get
ð)tu(t,x)ð=
óóóóó
sin2(x)
x2 (−x)e−tx
óóóóó
⩽ 1[0,1](x)+ xe−tx1[1,∞)(x)∈ 1([0,∞))
ð)2
tu(t,x)ð=
óóóóó
sin2(x)
x2 (−x)2e−tx
óóóóó
⩽ 1[0,1](x)+ x2e−tx1[1,∞)(x)∈ 1([0,∞)).
137

R.L. Schilling: Measures, Integrals & Martingales
Now the diﬀerentiability lemma shows thatf has two derivatives which are given by
f‡(t)=− ˚
∞
0
sin2(x)
x e−txdx,
f‡‡(t)= ˚
∞
0
sin2(x)e−txdx.
(ii) In order to calculatef‡‡we use that Riemann and Lebesgue integrals auszurechnen
coincide if a function is Riemann integrable (Theorem 12.8).
Usingsin2(x)= 1
2(1−cos(2 x))= 1
2Re(1− ei2x)we get
f‡‡(t)= 1
2Re
0
˚
∞
0
(1− ei2x)e−txdx
1
,
(cf. Problem 10.9). Using dominated convergence, we see
˚
∞
0
(1− ei2x)e−txdx= lim
R→∞ ˚
R
0
(1− ei2x)e−txdx.
Sincex →(1− ei2x)e−tx is Riemann integrable, we can integrate ‘as usual’:
˚
∞
0
(1− ei2x)e−txdx= lim
R→∞
 1
−te−tx
R
x=0
− lim
R→∞
 1
2i−tex(2i−t)
R
x=0
= 1
t − 1
t−2i.
Thus,
f‡‡(t)= 1
2Re
1
t − 1
t−2i

= 1
2
0
1
t − t
t2+4
1
= 2
t(t2+4) .
Thelimits limt→∞f(t)andlimt→∞f‡(t)followagainwithdominatedconvergence(the
necessary majorants are those from part (i)):
lim
t→∞
f(t)= ˚
∞
0
lim
t→∞
0sin2(x)
x2 e−tx
1
dx=0,
lim
t→∞
f‡(t)=− ˚
∞
0
lim
t→∞
0sin2(x)
x e−tx
1
dx=0.
(iii) Webeginwithaclosedexpressionfor f‡: fromthefundamentaltheoremof(Riemann)
integration we know
f‡(R)− f‡(t)= ˚
R
t
f‡‡(s)ds.
LettingR →∞we get using (ii)
f‡(t)=− lim
R→∞ ˚
R
t
f‡‡(s)ds
=− 1
2 lim
R→∞

logs−1
2log(s2+4)
R
s=t
= 1
2

logt−1
2log(t2+4)

= 1
2log t√
t2+4
.
138

Solution Manual. Last update 18th July 2019
Finally,
f(t)=− lim
R→∞ ˚
R
t
f‡(s)ds=− 1
2 ˚
∞
t
log s√
s2+4
ds.
(InthispartwehaveagainusedthefactthattheLebesgueintegralextendstheRiemann
integral.)
■■
Problem 12.26 Solution: We follow the hint: sincee−tx ⩾0 we can use Beppo Levi to get
˚
∞
0
e−xtdx= sup
n∈N ˚
n
0
e−xtdx= lim
n→∞ ˚
n
0
e−xtdx.
Moreover,x → e−tx is continuous, hence measurable and Riemann-integrable on compact inter-
vals, and we may (Theorem 12.8) use the Riemann integral to evaluate things.
˚
n
0
e−xtdx=
4
e−tx
−t
5n
x=0
n→∞
, , , , , , , , , , , , , , , , , , , , →1
t.
Thus, e−tx ∈ 1(0,∞) and ∫ ∞
0 e−xtdx = 1
t. Now we use the diﬀerentiability lemma, The-
orem 12.5. Foru(t,x)∶= e−tx we have
ð)tu(t,x)ð= ðxðe−tx ⩽ ðxðe−ax∈ 1(0,∞) ∀ t∈(a,∞), a>0,
(cf. Example 12.14). Therefore (use the diﬀerentiability lemma)
d
dt ˚
∞
0
e−txdx= ˚
∞
0
(−x)e−txdx ∀t∈(a,∞).
Sincea >0 is arbitrary, we get diﬀerentiability on(0,∞). Iterating this argument, we inver that
we can swap derivatives of any order with the integral. Morover,
dn
dtn
0
˚
∞
0
e−xtdx
1
= dn
dtn
1
t

⇒
0
˚
∞
0
(−x)ne−xtdx
1
= (−1)nn!
tn+1 .
Ift=1 , the claim follows.
■■
Problem 12.27 Solution: Throughoutweﬁx(a,b)⊂(0,∞)andtake t∈(a,b). AsinProblem12.17
we get
˚(0,1)
x−dx< ∞ ∀  <1 and ˚(1,∞)
x−dx< ∞ ∀  >1.
(i) Note that diﬀerentiability implies continuity, so it suﬃces to show thatΓ is m times
diﬀerentiable for everym.
Induction Hypothesis:Γ(m) exists and is of the form as claimed in the statement of the
problem.
139

R.L. Schilling: Measures, Integrals & Martingales
Induction Startm = 1: We have to show thatΓ(t) is diﬀerentiable. We want to use
the diﬀerentiability lemma. For this we remark ﬁrst of all, that the integrand function
t →(t,x)is diﬀerentiable on(a,b)and that
)t(t,x)= )te−xxt−1=e−xxt−1 logx.
We have now to ﬁnd a uniform (fort ∈ (a,b)) integrable dominating function for
ð)t(t,x)ð. Sincelogx ⩽xfor allx> 0 (the logarithm is a concave function!),
óóóe−xxt−1 logxóóó=e−xxt−1 logx
⩽e−xxt ⩽ e−xxb ⩽ Cbx−2 ∀x ⩾1, t ∈(a,b)
(for the last step multiply withx2 and use thatxe−x is continuous for every> 0 and
limx→∞xe−x=0 to ﬁndCb). Moreover,
óóóe−xxt−1 logxóóó ⩽xa−1ðlogxð
=xa−1 log1
x ⩽ Cax−1∕2 ∀x∈(0,1), t ∈(a,b)
where we use the fact thatlimx→0xlog 1
x =0 which is easily seen by the substitution
x=e−u andu →∞and the continuity of the functionx log 1
x.
Both estimates together furnish an integrable dominating function, so the diﬀerentiab-
ility lemma applies and shows that
Γ‡(t)= ˚(0,∞)
)t(t,x)dx= ˚(0,∞)
e−xxt−1 logxdx =Γ (1)(x).
InductionStep m ⇝m+1: Set(m)(t,x)= e−xxt−1(logx)m. Wewanttoapplythedif-
ferentiabilitylemmato Γ(m)(x). Withverymuchthesameargumentsasintheinduction
start we ﬁnd that(m+1)(t,x) =)t(m)(t,x) exists (obvious) and satisﬁes the following
bounds
óóóe−xxt−1(logx)m+1óóó=e−xxt−1(logx)m+1
⩽e−xxt+m
⩽e−xxb+m
⩽Cb,mx−2 ∀x ⩾1, t∈(a,b)
óóóe−xxt−1(logx)m+1óóó ⩽xa−1ðlogxðm+1
=xa−1

log1
x
m+1
⩽Ca,mx−1∕2 ∀x∈(0,1), t∈(a,b)
and the diﬀerentiability lemma applies completing the induction step.
140

Solution Manual. Last update 18th July 2019
(ii) Using a combination of Beppo Levi (indicated by ‘BL’), Riemann=Lebesgue (if the
Riemann integral over an interval exists) and integration by parts (for the Riemann in-
tegral, indicated by ‘parts’) techniques we get
tΓ(t)= lim
n→∞ ˚(1∕n,n)
e−xtxt−1dx (BL)
= lim
n→∞
(R) ˚
n
1∕n
e−x)xxtdx
= lim
n→∞
e−xxtn
x=1∕n− lim
n→∞
(R) ˚
n
1∕n
)xe−xxtdx (parts)
= lim
n→∞
(R) ˚
n
1∕n
e−xx(t+1)−1dx
= lim
n→∞ ˚(1∕n,n)
e−xx(t+1)−1dx
= ˚(0,∞)
e−xx(t+1)−1dx (BL)
=Γ(t+1).
(iii) We have to show that
logΓ(t+(1− )s) ⩽logΓ(t)+(1− )logΓ( s) ∀s,t> 0, ∈(0,1).
This is clearly equivalent to
Γ(t+(1− )s) ⩽[Γ(t)][Γ(s)]1− ∀s,t> 0, ∈(0,1).
Fixs,t> 0 and write= 1
p and1− = 1
q =1− 1
p wherep,q ∈(1,∞) are conjugate
exponents. We get using Hölder’s inequality
Γ(t+(1− )s)= ˚
∞
0
e−xxt+(1−)s−1dx
= ˚
∞
0
e−1
pxx
1
p(t−1)e−1
qxx
1
q(s−1)dx
⩽
4
˚
∞
0
e−xxt−1dx
51
p
4
˚
∞
0
e−xxs−)dx
51
q
⩽[Γ(t)][Γ(s)]1−.
(iii) Alternative–directcalculuation SincelogandΓarein C2wecanapplytheconvexity
criterion: logΓ is convex if, and only if,d2
dt2logΓ(t) ⩾0holds. We have
d
dtlogΓ(t)= Γ‡(t)
Γ(t)
d2
dt2logΓ(t)= Γ(t)Γ‡‡(t)−(Γ ‡(t))2
(Γ(t))2
which is non-negative iﬀ
0
!
⩽Γ(t)Γ‡‡(t)−(Γ ‡(t))2
141

R.L. Schilling: Measures, Integrals & Martingales
So with the notation from part (ii), along with the dominated convergence theorem
(indicated by ‘DC’ – this is needed forΓ‡, since its integrand will take negative values,
so Beppo Levi does not apply), we get
Γ(t)Γ‡‡(t)−(Γ ‡(t))2= lim
n→∞ ˚(1∕n,n) ˚(1∕n,n)
e−x−y(xy)t−1(logy)2dxdy (BL)
− lim
n→∞ ˚(1∕n,n) ˚(1∕n,n)
e−x−y(xy)t−1logxlogydxdy (DC)
= lim
n→∞
(R) ˚
n
1∕n ˚
n
1∕n
e−x−y(xy)t−1logy(logy−log x)dxdy
= lim
n→∞
(R) ˚
n
1∕n ˚
n
1∕n
e−x−y(xy)t−1logylogy
xdxdy
In the last expression we can change the roles ofxandywithout changing the value of
the integrals (Fubini), so we get
= lim
n→∞
1
2(R) ˚
n
1∕n ˚
n
1∕n
e−x−y(xy)t−1logylogy
xdxdy
+ lim
n→∞
1
2(R) ˚
n
1∕n ˚
n
1∕n
e−x−y(xy)t−1logxlogx
ydxdy
= lim
n→∞
1
2(R) ˚
n
1∕n ˚
n
1∕n
e−x−y(xy)t−1(logylogy
x+log xlogx
y)dxdy.
At last, using well-known logarithmic identities, we get
logylogy
x+log xlogx
y =log ylogy
x−log xlogy
x
=log y
x(logy−log x)
=

logy
x
2
and inserting this into the above integral gives
= lim
n→∞
1
2(R) ˚
n
1∕n ˚
n
1∕n
e−x−y(xy)t−1

logy
x
2
dxdy
= 1
2 ˚(0,∞) ˚(0,∞)
e−x−y(xy)t−1(logy
x)2
«››››››››››››ﬂ››››››››››››‹
⩾0
dxdy ⩾0. (BL)
This ﬁnishes the proof.
■■
Problem 12.28 Solution:
(i) The functionx → xlnx is bounded and continuous in[0,1], hence Riemann integrable.
SinceinthiscaseRiemannandLebesgueintegralscoincide,wemayuseRiemann’sintegral
and the usual rules for integration. Thus, changing variables according tox = e−t, dx =
−e−tdt and thens=(k+1)t,ds=(k+1) ds we ﬁnd,
˚
1
0
(xlnx)kdx= ˚
∞
0
e−t(−t)k
e−tdt
142

Solution Manual. Last update 18th July 2019
=(−1) k
˚
∞
0
tke−t(k+1)dt
=(−1) k
˚
∞
0
 s
k+1
k
e−s ds
k+1
=(−1) k
 1
k+1
k+1
˚
∞
0
s(k+1)−1e−sds
=(−1) k
 1
k+1
k+1
Γ(k+1).
(ii) Following the hint we write
x−x=e−xlnx=
∞É
k=0
(−1)k(xlnx)k
k! .
Sincefor x∈(0,1)thetermsunderthesumareallpositive,wecanuseBeppoLevi’stheorem
and the formulaΓ(k+1)= k!to get
˚(0,1)
x−xdx=
∞É
k=0
(−1)k1
k! ˚(0,1)
(xlnx)kdx
=
∞É
k=0
(−1)k1
k!(−1)k
 1
k+1
k+1
Γ(k+1)
=
∞É
k=0
 1
k+1
k+1
=
∞É
n=1
1
n
n
.
■■
Problem 12.29 Solution: Fix(a,b)⊂(0,1)andletalways u∈(a,b). Wehaveforx ⩾0andL∈ N0
ðxLf(u,x)ð= ðxðL óóóó
eux
ex+1
óóóó
=xL eux
ex+1
⩽xLeux
ex
=xLe(u−1)x
⩽ 1[0,1](x)+ Ma,b1(1,∞)(x)x−2
where we use thatu−1 <0, the continuity and boundedness ofxe−ax forx∈[1,∞) and ⩾0.
Ifx ⩽0 we get
ðxLf(u,x)ð= ðxðL óóóó
eux
ex+1
óóóó
= ðxðLe−uðxð
⩽ 1[−1,0](x)+ Na,b1(−∞,1)(x)ðxð−2.
Bothinequalitiesgivedominatingfunctionswhichareintegrable;therefore,theintegral ∫RxLf(u,x)dx
exists.
143

R.L. Schilling: Measures, Integrals & Martingales
Tosee m-folddiﬀerentiability,weusetheDiﬀerentiabilitylemma(Theorem12.5) m-times. Form-
ally, we have to use induction. Let us only make the induction step (the start is very similar!). For
this, observe that
)m
u(xnf(u,x))= )m
u
xneux
ex+1 = xn+meux
ex+1
but, as we have seen in the ﬁrst step withL=n+m, this is uniformly bounded by an integrable
function. Therefore, the Diﬀerentiability lemma applies and shows that
)m
u ˚R
xnf(u,x)dx= ˚R
xn)m
uf(u,x)dx= ˚R
xn+mf(u,x)dx.
■■
Problem 12.30 Solution: Becauseofthebinomialformualwehave (1+ x2)n ⩾1+ nx2; thisyields,
in particular,
óóóó
1+ nx2
(1+ x2)n
óóóó
⩽1.
Since
lim
n→∞
1+ nx2
(1+ x2)n =0 ∀ x∈(0,1)
(exponential growth is always stronger than polynomial growth!) we can use dominated conver-
gence and ﬁnd
lim
n→∞ ˚
1
0
1+ nx2
(1+ x2)ndx=0.
■■
Problem 12.31 Solution:
(i) We begin by showing thatf is well deﬁned, i.e. the integral expression makes sense. Recall
the following estimates
ðarctan(y)ð ⩽ ðyð, ðarctan(y)ð ⩽ 
2, y ∈ R,
(the ﬁrst inequality follows from the mean value theorem, the second from the deﬁnition of
arctan.) Moreover,
sinhx= 1
2(ex−e−x) ⩾ 1
2(ex−1) ⩾ 1
2
1
2x2 ∀x ⩾1.
Foru(t,x)∶=arctan

t
sinhx

we see
ðu(t,x)ð ⩽ 
2 1(0,1)(x)+ óóóó
t
sinhx
óóóó
1[1,∞)(x)
⩽ 
2 1[0,1](x)+ 1
4
1
x2 1[1,∞)(x)∈ 1((0,∞)).
This proves that the integralf(t)= ∫(0,∞)u(t,x)dx exists. In order to check diﬀerentiability
off,wehavetoﬁnd(Theorem12.5)amajorizingfunctionforthederivativeoftheintegrand.
FixR> 0 and lett∈(R−1,R). By the chain rule
)
)tu(t,x)= 1
1+

t
sinhx
2
1
sinhx
144

Solution Manual. Last update 18th July 2019
= 1
t2
sinhx+sinh x
.
Sincex → 1
R−2+sinhx is continuous, there is a constantC1>0 such that
sup
x∈[0,1]
1
R−2+sinh x ⩽C1.
Using0 ⩽sinhx ⩽1 forx∈[0,1], we get
ð)tu(t,x)ð ⩽ 1
R−2
sinhx+sinh x
⩽ 1
R−2+sinh x ⩽C1 ∀x∈[0,1].
Similarly we get forx> 1
ð)tu(t,x)ð ⩾ 1
sinhx =2 1
ex−e−x = 2
ex
1
1− e−2x
«›ﬂ›‹
⩽C2<∞
∈ 1((1,∞)).
Therefore,
ð)tu(t,x)ð ⩽C11(0,1](x)+2 C2
1
ex 1(1,∞)(x)∈ 1((0,∞)).
Usingthediﬀerentiabilitylemma,Theorem12.5,weﬁndthat f isdiﬀerentiableon(R−1,R)
and that
f‡(t)= ˚(0,∞)
1
t2
sinhx+sinh x
dx ∀t∈(R−1,R).
SinceR> 0isarbitrary, f isdiﬀerentiableon(0,∞). Thatlimt↓0f‡(t)doesnotexist,follows
directly from the closed expresson forf‡in part (ii).
(ii) Note thatf(0)=0 . In order to ﬁnd an expression forf‡, we perform the following substitu-
tion: u=cosh xand we get, observing thatcosh2x−sinh2x=1 :
f‡(t)= ˚(1,∞)
1
t2
√
u2−1
+
√
u2−1
1√
u2−1
du
= ˚(1,∞)
1
t2−1+ u2du.
(Observe: x → 1
t2
sinhx+sinhx
is continuous, hence Riemann-integrable. Since we have estab-
lished in part (i) the existence of the Lebesgue integral, we can use Riemann integrals (b/o
Theorem 12.8).) There are two cases:
• t> 1: We havet2−1 >0 and so
f‡(t)= 1
t2−1 ˚(1,∞)
1
1+
0
u√
t2−1
12du
= 1
t2−1
L√
t2−1arctan
H
u√
t2−1
IM∞
u=1
= 1√
t2−1
H

2 −arctan
H
1√
t2−1
II
= 1√
t2−1
arctan
√
t2−1

.
145

R.L. Schilling: Measures, Integrals & Martingales
• t< 1: ThenC ∶=
√
1− t2 makes sense and we get
u2+t2−1= u2−C2=(u+C)(u−c).
Moreover, by partial fractions,
1
u2−C2 = 1
2C
1
u+C − 1
2C
1
u−C
and so
˚(1,∞)
1
u2+t2−1 du= ˚(1,∞)
u2−C2
du
= 1
2C lim
R→∞
0
˚
R
1
1
u+C du− ˚
R
1
1
u−C du
1
= 1
2C lim
R→∞

ln
1+ C
1− C

+ln
R+C
R−C

= 1
2C ln
1+ C
1− C

= 1
2
√
1− t2
ln
H
1+
√
1− t2
1−
√
1− t2
I
.
The ﬁrst part of our argument shows, in particular,
˚
∞
1
f‡(t)dt=∞.
Sincef(t)= f(1)+ ∫ t
1 f‡(s)ds,t ⩾1, we getlimt→∞f(t)=∞ .
■■
Problem 12.32 Solution:
(i) Since
óóóó
dm
dtme−tXóóóó
= óóóXme−tXóóó ⩽Xm
m applications of the diﬀerentiability lemma, Theorem 12.5, show that(m)
X (0+) exists and
that
(m)
X (0+)=(−1) m
˚ XmdP.
(ii) Using the exponential series we ﬁnd that
e−tX−
mÉ
k=0
Xk(−1)ktk
k! =
∞É
k=m+1
Xk(−1)ktk
k!
=tm+1
∞É
j=0
Xm+1+j (−1)m+1+jtj
(m+1+ j)!.
Since the left-hand side has a ﬁniteP-integral, so has the right, i.e.
˚
 ∞É
j=0
Xm+1+j (−1)m+1+jtj
(m+1+ j)!

dP converges
146

Solution Manual. Last update 18th July 2019
and we see that
˚

e−tX−
mÉ
k=0
Xk(−1)ktk
k!

dP=o(tm)
ast →0.
(iii) We show, by induction inm, that
óóóó
e−u−
m−1É
k=0
(−u)k
k!
óóóó
⩽ um
m! ∀u ⩾0. (*)
Because of the elementary inequality
ðe−u−1ð ⩽u ∀u ⩾0
the start of the inductionm=1 is clear. For the induction stepm →m+1 we note that
óóóó
e−u−
mÉ
k=0
(−u)k
k!
óóóó
= óóóó ˚
u
0

e−y−
m−1É
k=0
(−y)k
k!

dyóóóó
⩽ ˚
u
0
óóóó
e−y−
m−1É
k=0
(−y)k
k!
óóóó
dy
(*)
⩽ ˚
u
0
ym
m!dy
= um+1
(m+1)! ,
and the claim follows.
Settingx=tX in (*), we ﬁnd by integration that
±
0
˚ e−tX−
m−1É
k=0
(−1)ktk ∫ XkdP
k!
1
⩽
tm ∫ XmdP
m! .
(iv) Ift is in the radius of convergence of the power series, we know that
lim
m→∞
ðtðm ∫ XmdP
m! =0
which, when combined with (iii), proves that
X(t)= lim
m→∞
m−1É
k=0
(−1)ktk ∫ XkdP
k! .
■■
Problem 12.33 Solution:
(i) Wrong,u is NOT continuous on the irrational numbers. To see this, just take a sequence of
rationalsqj ∈ Q∩[0,1]approximatingp∈[0,1] ⧵ Q. Then
lim
j
u(qj)=1 ≠0= u(p)= u(lim
j
qj).
147

R.L. Schilling: Measures, Integrals & Martingales
(ii) True. Mind thatv is not continuous at0, but{n−1,n ∈ N}∪{0} is still countable.
(iii) True. Thepointswhere uandvarenot 0(thatis: wheretheyare 1)arecountablesets,hence
measurable and also Lebesgue null sets. This shows thatu,v are measurable and almost
everywhere0, hence∫ ud =0= ∫ vd.
(iv) True. SinceQ∩[0,1]aswellas [0,1] ⧵ Qaredensesubsetsof [0,1],ALLlowerresp.upper
Darboux sums are always
S[u] ≡0 resp. S[u] ≡1
(foranyﬁnitepartition  of[0,1]). Thusupperandlowerintegralsof uhavethevalue 0resp.
1 and it follows thatucannot be Riemann integrable.
■■
Problem 12.34 Solution: NotethateveryfunctionwhichhasﬁnitelymanydiscontinuitiesisRiemann
integrable. Thus, if{qj}j∈N is an enumeration ofQ, the functionsuj(x) ∶= 1{q1,q2,…,qj}(x) are
Riemannintegrable(withRiemannintegral 0)whiletheirincreasinglimit u∞= 1QisnotRiemann
integrable.
■■
Problem 12.35 Solution: Of course we have to assume thatu is Borel measurable! By assumption
we know thatuj ∶=u1[0,j] is (properly) Riemann integrable, hence Lebesgue integrable and
˚[0,j]
ud = ˚[0,j]
ujd= (R)˚
j
0
u(x)dx , , , , , , , , , , , , , , , , , , , , →
j→∞ ˚
∞
0
u(x)dx.
ThelastlimitexistsbecauseofimproperRiemannintegrability. Moreover,thislimitisanincreas-
ing limit, i.e. a ‘sup’. Since0 ⩽uj ↑u we can invoke Beppo Levi’s theorem and get
˚ ud =sup
j ˚ ujd= ˚
∞
0
u(x)dx< ∞
proving Lebesgue integrability.
■■
Problem 12.36 Solution: Observe thatx2 = k ⇐ ⇒ x =
√
k,x ⩾ 0,k ∈ N0. Thus, Since
sinx2 iscontinuous,itisoneveryboundedintervalRiemannintegrable. Byachangeofvariables,
y=x2, we get
˚
√
b
√
a
ðsin(x2)ðdx= ˚
b
a
ðsinyð dy
2√y
= ˚
b
a
ðsinyð
2√y
dy
which means that fora=ak =k andb=bk =(k+1) =ak+1 the values∫
√ak+1
√ak
ðsin(x2)ðdx
are a decreasing sequence with limit0. Since on√ak,√ak+1
 the functionsinx2 has only one
148

Solution Manual. Last update 18th July 2019
sign (and alternates its sign from interval to interval), we can use Leibniz’ convergence criterion
to see that the series
É
k ˚
√ak+1
√ak
sin(x2)dx (*)
converges, hence the improper integral exists.
Thefunction cosx2 canbetreatedsimilarly. Alternatively,weremarkthat sinx2=cos(x2−∕2).
The functions are not Lebesgue integrable. Either we show that the series (*) does not converge
absolutely, or we argue as follows:
sinx2=cos(x2−∕2)showsthat ∫ ðsinx2ðdx and ∫ ðcosx2ðdx eitherbothconvergeordiverge.
If they would converge (this is equivalent to Lebesgue integrability...) we would ﬁnd because of
sin2+cos2 ≡1 andðsinð,ðcosð ⩽1,
∞= ˚
∞
0
1dx= ˚
∞
0
(sinx2)2+(cos x2)2dx
= ˚
∞
0
(sinx2)2dx+ ˚
∞
0
(cosx2)2dx
⩽ ˚
∞
0
ðsinx2ðdx+ ˚
∞
0
ðcosx2ðdx < ∞,
which is a contradiction.
■■
Problem 12.37 Solution: Letr < sand, without loss of generality,a ⩽ b. A change of variables
yields
˚
s
r
f(bx)− f(ax)
x dx= ˚
s
r
f(bx)
x dx− ˚
s
r
f(ax)
x dx
= ˚
bs
br
f(y)
y dy− ˚
as
ar
f(y)
y dy
= ˚
bs
as
f(y)
y dy− ˚
br
ar
f(y)
y dy
Using the mean value theorem for integrals, I.12, we get
˚
s
r
f(bx)− f(ax)
x dx=f(s) ˚
bs
as
1
ydy−f(r) ˚
br
ar
1
ydy
=f(s)ln b
a−f(r)ln b
a.
Sinces∈(as,bs)andr∈(ar,br), we ﬁnd thats , , , , , , , , , , , , , , , , , , , , →
s→∞
∞andr , , , , , , , , , , , , , , , , →
r→0
0 which means that
˚
s
r
f(bx)− f(ax)
x dx= f(s)− f(r)ln b
a
s→∞
, , , , , , , , , , , , , , , , , , , , , , , , →
r→0
(M−m)ln b
a.
■■
149



13 The function spaces p.
Solutions to Problems 13.113.26
Problem 13.1 Solution:
(i) We use Hölder’s inequality forr,s ∈(1,∞)and 1
s + 1
t =1 to get
‖u‖q
q = ˚ ðuðqd = ˚ ðuðq⋅ 1d
⩽
0
˚ ðuðqrd
11∕r
⋅
0
˚ 1sd
11∕s
=
0
˚ ðuðqrd
11∕r
⋅((X))1∕s.
Now let us chooserands. We take
r= p
q >1 - ⇒1
r = q
p and 1
s =1− 1
r =1− q
p,
hence
‖u‖q =
0
˚ ðuðpd
1q∕p⋅1∕q
⋅((X))(1−q∕p)(1∕q)
=
0
˚ ðuðpd
1q∕p⋅1∕q
⋅((X))1∕q−1∕p
= ‖u‖p⋅((X))1∕q−1∕p.
(ii) Ifu∈ p we know thatuis measurable and‖u‖p<∞. The inequality in (i) then shows that
‖u‖q ⩽ const⋅‖u‖p<∞,
henceu∈ q. This givesp⊂ q. The inclusionq ⊂ 1 follows by takingp ⇝q,q ⇝1.
Let(un)n∈N⊂ p beaCauchysequence,i.e. limm,n→∞‖un−um‖p=0 . Sincebytheinequal-
ity in (i) also
lim
m,n→∞
‖un−um‖q ⩽(X)1∕q−1∕p lim
m,n→∞
‖un−um‖p=0
we get that(un)n∈N⊂ q is also a Cauchy sequence inq.
(iii) No, the assertion breaks down completely if the measure has inﬁnite mass. Here is an
example:  = Lebesgue measure on(1,∞). Then the functionf(x) =1
x is not integrable
over[1,∞), butf2(x) = 1
x2 is. In other words:f ∉ 1(1,∞) butf ∈ 2(1,∞), hence
2(1,∞)⊄ 1(1,∞). (Playingaroundwithdiﬀerentexponentsshowsthattheassertionalso
fails for otherp,q ⩾1....).
151

R.L. Schilling: Measures, Integrals & Martingales
■■
Problem 13.2 Solution: This is going to be a bit messy and rather than showing the ‘streamlined’
solution we indicate how one could ﬁnd out the numbers oneself. Now let be some number in
(0,1) and let, be conjugate indices: 1
 + 1
 = 1where , ∈ (1,∞). Then by the Hölder
inequality
˚ ðuðrd = ˚ ðuðrðuðr(1−)d
⩽
0
˚ ðuðrd
11

0
˚ ðuðr(1−)d
11

=
0
˚ ðuðrd
1 r
r
0
˚ ðuðr(1−)d
1 r(1−)
r(1−)
.
Takingrth roots on both sides yields
‖u‖r ⩽
0
˚ ðuðrd
1 
r
0
˚ ðuðr(1−)d
1 (1−)
r(1−)
= ‖u‖
r‖u‖1−
r(1−).
This leads to the following system of equations:
p=r, q =r(1− ), 1= 1
 + 1

with unknown quantities,, . Solving it yields
=
1
r − 1
q
1
p− 1
q
,  = q−p
q−r = q−p
r−p.
■■
Problem 13.3 Solution:
(i) Ifu,v ∈ p(),then u+vanduareagainin p();thisfollowsfromthehomogeneity
oftheintegralandMinkowski’sinequality(Corollary13.4. UsingtheCauchy–Schwarz
inequality, the productuv is in p(), ifu,v ∈ 2p(). More generally: if there are
conjugate numbers, ∈[1,∞] (i.e.−1+−1=1 ), such thatu∈ p andv∈ p,
thenuv∈ p().
(ii) Consider the measure space((0,1),ℬ(0,1),) and setu(x) ∶=v(x) ∶=x−1∕3. This
gives
˚
1
0
ðu(x)ð2dx= ˚
1
0
x−2∕3dx=3 x1∕31
x=0=3 <∞,
i.e.u,v ∈ 2(). On the other hand,u⋅v∉ 2()as
˚
1
0
ðu(x)v(x)ð2dx= ˚
1
0
x−4∕3dx=lim
r→0
−3x−1∕31
x=r=∞.
This proves that2() is not an algebra. Deﬁne u∶=u2 and v∶=v2, we get a similar
counterexample which works in1().
152

Solution Manual. Last update 18th July 2019
(iii) From Minkowski’s inequality we get
‖u‖p= ‖(u−v)+ v‖p ⩽ ‖u−v‖p+‖v‖p
- ⇒‖u‖p−‖v‖p ⩽ ‖u−v‖p.
If we change the rôles ofuandv, we obtain
‖v‖p−‖u‖p ⩽ ‖v−u‖p= ‖u−v‖p
and, therefore,
óóó‖u‖p−‖v‖p
óóó=max{ ‖u‖p−‖v‖p,‖v‖p−‖u‖p} ⩽ ‖u−v‖p.
■■
Problem 13.4 Solution:
(i) We consider the three cases separately.
(a) Every mapu∶(Ω,{ç,Ω}) →(R,{ç, R}) is measurable.Indeed: u is measurable if,
and only if,u−1(A)∈{ç ,Ω}for allA∈A ={ç, R}. Since
u−1(ç)=ç u−1(R)=Ω
this is indeed true for any mapu.
(b) Every measurable mapu∶(Ω,{ç,Ω}) →(R,ℬ(R)) is constantIndeed: Suppose,u
is not constant, i.e. there are!1,!2 ∈ Ωandx,y ∈ R,x ≠ y, such thatu(!1) =x,
u(!2) =y. Thenu−1({x}) ∉ {ç,Ω} as!1 ∈ u−1({x}) (and sou−1({x}) ≠ ç) and
!2∉u−1({x}) (and sou−1({x}) ≠Ω).
(c) Everymeasurablemap u∶(Ω,{ç,Ω}) →(R,P(R))isclearly{ç,Ω}∕ℬ(R)-measurable.
From(b)weknowthatsuchfunctionsareconstant. Ontheotherhand,constantmaps
are measurable for any-algebra. Therefore, every{ç,Ω}∕P(R)-measurable map is
constant.
(ii) We determine ﬁrst the(B)-measurable maps. We claim: every(B)∕ℬ(R)-measurable
map is of the form
u(!)= c11B(!)+ c21Bc(!), ! ∈Ω, (⋆)
forc1,c2∈ R. Indeed: Ifu is given by (⋆), then
u−1(A)=
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪⎩
Ω, c 1,c2∈A,
B, c 1∈A,c2∉A,
Bc, c 1∉A,c2∈A,
ç, c 1,c2∉A
153

R.L. Schilling: Measures, Integrals & Martingales
for anyA ∈ ℬ(R). Therefore, u is(B)∕ℬ(R)-measurable. Conversely, assume that
the functionu is (B)∕ℬ(R)-measurable. Choose any!1 ∈ B, !2 ∈ Bc and deﬁne
c1 = u(!1),c2 = u(!2). Ifu were not of the form (⋆), then there would be some!∈ Ω
such thatu(!) ∉ {c1,c2}. In this caseA ∶= {u(!)} satisﬁesu−1(A) ∉ {ç,Ω,B,B c},
contradicting the measurability ofu.
By deﬁnition,
p(Ω,(B),)=
<
u∶(Ω,(B)) →(R,ℬ(R))messbar∶ ˚ ðuðpd< ∞
=
.
We have already shown that the(B)-measurable maps are given by (⋆). Because of the
linearity of the integral we see that
˚ ðuðpd = ðc1ðp(B)+ ðc2ðp(Bc).
Consequently,u∈ p(Ω,(B),)if, and only if,
• c1=0 or(B)<∞
• c2=0 or(Bc)<∞.
In particular, every map of the form (⋆) is inp(Ω,(B),)if is a ﬁnite measure.
■■
Problem 13.5 Solution: Proof by induction inN.
StartN =2 : this is just Hölder’s inequality.
Hypothesis: the generalized Hölder inequality holds for someN ⩾2.
StepN ⇝ N +1 :. Letu1,…,uN,w beN +1 functions and letp1,…,pN,q >1 be such that
p−1
1 +p−1
2 +…+ p−1
N +q−1=1 . Setp−1∶=p−1
1 +p−1
2 +…+ p−1
N . Then, by the ordinary Hölder
inequality,
˚ ðu1⋅u2⋅…⋅uN⋅wðd ⩽
0
˚ ðu1⋅u2⋅…⋅uNðpd
11∕p
‖u‖q
=
0
˚ ðu1ðp⋅ðu2ðp⋅…⋅ðuNðpd
11∕p
‖u‖q
Now use the induction hypothesis which allows us to apply the generalized Hölder inequality for
N (!) factorsj ∶=pj∕p, and thus∑N
j=1−1
j =p∕p=1 , to the ﬁrst factor to get
˚ ðu1⋅u2⋅…⋅uN⋅wðd =
0
˚ ðu1ðp⋅ðu2ðp⋅…⋅ðuNðpd
11∕p
‖u‖q
⩽ ‖u‖p1⋅‖u‖p2⋅…⋅‖u‖pN‖u‖q.
■■
154

Solution Manual. Last update 18th July 2019
Problem 13.6 Solution: Draw a picture similar to the one used in the proof of Lemma 13.1 (note
that the increasing function need not be convex or concave....). Without loss of generality we can
assume thatA,B >0 are such that(A) ⩾B which is equivalent toA ⩾ (B) since and are
inverses. Thus,
AB= ˚
B
0
 ()d+ ˚
 (B)
0
()d+ ˚
A
 (B)
Bd.
Using the fact thatincreases, we get that
( (B))= B - ⇒(C) ⩾B ∀C ⩾ (B)
and we conclude that
AB= ˚
B
0
 ()d+ ˚
 (B)
0
()d+ ˚
A
 (B)
Bd
⩽ ˚
B
0
 ()d+ ˚
 (B)
0
()d+ ˚
A
 (B)
()d
= ˚
B
0
 ()d+ ˚
A
0
()d
=Ψ(B)+Φ( A).
■■
Problem 13.7 Solution: Let us show ﬁrst of all thatp-limk→∞uk = u. This follows immediately
fromlimk→∞‖u−uk‖p=0 since the series∑∞
k=1‖u−uk‖p converges.
Therefore, we can ﬁnd a subsequence(uk(j))j∈N such that
lim
j→∞
uk(j)(x)= u(x) almost everywhere.
Now we want to show thatu is the a.e. limit of the original sequence. For this we mimic the trick
from the Riesz–Fischer theorem 13.7 and show that the series
∞É
j=0
(uj+1−uj)= lim
K→∞
KÉ
j=0
(uj+1−uj)= lim
K→∞
uK
(again we agree onu0 ∶= 0for notational convenience) makes sense. So let us employ Lemma
13.6 used in the proof of the Riesz–Fischer theorem to get
ôôôôôô
∞É
j=0
(uj+1−uj)
ôôôôôôp
⩽
ôôôôôô
∞É
j=0
ðuj+1−ujð
ôôôôôôp
⩽
∞É
j=0
‖uj+1−uj‖p
⩽
∞É
j=0
 ‖uj+1−u‖p+‖u−uj‖p

<∞
155

R.L. Schilling: Measures, Integrals & Martingales
whereweuseMinkowski’sinequality,thefunction ufromaboveandthefactthat ∑∞
j=1‖uj−u‖p<
∞ along with‖u1‖p <∞. This shows thatlimK→∞uK(x)= ∑∞
j=0(uj+1(x)− uj(x)) exists almost
everywhere.
We still have to show thatlimK→∞uK(x) =u(x). For this we remark that a subsequence has
necessarily the same limit as the original sequence—whenever both have limits, of course. But
then,
u(x)= lim
j→∞
uk(j)(x)= lim
k→∞
uk(x)=
∞É
j=0
(uj+1(x)− uj(x))
and the claim follows.
■■
Problem 13.8 Solution: That for every ﬁxedxthe sequence
un(x)∶= n1(0,1∕n)(x) , , , , , , , , , , , , , , , , , , , , →
n→∞
0
is obvious. On the other hand, for any subsequence(un(j))j we have
˚ ðun(j)ðpd=n(j)p 1
n(j) =n(j)p−1 , , , , , , , , , , , , , , , , , , , , →
j→∞
c
withc=1 incase p=1 andc=∞ ifp> 1. Thisshowsthatthe p-limitofthissubsequence—let
us call itw if it exists at all—cannot be (not even a.e.)u=0 .
Ontheotherhand,weknowthatasub-subsequence ( uk(j))j of(uk(j))j convergespointwisealmost
everywhere to thep-limit:
lim
j
 uk(j)(x)= w(x).
Since the full sequencelimnun(x) =u(x) = 0has a limit, this shows that the sub-sub-sequence
limitw(x)=0 almost everywhere—a contradiction. Thus,wdoes not exist in the ﬁrst place.
■■
Problem 13.9 Solution: Using Minkowski’s and Hölder’s inequalities we ﬁnd for all >0
‖ukvk−uv‖1= ‖ukvk−ukv+ukv−uv‖
⩽ ‖uk⋅(vk−v)‖+‖(uk−u)v‖
⩽ ‖uk‖p‖vk−v‖q+‖uk−u‖p‖v‖q
⩽(M+‖v‖q)
for alln ⩾ N. We use here that the sequence(‖uk‖p)k∈N is bounded. Indeed, by Minkowski’s
inequality
‖uk‖p= ‖uk−u‖p+‖u‖p ⩽+‖u‖p=∶M.
■■
156

Solution Manual. Last update 18th July 2019
Problem 13.10 Solution: We use the simple identity
‖un−um‖2
2= ˚ (un−um)2d
= ˚ (u2
n−2unum+um)d
= ‖un‖2
2+‖um‖2
2−2 ˚ unumd.
(*)
Case1: un →uin 2. Thismeansthat (un)n∈N isan 2 Cauchysequence,i.e.that limm,n→∞‖un−
um‖2
2=0 . On the other hand, we get from the lower triangle inequality for norms
lim
n→∞
óó‖un‖2−‖u‖2óó ⩽ lim
n→∞
‖un−u‖2=0
so that alsolimn→∞‖un‖2
2=lim m→∞‖um‖2
2= ‖u‖2
2. Using (*) we ﬁnd
2 ˚ unumd = ‖un‖2
2+‖um‖2
2−‖un−um‖2
2
, , , , , , , , , , , , , , , , , , , , , , , , , , , , →
n,m→∞
‖u‖2
2+‖u‖2
2−0
=2 ‖u‖2
2.
Case 2:Assume thatlimn,m→∞ ∫ unumd =c for some numberc∈ R. By the very deﬁnition of
this double limit, i.e.
∀ >0 ∃ N ∈ N ∶ óóóó˚ unumd−cóóóó
< ∀n,m ⩾N,
weseethat limn→∞ ∫ unund =c=lim m→∞ ∫ umumd hold(withthesame c!). Therefore,again
by (*), we get
‖un−um‖2
2= ‖un‖2
2+‖um‖2
2−2 ˚ unumd
, , , , , , , , , , , , , , , , , , , , , , , , , , , , →
n,m→∞
c+c−2c = 0,
i.e.(un)n∈N is a Cauchy sequence in2 and has, by the completeness of this space, a limit.
■■
Problem 13.11 Solution: Use the exponential series to conclude from the positivity ofℎ andu(x)
that
exp(ℎu)=
∞É
j=0
ℎjuj
j! ⩾ ℎN
N!uN.
Integrating this gives
ℎN
N! ˚ uNd ⩽ ˚ exp(ℎu)d< ∞
and we ﬁnd thatu∈ N. Since is a ﬁnite measure we know from Problem 13.1 that forN >p
we haveN ⊂ p.
■■
157

R.L. Schilling: Measures, Integrals & Martingales
Problem 13.12 Solution:
(i) We have to show thatðun(x)ðp ∶= np(x+n)−p has ﬁnite integral—measurability is clear
sinceun iscontinuous. Sincenp isaconstant,wehaveonlytoshowthat (x+n)−p isin 1.
Set ∶=p >1. Then we get from a Beppo Levi and a domination argument
˚(0,∞)
(x+n)−(dx) ⩽ ˚(0,∞)
(x+1)−(dx)
⩽ ˚(0,1)
1(dx)+ ˚(1,∞)
(x+1)−(dx)
⩽1+ lim
k→∞ ˚(1,k)
x−(dx).
Now using that Riemann=Lebesgue on intervals where the Riemann integral exists, we get
lim
k→∞ ˚(1,k)
x−(dx)= lim
k→∞ ˚
k
1
x−dx
= lim
k→∞
(1− )−1x1−k
1
=(1− )−1 lim
k→∞
 k1−−1
=(−1)−1 < ∞
which shows that the integral is ﬁnite.
(ii) We have to show thatðvn(x)ðq ∶= nqe−qnx is in 1—again measurability is inferred from
continuity. Sincenq is a constant, it is enough to show thate−qnx is integrable. Set=qn.
Since
lim
x→∞
(x)2e−x =0 and e−x ⩽1 ∀ x ⩾0,
and sincee−x is continuous on[0,∞), we conclude that there are constantsC,C() such
that
e−x ⩽min
<
1, C
(x)2
=
⩽C()min
$
1, 1
x2
%
=C()

1(0,1)(x)+ 1[1,∞)
1
x2

but the latter is an integrable function on(0,∞).
■■
Problem 13.13 Solution: Without loss of generality we may assume that ⩽ . We distinguish
between the casex∈(0,1)andx∈[1,∞). Ifx ⩽1, then
1
x ⩾ 1
x+x ⩾ 1
x+x = 1∕2
x+x ∀x ⩽1;
this shows that(x+x)−1 is in1((0,1),dx)if, and only if, <1.
158

Solution Manual. Last update 18th July 2019
Similarly, ifx ⩾1, then
1
x ⩾ 1
x+x ⩾ 1
x+x = 1∕2
x+x ∀x ⩾1
this shows that(x+x)−1 is in1((1,∞),dx)if, and only if, >1.
Thus,(x+x)−1 is in1(R,dx)if, and only if, both <1 and >1.
■■
Problem 13.14 Solution: If we useX={1,2,…,n},x(j)= xj,=1+⋯+n we have
0 nÉ
j=1
ðxjðp
11∕p
= ‖x‖p()
and it is clear that this is a norm forp ⩾ 1 and, in view of Problem 13.19 it is not a norm for
p < 1 since the triangle (Minkowski) inequality fails. (This could also be shown by a direct
counterexample.
■■
Problem 13.15 Solution: Withoutlossofgeneralitywecanrestrictourselvestopositivefunctions—
else we would consider positive and negative parts. Separability can obviously considered separ-
ately!
Assumethat 1
+ isseparableandchoose u∈ p
+. Thenup∈ 1 and,becauseofseparability,there
is a sequence(fn)n⊂D1⊂ 1 such that
fn
in 1
, , , , , , , , , , , , , , , , , , , , →
n→∞
up - ⇒up
n
in 1
, , , , , , , , , , , , , , , , , , , , →
n→∞
up
ifweset un∶=f1∕p
n ∈ p. Inparticular,un(k)(x) →u(x)almosteverywhereforsomesubsequence
and‖un(k)‖p , , , , , , , , , , , , , , , , , , , , →
k→∞
‖u‖p. Thus, Riesz’s theorem 13.10 applies and proves that
p∋un(k)
in p
, , , , , , , , , , , , , , , , , , , , , →
k→∞
u.
Obviously the separating setDp is essentially the same asD1, and we are done.
The converse is similar (note that we did not make any assumptions onp ⩾ 1 orp <1—this is
immaterial in the above argument).
■■
Problem 13.16 Solution: We have seen in the lecture that, wheneverlimn→∞‖u−un‖p = 0, there
isasubsequence un(k) suchthat limk→∞un(k)(x)= u(x)almosteverywhere. Since,byassumption,
limj→∞uj(x) =w(x) a.e., we have also thatlimj→∞un(j)(x) =w(x) a.e., henceu(x) =w(x)
almost everywhere.
■■
159

R.L. Schilling: Measures, Integrals & Martingales
Problem 13.17 Solution: We remark thaty → logy is concave. Therefore, we can use Jensen’s
inequality for concave functions to get for the probability measure∕(X)= (X)−11X
˚ (logu) d
(X) ⩽log
0
˚ u d
(X)
1
=log
H
∫ ud
(X)
I
=log
0
1
(X)
1
,
and the claim follows.
■■
Problem 13.18 Solution: As a matter of fact,
˚(0,1)
u(s)ds⋅ ˚(0,1)
logu(t)dt ⩽ ˚(0,1)
u(x)log u(x)dx.
We begin by proving the hint.logx ⩾0 ⇐ ⇒x ⩾1. So,
∀y ⩾1∶

logy ⩽ylogy ⇐ ⇒1 ⩽y

and ∀y ⩽1∶

logy ⩽ylogy ⇐ ⇒1 ⩾y

.
Assume now that∫(0,1)u(x)dx =1 . Substituting in the above inequalityy=u(x) and integrating
over(0,1) yields
˚(0,1)
logu(x)dx ⩽ ˚(0,1)
u(x)log u(x)dx.
Now assume that= ∫(0,1)u(x)dx. Then∫(0,1)u(x)∕dx =1 and the above inequality gives
˚(0,1)
logu(x)
 dx ⩽ ˚(0,1)
u(x)
 logu(x)
 dx
which is equivalent to
˚(0,1)
logu(x)dx−log 
= ˚(0,1)
logu(x)dx− ˚(0,1)
logdx
= ˚(0,1)
logu(x)
 dx
⩽ ˚(0,1)
u(x)
 logu(x)
 dx
= 1
 ˚(0,1)
u(x)log u(x)
 dx
= 1
 ˚(0,1)
u(x)log u(x)dx− 1
 ˚(0,1)
u(x)log dx
= 1
 ˚(0,1)
u(x)log u(x)dx− 1
 ˚(0,1)
u(x)dxlog
160

Solution Manual. Last update 18th July 2019
= 1
 ˚(0,1)
u(x)log u(x)dx−log .
The claim now follows by addinglog on both sides and then multiplying by= ∫(0,1)u(x)dx.
■■
Problem 13.19 Solution:
(i) Letp∈(0,1)andpicktheconjugateindex q∶=p∕(p−1)<0. Moreover,s∶=1∕p∈(1,∞)
and the conjugate indext, 1
s + 1
t =1 , is given by
t= s
s−1 =
1
p
1
p−1
= 1
1− p ∈(1,∞).
Thus, using the normal Hölder inequality fors,t we get
˚ upd = ˚ upwp
wpd
⩽
0
˚
 upwps
d
11∕s0
˚ w−pt d
11∕t
=
0
˚ uw d
1p0
˚ wp∕(p−1) d
11−p
.
Takingpth roots on either side yields
0
˚ upd
11∕p
⩽
0
˚ uw d
10
˚ wp∕(p−1) d
1(1−p)∕p
=
0
˚ uw d
10
˚ wq d
1−1∕q
and the claim follows.
(ii) This‘reversed’Minkowskiinequalityfollowsfromthe‘reversed’Hölderinequalityinexactly
thesamewayasMinkowski’sinequalityfollowsfromHölder’sinequality,cf.Corollary13.4.
To wit:
˚ (u+v)pd = ˚ (u+v)⋅(u+v)p−1d
= ˚ u⋅(u+v)p−1d+ ˚ v⋅(u+v)p−1d
(i)
⩾ ‖u‖p⋅ôôô(u+v)p−1ôôôq
+‖v‖p⋅ôôô(u+v)p−1ôôôq
.
Dividing both sides by‖ðu+vðp−1‖q proves our claim since
ôôô(u+v)p−1ôôôq
=
0
˚ (u+v)(p−1)qd
11∕q
=
0
˚ (u+v)pd
11−1∕p
.
■■
Problem 13.20 Solution: By assumption,ðuð ⩽ ‖u‖∞ ⩽C <∞andu ≢0.
161

R.L. Schilling: Measures, Integrals & Martingales
(i) We have
Mn= ˚ ðuðnd ⩽Cn
˚ d =Cn(X)∈(0 ,∞).
Note thatMn>0.
(ii) By the Cauchy–Schwarz-Inequality,
Mn= ˚ ðuðnd
= ˚ ðuð
n+1
2 ðuð
n−1
2 d
⩽
0
˚ ðuðn+1d
11∕20
˚ ðuðn−1d
11∕2
=
√
Mn+1Mn−1.
(iii) The upper estimate follows from
Mn+1= ˚ ðuðn+1d ⩽ ˚ ðuðn⋅‖u‖∞d = ‖u‖∞Mn.
SetP ∶=∕(X); the lower estimate is equivalent to
0
˚ ðuðn d
(X)
11∕n
⩽
∫ ðuðn+1 d
(X)
∫ ðuðn d
(X)
⇐ ⇒
0
˚ ðuðndP
11+1∕n
⩽ ˚ ðuðn+1dP
⇐ ⇒
0
˚ ðuðndP
1(n+1)∕n
⩽ ˚ ðuðn+1dP
and the last inequality follows easily from Jensen’s inequality sinceP is a probability meas-
ure:
0
˚ ðuðndP
1(n+1)∕n
˚ ðuðn⋅n+1
n dP = ˚ ðuðn+1dP.
(iv) Following the hint we get
‖u‖n ⩾

u> ‖u‖∞−1∕n ‖u‖∞− n→∞
, , , , , , , , , , , , , , , , , , , , →
→0
‖u‖∞,
i.e.
liminf
n→∞
‖u‖n ⩾ ‖u‖∞.
Combining this with the estimate from (iii), we get
‖u‖∞ ⩽liminf
n→∞
(X)−1∕n‖u‖n
(iii)
⩽ liminf
n→∞
Mn+1
Mn
⩽limsup
n→∞
Mn+1
Mn
⩽ ‖u‖∞.
162

Solution Manual. Last update 18th July 2019
■■
Problem 13.21 Solution: The hint says it all.... Maybe, you have a look at the specimen solution of
Problem 13.20, too.
Case 1:‖u‖L∞ <∞. ForA ∶={u ⩾ ‖u‖∞−}, >0, we gave(A)>0and
‖u‖p ⩾
0
˚A
(‖u‖∞−)pd
11
p
=( ‖u‖∞−)(A)
1
p.
Therefore,
liminf
p→∞
‖u‖p ⩾liminf
n→∞
0
(‖u‖∞−)(A)
1
p
1
= ‖u‖∞−.
Since >0 is arbitrary, this shows thatliminf p→∞‖u‖p ⩾ ‖u‖∞.
On the other hand, we have forp>q
˚ ðu(x)ðpd = ˚ ðu(x)ðp−qðu(x)ðqd ⩽ ‖u‖p−q
∞ ‖u‖q
q.
Takingpth roots on both sides of the inequality, we get
limsup
p→∞
‖u‖p ⩽limsup
p→∞
0
‖u‖
p−q
p
∞ ‖u‖
q
p
q
1
= ‖u‖∞.
This ﬁnishes the proof for all‖u‖L∞ <∞.
Case 2:‖u‖L∞ =∞ . The estimate
limsup
p→∞
‖u‖p ⩽ ‖u‖∞
is trivially true. The converse inequality follows like this: DeﬁneAR ∶= {u ⩾ R},R >0. We
have(Ar)>0(otherwise ‖u‖L∞ <∞!) and, as in the ﬁrst part of the proof, we ﬁnd
‖u‖p ⩾
0
˚AR
Rpd
11
p
=R(AR)
1
p.
Thus,liminf p→∞‖u‖p ⩾Rand sinceR> 0 is arbitrary, the claim follows:
liminf
p→∞
‖u‖p ⩾∞= ‖u‖∞.
■■
Problem 13.22 Solution: We begin with two observations
• Ifr ⩽s ⩽q, then‖u‖r ⩽ ‖u‖s. This follows from Jensen’s inequality (Theorem 13.13) and
thefactthat V(x)∶= xs∕r,x∈ R,isconvex(cf.alsoProblem13.1). Inparticular, ‖u‖r<∞
for allr∈(0,q).
163

R.L. Schilling: Measures, Integrals & Martingales
• We have
˚ logðuðd ⩽log‖u‖p ∀p∈(0,q). (⋆)
This follows againfrom Jensen’s inequality applied to theconvex functionV(x)∶=−log x:
−log
0
˚ ðuðpd
1
⩽ ˚ −log(ðuðp)d−p ˚ logðuðd;
therefore,
log‖u‖p= 1
plog
0
˚ ðuðpd
1
⩾ ˚ logðuðd.
Because of (⋆) it is enough to show thatlimp→0‖u‖p ⩽exp(∫ lnðuðd). (Note: by the monoton-
icity of‖u‖p asp ↓0we know that the limitlimp→0‖u‖p exists.) Note that
loga=inf
p>0
ap−1
p , a> 0. (⋆⋆)
(Hint: show by diﬀerentiation thatp → ap−1
p is increasing.
Usel’Hospital’sruletoshowthatlimp→0
ap−1
p =log a.) Frommonotoneconvergence(mc)weget
˚ logðuðd
mc
= inf
p>0 ˚
ðuðp−1
p d
=inf
p>0
∫ ðuðpd−1
p
=inf
p>0
‖u‖p
p−1
p
(⋆⋆)
= log‖u‖p
for allp> 0. Lettingp →0 ﬁnishes the proof.
■■
Problem 13.23 Solution: Withoutlossofgeneralitywemayassumethat f ⩾0. Weusethefollowing
standard representation off, see (8.7):
f =
NÉ
j=0
j1Aj
with 0 = 0 < 1 < … < N < ∞ and mutually disjoint setsAj. Clearly, {f ≠ 0} =
A1⊍⋯⊍AN.
Assume ﬁrst thatf ∈ ∩ p(). Then
∞> ˚ fpd =
NÉ
j=1
p
j(Aj) ⩾
NÉ
j=1
p
1(Aj)= p
1({f ≠0});
thus({f ≠0})<∞.
Conversely, if({f ≠0})<∞, we get
˚ fpd =
NÉ
j=1
p
j(Aj) ⩽
NÉ
j=1
p
N(Aj)= p
N({f ≠0})<∞.
164

Solution Manual. Last update 18th July 2019
Sincethisintegrabilitycriteriondoesnotdependon p ⩾1,itisclearthat +∩p()= +∩1(),
and the rest follows since = +− +.
■■
Problem 13.24 Solution: (i) ⇐ ⇒(ii) and (iii)⇐ ⇒(iv), sinceΛ is concave if, and only if,V =−Λ
is convex. Moreover, (iii) generalizes (i) and (iv) gives (ii). It is, therefore, enough to verify (iii).
Sinceuis integrable and takes values in(a,b), we get
a= ˚ a(dx)< ˚ u(x)(dx)< ˚ b(dx)= b.
Thisshowsthatthel.h.S.oftheJenseninequalityiswell-deﬁned. Therestoftheproofissimilarto
theoneofTheorem13.13: takesomeaﬃne-linear l(x)= x+ ⩽V(x)–hereweonlyconsider
x∈(a,b)– and notice that
l
0
˚ ud
1
= ˚ ud += ˚ (u+)d ⩽ ˚ V(u)d.
Now go to the sup over all aﬃne-linearl belowV and the claim follows.
■■
Problem 13.25 Solution:
(i) Note thatΛ(x)= x1∕q is concave—e.g. diﬀerentiate twice and show that it is negative—and
using Jensen’s inequality for positivef,g ⩾0 yields
˚ fgd = ˚ gf−p∕q1{f ≠0}fpd
⩽ ˚ fpd
H
∫ gqf−p1{f ≠0}fpd
∫ fpd
I1∕q
⩽
0
˚ fpd
11−1∕q0
˚ gqd
11∕q
where we use1{f ≠0} ⩽1 in the last step.
Note thatfg ∈ 1 follows from the fact that gqf−p1{f ≠0}
fp=gq ∈ 1.
(ii) The functionΛ(x)=( x1∕p+1)p has second derivative
Λ‡‡(x)= 1− p
p
 1+ x−1∕px−1−1∕p ⩽0
showing thatΛis concave. Using Jensen’s inequality gives forf,g ⩾0
˚ (f+g)p1{f ≠0}d = ˚
g
f 1{f ≠0}+1
p
fp1{f ≠0}d
⩽ ˚{f ≠0}
fpd
L0 ∫ gp1{f ≠0}d
∫{f ≠0}fpd
11∕p
+1
Mp
=
40
˚{f ≠0}
gpd
11∕p
+
0
˚{f ≠0}
fpd
11∕p5p
.
165

R.L. Schilling: Measures, Integrals & Martingales
Adding on both sides∫{f=0}(f +g)pd = ∫{f=0}gpd yields, because of the elementary
inequalityAp+Bp ⩽(A+B)p,A,B ⩾0, p⩾1,
˚ (f+g)pd
⩽
40
˚{f ≠0}
gpd
11∕p
+
0
˚{f ≠0}
fpd
11∕p5p
+
4
˚{f=0}
gpd
5p∕p
⩽
40
˚ gpd
11∕p
+
0
˚ fpd
11∕p5p
.
■■
Problem 13.26 Solution: Using Hölder’s inequality we get
ðf−aðp ⩽(ðfð+ðað)p=(1 ⋅ðfð+1 ⋅ðað)p ⩽2p−1(ðfðp+ðaðp).
Since(X)<∞, this shows that both sides of the asserted integral inequality are ﬁnite.
Withoutlossofgeneralitywemayassumethat a> 0,otherwisewewouldconsider −f insteadof
f.
Without loss of generality we may assume thatm = ∫ fd = 0, otherwise we would consider
f− ∫ fd instead off.
Observe that
˚{0<f<2a}
ðfðpd ⩽(2a)p−1
˚{0<f<2a}
ðfðd
⩽(2a)p−1
˚{f>0}
ðfðd
=(2a)p−1
˚{f<0}
ðfðd.
In the last line we use the fact that
˚{f>0}
ðfðd = ˚ f+d
∫ fd =0
= ˚ f−d = ˚{f<0}
ðfðd.
Thus,
˚{0<f<2a}
ðfðpd ⩽(2a)p−1
˚{f<0}
ðfðd
⩽2p−1
˚{f<0}
(ap∨ðfðp)d
⩽2p−1
˚{f<0}
ðf−aðpd.
(*)
Moreover,
˚{f>2a}
ðfðpd ⩽2p
˚{f>2a}
ðf−aðpd, (**)
which follows from
f >2a - ⇒ðf−að=f−a>a.
166

Solution Manual. Last update 18th July 2019
Finally,
˚{f ⩽0}
ðfðpd ⩽2p
˚{f ⩽0}
ðf−aðpd. (***)
If we combine (*)–(***) we get
˚ ðfðpd =
<
˚{f>2a}
+ ˚{0<f<2a}
+ ˚{f ⩽0}
=
ðfðpd
⩽2p
˚{f>2a}
ðf−aðpd+(2p−1+1) ˚{f ⩽0}
ðf−aðpd
⩽2p
˚ ðf−aðpd.
Solution 2 to 13.26: We need the following inequality fora,b ∈ R which follows from Hölder’s
inequality:
ða−bðp ⩽(ðað+ðbð)p=(1 ⋅ðað+1 ⋅ðbð)p ⩽2p−1(ðaðp+ðbðp).
Setb= f(x). Since(X) <∞, this shows that both sides of the claimed integral inequality are
ﬁnite.
Assume ﬁrst that(X)=1 . Then we ﬁnd
ðf(x)− mðp ⩽(ðf(x)− að+ðm−að)p
⩽2p−1ðf(x)− aðp+2p−1ðm−aðp
=2 p−1ðf(x)− aðp+2p−1óóóó˚ f(y)(dy)− aóóóó
p
=2 p−1ðf(x)− aðp+2p−1óóóó˚ (f(y)− a)(dy)óóóó
p
⩽2p−1ðf(x)− aðp+2p−1
˚ ðf(y)− aðp(dy)
by Jensen’s inequality. Now we divide by2p and integrate both sides with respect to(dx)to get
2−p
˚ ðf(x)− mðp(dx) ⩽ 1
2 ˚ ðf(x)− aðp(dx)+ 1
2 ˚ ðf(y)− aðp(dy)
which proves our claim for probability measures.
If is a general ﬁnite measure we setg∶=f− ∫ fd and use the previous estimate
˚ ðgðp d
(X) ⩽2p−1
˚ ðg−að d
(X) ∀a∈ R.
Sincea is arbitrary, we see from this
˚ ðf−mðp d
(X) ⩽2p−1
˚ ðf−bð d
(X) ∀b∈ R.
Remark: the same argument shows that we get for any convex function with the ‘doubling
property’(2x) ⩽c(x)for allx:
˚ (f−m)d ⩽c ˚ (f−a)d ∀a∈ R.
■■
167



14 Product measures and Fubini's theorem.
Solutions to Problems 14.114.20
Problem 14.1 Solution:
• We have
(x,y)∈
0˝
i
Ai
1
×B ⇐ ⇒x∈
˝
i
Ai andy∈B
⇐ ⇒∃i0∶x∈Ai0 andy∈B
⇐ ⇒∃i0∶(x,y)∈ Ai0×B
⇐ ⇒(x,y)∈
˝
i
(Ai×B).
• We have
(x,y)∈
0Ì
i
Ai
1
×B ⇐ ⇒x∈
Ì
i
Ai andy∈B
⇐ ⇒∀i∶x∈Ai andy∈B
⇐ ⇒∀i∶(x,y)∈ Ai×B
⇐ ⇒(x,y)∈
Ì
i
(Ai×B).
• Using the formulaA×B = −1
1 (A)∩ −1
2 (B) (see page 135 and the fact that inverse maps
interchange with all set operations, we get
(A×B)∩( A‡×B‡)=

−1
1 (A)∩ −1
2 (B)

∩

−1
1 (A‡)∩ −1
2 (B‡)

=

−1
1 (A)∩ −1
1 (A‡)

∩

−1
2 (B)∩ −1
2 (B‡)

=−1
1 (A∩A‡)∩ −1
2 (B∩B‡)
=(A∩A‡)×( B∩B‡).
• Using the formulaA×B = −1
1 (A)∩ −1
2 (B) (see page 135 and the fact that inverse maps
interchange with all set operations, we get
Ac×B=−1
1 (Ac)∩ −1
2 (B)
= −1
1 (A)c
∩−1
2 (B)
=−1
1 (X)∩ −1
2 (B)∩ −1
1 (A)c
169

R.L. Schilling: Measures, Integrals & Martingales
=−1
1 (X)∩ −1
2 (B)∩
$−1
1 (A)c
∪−1
2 (B)c%
=(X×B)∩ −1
1 (A)∩ −1
2 (B)c
=(X×B)∩ A×Bc
=(X×B) ⧵(A×B).
• We have
A×B ⊂A‡×B‡ ⇐ ⇒(x,y)∈ A×B - ⇒(x,y)∈ A‡×B‡
⇐ ⇒x∈A,y ∈B - ⇒x∈A‡,y ∈B‡
⇐ ⇒A⊂A ‡, B ⊂B‡.
■■
Problem 14.2 Solution: Pick two exhausting sequences(Ak)k ⊂ A and (Bk)k ⊂ ℬ such that
(Ak),(Bk)<∞andAk ↑X,Bk ↑Y. Then, because of the continuity of measures,
×(A×N)=lim
k
× (A×N)∩( Ak×Bk)
=lim
k
× (A∩Ak)×( N∩Bk)
=lim
k
(A∩Ak)
«››ﬂ››‹
<∞
⋅(N∩Bk)
«›››ﬂ›››‹
⩽(N)=0

=0.
SinceA×N ∈A ×ℬ⊂A ⊗ℬ, measurability is clear.
■■
Problem 14.3 Solution:
• (a) ⇒(b): Iff is1×2-negligible, we can use Tonelli’s theorem to infer that
0= ˚E1
0
˚E2
ðf(x1,x2)ðd2(x2)
1
d1(x1).
Using Theorem 11.2 we ﬁnd
1
0
˚E2
ðf(⋅,x2)ðd2(x2) ≠0
1
0.
This means thatf(x1,⋅)is for1-almost allx12-negligible.
• (b) ⇒(a): Set
N ∶=
<
x1∈E1; ˚E2
ðf(x1,x2)ðd2(x2) ≠0
=
.
By assumption,1(N)=0 . Therefore,
˚E1
0
˚E2
ðf(x1,x2)ðd2(x2)
1
d1(x1)= ˚N
0
˚E2
ðf(x1,x2)ðd2(x2)
1
d1(x1)
170

Solution Manual. Last update 18th July 2019
+ ˚E1⧵N
0
˚E2
ðf(x1,x2)ðd2(x2)
1
d1(x1).
The ﬁrst integral on the right-hand side is, by Theorem 11.2 equal to0. The second integral
is also0, due to the deﬁnition of the setN. Using Tonelli’s theorem we see
˚E1×E2
ðf(x1,x2)ðd1×2(x1,x2)=0 .
• (a) ⇔(c): Use the symmetry in the variables or argue as in “(a)⇔(b)”.
■■
Problem 14.4 Solution: Since the two expressions are symmetric inx andy, they must coincide if
they converge. Let us, therefore only look at the left hand side.
The inner integral,
˚(0,∞)
e−xysinx(dx)
clearly satisﬁes
˚(0,∞)
óóóe−xysinxóóó(dx) ⩽ ˚(0,∞)
e−xy(dx)
= ˚
∞
0
e−xydx
=
4
− e−xy
y
5∞
x=0
= 1
x.
Sincetheintegrandiscontinuousandhasonlyonesign,wecanuseRiemann’sintegral. Thus,the
integral exists. To calculate its value we observe that two integrations by parts yield
˚
∞
0
e−xysinxdx =−e−xycosxóóó
∞
x=0
− ˚
∞
0
ye−xycosxdx
=1− y ˚
∞
0
e−xycosxdx
=1− y
0
e−xysinxóóó
∞
x=0
+ ˚
∞
0
ye−xysinxdx
1
=1− y2
˚
∞
0
e−xysinxdx.
And if we solve this equality for the integral expression, we get
(1+ y2) ˚
∞
0
e−xysinxdx =1 - ⇒ ˚
∞
0
e−xysinxdx = 1
1+ y2.
Alternative: Sincesinx=Im eix we get
˚
∞
0
e−xysinxdx =Im ˚
∞
0
e−(y−i)xdx=Im 1
y−i =Im y+i
y2+1 = 1
y2+1 .
171

R.L. Schilling: Measures, Integrals & Martingales
Thus the iterated integral exists, since
˚(0,∞)
óóóó
sinx
1+ x2
óóóó
dx ⩽ ˚(0,∞)
1
1+ x2dx=arctan xóóó
∞
0
= 
2.
(Here we use again that improper Riemann integrals with positive integrands coincide with Le-
besgue integrals.)
In principle, the existence and equality of iterated integrals is not good enough to guarantee the
existenceofthedoubleintegral. Forthisoneneedstheexistenceofthe absoluteiteratedintegrals—
cf.Tonelli’stheorem14.8. Inthepresentcaseonecanseethattheabsoluteiteratedintegralsexist,
though:
On the one hand we ﬁnd
˚(0,∞)
e−xyðsin(x)ð(dx) ⩽ e−xy
−y
óóóó
∞
0
= 1
y
and siny
y is, as a bounded continuous function, Lebesgue integrable over(0,1).
On the other hand we can use integration by parts to get
˚
(k+1)
k
e−xysinxdx = e−xy
−y sinxóóó
(k+1)
k
− ˚
(k+1)
k
e−xy
−y cosxdx
= e−xy
−y2 cosxóóó
(k+1)
k
− ˚
(k+1)
k
e−xy
−y2(−1)sin xdx
which is equivalent to
y2+1
y2 ˚
(k+1)
k
e−xysinxdx = e−(k+1)y
−y2 (−1)k+1− e−ky
−y2 (−1)k
= (−1)k
y2 (e−(k+1)y+e−ky),
i.e. ∫ (k+1)
k e−xysinxdx =(−1) k 1
y2+1(e−(k+1)y+e−ky).
Now we ﬁnd a bound fory∈(1,∞).
˚(0,∞)
e−xyðsin(x)ðdx=
∞É
k=0 ˚
(k+1)
k
e−xysinx(−1)kdx
=
∞É
k=0
(−1)k(−1)k 1
y2+1(e−(k+1)y+e−ky)
⩽ 2
y2+1
∞É
k=0
(e−y)k
y>1
⩽ 2
y2+1
∞É
k=0
(e−)k
which means that the left hand side is integrable over(1,∞).
Thus we have
˚(0,∞) ˚(0,∞)
ðe−xysinxsinyð(dx)(dy)
172

Solution Manual. Last update 18th July 2019
⩽ ˚(0,1]
siny
y (dy)+ ˚(1,∞)
2
y2+1 (dy)
∞É
k=0
(e−)k
<∞.
By Fubini’s theorem we know that the iterated integrals as well as the double integral exist and
their values are identical.
Alternative proof for the absolute convergence of the integral:1 Let
f(x,y)= e−xyðsinxsinyð ⩾0 ∀x,y ⩾0.
By monotone convergence and Tonelli’s theorem
¸ f(x,y)dxdy = lim
A,B→∞ ¸(0,A]×(0,B]
f(x,y)dxdy
= sup
A,B⩾0 ˚(0,A] ˚(0,B]
f(x,y)dydx.
Since the integrands are bounded and continuous, we can use Riemann integrals. FixA >1 and
B >1.Then
˚
A
0 ˚
B
0
= ˚
1
0 ˚
1
0
+ ˚
1
0 ˚
B
1
+ ˚
1
0 ˚
A
1
+ ˚
A
1 ˚
B
1
Now we can estimate these expressions separately: sinceðsintð ⩽ ðtð we have
˚
1
0 ˚
1
0
f(x,y)dydx ⩽ ˚
1
0 ˚
1
0
1dxdy =1.
˚
1
0 ˚
B
1
f(x,y)dydx ⩽ ˚
B
1
L
˚
1
0
xe−xydx
M
dy
=1− 1
e + e−B−1
B <1− 1
e.
˚
1
0 ˚
A
1
f(x,y)dxdy ⩽ ˚
A
1
L
˚
1
0
ye−xydy
M
dx
=1− 1
e + e−A−1
A <1− 1
e.
˚
A
1 ˚
B
1
f(x,y)dxdy ⩽ ˚
B
1
4
˚
A
1
xe−xydx
5
dy
= 1
e −e−A+ e−AB−e−B
B < 1
e.
These estimates now show
˚
∞
0 ˚
∞
0
e−xyðsinxsinyð dxdy ⩽3− 1
e.
■■
1This much more elegant proof was communicated to me in July 2012 by Alvaro H. Salas from the Universidad Nacional de
Colombia, Department of Mathematics
173

R.L. Schilling: Measures, Integrals & Martingales
Problem 14.5 Solution: Note that
d
dy
y
x2+y2 = x2−y2
(x2+y2)2.
Thus we can compute
˚(0,1) ˚(0,1)
x2−y2
(x2+y2)2dydx = ˚(0,1)
1
x2+1 dx=arctan xóóó
1
0
= 
4.
By symmetry ofxandyin the integrals it follows that
˚(0,1) ˚(0,1)
y2−x2
(x2+y2)2dydx =− 
4
andthereforethedoubleintegralcannotexist. Sincetheexistencewouldimplytheequalityofthe
two above integrals. We can see this directly by
˚(0,1) ˚(0,1)
óóóóó
x2−y2
(x2+y2)2
óóóóó
dydx ⩾ ˚
1
0 ˚
x
0
x2−y2
(x2+y2)2dydx
= ˚
1
0
x
x2+x2dx
= 1
2 ˚
1
0
1
xdx=∞.
■■
Problem 14.6 Solution: Since the integrand is odd, we have fory ≠0:
˚(−1,1)
xy
(x2+y2)2 dx=0
and{0} is a null set. Thus the iterated integrals have common value0. But the double integral
does not exist, since for the iterated absolute integrals we get
˚(−1,1)
óóóó
xy
(x2+y2)2
óóóó
dx= 1
ðyð ˚
1∕ðyð
0

(2+1)2d ⩾ 2
ðyð ˚
1
0

(2+1)2d
«››››››››ﬂ››››››››‹
<∞
.
Here we use the substitutionx = ðyð and the fact thatðyð ⩽ 1, thus1∕ðyð ⩾ 1. But the outer
integral is bounded below by
˚(−1,1)
2
ðyðdy which is divergent.
■■
Problem 14.7 Solution: We use the generic notationf(x,y)for any of the integrands.
a) We have
˚
1
0
f(x,y)dy=
óóóx− 1
2
óóó
x− 1
2
3
174

Solution Manual. Last update 18th July 2019
and this function is not integrable (inx) in the interval(0,1). For0<y ⩽ 1
2 we have
˚
1
0
f(x,y)dx= ˚
1
2−y
0

x−1
2
−3
dx+ ˚
1
1
2+y

x−1
2
−3
dx=0.
For 1
2 ⩽y ⩽1 this integral is again0. Therefore,
˚
1
0
H
˚
1
0
f(x,y)dx
I
dy=0.
Finally,
˚
1
0
ðf(x,y)ðdy= óóóx− 1
2
óóó
−2
- ⇒ ˚
1
0 ˚
1
0
ðf(x,y)ðdxdy =∞.
b) We have
˚
1
0 ˚
1
0
x−y
(x2+y2)3∕2dydx = ˚
1
0
4
1
x
x+y
(x2+y2)1∕2
5y=1
y=0
dx
= ˚
1
0
L
x+1√
x2+1−1
M
dx
=
L
ln x+
√
x2+1
1+
√
x2+1−1
Mx=1
x=0
=ln2 .
Bcause of (anti-)symmetry we ﬁnd
˚
1
0 ˚
1
0
x−y
(x2+y2)3∕2dxdy =−ln2 .
Morevoer,
1
2 ˚
1
0 ˚
1
0
óóóó
x−y
(x2+y2)3∕2
óóóó
dydx = ˚
1
0 ˚
x
0
x−y
(x2+y2)3∕2dydx
= ˚
1
0
4
1
x
x−y
(x2+y2)1∕2
5y=x
y=0
dx
=(
√
2−1) ˚
1
0
dx
x
=∞.
c) Sincef is positive, Tonelli’s theorem ensures that all three integrals coincide. Letp ≠1. We
get
˚
1
0 ˚
1
0
(1− xy)−pdydy = 1
p−1 ˚
1
0
 (1− x)1−p−1 dx
x .
This integral is ﬁnite if, and only if,p< 2. Forp=1 we have
˚
1
0 ˚
1
0
(1− xy)−pdydy =− ˚
1
0
ln(1− x)dx
x <∞.
175

R.L. Schilling: Measures, Integrals & Martingales
■■
Problem 14.8 Solution:
(i) We have[−n,n] ↑ R asn →∞ and([−n,n])=2 n <∞. This shows-ﬁniteness of
. Let(qj)j∈N beanenumerationof Q; setAn∶={q1,…,qn}∪( R ⧵ Q),thenwehave
An ↑ R andQ(An)= n< ∞. This shows-ﬁniteness ofQ.
We will show thatR is not-ﬁnite. AssumeR were-ﬁnite. Thus, there would be
a sequenceAn ↑ R,n ∈ N, such thatR(An) < ∞. SinceR is a counting measure,
everyAn iscountable. Thus, Risacountableunionofcountablesets,hencecountable
– a contradiciton.
(ii) The rationalsQ are anull set, hence1
y Q is for eachyanull set. We have
˚(0,1)
1Q(x⋅y)(dx)=0 ∀ y∈ R.
This implies
˚(0,1) ˚(0,1)
1Q(x⋅y)d(x)dR(y)=0 .
(iii) Letx∈(0,1). The set(1
x Q)∩(0 ,1) contains inﬁnitely many values, so
˚(0,1)
1Q(x⋅y)R(dy)=∞ ∀ x.
Therefore, the iterated integral is∞.
(iv) Letx∈(0,1) ⧵ Q. Sincey⋅x∉ Q for anyy∈ Q, we have
˚(0,1)
1Q(x⋅y)Q(dy)=0 ∀ x∈(0,1) ⧵ Q.
On the other hand, ifx∈ Q∩(0,1), theny⋅x∈ Q for anyy∈ Q and so
˚(0,1)
1Q(x⋅y)Q(dy)=∞ ∀ x∈(0,1)∩ Q.
Since Q is anull set, we get
˚(0,1) ˚(0,1)
1Q(x⋅y)Q(dy)(dx)= ˚(0,1)
1Q(x)⋅∞d(x)=0 .
(v) The results of (iii),(iv) do not contradict Fubini’s or Tonelli’s theorem, since these the-
orems require-ﬁniteness of all measures.
■■
Problem 14.9 Solution:
(i) Since the integrand is positive, we can use Tonelli’s theorem and work out the integral
as an iterated integral
I ∶= ˚[0,∞)2
dxdy
(1+ y)(1+ x2y)
176

Solution Manual. Last update 18th July 2019
= ˚[0,∞)
1
1+ y
0
˚[0,∞)
1
1+ x2ydx
1
dy
= ˚[0,∞)
1
1+ y
arctan(x√y)
√y
óóóó
∞
x=0
dy
= 
2 ˚ [0,∞) 1
1+ y
1√y
dy.
(Observe that the integrand is continuous, which enables us to use Riemann integrals
on bounded intervals. Note that∫[0,∞)⋯=sup n∈N ∫[0,n)… because of monotone con-
vergence.) Using the substitutionu= √y, we get
I = 
2 ˚[0,∞)
1
1+ u2du=arctan(u)
óóóó
∞
u=0
= 2
2 .
(ii) We use partial fractions in (i):
1
1+ y
1
1+ x2y = 1
1− x2
1
1+ y− x2
1− x2
1
1+ x2y.
Thus,
I = ˚[0,∞)
0
˚[0,∞)
1
1− x2
1
1+ y− x2
1− x2
1
1+ x2ydy
1
dx
= ˚[0,∞)
0
lim
R→∞
4
1
1− x2ln(1+ R)− x2
1− x2
ln(1+ x2R)
x2
51
dx
= ˚(0,∞)
1
1− x2
0
lim
R→∞
ln
0
1+ R
1+ x2R
11
dx
= ˚[0,∞)
1
1− x2ln(x−2)dx
=2 ˚[0,∞)
ln(x)
x2−1 dx.
From (i) we infer that∫[0,∞)
lnx
x2−1dx= I
2 = 2
4 .
(iii) Using the geometric series we ﬁnd
1
x2−1 =−
É
n⩾0
(x2)n=−
É
n⩾0
x2n, ðxð<1,
as well as
1
x2−1 = 1
x2
1
1− x−2 = 1
x2
É
n⩾0
(x−2)n=
É
n⩾0
x−2(n+1), ðxð>1.
Thus,
˚(0,∞)
lnx
x2−1 dx=−
É
n⩾0 ˚(0,1)
x2nlnxdx +
É
n⩾0 ˚(1,∞)
x−2(n+1)lnxdx. (⋆)
(In order to swap summation and integration, we use dominated convergence!) Using
integration by parts, we ﬁnd
˚(0,1)
x2nlnxdx = x2n+1
2n+1 lnx
óóóó
1
x=0
− 1
2n+1 ˚(0,1)
x2ndx
177

R.L. Schilling: Measures, Integrals & Martingales
=− 1
(2n+1)2
and, in a similar fashion,
˚(1,∞)
x−2(n+1)lnxdx = x−2(n+1)+1
−2(n+1)+1 lnxóóóó
∞
x=1
− 1
−2(n+1)+1 ˚(1,∞)
x−2(n+1)dx
= 1
(−2(n+1)+1) 2 = 1
(2n+1)2.
Inserting these results into (⋆), the claim follows from part (ii).
■■
Problem 14.10 Solution:
(i) Sinceis-ﬁnite,thereisanexhaustingsequence (Gn)n∈N⊂ℬ(R)suchthat (Gn)<∞
andGn ↑ R. For eachn∈ N the set
Bn
k∶=
$
x∈Gn;({x})> 1
k
%
is ﬁnite.Indeed: Assume there were countably inﬁnitely many(xj)j∈N⊂B n
k,xj ≠xi for
i ≠j. Since the sets{xj},j ∈ N, are disjoint, we conclude that
(Gn) ⩾
H
É
j∈N
{xj}
I
=
É
j∈N
({xj})=∞ .
This is a contradiction to(Gn)<∞.
Thus, the set
Bn∶={x∈Gn;({x})>0}=
˝
k∈N
$
x∈Gn;({x})> 1
k
%
is countable and so is
D=
˝
n∈N
Bn
as it is a countable union of countable sets.
(ii) For the diagonal1Δ(x,y)= 1{y}(x)1R(y)we ﬁnd from Theorem 14.5:
×(Δ)= ˚R
0
˚ 1{y}(x)(dx)
1
(dy)
= ˚R
({y})1D(y)(dy)
=
É
y∈D
({y})({y}).
(In the last step we use thatD is countable.)
■■
178

Solution Manual. Last update 18th July 2019
Problem 14.11 Solution: Note that the diagonalΔ ⊂ R2 is measurable, i.e. the (double) integrals
are well-deﬁned. The inner integral on the l.h.S. satisﬁes
˚[0,1]
1Δ(x,y)(dx)= ({y})=0 ∀ y∈[0,1]
so that the left-hand side
˚[0,1]˚[0,1]
1Δ(x,y)(dx)(dy)= ˚[0,1]
0(dy)=0 .
On the other hand, the inner integral on the right-hand side equals
˚[0,1]
1Δ(x,y)(dy)= ({x})=1 ∀ x∈[0,1]
so that the right-hand side
˚[0,1]˚[0,1]
1Δ(x,y)(dy)(dx)= ˚[0,1]
1(dx)=1 .
Thisshowsthatthedoubleintegralsarenotequal. ThisdoesnotcontradictTonelli’stheoremsince
 is not-ﬁnite.
■■
Problem 14.12 Solution:
(i) Note that, due to the countability ofNand N× Nthere are no problems with measurability
and-ﬁniteness (of the counting measure).
Tonelli’s Theorem.Let(ajk)j,k∈N be a double sequence of positive numbersajk ⩾0. Then
É
j∈N
É
k∈N
ajk =
É
k∈N
É
j∈N
ajk
with the understanding that both sides are either ﬁnite or inﬁnite.
Fubini’s Theorem.Let(ajk)j,k∈N⊂ R be a double sequence of real numbersajk. If
É
j∈N
É
k∈N
ðajkð or
É
k∈N
É
j∈N
ðajkð
isﬁnite,thenallofthefollowingexpressionsconvergeabsolutelyandsumtothesamevalue:
É
j∈N
0 É
k∈N
ðajkð
1
,
É
k∈N
0É
j∈N
ðajkð
1
,
É
(j,k)∈N×N
ðajkð.
(ii) Consider the (obviously-ﬁnite) measuresj ∶= ∑
k∈Aj
k and = ∑
j∈Nj. Tonelli’s
theorem tells us that
É
j∈N
É
k∈Aj
ðxkð= ˚N˚N
ðxkðj(dk)(dj)
= ˚N˚N
ðxkð1Aj(k)(dk)(dj)
179

R.L. Schilling: Measures, Integrals & Martingales
= ˚N˚N
ðxkð1Aj(k)(dj)(dk)
= ˚N
ðxkð
0
˚N
1Aj(k)(dj)
1
«›››››››››››ﬂ›››››››››››‹
=1, as theAj are disjoint
(dk)
= ˚N
ðxkð(dk)
=
É
k∈N
ðxkð.
■■
Problem 14.13 Solution:
(i) SetU(a,b)∶= a−b. Then
U(u(x),y)1[0,∞)(y) ⩾0 ⇐ ⇒u(x) ⩾y ⩾0
andU(u(x),y)1[0,∞)(y)isacombination/sum/productof ℬ(R2)resp.ℬ(R)-measurablefunc-
tions. ThusS[u]isℬ(R2)-measurable.
(ii) Yes, true, since by Tonelli’s theorem
2(S[u])= ˚R2
1S[u](x,y)2(d(x,y))
= ˚R˚R
1{(x,y)∶u(x)⩾y⩾0}(x,y)1(dy)1(dx)
= ˚R˚[0,u(x)]
11(dy)1(dx)
= ˚R
u(x)1(dx)
(iii) Measurability follows from (i) and with the hint. Moreover,
2(Γ[u])= ˚R2
1Γ[u](x,y)2(d(x,y))
= ˚R˚R
1{(x,y)∶y=u(x)}(x,y)1(dy)1(dx)
= ˚R˚[u(x),u(x)]
11(dy)1(dx)
= ˚R
1({u(x)})1(dx)
= ˚R
01(dx)
=0.
■■
Problem 14.14 Solution: The hint given in the text should be good enough to solve this problem....
■■
180

Solution Manual. Last update 18th July 2019
Problem 14.15 Solution: Since(i)implies(ii),wewillonlyprove(i)undertheassumptionthatboth
(X,A,)and(Y, ℬ,)arecompletemeasurespaces. Notethatwehavetoassume -ﬁnitenessof
and,otherwisetheproductconstructionwouldnotwork. Picksomeset Z ∈P(X) ⧵A (which
is, because of completeness, not a null-set!), and some-null setN ∈ℬ and considerZ×N.
We get for some exhausting sequence(Ak)k⊂A,Ak ↑X and(Ak)<∞:
×(X×N)= sup
k∈N
×(Ak×N)
= sup
k∈N
  (Ak)
«ﬂ‹
<∞
⋅ (N)
«ﬂ‹
=0

=0;
thusZ×N ⊂X×N isasubsetofameasurable ×nullset,henceitshouldbe A⊗ℬ-measurable,
if the product space were complete. On the other hand, because of Theorem 14.17(iii), ifZ×N
isA ⊗ℬ-measurable, then the section
x → 1Z×N(x,y)= 1Z(x)1N(y)
y∈N
= 1Z(x)
isA-measurable which is only possible ifZ ∈A.
■■
Problem 14.16 Solution:
(i) LetA∈ℬ[0,∞)⊗P(N), ﬁxk∈ N and consider
1A(x,k) and Bk∶={x∶ 1A(x,k)=1};
because of Theorem 14.17(iii),Bk∈ℬ[0,∞). Since
(x,k)∈ A ⇐ ⇒ 1A(x,k)=1
⇐ ⇒∃k∈ N∶ 1A(x,k)=1
⇐ ⇒∃k∈ N∶x∈Bk
it is clear thatA= ⋃
k∈NBk×{k}.
(ii) LetM ∈ P(N) and set ∶= ∑
j∈Nj; we know that is a (-ﬁnite) measure onP(N).
Using Tonelli’s theorem 14.8 we get
(B×M)∶=
É
m∈M
(B×{m})
∶=
É
m∈M ˚B
e−t tm
m!(dt)
= ˚M ˚B
e−t tm
m!(dt)(dm)
= ¸B×M
e−t tm
m!×(dt,dm)
181

R.L. Schilling: Measures, Integrals & Martingales
which shows that the measure(dt,dm) ∶=e−t tm
m!×(dt,dm) has all the properties re-
quired by the exercise.
Theuniquenessfollows,however,fromtheuniquenesstheoremformeasures(Theorem5.7):
the family of ‘rectangles’ of the formB×M ∈ℬ[0,∞)× P(N) is a∩-stable generator of
the product-algebraℬ[0,∞)⊗P(N)and contains an exhausting sequence, say,[0,∞)×
{1,2,…k} ↑ [0,∞)× N. But on this generator is (uniquely) determined by prescribing
the values(B×{m}).
■■
Problem 14.17 Solution: Assume ﬁrst that ⩾ 0. The point here is that Corollary 14.15 does not
apply to the functions → e−s since this function is decreasing and has the value1 fors = 0.
Consider therefore(s)∶=1− e−s. This is admissible in 14.15 and we get
˚ (T)dP= ˚
 1− e−TdP= ˚
∞
0
e−s P(T ⩾s)ds.
Rearranging this equality then yields
˚ e−TdP=1−  ˚
∞
0
e−s P(T ⩾s)ds.
If< 0 the formula remains valid if we understand it in the sense that either both sides are ﬁnite
or both sides are inﬁnite. The above argument needs some small changes, though. First,e−s
is now increasing (which is ﬁne) but still takes the value1 if s = 0. So we should change to
(s) ∶=e−s−1 . Now the same calculation as above goes through. If one side is ﬁnite, so is
the other; and if one side is inﬁnite, then the other is inﬁnite, too. The last statement follows from
Theorem 14.13 or Corollary 14.15.
■■
Problem 14.18 Solution:
(i) This is similar to Problem 6.1, in particular (i) and (vi).
(ii) Note that
1B(x,y)= 1(a,b](x)1[x,b](y)
= 1(a,b](y)1(a,y](x)
= 1(a,b](x)1(a,b](y)1[0,∞)(y−x);
thelastexpressionis,however,aproductof(combinationsof)measurablefunctions,thus 1B
is measurable and so is thenB.
Without loss of generality we can assume thata> 0, all other cases are similar.
Using Tonelli’s theorem 14.8 we get
×(B)= ¸ 1B(x,y)×(dx,dy)
182

Solution Manual. Last update 18th July 2019
= ¸ 1(a,b](y)1(a,y](x)×(dx,dy)
= ˚(a,b] ˚(a,y]
(dx)(dy)
= ˚(a,b]
(a,y](dy)
= ˚(a,b]
 (0,y]− (0,a](dy)
= ˚(a,b]
(0,y](dy)− (0,a] ˚(a,b]
(dy)
= ˚(a,b]
F(y)dG(y)− F(a) G(b)− G(a). (*)
We remark at this point already that a very similar calculation (with, and F,G inter-
changed and with an open interval rather than a semi-open interval) yields
¸ 1(a,b](y)1(y,b](x)(dx)(dy)
= ˚(a,b]
G(y−)dF(y)− G(a) F(b)− F(a).
(**)
(iii) On the one hand we have
× (a,b]×( a,b]=(a,b](a,b]
=  F(b)− F(a) G(b)− G(a) (+)
and on the other we ﬁnd, using Tonelli’s theorem at step (T)
× (a,b]×( a,b]
= ¸ 1(a,b](x)1(a,b](y)(dx)(dy)
= ¸ 1(a,y](x)1(a,b](y)(dx)(dy)+
+ ¸ 1(y,b](x)1(a,b](y)(dx)(dy)
T
= ¸ 1(a,b](x)1[x,b](y)(dy)(dx)+
+ ¸ 1(y,b](x)1(a,b](y)(dx)(dy)
∗,∗∗
= ˚(a,b]
F(y)dG(y)− F(a) G(b)− G(a)+
+ ˚(a,b]
G(y−)dF(y)− G(a) F(b)− F(a).
Combining this formula with the previous one marked (+) reveals that
F(b)G(b)− F(a)G(a)= ˚(a,b]
F(y)dG(y)+ ˚(a,b]
G(y−)dF(y).
183

R.L. Schilling: Measures, Integrals & Martingales
Finally, observe that
˚(a,b]
 F(y)− F(y−)dG(y)= ˚(a,b]
({y})(dy)
=
É
a<y⩽b
({y})({y})
=
É
a<y⩽b
ΔF(y)ΔG(y).
(Mind that the sum is at most countable because of Lemma 14.14) from which the claim
follows.
(iv) It is clear that uniform approximation allows to interchange limiting and integration proced-
ures so that we *really* do not have to care about this. We show the formula for monomials
t,t2,t3,... by induction. Writen(t)= tn,n∈ N.
Inductionstart n=1 : inthiscase 1(t)= t,‡
1(t)=1 and(F(s))−(F(s−))−ΔF(s)=0 ,
i.e. the formula just becomes
F(b)− F(a)= ˚(a,b]
dF(s)
which is obviously true.
Induction assumption:for somenwe know that
n(F(b))− n(F(a))= ˚(a,b]
‡
n(F(s−))dF(s)
+
É
a<s⩽b

n(F(s))− n(F(s−))− ‡
n(F(s−))ΔF(s)

.
Induction stepn ⇝n+1: Write, for brevityF =F(s) andF− =F(s−). We have because
of (iii) withG=n◦F and because of the induction assumption
n+1(F(b))− n+1(F(a))
=F(b)n(F(b))− F(a)n(F(a))
= ˚(a,b]
Fn
−dF + ˚(a,b]
F−dFn+
É
ΔFΔFn
= ˚(a,b]
Fn
−dF + ˚(a,b]
F−‡
n(F−)dF+
+
É
F−n(F)− F−n(F−)− F−‡
n(F−)ΔF

+
É
ΔFΔFn
= ˚(a,b]
Fn
−dF + ˚(a,b]
F−nFn−1
− dF+
+
É
F−Fn−Fn+1
− −F−nFn−1
− ΔF +ΔFΔFn

= ˚(a,b]
(n+1)Fn
−dF +
É
F−Fn−Fn+1
− −nFn
−ΔF +ΔFΔFn

= ˚(a,b]
‡
n+1◦F−dF +
É
F−Fn−Fn+1
− −nFn
−ΔF +ΔFΔFn

184

Solution Manual. Last update 18th July 2019
The expression under the sum can be written as
F−Fn−Fn+1
− −nFn
−ΔF +ΔFΔFn
=(F−−F)Fn+Fn+1−Fn+1
− −nFn
−ΔF +ΔFΔFn
=Fn+1−Fn+1
− +ΔF

−Fn−nFn
−+ΔFn

=Fn+1−Fn+1
− +ΔF

−Fn−nFn
−+Fn−Fn
−

=Fn+1−Fn+1
− −(n+1)Fn
−ΔF
=n+1◦F −n+1◦F−−‡
n+1◦F−ΔF
and the induction is complete.
■■
Problem 14.19 Solution:
(i) We have the following pictures:
✲
✻
1 3 4 5 6 9 /u1D465
2
4
3
/u1D453(/u1D465)
1
Thisisthegraphoftheoriginalfunc-
tionf(x).
Open and full dots indicate the con-
tinuity behaviour at the jump points.
x-values are to be measured in-
length,i.e. xisapointinthemeasure
space(X,A,).
✲
✻
2 3 4 /u1D461
/u1D45A 1
/u1D45A 2
/u1D45A 3
/u1D707/u1D453 (/u1D461)
1
This is the graph of the associated
distribution functionf(t). It is de-
creasing and left-continuous at the
jump points.
t-valuesaretobemeasuredusingLe-
besgue measure in[0,∞).
m1= [4,5]
m2−m1= [6,9]
m3−m2= [4,5]
185

R.L. Schilling: Measures, Integrals & Martingales
✲
✻
2
3
4
/u1D453 ∗(/u1D709)
/u1D45A 1 /u1D45A 2 /u1D45A 3 /u1D709
1
Thisisthegraphofthedecreasingre-
arrangementf∗() off(x). It is de-
creasing and right-continuous at the
jump points. (Please note that the
picture is wrong and actually depicts
the left-continuous inverse which is
inf{t ∶ f(t) < } — mind the “⩽”
vs. “<” inside the inﬁmum)
-values are to be measured using
Lebesgue measure in[0,∞).
m1,m2,m3 are as in the previous pic-
ture.
(ii) The ﬁrst equality,
˚R
ðfðpd =p ˚
∞
0
tp−1f(t)dt,
follows immediately from Theorem 14.13 withu= ðfðandf(t)= ({ðfð ⩾t}).
To show the second equality we have two possibilities. We can...
a) ...show the second equality ﬁrst for (positive) simple functions and use then a (by now
standard...) Beppo Levi/monotone convergence argument to extend the result to all positive
measurable functions. Assume thatf(x) =∑N
j=0aj1Bj(x) is a positive simple function in
standard representation, i.e.a0 = 0< a1 < ⋯ < an < ∞ and the setsBj = {f = aj} are
pairwise disjoint. Then we have
({f =aj})= ({f ⩾aj} ⧵{f ⩾aj+1})
=({f ⩾aj})− ({f ⩾aj+1})
=f(aj)− f(aj+1) (an+1∶=∞,f(an+1)=0 )
=1 (f(aj+1),f(aj)]
=1(f∗=aj).
This proves
˚ fpd =
nÉ
j=0
ap
j(Bj)=
nÉ
j=0
ap
j1(f∗=aj)= ˚ (f∗)pd1
and the general case follows from the above-mentioned Beppo Levi argument.
or we can
b)use Theorem 14.13 once again withu=f∗ and=1 provided we know that
 {ðfð ⩾t}=1 {f∗ ⩾t}.
186

Solution Manual. Last update 18th July 2019
This, however, follows from
f∗() ⩾t ⇐ ⇒inf{s∶f(s) ⩽} ⩾t
⇐ ⇒f(t) ⩾ (asf is right cts. & decreasing)
⇐ ⇒ {ðfð ⩾t} ⩾
and therefore
1 { ⩾0∶ f∗() ⩾t}=1 { ⩾0∶ (ðfð ⩾t) ⩾}=(ðfð ⩾t).
■■
Problem 14.20 Solution: (By Franzsika Kühn) Fixt ∈ R. Applying the fundamental theorem of
calculus and Fubini’s theorem, we ﬁnd
F(t+ℎ)− F(t)= ˚X
((t+ℎ,x)− (t,x))(dx)= ˚X ˚
t+ℎ
t
)t(r,x)dr(dx)
= ˚
t+ℎ
t ˚X
)t(r,x)(dx)
«››››››››››ﬂ››››››››››‹
=∶f(r)
dr.
for allℎ∈ R. Sincef is (by assumption) continuous, this implies
lim
ℎ→0
1
ℎ(F(t+ℎ)− F(t))= lim
ℎ→0
1
ℎ ˚
t+ℎ
t
f(r)dr=f(t)
def
= ˚X
)t(t,x)(dx).
■■
187



15 Integrals with respect to image
measures.
Solutions to Problems 15.115.16
Problem 15.1 Solution: The ﬁrst equality
˚ ud(T(f))= ˚ u◦T fd
is just Theorem 15.1 combined with Lemma 10.8 the formula for measures with a density.
The second equality
˚ u◦T fd= ˚ uf◦T−1dT()
is again Theorem 15.1.
The third equality ﬁnally follows again from Lemma 10.8.
■■
Problem 15.2 Solution: Observe thatT is represented by then×n diagonal matrixA with entries
. SincedetA=n, the claim follows from Example 15.3(iii).
■■
Problem 15.3 Solution: Letx,y ∈ R. We have
1[0,1](x−y)1[0,1](y)= 1[−x,−x+1](−y)1[0,1](y)
= 1[x−1,x](y)1[0,1](y)
=
⎧
⎪
⎪
⎨
⎪
⎪⎩
0, x< 0orx> 2,
1[0,x](y), x ∈[0,1],
1[x−1,1], x ∈[1,2].
(∗)
This shows that
(1[0,1]∗ 1[0,1])(x)= ˚R
1[0,1](x−y)1[0,1](y)dy
=
⎧
⎪
⎪
⎨
⎪
⎪⎩
0, x< 0 or x> 2,
∫ x
0 dy=x, x ∈[0,1],
∫ 1
x−1dy=2− x, x ∈[1,2],
189

R.L. Schilling: Measures, Integrals & Martingales
=x1[0,1](x)+(2− x)1[1,2](x).
Since convolutions are linear and commutative, we get
(1[0,1]∗1[0,1]∗ 1[0,1])(x)
=  1[0,1]∗( 1[0,1]∗ 1[0,1])(x)
= ˚ 1[0,1](x−y)(y1[0,1](y)+(2− y)1[1,2](y))dy
= ˚ y1[0,1](x−y)1[0,1](y)dy+ ˚ (2− y)1[0,1](x−y)1[1,2](y)dy
=∶I1(x)+ I2(x).
Let us work out the two integrals separately. For the ﬁrst expression we ﬁnd using (∗)
I1(x)=
⎧
⎪
⎪
⎨
⎪
⎪⎩
0, x> 0 or x> 2,
∫ x
0 y= x2
2, x ∈[0,1],
∫ 1
1−xydy = 1
2(1−(1− x)2), x ∈[1,2].
= x2
2 1[0,1](x)+ 1
2(1−(1− x)2)1[1,2](x).
A similar calculation for the second integral yields
1[0,1](x−y)1[1,2](y)= 1[x−1,x](y)1[1,2](y)=
⎧
⎪
⎪
⎨
⎪
⎪⎩
0, x< 1 or x> 3,
1[1,x](y), x ∈[1,2],
1[x−1,2](y), x ∈[2,3].
This gives
I2(x)=
⎧
⎪
⎪
⎨
⎪
⎪⎩
0, x< 1 or x> 3,
∫ x
1 (2− y)dy=2(x−1)− 1
2(x2−1), x ∈[1,2],
∫ 2
x−1(2− y)dy=2(3− x)− 1
2(4−(1− x)2), x ∈[2,3]
=

2(x−1)− 1
2(x2−1)

1[1,2](x)+

2(1+ x)− 1
2(4−(1− x)2)

1[2,3](x).
Finally
(1[0,1]∗ 1[0,1]∗ 1[0,1])(x)= x2
2 1[0,1](x)+

−x2+3x−3
2

1[1,2](x)+

2(3− x)− 1
2(4−(1− x)2)

1[2,3](x).
■■
Problem 15.4 Solution: Observe that the assertion is equivalent to saying
(suppu+supp w)c ⊂(supp(u∗w))c.
190

Solution Manual. Last update 18th July 2019
Assume thatx0 ∈ (suppu+supp w)c. Since this is an open set, there is somer >0 such that
Br(x0)⊂(suppu+supp w)c. Pick anyx∈Br(x0). For ally∈supp wwe ﬁndx−y∉supp u. In
particular,
u(x−y)⋅w(y)=0 ∀ y∈supp w.
On the other hand, the very deﬁnition of the support, gives
u(x−y)⋅w(y)=0 ∀ y∉supp w.
This implies thatu(x−y)w(y)=0 for ally∈ Rn. From the deﬁnition of the convolution we see
that(u∗w)(x)=0 . Sincex∈Br(x0)is arbitrary, we getx0∉supp(u∗w).
■■
Problem 15.5 Solution:
(i) The measurability ofu,w entails that(x,y) → u(xy−1)w(y) is again measurable. From
Tonelli’s theorem we see the measurability ofx → u⊛w (x). In order to show com-
mutativity, we use the transformation theorem (Theorem 15.1) for the linear mapz ∶=
Φ(y)∶= xy−1:
u⊛w (x)= ˚(0,∞)
u(xy−1)w(y)dy
y
= ˚(0,∞)
u(z)w(x−1z)dz
z
=w⊛u (x).
Again by Tonelli’s theorem
˚(0,∞)
u⊛w (x)(dx)= ˚(0,∞)
0
˚(0,∞)
u(xy−1)w(y)dy
y
1
dx
x
= ˚(0,∞)
0
˚(0,∞)
u(xy−1)dx
x
1
w(y)dy
y . (⋆)
Fix y ∈ (0,∞) and deﬁney ∶= y−1x. From Theorem 7.10 we know that the image
measurey()(dz) of is given byy(dz) gegeben ist, and because of Theorem 15.1 we
get
˚(0,∞)
u(xy−1)dx
x =y−1
˚(0,∞)
u(xy−1) dx
xy−1
=y−1
˚(0,∞)
u(z)
y()(dz)
z
= ˚(0,∞)
u(z)dz
z . (⋆⋆)
If we insert this into (⋆), we obtain
˚(0,∞)
u⊛w (x)(dx)= ˚(0,∞)
0
˚(0,∞)
u(z)dz
z
1
w(y)dy
y
= ˚(0,∞)
ud ˚(0,∞)
wd.
191

R.L. Schilling: Measures, Integrals & Martingales
(ii) Consider ﬁrst the casep=∞ : Asðu(xy−1)ð ⩽ ‖u‖L∞() for-a.a.y∈(0,∞), we get
ðu⊛w (x)ð ⩽ ˚ ðu(xy−1)w(y)ð(dy) ⩽ ‖u‖L∞
˚ ðw(y)ð(dy)= ‖u‖L∞‖w‖1.
This proves‖u⊛w ‖L∞ ⩽ ‖u‖L∞‖w‖1.
Now we takep∈[1,∞). Note that
(dy)∶= 1
‖w‖1
ðw(y)ð(dy)
is a probability measure. Jensen’s inequality (forV(x)= xp) yields
ðu⊛w (x)ðp ⩽
0
˚(0,∞)
ðu(xy−1)ððw(y)ð(dy)
1p
= ‖w‖p
1
0
˚(0,∞)
ðu(xy−1)ð(dy)
1p
⩽ ‖w‖p
1 ˚(0,∞)
ðu(xy−1)ðp(dy)
= ‖w‖p−1
1 ˚(0,∞)
ðu(xy−1)ðpðw(y)ð(dy),
and from Tonelli’s theorem we get
˚ ðu⊛w (x)ðpd(x) ⩽ ‖w‖p−1
1 ˚(0,∞)
0
˚(0,∞)
ðu(xy−1)ðpðw(y)ð(dy)
1
(dx)
= ‖w‖p−1
1 ˚(0,∞)
0
˚(0,∞)
ðu(xy−1)ðp(dx)
1
ðw(y)ð(dy).
Just as in (⋆⋆) we conclude that
˚(0,∞)
ðu(xy−1)ðp(dx)
def
= ˚(0,∞)
ðu(xy−1)ðpdx
x = ˚(0,∞)
ðu(z)ðpdz
z
def
= ˚(0,∞)
ðu(z)ðp(dz).
If we insert this result into the estimates from above we see
˚ ðu⊛w (x)ðpd(x) ⩽ ‖w‖p−1
1 ˚(0,∞)
0
˚(0,∞)
ðu(z)ðp(dz)
1
ðw(y)ð(dy)
= ‖w‖p−1
1 ˚ ðuðpd ˚ ðwðd
= ‖w‖1‖u‖p
p.
Finally, takepth roots:
‖u⊛w ‖p ⩽ ‖w‖1‖u‖p.
■■
Problem 15.6 Solution: We have for anyC ∈ℬ
T()ðB(C)= T()(B∩C)
192

Solution Manual. Last update 18th July 2019
= T−1(B∩C)
= T−1(B)∩ T−1(C)
= A∩T−1(C)
=ðA
 T−1(C)
=T(ðA)(C).
■■
Problem 15.7 Solution: By deﬁnition, we ﬁnd for any Borel setB∈ℬ(Rn)
x⋆y(B)= ¸ 1B(s+t)x(ds)y(dt)
= ˚ 1B(x+t)y(dt)
= 1B(x+y)
= ˚ 1B(z)x+y(dz)
whichmeansthat x⋆y=x+y. Notethat,byTonelli’stheoremtheorderoftheiteratedintegrals
is irrelevant.
Similarly, sincez+t∈B ⇐ ⇒t∈B−z, we ﬁnd
z⋆(B)= ¸ 1B(s+t)z(ds)(dt)
= ˚ 1B(z+t)(dt)
= ˚ 1B−z(t)(dt)
=(B−z)
=−z()(B)
wherez(t)∶= (t−z)is the shift operator so that−1
−z(B)= B−z.
■■
Problem 15.8 Solution: Sincex+y∈B ⇐ ⇒x∈B−y,wecanrewriteformulain15.4(iii)inthe
following way:
⋆ (B)= ¸ 1B(x+y)(dx)(dy)
= ˚
4
˚ 1B−y(x)(dx)
5
(dy)
= ˚ (B−y)(dy).
Similarly we get
⋆ (B)= ˚ (B−y)(dy)= ˚ (B−x)(dx).
193

R.L. Schilling: Measures, Integrals & Martingales
Thus, if has no atoms, i.e. if({z})=0 for allz∈ Rn, we ﬁnd
⋆ ({z})= ˚  {z}− y(dy)= ˚  {z−y}
«ﬂ‹
=0
(dy)=0 .
■■
Problem 15.9 Solution: BecauseofTonelli’stheoremwecaniteratetheverydeﬁnitionof‘convolu-
tion’ of two measures, Deﬁnition 15.4(iii), and get
1⋆⋯⋆n(B)= ˚ ⋯ ˚ 1B(x1+⋯+xn)1(dx1)⋯n(dxn)
so that the formula derived at the end of Remark 15.5(ii), page 156, applies and yields
˚ ð!ð P⋆n(d!)
= ˚ ⋯ ˚ ð!1+!2+⋯+!nð P(d!1) P(d!2)⋯ P(d!n)
∗
⩽ ˚ ⋯ ˚

ð!1ð+ð!2ð+⋯+ð!nð

P(d!1) P(d!2)⋯ P(d!n)
=
nÉ
j=1 ˚ ⋯ ˚ ð!jð P(d!1) P(d!2)⋯ P(d!n)
=
nÉ
j=1 ˚ ð!jð P(d!j)⋅
˙
k≠j ˚ P(d!k)
=
nÉ
j=1 ˚ ð!jð P(d!j)
=n ˚ ð!1ð P(d!1)
where we use the symmetry of the iterated integrals in the integrating measures as well as the fact
that P(Rn) = ∫ P(d!k) = 1. Note that we could have+∞ on either side, i.e. the integrability
condition is only important for the second assertion.
The equality∫ ! P⋆n(d!)= n ∫ ! P(d!) follows with same calculation (note that we do not get
an inequality as there is no need for the triangle inequality at point (*) above). The integrability
condition is now needed since the integrands are no longer positive. Note that, since! ∈ Rn,
the above equality is an equality between vectors inRn; this is no problem, just read the equality
coordinate-by-coordinate.
■■
Problem 15.10 Solution: Sincetheconvolution p →u⋆p islinear,itisenoughtoconsidermonomi-
als of the formp(x)= xk. Thus, by the binomial formula,
u⋆p (x)= ˚ u(x−y)ykdy
= ˚ u(y)(x−y)kdy
194

Solution Manual. Last update 18th July 2019
=
kÉ
j=0
0
k
j
1
xj
˚ u(y)yk−jdy.
Sincesuppuiscompact, thereissome r> 0suchthat suppu⊂B r(0)andwegetforany m∈ N0,
and in particular form=k−j orm=k, that
óóóó˚ u(y)ymdyóóóó
⩽ ˚suppu
‖u‖∞ðyðmdy
⩽ ˚Br(0)
‖u‖∞rmdy
=2r⋅rm⋅‖u‖∞
which is clearly ﬁnite. This shows thatu⋆p exists and that it is a polynomial.
■■
Problem 15.11 Solution: That the convolutionu⋆w is bounded and continuous follows from The-
orem 15.8.
Monotonicity follows from the monotonicity of the integral: ifx ⩽z, then
u⋆w (x)= ˚ u(y)
«ﬂ‹
⩾0
⋅w(x−y)
«›ﬂ›‹
⩽w(z−y)
dy ⩽ ˚ u(y)⋅w(z−y)dy=u⋆w (y).
■■
Problem 15.12 Solution: (This solution is written foru∈Cc(Rn)andw∈C∞(Rn)).
Let)i=)∕)xi denote the partial derivative in directionxi wherex=(x1,…,xn)∈ Rn. Since
w∈C∞ - ⇒)iw∈C∞,
it is enough to show)i(u ⋆ w) = u ⋆ )iw and to iterate this equality. In particular, we ﬁnd
)(u⋆w )= u⋆) w where
) = )1+⋯n
)1x1⋯)nxn
,  ∈ Nn
0.
Sinceu has compact support and since the derivative is a local operation (i.e., we need to know a
function only in a neighbourhood of the point where we diﬀerentiate), and since we have for any
r> 0
sup
y∈suppu
sup
x∈Br(0)
óóóó
)
)xi
w(x−y)óóóó
⩽c(r),
wecanusethediﬀerentiabilitylemmaforparameter-dependentintegrals,Theorem12.5toﬁndfor
anyx∈Br∕2(0), say,
)
)xi ˚ u(y)w(x−y)dy= ˚ u(y) )
)xi
w(x−y)dy
= ˚ u(y)  )
)xi
w(x−y)dy
195

R.L. Schilling: Measures, Integrals & Martingales
=u⋆) iw(x).
■■
Problem 15.13 Solution: Lett be a Friedrichs molliﬁer. From Lemma 15.10 we know
u∈Cc(Rn) - ⇒u∗t∈C∞
c (Rn).
Sinceu∈Cc(Rn)is uniformly continuous, we ﬁnd that
lim
t→0
sup
x
ðu(x)− u(x−tz)ð=0
and since∫ t(y)dy= ∫ t(x−y)dy=1 we get
ðu(x)− u∗t(x)ð= óóóó˚ (u(x)− u(y))t(x−y)dyóóóó
⩽ ˚ ðu(x)− u(y)ðt−n x−y
t
dy
= ˚ ðu(x)− u(x−tz)ð(z)dz
⩽ ˚ sup
x
ðu(x)− u(x−tz)ð(z)dz
dom. conv.
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , →
t→0
0.
In the last step we use the integrable dominating function2‖u‖∞(u).
■■
Problem 15.14 Solution: ThemeasurabilityconsiderationsarejustthesameasinTheorem15.6, so
we skip this part.
By assumption,
1
p+1
q =1+ 1
r;
We can rewrite this as
1
r +
4
1
p−1
r
5
«›ﬂ›‹
=1− 1
q∈[0,1)
+
4
1
q −1
r
5
«›ﬂ›‹
=1− 1
p∈[0,1)
=1. (*)
Now write the integrand appearing in the deﬁnition ofu⋆w (x)in the form
ðu(x−y)w(y)ð=

ðu(x−y)ðp∕rðw(y)ðq∕r

⋅

ðu(x−y)ð1−p∕r

⋅

ðw(y)ð1−q∕r

and apply the generalized Hölder inequality (cf. Problem 13.5) with the exponents from (*):
ðu⋆w (x)ð ⩽ ˚ ðu(x−y)w(y)ðdy
196

Solution Manual. Last update 18th July 2019
⩽
4
˚ ðu(x−y)ðpðw(y)ðqdy
51
r
4
˚ ðu(x−y)ðpdy
51
p−1
r
4
˚ ðw(y)ðqdy
51
q−1
r
.
Raising this inequality to therth power we get, because of the translation invariance of Lebesgue
measure,
ðu⋆w (x)ðr ⩽
4
˚ ðu(x−y)ðpðw(y)ðqdy
5
‖u‖r−p
p ⋅‖w‖r−q
q
= ðuðp⋆ðwðq(x)⋅‖u‖r−p
p ⋅‖w‖r−q
q .
Now we integrate this inequality overx and use Theorem 15.6 forp=1 and the integral
˚ ðuðp⋆ðwðq(x)dx= ‖ðuðp⋆ðwðq‖1 ⩽ ‖u‖p
p⋅‖w‖q
q.
Thus,
‖u⋆w ‖r
r= ˚ ðu⋆w (x)ðrdx ⩽ ‖u‖p
p⋅‖w‖q
q⋅‖u‖r−p
p ⋅‖w‖r−q
q = ‖u‖r
p⋅‖w‖r
q
and the claim follows.
■■
Problem 15.15 Solution: ForN = 1the inequality is trivial, forN = 2it is in line with Problem
15.14 withp=q.
Let us, ﬁrst of all, give aheuristic derivationof this result which explains how one arrives at the
particularformforthevalueof p=p(r,N). Wemayassumethat N ⩾2. SetFj ∶=fj⋆…⋆fN
forj=1,2,…N−1. Then
‖f1⋆⋯⋆fN‖r
⩽ ‖f1‖p‖F2‖q2 = ‖f1‖p‖f2⋆F3‖q2
by Pr. 15.14 where1
r +1= 1
p+ 1
q2
=  1
p−1+ 1
q2
+1
⩽ ‖f1‖p‖f2‖p‖F3‖q3 = ‖f1‖p‖f2‖p‖f3⋆F4‖q3
by Pr. 15.14 where1
r +1=  1
p−1+ 1
p+ 1
q3
«ﬂ‹
= 1
q2
+1
=2  1
p−1+1+ 1
q3
and repeating this procedureN−2 times we arrive at
‖f1⋆⋯⋆fN‖r ⩽ ‖f1‖p⋯‖fN−2‖p⋅‖fN−1⋆fN‖qN−1
⩽ ‖f1‖p⋯‖fN−2‖p⋅‖fN−1‖p⋅‖fN‖qN
with the condition
1
r +1=( N−2)
1
p−1

+1+ 1
qN−1
=(N−2)
1
p−1

+1
p+ 1
qN
197

R.L. Schilling: Measures, Integrals & Martingales
and since we needqN =p we get
1
r +1=( N−2)
1
p−1

+2
p = N
p −N+2
and rearranging this identity yields
p= Nr
(N−1)r+1 .
Ifyoudonotlikethisderivationofifyougotlostcountingtherepetitions,here’sthe formalproof
using induction—but with the drawback that one needs a good educated guess whatp= p(N,r)
should look like. The start of the inductionN = 2is done in Problem 15.14 (starting atN = 1
won’t help much as we need Young’s inequality forN =2 anyway...).
The induction hypothesis is, of course,
‖f1⋆⋯⋆fM‖t ⩽
M˙
j=1
‖fj‖ for allM =1,2,…,N −1
wheret> 0 is arbitrary and = Mt
(M−1)t+1.
The induction step uses Young’s inequality:
‖f1⋆f2⋆⋯⋆fN‖r ⩽ ‖f1‖p⋅‖f2⋆⋯⋆fN‖q
wherep= Nr
(N−1)r+1 andq is given by
1
r +1= 1
q +1
q = (N−1)r+1
Nr +1
q =1+ 1
q − 1
N + 1
Nr
so that
q= Nr
N+r−1 .
Using the induction hypothesis we now get
‖f1⋆⋯⋆fN‖r ⩽ ‖f1‖p⋅‖f2⋆⋯⋆fN‖q ⩽ ‖f1‖p⋅ ‖f2‖s⋯‖fN‖s

wheresis, because of the induction assumption, given by
s= (N−1)q
(N−2)q+1
=
(N−1) Nr
N+r−1
(N−2) Nr
N+r−1+1
= (N−1)Nr
(N−2)Nr+N+r−1
= (N−1)Nr
N2r−2Nr+r+(N−1)
= (N−1)Nr
(N−1)2r+(N−1)
= Nr
(N−1)r+1 =p
and we are done.
■■
198

Solution Manual. Last update 18th July 2019
Problem 15.16 Solution: Note thatv(x)= d
dx(1−cos x)1[0,2)(x)= 1(0,2)(x)sin x. Thus,
(i)
u⋆v (x)= ˚
2
0
1R(x−y)sin ydy = ˚
2
0
sinydy =0 ∀ x.
(ii) Since all functionsu,v,w, are continuous, we can use the usual rules for the (Riemann)
integralandget,usingintegrationbypartsandthefundamentaltheoremofintegralcalculus,
v⋆w (x)= ˚
d
dx(x−y) ˚
x
−∞
(t)dtdx
= ˚
 − d
dy(x−y)
˚
y
−∞
(t)dtdx
= ˚ (x−y) d
dy ˚
y
−∞
(t)dtdx
= ˚ (x−y)(y)dy
=⋆ (x).
Ifx ∈ (0,4), thenx−y ∈ (0,2) for some suitabley = y= and even for ally from an
interval(y0−,y0+) ⊂ (0,2). Since  is positive with support[0,2], the positivity
follows.
(iii) Obviously,
(u⋆v )⋆w
(i)
=0 ⋆w =0
while
u⋆ (v⋆w )(x)= ˚ 1R(x−y)v⋆w (y)dy
= ˚ v⋆w (y)dy
= ˚ ⋆ (y)dy
>0.
Note thatw is not an (pth power,p< ∞) integrable function so that we cannot use Fubini’s
theorem to prove associativity of the convolution.
■■
199



16 Integrals of images and Jacobi's
transformation rule.
Solutions to Problems 16.116.12
Problem 16.1 Solution: SinceF andFi areF-sets, we get
F =
˝
k∈N
Ck, F i=
˝
k∈N
Ci
k
for closed setsCk resp.Ci
k. Since complements of closed sets are open, we ﬁnd, using the rules
for (countable) unions and intersections that
(i)
nÌ
i=1
Fi=
nÌ
i=1
˝
k∈N
Ci
k=
˝
k∈N
nÌ
i=1
Ci
k
«ﬂ‹
closed set
.
(ii)
˝
i∈N
Fi=
˝
i∈N
˝
k∈N
Ci
k=
˝
(i,k)∈N×N
Ci
k
«››››ﬂ››››‹
countable union!
.
Moreover,
Ì
i∈N
Fc
i =
Ì
i∈N
Ì
k∈N
Ci
k
c
=
Ì
(i,k)∈N×N
Ci
k
c
«››››››ﬂ››››››‹
countable intersection!
.
(iii) F =
˝
k∈N
Ck - ⇒Fc =
4 ˝
k∈N
Ck
5c
=
Ì
k∈N
Cc
k
«ﬂ‹
open
.
(iv) Set c1∶=C andCi=ç ,i ⩾2. ThenC =
˝
i∈N
Ci is anF-set.
■■
Problem 16.2 Solution: Write= n andℬ = ℬ(Rn). FixB ∈ ℬ. According to Lemma 16.12
there are setsF ∈F andG∈G such that
F ⊂B ⊂G and (F)= (B)= (G).
Sinceforclosedsets Cj andopensets Uj wehave F = ⋃Cj andG= ⋂Uj wegetforsome  >0
and suitableM =M ∈ N, N=N ∈ N that
C1∪⋯∪CN ⊂B ⊂U1∩⋯∩UM
201

R.L. Schilling: Measures, Integrals & Martingales
and
óóó(U1∩⋯∩UM)− (B)óóó ⩽, (*)
óóó(B)− (C1∪⋯∪CN)óóó ⩽. (**)
Sinceﬁniteunionsofclosedsetsareclosedandﬁniteintersectionsofopensetsareopen,(*)proves
outer regularity while (**) proves inner regularity (w.r.t. close sets).
To see inner regularity with compact sets, we note that the closed setC‡ ∶= C1∪⋯∪CN is
approximated by the following compact sets
Kl ∶=Bl(0)∩ C‡ ↑C‡ as l →∞
and, because of the continuity of measures, we get for suitably largeL=L ∈ N that
óóó(KL)− (C1∪⋯∪CN)óóó ⩽
which can be combined with (**) to give
óóó(KL)− (B)óóó ⩽2.
This shows inner regularity for the compact sets.
■■
Problem 16.3 Solution: Notation (for brevity): Write = n, ̄ = n, ℬ = ℬ(Rn) andℬ∗ =
ℬ∗(Rn). By deﬁnition,B∗ =B∪N∗ whereN∗ is a subset of aℬ-measurable null setN. (We
indicateℬ∗-sets by an asterisk,C (with and without ornaments and indicesC‡ ...) is always a
closed set andU etc. is always an open set.
Solution 1:Following the hint we get (with the notation of Problem 11.6)
(B)= ̄(B∗)= ∗(B∗)
= inf
ℬ∋A⊃B∗
(A) (by 11.6)
= inf
ℬ∋A⊃B∗
inf
U⊃A
(U) (by 16.2)
⩽ inf
U‡⊃B∪N
inf
U⊃U‡
(U) (asB∗⊂B ∪N)
= inf
U‡⊃B∗
(U‡) (by 16.2)
=(B∪N) (by 16.2)
⩽(B)+ (N)
=(B).
Inner regularity (for closed sets) follows similarly,
(B)= ̄(B∗)= ∗(B∗)
202

Solution Manual. Last update 18th July 2019
= sup
ℬ∋A⊂B∗
(A) (by 11.6)
= sup
ℬ∋A⊂B∗
sup
C⊂A
(C) (by 16.2)
⩾ sup
C‡⊂B∗
sup
C⊂C‡
(C)
= sup
C‡⊂B∗
(C‡) (by 16.2)
⩾ sup
C‡⊂B
(C‡) (asB ⊂B∗)
=(B), (by 16.2)
and inner regularity for compact sets is the same calculation.
There is a more elementary ....
Solution 2:(without Problem 11.6). Using the deﬁnition of the completion we get
̄(B∗)= (B)= sup
C‡⊂B
(C‡)
⩽ sup
C⊂B∗
(C)
⩽ sup
C‡‡⊂B∪N
(C‡‡)
=(B∪N)
=(B)
as well as
̄(B∗)= (B)= inf
U‡⊃B
(U‡)
⩽ inf
U⊃B∗(U)
⩽ inf
U‡‡⊃B∪N
(U‡‡)
=(B∪N)
=(B).
■■
Problem 16.4 Solution:
(i) Using the result of Problem 7.12 we writex,y ∈C as triadic numbers:
x=
∞É
i=1
xi
3i =0.x1x2x3… and y=
∞É
i=1
yi
3i =0.y1y2y3…
wherexi,yi ∈ {0,2}. In order to enforce uniqueness, we only want to havetruly inﬁnite
sums, i.e. we use0.002222… instead of0.01000… etc.
203

R.L. Schilling: Measures, Integrals & Martingales
Obviously, everyz∈C−C is of the formz=x−y withx,y ∈C and soz=0.z1z2z3…
withzi=xi−yi∈{−2,0,2}. Thus,
1
2(z+1)= 1
2
H ∞É
i=1
xi−yi
3i +
∞É
i=1
2
3i
I
= 1
2
∞É
i=1
xi−yi+2
3i =
∞É
i=1
wi
3i.
Byconstruction, wi= 1
2(xi−yi+2)∈ 1
2{0,2,4}={0 ,1,2},i.e.thenumbers 1
2(z+1) make
up the whole interval[0,1].
This shows thatC−C =[−1,1].
(ii) Let(x,y)= x−yasinthehint. ThisisaLipschitz(Hölder- 1)continuousmapfrom R2 → R
andithasthefollowingproperty: C×C →(C,C)=[−1 ,1]. ButC×C isaLebesguenull
set inR2 while1[−1,1]=2 . This situation cannot occur in Corollary 16.14.
■■
Problem 16.5 Solution:
(i) Obviously,G ⊂ℬ[0,∞). On the other hand,(G)contains all open intervals of the form
(,)=
˝
n∈N
− 1
n,∞ ⧵,∞, 0 ⩽ < <∞ (*)
and all intervals of the form
[0,)=[0 ,∞) ⧵[,∞),  > 0. (**)
Thus,
(G)⊃O(R)∩[0 ,∞)
since any open setU ∈O(R)is a countable union of open intervals,
U =
˝
<,,∈Q
(,)⊂U
(,),
so thatU∩[0,∞)∈ O∩[0,∞)is indeed a countable union of sets of the form (*) and (**).
Thus,
ℬ[0,∞)= (O∩[0,∞))⊂(G)⊂ℬ[0,∞).
(ii) That isameasurefollowsfromLemma10.8(foraproof,seetheonlinesection‘additional
material’). Since
(B)= (T−1
1∕5(B))= T1∕5()(B)
whereT1∕5(x)= 1
5⋅x, is an image measure, hence a measure.
Since
[a,∞)= [5a,∞) ⩽[a,∞) ∀ a ⩾0,
204

Solution Manual. Last update 18th July 2019
we haveóóóG
⩽óóóG
. On the other hand,
3
5, 4
5
=[3,4)=1 >0= 3
5, 4
5
.
This does not contradict Lemma 16.6 sinceG is not a semi-ring.
■■
Problem 16.6 Solution: We want to show that
a) n(x+B)= n(B),B∈ℬ(Rn), x∈ Rn (Theorem 5.8(i));
b) n(t⋅B)= tnn(B),B∈ℬ(Rn), t⩾0 (Problem 5.9);
c) A(n)= ðdetA−1ð⋅n,A∈ Rn×n,detA ≠0 (Theorem 7.10).
From Theorem 16.4 we know that for anyC1 diﬀeomorphism the formula
n((B))= ˚B
ðdetDðdn
holds. Thus a), b), c) follow upon setting
a) (y)= x+y - ⇒D ≡1 - ⇒ðdetDð ≡1;
b) (y)= t⋅y - ⇒D ≡t⋅id - ⇒ðdetDð ≡tn;
c) (y)= A−1y - ⇒D(y) ≡A−1 - ⇒ðdetDð ≡ ðdetAð−1.
■■
Problem 16.7 Solution:
(i) The mapΦ∶ R∋x →(x,f(x)) is obviously bijective and diﬀerentiable with deriv-
ativeDΦ(x)=(1 ,f ‡(x)) so thatðDΦ(x)ð2 =1+( f‡(x))2. The inverse ofΦ is given
byΦ−1∶(x,f(x)) →xwhich is clearly diﬀerentiable.
(ii) Since ðDΦ(x)ð =
√
1+( f‡(x))2 is positive and measurable, it is a density function
and ∶= ðDΦ(x)ð⋅ is a measure, cf. Lemma 10.8, while = Φ() is an image
measure in the sense of Deﬁnition 7.7.
(iii) This is Theorem 15.1 and/or Problem 15.1.
(iv) The normal is, by deﬁnition, orthogonal to the gradient:DΦ(x) = (1,f ‡(x)); obvi-
ouslyðn(x)ð=1 and
n(x)⋅DΦ(x)=
H
−f‡(x)
1
I
⋅
H
1
f‡(x)
I
√
1+( f‡(x))2
=0.
Further,
Φ(x,r)=
⎛
⎜
⎜⎝
x− rf‡(x)√
1+[f‡(x)]2
f(x)+ r√
1+[f‡(x)]2
⎞
⎟
⎟⎠
,
205

R.L. Schilling: Measures, Integrals & Martingales
so that
DΦ(x,r)=
0)Φ(x,r)
)(x,r)
1
=
⎛
⎜
⎜⎝
1− r )
)x
f‡(x)√
1+[f‡(x)]2 f‡(x)+ r )
)x
1√
1+[f‡(x)]2
− f‡(x)√
1+[f‡(x)]2
1√
1+[f‡(x)]2
⎞
⎟
⎟⎠
For brevity we writef,f ‡,f ‡‡instead off(x),f ‡(x),f ‡‡(x). Now
)
)x
f‡(x)√
1+[ f‡(x)]2
=
f‡‡√
1+[ f‡]2−f‡ f‡f‡‡
√
1+[f‡]2
1+[ f‡]2
and
)
)x
1√
1+[ f‡(x)]2
=
− f‡f‡‡
√
1+[f‡]2
1+[ f‡]2.
Thus,detDΦ(x,r)becomes
1√
1+[ f‡]2
0
1−
rf ‡‡√
1+[ f‡]2− r[f‡]2f‡‡
√
1+[f‡]2
1+[ f‡]2
1
+ f‡
√
1+[ f‡]2
0
f‡−
rf ‡f‡‡
√
1+[f‡]2
1+[ f‡]2
1
= 1√
1+[ f‡]2
−
rf ‡‡− r[f‡]2f‡‡
1+[f‡]2
1+[ f‡]2 + [f‡]2
√
1+[ f‡]2
−
r[f‡]2f‡‡
1+[f‡]2
1+[ f‡]2
= 1+[ f‡]2
√
1+[ f‡]2
− rf ‡‡
1+[ f‡]2
=
√
1+[ f‡]2− rf ‡‡
1+[ f‡]2
Ifx is from a compact set, say[c,d], we can, because of the continuity off,f ‡and
f‡‡, achieve that for suﬃciently small values ofðrð< we get thatdetDΦ>0, i.e.Φ
is a localC1-diﬀeomorphism.
(v) The set is a ‘tubular’ neighbourhood of radiusr around the graphΓf forx ∈ [c,d].
Measurability follows, sinceΦ is a diﬀeomorphism, from the fact that the setC(r) is
the image of the cartesian product of measurable sets.
(vi) Because of part (iv) we have, for ﬁxedx and suﬃciently small values ofr, that the
determinant is positive so that
lim
r↓0
1
2r ˚(−r,r)
óóódetDΦ(x,s)óóó1(ds)
=lim
r↓0
1
2r ˚(−r,r)
óóóó
√
1+( f‡(x))2− sf ‡‡(x)
1+( f‡(x))2
óóóó
1(ds)
=lim
r↓0
1
2r ˚(−r,r)
0√
1+( f‡(x))2− sf ‡‡(x)
1+( f‡(x))2
1
1(ds)
206

Solution Manual. Last update 18th July 2019
=lim
r↓0
1
2r ˚(−r,r)
√
1+( f‡(x))21(ds)
−lim
r↓0
1
2r ˚(−r,r)
sf ‡‡(x)
1+( f‡(x))21(ds)
=
√
1+( f‡(x))2− f‡‡(x)
1+( f‡(x))2lim
r↓0
1
2r ˚(−r,r)
s1(ds)
=
√
1+( f‡(x))2
= óóódetDΦ(x,0)óóó.
(vii) We have
1
2r ˚R2
1C(r)(x,y)2(dx,dy)
= 1
2r ˚R2
1Φ(Φ−1(C)×(−r,r))(x,y)2(dx,dy)
= 1
2r ˚R2
1Φ−1(C)×(−r,r)(z,s)óóódetDΦ(z,s)óóó2(dz,ds) (Thm 16.4)
= ˚R
1Φ−1(C)(z)
4
1
2r ˚(−r,r)
óóódetDΦ(z,s)óóó1(ds)
5
«››››››››››››››››››››››ﬂ››››››››››››››››››››››‹
, , , , , , , , , , , , , →
r↓0
ðdetDΦ(z,0)ð
1(dz). (Tonelli)
SinceΦ−1(C)isaboundedsubsetof R, wecanusetheresultofpart(vii)anddomin-
ated convergence and the proof is ﬁnished.
(viii) This follows from (i)–(iii) and the fact that
óóódetDΦ(x,0)óóó=
√
1+( f‡(x))2
andthegeometricalmeaningoftheweightedarea 1
2r2(C(r))—recallthat C(r)wasa
tubular neighbourhood of the graph.
■■
Problem 16.8 Solution:
(i) ðdetDΦ(x)ðispositiveandmeasurable,henceadensityand,byLemma10.8, ðdetDΦð⋅
d is a measure. Therefore,Φ(ðdetDΦð⋅ d) is an image measure in the sense of
Deﬁnition 7.7.
Usingtherulesfordensitiesandintegralsw.r.t.imagemeasuresweget(cf.e.g.Theorem
15.1 and/or Problem 15.1)
˚M
udM = ˚M
udΦ ðdetDΦð⋅d= ˚Φ−1(M)
u◦Φ⋅ðdetDΦðdd.
(ii) This is the formula from part (i) withΦ= r; observe thatr(Rn)= Rn.
(iii) The equality
˚ udn= ˚(0,∞)˚{‖x‖=1}
u(rx)rn−1(dx)1(dr)
207

R.L. Schilling: Measures, Integrals & Martingales
is just Theorem 16.22. The equality
˚(0,∞)˚{‖x‖=r}
u(x)(dx)1(dr)
= ˚(0,∞)˚{‖x‖=1}
u(rx)rn−1(dx)1(dr)
follows from part (ii).
■■
Problem 16.9 Solution: We have
Γ 1
2
= ˚(0,∞)
y−1∕2e−y(dy).
Using the change of variablesy=(x)= x2, we getD(x)=2 xand
Γ 1
2
=2 ˚(0,∞)
e−x2
(dx)=2 ˚(−∞,∞)
e−x2
(dx)
16.16
=
√
.
■■
Problem 16.10 Solution: WriteΦ=(Φ 1,Φ2,Φ3). Then
DΦ(r,,! )=
⎛
⎜
⎜
⎜⎝
)Φ1
)r
)Φ1
)
)Φ1
)!
)Φ2
)r
)Φ2
)
)Φ2
)!
)Φ3
)r
)Φ3
)
)Φ3
)!
⎞
⎟
⎟
⎟⎠
=
⎛
⎜
⎜
⎜⎝
coscos! −rsincos! −rcossin!
sincos! r coscos! −rsinsin!
sin! 0 rcos!
⎞
⎟
⎟
⎟⎠
Developing according to the bottom row we calculate for the determinant
detDΦ(r,,! )
=sin !det
H
−rsincos! −rcossin!
rcoscos! −rsinsin!
I
+rcos!det
H
coscos! −rsincos!
sincos! r coscos!
I
=sin !

r2sin2cos!sin!+r2cos2cos!sin!

+rcos!

rcos2cos2!+rsin2cos2!

=r2sin2!cos!+r2cos!cos2!
=r2cos!
where we use repeatedly the elementary relationsin2+cos2=1 .
Thus,
Ì
R3
u(x,y,z)d3(x,y,z)
208

Solution Manual. Last update 18th July 2019
= Ì
Φ−1(R3)
u◦Φ(r,,! )ðdetDΦ(r,,! )ðd3(r,,! )
= ˚
∞
0 ˚
2
0 ˚
∕2
−∕2
U(rcoscos!,rsincos!,rsin!)r2cos!drdd!.
■■
Problem 16.11 Solution:
(i) We change in
Γ(x)= ˚
∞
0
e−ttx−1dt
variables according tou2=t, and get
Γ(x)=2 ˚
∞
0
e−u2
u2x−1du.
Using Tonelli’s theorem we ﬁnd
Γ(x)Γ(y)=4
0
˚
∞
0
e−u2
u2x−1du
10
˚
∞
0
e−v2
v2y−1dv
1
=4 ˚(0,∞)2
e−u2−v2
u2x−1v2y−1d(u,v).
(ii) We have to show thatB(x,y)Γ(x+y)=Γ( x)Γ(y). Using polar coordinates in (i) we see
Γ(x)Γ(y)=4 ˚
∞
r=0 ˚
2
=0
e−r2
r2x+2y−1(cos)2x−1(sin)2y−1ddr
=4
0
˚
∞
r=0
e−r2
r2x+2y−1dr
1H
˚
∕2
=0
(cos)2x−1(sin)2y−1d
I
. (⋆)
Settings∶=r2 we see
˚
∞
r=0
e−r2
r2x+2y−1dr= 1
2 ˚
∞
s=0
e−ss(x+y)−1ds= 1
2Γ(x+y).
Change variables in the second integral of (⋆) according tot = cos2 and usesin2+
cos2=1 . This yields
˚
∕2
=0
(cos)2x−1(sin)2y−1d= 1
2 ˚
1
0
t2x−1(1− t)2y−1dt= 1
2B(x,y).
■■
Problem 16.12 Solution: We introduce planar polar coordinates as in Example 16.15:
(x,y)=( rcos,r sin), r> 0, ∈[0,2).
209

R.L. Schilling: Measures, Integrals & Martingales
Thus,
¸
‖x‖2+‖y‖2<1
xmynd2(x,y)
= ˚
1
0 ˚
2
0
rn+m+1 cosm sinndrd
=
0
˚
1
0
rn+m+1dr
10
˚
2
0
cosm sinnd
1
= rm+n+2
m+n+2
óóóó
r=1
r=0
0
˚
2
0
cosm sinnd
1
= 1
m+n+2 ˚
2
0
cosm sinnd.
(*)
Consider the integral
1
m+n+2 ˚
2
0
cosm sinnd;
Since sine and cosine are periodic and since we integrate over a whole period, we can also write
1
m+n+2 ˚

−
cosm sinnd;
Ifnis odd,sinn is odd whilecosm is always even. Thus, the integral equals, for oddn, zero.
Since the l.h.s. of the expression (*) is symmetric inmandn, so is the r.h.s. and we get
¸
‖x‖2+‖y‖2<1
xmynd2(x,y)=0
whenevermornor both are odd.
If bothm andnare even, we get
¸
‖x‖2+‖y‖2<1
x>0,y>0
xmynd2(x,y)= ¸
‖x‖2+‖y‖2<1
±x>0,±y>0
xmynd2(x,y)
for any choice of signs, thus
¸
‖x‖2+‖y‖2<1
xmynd2(x,y)=4 ¸
‖x‖2+‖y‖2<1
x>0,y>0
xmynd2(x,y).
Introducing planar polar coordinates yields, as seen above, for evenm andn,
4 ¸
‖x‖2+‖y‖2<1
x>0,y>0
xmynd2(x,y)= 4
m+n+2 ˚
∕2
0
cosm sinnd
= 4
m+n+2 ˚
1
0
(1− t2)
m−1
2 (t2)
n−1
2 tdt
210

Solution Manual. Last update 18th July 2019
whereweusethesubstitution t=sin andcos=
√
1−sin 2=
√
1− t2. Afurthersubstitution
s=t2 yields
= 2
m+n+2 ˚
1
0
(1− s)
m−1
2 s
n−1
2 ds
= 2
m+n+2 ˚
1
0
(1− s)
m+1
2 −1s
n+1
2 −1ds
= 2
m+n+2 B m+1
2 , n+1
2

whichisEuler’sBetafunction. Thereisawell-knownrelationbetweentheEulerBeta-andGamma
functions:
B(x,y)= Γ(x)Γ(y)
Γ(x+y) (*)
so that, ﬁnally,
¸
‖x‖2+‖y‖2<1
xmynd2(x,y)=
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪⎩
0 m ornodd;
2
m+n+2
Γ
 m+1
2

Γ
 n+1
2

Γ
 n+m+2
2
 else
=
Γ
 m+1
2

Γ
 n+1
2

Γ
 n+m+4
2

where we also use the rule thatxΓ(x)=Γ( x+1).
Let us brieﬂy sketch the proof of (*): our calculation shows that
B(x,y)=2 ˚
∕2
0
sin2x−1cos2y−1d;
multiplyingthisformulawith r2x+2y−1e−r2
, integratingw.r.t.rover(0,∞)andchangingvariables
according tos=r2 yields on the one hand
˚
∞
0
B(x,y)r2x+2y−1e−r2
dr= 1
2 ˚
∞
0
B(x,y)sx+y−1e−sds
= 1
2B(x,y)Γ(x+y)
while, on the other hand, we get by switching from polar to cartesian coordinates,
˚
∞
0
B(x,y)r2x+2y−1e−r2
dr
=2 ˚
∞
0 ˚
∕2
0
sin2x−1cos2y−1r2x+2y−1e−r2
drd
=2 ˚
∞
0 ˚
∕2
0
(rsin)2x−1(rcos)2y−1e−r2
rdrd
=2 ¸(0,∞)×(0,∞)
2x−12y−1e−2−2
dd
=2 ˚(0,∞)
2x−1 e−2
d ˚(0,∞)
2y−1e−2
d
211

R.L. Schilling: Measures, Integrals & Martingales
= 1
2 ˚(0,∞)
sx−1e−sds ˚(0,∞)
ty−1e−tdt
= 1
2Γ(x)Γ(y)
with the obvious applications of Tonelli’s theorem and, in the penultimate equality, the obvious
substitutions.
■■
212

17 Dense and determining sets.
Solutions to Problems 17.117.9
Problem 17.1 Solution: Letf ∈ p()and ﬁx >0. It is enough to show that there is someℎ∈ 
suchthat ‖f−ℎ‖p ⩽. Sinceisdensein p(),thereexistssome g∈ satisfying‖f−g‖p ⩽
∕2. On the other hand, as is dense in, there is someℎ∈  such that‖g−ℎ‖p ⩽∕2. Now
the triangle inequality gives
‖f−ℎ‖p ⩽ ‖f−g‖p+‖g−ℎ‖p ⩽ 
2+ 
2.
■■
Problem 17.2 Solution:
(i) Continuityfollowsfromthecontinuityofthefunction x →d(x,A), cf.(17.1). Clearly,
0 ⩽uk ⩽1 andukðK =1 anduðUc
k =0 . SinceUK ↓K, we getuk ↓ 1K. SinceUk is
closed and bounded, it is clear thatUk is compact, i.e.suppuk is compact.
(ii) This follows from (i) and monotone convergence.
(iii) We have(K) =(K) for all compact setsK ⊂ Rn and the compact sets generate
the Borel-algebra. In particular, this holds for[−k,k]n ↑ Rn, so that the conditions
fortheuniquenesstheoremformeasures(Theorem5.7)aresatisﬁed. Weconcludethat
=.
(iv) Since eachx has a compact neighbourhood, we can choosek so large thatB1∕k(x)
becomescompact. Inparticular, K ⊂⋃
x∈KB1∕k(x)(x)isanopencover. Wecanchoose
eachk(x) so large, thatB1∕k(x)(x) has a compact closure. SinceK is compact, we ﬁnd
ﬁnitelymanyxi suchthat K ⊂⋃
iB1∕k(xi)(xi)= Uk wherek∶=max iki. Inparticular,
Uk⊂ ⋃
iB1∕(xi)(xi)iscompact. Thisproducesasequenceof Uk ↓K. Therestfollows
almost literally as in the previous steps.
■■
Problem 17.3 Solution:
(i) We have to show that‖ℎf‖p
p = ‖f‖p for allp ∈ p(dx). This is an immediate con-
sequence of the invariance of Lebesgue measure under translations:
‖ℎf‖p
p= ˚R
ðf(x−ℎ)ðpdx= ˚R
ðf(y)ðpdy= ‖f‖p
p.
213

R.L. Schilling: Measures, Integrals & Martingales
(ii) We show the assertion ﬁrst forf ∈Cc(R). Iff ∈Cc(R), thenK ∶=supp f is compact.
PickR> 0 in such a way thatK+B1(0)⊂BR(0). Sincelimℎ→0f(x−ℎ)= f(x)and
ðf(x−ℎ)− f(x)ð ⩽2‖f‖∞1BR(0)(x)∈ p(dx)
for anyℎ< 1, we can use dominated convergence to get
‖ℎf−f‖p
p= ˚ ðf(x−ℎ)− f(x)ðpdx , , , , , , , , , , , , , , , , , →
ℎ→0
0.
Now takef ∈ p(dx). Since Cc(R) is dense inp(dx), cf. Theorem 17.8, there is a
sequence(fn)n∈N⊂C c(R)such that‖fn−f‖p →0. From part (i) we get
‖ℎf−f‖p ⩽ ‖ℎ(f−fn)‖p
«››››››ﬂ››››››‹
⩽‖fn−f‖p
+‖ℎfn−fn‖p+‖fn−f‖p
, , , , , , , , , , , , , , , , , →
ℎ→0
2‖fn−f‖p , , , , , , , , , , , , , , , , , , , , →
n→∞
0.
This ﬁnishes the proof of the ﬁrst assertion. The second claim follows in a similar way.
Consider ﬁrstf ∈ Cc(R) andK ∶= suppf. SinceK is compact, there is someR >0
with(ℎ+K)∩ K =ç 1 for allℎ>R . Ifℎ>R , then
ðf(x−ℎ)− f(x)ðp= ðf(x−ℎ)ðp1K(x+ℎ)+ ðf(x)ðp1K(x)
and so
‖ℎf−f‖p
p= ˚K+ℎ
ðf(x−ℎ)ðpdx+ ˚K
ðf(x)ðpdx
= ˚K
ðf(y)ðpdy+ ˚K
ðf(x)ðpdx
=2 ‖f‖p
p.
Thisprovestheassertionfor f ∈Cc(R),andthegeneralcasefollowsviadensityasinthe
ﬁrst part of (ii).
■■
Problem 17.4 Solution:
(i) Continuity is an immediate consequence of the dominated convergence theorem: assume
that(xn)n∈N is a sequence converging tox∈ R. Since 1[xn−ℎ,xn+ℎ] → 1[x−ℎ,x+ℎ] a.e. and
f ∈ 1(dx), we see thatMℎf(xn) →Mℎf(x)asn →∞.
Contractivity ofMℎ follows from
˚ ðMℎf(x)ðdx= 1
2ℎ ˚
óóóóó˚
x+ℎ
x−ℎ
f(t)dt
óóóóó
dx
⩽ 1
2ℎ ˚
ℎ
−ℎ ˚ ðf(x+t)ðdx
«››››››››ﬂ››››››››‹
∫ ðf(y)ðdy=‖f‖1
dt ⩽ ‖f‖1
(use Tonelli’s theorem to interchange the order of integrations).
1We use the notationℎ+K ∶={ℎ+x;x∈K}.
214

Solution Manual. Last update 18th July 2019
(ii) Assume ﬁrst thatf ∈Cc(R). Because of the continuity of the functionf we ﬁnd
ðMℎf(x)− f(x)ð ⩽ 1
2ℎ ˚
ℎ
−ℎ
ðf(x+t)− f(x)ðdx ⩽ sup
t∈[−ℎ,ℎ]
ðf(x+t)− f(x)ð , , , , , , , , , , , , , , , , , →
ℎ→0
0
for allx ∈ R. Since the support off,K ∶= suppf, is compact, there is someR >0
suchthat K+B1(0)⊆BR(0). Forℎ< 1weget Mℎf(x)=0= f(x)ifx∉BR(0). Since
ðMℎf(x)ð ⩽ ðf(x)ðforx∈ R, we get
ðMℎf(x)− f(x)ð= ðMℎf(x)− f(x)ð1BR(0)(x) ⩽2‖f‖∞1BR(0)(x)∈ 1(dx).
An application of the dominated convergence theorem reveals
‖Mℎf−f‖1= ˚ ðMℎf(x)− f(x)ðdx
ℎ→0
, , , , , , , , , , , , , , , , , →0,
i.e. the claim is true for anyf ∈Cc(R). Now we take a generalf ∈ 1(dx). Because of
Theorem 17.8 there is a sequence(fn)n∈N⊂C c(R)such that‖fn−f‖1 →0. Therefore,
‖Mℎf−f‖1 ⩽ ‖Mℎ(f−fn)‖1
«›››››››ﬂ›››››››‹
=‖fn−f‖1
+‖Mℎfn−fn‖1+‖fn−f‖1
, , , , , , , , , , , , , , , , , →
ℎ→0
2‖fn−f‖1 , , , , , , , , , , , , , , , , , , , , →
n→∞
0.
■■
Problem 17.5 Solution:
(i) LetA ∈ ℬ(X) such thatf ∶= 1A ∈ p(). Clearly,(A) < ∞ and because of the
outer regularity of there is an open setU ⊂ Xsuch thatA ⊂ Uand(U) < ∞.
Literally as in the proof of Lemma 17.3 we can construct some ∈CLip(X)∩ p()
with‖f−‖p ⩽ (just replace in the proofCb(X)withCLip(X)).
(ii) Iff ∈ p(), then the Sombrero lemma shows that there is a sequence of simple func-
tions (fn)n∈N satisfying 0 ⩽ fn ⩽ f, fn ↑ f. Using the monotone convergence
theorem, we see∫(f −fn)pd ↓ 0; in particular, there is somen ∈ N such that
‖fn−f‖p ⩽ . Using linearity and the result of part (i), we get some ∈ CLip(X)
such that‖fn−‖p ⩽. Therefore,
‖f−‖p ⩽ ‖f−fn‖p+‖fn−‖p ⩽2.
(iii) We use the decompositionf = f+−f−. Sincef+,f − ∈ p(), part (ii) furnishes
functions , ∈ CLip(X)∩ p() such that‖f+−‖p ⩽  and ‖f−− ‖p ⩽ .
Consequently,
‖f−(− )‖p ⩽ ‖f+−‖p+‖f−− ‖p ⩽2.
■■
215

R.L. Schilling: Measures, Integrals & Martingales
Problem 17.6 Solution: A setU ⊂X is said to berelatively compactif it closureU is compact.
(i) Let(xn)n∈N be a countable dense subset ofX. By assumption, eachxn has a relatively
compact open neighbourhood:xn ∈ Vn andVn is compact. SinceB1∕k(xn) ⊂ Vn for
suﬃciently large values ofk ⩾ k0(xn), we see that the ballsB1∕k(xn),k ⩾ k0(xn), are
also relatively compact. Thus,
{B1∕k(xn)∶ n∈ N,k ⩾k0(xn)}=∶{ Un;n∈ N}
is a sequence of relatively compact, open sets. For any open setU ⊂X we ﬁnd
U =
˝
n∈N
Un⊂U
Un.
(The inclusion ‘⊃’ is obvious. In order to see ‘⊂’ we observe that for anyx∈U there
is somer >0 withBr(x) ⊂ U. Since(xn)n∈N is dense, we may choosen ∈ N and
k ⩾k0(xn)such thatB1∕k(xn)⊂B r(x)⊂U .)
(ii) The setsKn∶=U1∪⋯∪Un are compact and increase towardsX.
(iii) Assumethat U ⊂X isanopensetsuchthat (U)<∞andlet (Un)n∈N bethesequence
from part (i). Because of (i), there is a subsequence(Un(k))k∈N ⊂ (Un)n∈N such that
U = ⋃
kUn(k). Set Wn ∶= ⋃n
k=1Un(k) and observe thatWn ∈ . Since Wn ↑ U,
Beppo Levi’s theorem shows that
‖1Wn− 1U‖p , , , , , , , , , , , , , , , , , , , , →
n→∞
0.
This tells us that1U ∈ .
(iv) First we show that is outer regular. Set
Gn∶=
n˝
k=1
Uk.
Obviously, theGn are open sets,Gn ↑X and(Gn)<∞ – here we use that theUk are
relativelycompactandthat isﬁniteoncompactsets. Thismeansthattheassumptions
of Theorem H.3 are satisﬁed, and we see that is outer regular.
LetB∈ℬ(X),(B)<∞ and ﬁx >0. Since is outer regular, there is a sequence
of open sets(Un)n∈N such thatUn ⊃ Band(Un) < ∞. By monotone convergence,
‖1Un− 1B‖p →0asn →∞. Pickn∈ Nsuch that‖1Un− 1B‖p ⩽. Because of (iii),
there is someD∈ with‖1Un− 1D‖p ⩽. Consequently,
‖1B− 1D‖p ⩽ ‖IB− 1Un‖p+‖1Un− 1D‖p ⩽2.
(v) By deﬁnition, ⊂ p(), i.e. it is enough to show that for everyf ∈ p() and
 >0 there is someD ∈  such that‖f − 1D‖p ⩽ . Using the Sombrero lemma
(Corollary 8.9) and the dominated convergence theorem we can construct a sequence
216

Solution Manual. Last update 18th July 2019
ofsimplefunctions (fn)n∈N⊂ p()suchthat ‖f−fn‖p →0. Ifnissuﬃcientlylarge,
we have‖f−fn‖p ⩽. Sincefn is of the form
fn(x)=
NÉ
j=1
cj1Bj(x)
wherecj ∈ R, Bj ∈ ℬ(X), j = 1,…,N , we can use part (iv) to getD ∈  with
‖fn − 1D‖p ⩽ . With the triangle inequality we see that‖f − 1D‖p ⩽ 2. The
separability ofp()now follows from the fact that is a countable set.
■■
Problem 17.7 Solution:
(i) Assume ﬁrst thatAis an open set. Without loss of generalityA ≠ç. Fix >0. Since
$
x∈A∶d(x,Ac)< 1
n
%
↓ç asn →∞
the continuity of measures furnishes someN ∈ N such that

$
d(⋅,Ac)< 1
n
%
< ∀n ⩾N.
Deﬁnen(x) ∶= min{nd(x,Ac),1}. Clearly,n ∈ Cb(X) and ‖‖∞ ⩽1 =‖1A‖∞.
Since0 ⩽n ⩽ 1A∈ p we even haven∈ p(). Moreover,
{1A ≠n}⊂
$
d(⋅,Ac)< 1
n
%
;
therefore,{1A ≠n} ⩽ for alln ⩾N. Using dominated convergence gives‖1A−
n‖p , , , , , , , , , , , , , , , , , , , , →
n→∞
0. If n ⩾ N is large enough, we get‖1A−n‖p ⩽ . For suchn, the
functionsn satisfy all requirements of the theorem.
In order to show the claim for any Borel setA∈ℬ(X), we proceed as in the proof of
Lemma 17.3: letU ⊂X,(U)<∞, and deﬁne
D ∶={A∈ℬ(U)∶∀  >0 ∃ ∈Cb(X)∩p()satisfying the assertion forf = 1A}.
AsintheproofofLemma17.3weseethat D isaDynkinsystem. Byconstruction,the
open sets are contained inD, and soℬ(U)⊂D.
IfA∈ℬ(X) is an arbitrary Borel set with1A ∈ p(), we have(A)<∞. Since
isouterregular,thereexistsanopenset U ⊂X suchthat A⊂U and(U)<∞. Since
A∈ℬ(U)⊂D, the claim follows.
(ii) Letf ∈ p(),0 ⩽ f ⩽1, and ﬁx >0. Without loss of generality we may assume
that‖f‖∞=1 ,otherwisewewoulduse f∕‖f‖∞. The(proofofthe)Sombrerolemma
(Theorem 8.8) shows that
fn∶=
n2n−1É
k=0
k
2n 1$
k
2n ⩽f< k+1
2n
%+n1{f>n}
0 ⩽f ⩽1
=
2n−1É
k=0
k
2n 1$
k
2n ⩽f< k+1
2n
%, n ∈ N,
217

R.L. Schilling: Measures, Integrals & Martingales
monotonically converges tof. Withf0∶=0 we get
f = lim
n→∞
(fn−f0)= lim
n→∞
nÉ
j=1
(fj−fj−1)=
É
j⩾1
(fj−fj−1)=
É
j⩾1
1
2jj
forj ∶=2 j(fj−fj−1). We claim that
j(x)∈{0 ,1} ∀x∈
$
fj−1= k
2j−1
%
.. (⋆⋆)
Indeed: By deﬁnition,fj attains on
$
fj−1= k
2j−1
%
=
$
k
2j−1 ⩽f <k+1
2j−1
%
only the val-
ues 2k
2j and 2k+1
2j . Intheﬁrstcase,wehave j =0 ,inthelatter j =1 . Thus,j(x)=1
happens if, and only if,
x∈
$
fj = 2k+1
2j
%
=
$2k+1
2j ⩽f <2k+2
2j
%
.
Therefore, we can writeAj ∶={j =1} in the following form
Aj =
2n−1−1˝
k=0
$2k+1
2j ⩽f <2k+2
2j
%
.
Sincej = 1Aj, we get
f =
É
j⩾1
1
2j 1Aj.
Observethat 1Aj ⩽2jf ∈ p(). Becauseofpart(i),thereisforevery j ⩾1afunction
j, ∈Cb(X)∩ p()such that
‖j,−j‖p ⩽ 
2j,{j, ≠j} ⩽ 
2j and ‖j,‖∞ ⩽ ‖j‖∞ ⩽1.
The function ∶= ∑
j⩾1
j,
2j enjoys all required properties:
•  is continuous (since it is the uniform limit of continuous functions):
ôôôôôô
−
nÉ
j=1
j,
2j
ôôôôôô∞
⩽
∞É
j=n+1
1
2j‖j,‖∞ ⩽
∞É
j=n+1
1
2j , , , , , , , , , , , , , , , , , , , , →
n→∞
0.
• ‖‖∞ ⩽ ∑
j⩾1
‖j,‖∞
2j ⩽ ∑
j⩾1
1
2j =1= ‖f‖∞.
• ‖−f‖p ⩽ ∑
j⩾1
1
2j‖j,−j‖p ⩽∑
j⩾1
1
2j ⩽. In particular, ∈ p().
• { ≠f} ⩽ ∑
j⩾1{j, ≠j} ⩽ ∑
j⩾12−j =.
(iii) Observe,ﬁrstofall,thatthetheoremholdsforall g∈ p()with0 ⩽g ⩽ ‖g‖∞<∞;
for this, apply part (ii) tog∕‖g‖∞. Without loss of generality we may assume for such
g that ⩾0; otherwise we would consider ∶=∨0.
Letf ∈ p() and‖f‖∞<∞. We writef =f+−f− and, because of the preceding
remark, there are functions,  ∈Cb(X)∩ p(), ⩾0,  ⩾0, such that
‖‖∞ ⩽ ‖f+‖∞,  f+ ≠
 ⩽ and ‖f+−‖p ⩽
218

Solution Manual. Last update 18th July 2019
and
‖ ‖∞ ⩽ ‖f−‖∞,  f− ≠ 
 ⩽ and ‖f−− ‖p ⩽.
ForΦ ∶=−  ∈Cb(X)∩ p()we ﬁnd
{Φ ≠f} ⩽{ ≠f+}+ {  ≠f−} ⩽2
as well as
‖Φ‖∞ ⩽max{‖f+‖∞,‖f−‖∞}= ‖f‖∞
(this step requires that ⩾0 and  ⩾0). The triangle inequality yields
‖f−Φ‖p ⩽ ‖f+−‖p+‖f−− ‖p ⩽2.
Consequently,Φ satisﬁes the conditions of the theorem forf.
(iv) Fixf ∈ p()and >0. Using the Markov inequality we get
{ðfð ⩾R} ⩽ 1
Rp ˚ ðfðpd.
In particular, we can pick a suﬃciently largeR >0 such that{ðfð ⩾R} ⩽. Using
monotone convergence, we see
˚{ðfð>R}
ðfðpd<
ifR> 0 is large. SettingfR∶=(−R)∨ f∧R, we can use (iii) to construct a function
 ∈Cb(X)∩ p()with
‖‖∞ ⩽ ‖fR‖∞,  fR ≠
 ⩽ 
Rp and ‖fR−‖p ⩽.
Obviously,‖‖∞ ⩽ ‖f‖∞. Moreover,
‖−f‖p
p
= ˚
{ðfð⩽R}
ð−fðpd+ ˚
{ðfð>R}
∩{=fR}
ð−fðpd
«››››››››››››ﬂ››››››››››››‹
=∶I1
+ ˚
{ðfð>R}
∩{≠fR}
ð−fðpd
«››››››››››››ﬂ››››››››››››‹
=∶I2
⩽ ‖−fR‖p
p+I1+I2.
Let us estimateI1 andI2 separately. SincefRð{ðfð>R}=R, we get
I1= ˚{f>R}∩{=fR}
(f−R)pd+ ˚{f<−R}∩{=fR}
(−R−f)pd
⩽ ˚{f>R}∩{=fR}
fp
«ﬂ‹
ðfðp
d+ ˚{f<−R}∩{=fR}
(−f)p
«ﬂ‹
ðfðp
d
⩽ ˚{ðfð>R}
ðfðpd<.
219

R.L. Schilling: Measures, Integrals & Martingales
With the elementary estimate
ða+bðp ⩽C(p)(ap+bp) ∀a,b ⩾0, p⩾1 (♯)
(in fact,C(p)=2 p−1) we get
I2 ⩽C(p) ˚{ðfð>R}∩{≠fR}
ððpd+C(p) ˚{ðfð>R}∩{≠fR}
ðfðpd
⩽C(p)‖‖p
∞{ ≠fR}+ C(p) ˚{ðfð>R}
ðfðpd
⩽C(p)Rp 
Rp +C(p).
Therefore,
‖−f‖p
p ⩽p++2C(p).
Since >0 is arbitrary,‖−f‖p is as small as we want it to be. Finally,
{f ≠} ⩽{fR ≠}+ {ðfð ⩾R} ⩽2.
This shows that enjoys all required properties.
Remark: (♯) follows from Hölder’s inequality
óóóóóó
nÉ
j=1
xj⋅yj
óóóóóó
⩽
H nÉ
j=1
ðxjðp
I1
p
⋅
H nÉ
j=1
ðyjðq
I1
q
forx,y ∈ Rn andconjugateindices p,q ⩾1. Ifwetake,inparticular, d=2 ,x=(a,b),
y=(1,1), then
ða⋅1+ b⋅1ð ⩽(ðaðp+ðbðp)
1
p ⋅2
1
q.
Raising both sides to thepth power proves the estimate.
■■
Problem 17.8 Solution: We see immediately that∫ b
a p(x)f(x)dx = 0for all polynomialsp. Fix
g∈C[a,b]and >0. ByWeierstraß’theorem,thereissomepolynomialpsuchthat ‖g−p‖∞ ⩽.
Therefore,
óóóóó˚
b
a
g(x)f(x)dx
óóóóó
=
óóóó ˚
b
a
(g(x)− p(x))f(x)dx+ ˚
b
a
p(x)f(x)dx
«››››››››ﬂ››››››››‹
=0
óóóó
⩽ ˚
b
a
ðp(x)− g(x)ð
«›››››ﬂ›››››‹
⩽
ðf(x)ðdx
⩽ ˚
b
a
ðf(x)ðdx.
From this we conclude that
˚
b
a
g(x)f(x)dx=0 ∀ g∈C[a,b].
220

Solution Manual. Last update 18th July 2019
Deﬁne measures± by ±(dx) ∶= 1[a,b](x)1{±f>0}(x)dx. Then ∫ gd + = ∫ gd − for all
g ∈C[a,b]. According to Theorem 17.12,C[a,b] is a determining set, and so+ =−. This is
only possible if=0 , hencef =0 Lebesgue a.e.
■■
Problem 17.9 Solution:
(i) First of all, we note that it is enough to know that the polynomials are uniformly dense
intheset C[−1,1]. Thisfollowsimmediatelyfromtheobservationthatanyfunctionin
C[0,1] can be mapped ontoC[a,b] using the aﬃne transforma+t(b−a),t∈[0,1] –
and vice versa. Fixu∈C[−1,1] and deﬁne a sequence of polynomials(pn)n∈N by
pn(x)∶= 1
cn
0
x2
16−1
1n
, x ∈ R,
wherecn∶= ∫ 4
−4(x2∕16−1)ndx. Sinceu∈C[−1,1],thereissome  u∈C(R)suchthat
 u(x)=0 forðxð>2 and u(x)= u(x) forx∈[−1,1]. Deﬁne pn(x)∶= pn(x)1[−4,4](x)
and
un(x)∶=  u⋆ pn(x)= ˚  u(x−y) pn(y)dy, x ∈ R.
We ﬁnd
un(x)= ˚  u(x−y)pn(y)dy ∀x∈[−2,2],
since
ðxð ⩽2 - ⇒ u(x−y)=0 ∀ ðyð>2.
Using the fact that
un(x)= ˚  u(y)pn(x−y)dy, x ∈[−2,2]
we see thatunð[−2,2] is a polynomial. Let us show thatun →  uconverges uniformly –
and since uð[−1,1]=u, the claim follows. Using that pn ⩾0 and ∫  pndx=1 we get
óóun(x)−  u(x)óó=
óóóó˚ ( u(x−y)−  u(x)) pn(y)dy
óóóó
⩽ ˚
−1
R,1
R
ð u(x−y)−  u(x)ð pn(y)dy
+ ˚R⧵

−1
R,1
R
ð u(x−y)−  u(x)ð pn(y)dy
=∶I1(x)+ I2(x)
for allR >0. Let us boundI1 and I2 separately. Since u(x) = 0for ðxð > 2, the
function uis uniformly continuous and we get
I1(x) ⩽ sup
y∈

−1
R,1
R
ð u(x−y)−  u(x)ð ˚
−1
R,1
R
 pn(y)dy
221

R.L. Schilling: Measures, Integrals & Martingales
⩽ sup
y∈

−1
R,1
R
ð u(x−y)−  u(x)ð
, , , , , , , , , , , , , , , , , , , , , , →
R→∞
0
uniformly for allx. Because of the boundedness of uwe see that
I2(x) ⩽2‖ u‖∞ ˚R⧵

−1
R,1
R
 pn(y)dy.
Since pn(y) ↓0forally ≠0,wecanusethemonotoneconvergencetheoremtoconclude
thatI2 , , , , , , , , , , , , , , , , , , , , →
n→∞
0uniformly inx. This proves the claim.
(ii) Fixu ∈ Cc[0,∞). Since u has compact support,u(x) = 0for largex; in particular,
u◦(−log)(x)=0 ifx is small. Therefore,
⎧
⎪
⎨
⎪⎩
u◦(−log)(x), x ∈(0,1]
0, x =0,
deﬁnesacontinuousfunctionon [0,1]. Accordingto(i),thereisasequenceofpolyno-
mials(pn)n∈N withpn →u◦(−log) uniformly.
(iii) Forp(x)∶= xn we obviously havep(e−t)= e−nt=n(t)and, by assumption,
˚ p(e−t)(dt)= ˚ n(t)(dt)= ˚ n(t)(dt)= ˚ p(e−t)(dt). (⋆)
Using the linearity of the integral, this equality extends to arbitrary polynomialsp.
Assume thatu ∈ Cc[0,∞) and (pn)n∈N as in (ii). Sincepn converges uniformly to
u◦(−log), we can interchange integration and limit to get
˚ ud = ˚ (u◦(−log))(e−t)(dt)
= lim
n→∞ ˚ pn(e−t)(dt)
(⋆)
= lim
n→∞ ˚ pn(e−t)(dt)
= ˚ (u◦(−log))(e−t)(dt)
= ˚ ud.
■■
222

18 Hausdor measure.
Solutions to Problems 18.118.7
Problem 18.1 Solution: This is clear from the monotonicity of the inﬁmum and the fact that there
are moreP--covers thanC--covers, i.e. we have


,P(A) ⩽ 

,C(A).
■■
Problem 18.2 Solution: From the proof of Corollary 18.10 we know, using the monotonicity of
measures


(A)= (G) = lim
k→∞
(Uk)
Uk ⊃A
⩾ inf (U)∶ U ⊃A, Uopen U ⊃A
⩾ 

(A).
When using the monotonicity we must make sure that(Uk) < ∞ – this we can enforce by
Uk ⇝Uk∩U (whereU is the open set with ﬁnite Hausdorﬀ measure).
For counting measure this is clearly violated: Any open setU ⊃ A∶= {a} has inﬁnitely many
points! NeverthelessAis itself aG-set.
■■
Problem 18.3 Solution: By Corollary 18.10 there are open setsUi such thatH ∶= ⋂
iUi ⊃ Band
(H ⧵B)=0 or (H)= (B). Now we can write eachUi as anF-set:
Ui=
˝
Br(x)⊂Ui,x∈Ui
Br∕2(x)
isindeedacountableunionofclosedsets,since Ui⊂X containsacountabledensesubset. Sowe
have
Ui=
˝
k
Fik for closed setsFik.
Without loss of generality we may assume that the setsFik increase ink, otherwise we would
considerFi1∪⋯∪Fik. By the continuity of measure (here we require the measurability ofB!)
we have
lim
k→∞
(B∩Fik)= (B∩Ui)= (B).
223

R.L. Schilling: Measures, Integrals & Martingales
In particular, for every >0there is somek(i)with
(B ⧵Fik(i)) ⩽∕2i, i ∈ N.
Consider the closed setF = ⋂
iFik(i) and observe that
(F) ⩾ (F ∩B) ⩾ (B)−
É
i
(B ⧵Fik(i)) ⩾ (B)−
É
i

2i = (B)− .
SinceF ⊂⋂
iUi, we get
(F ⧵B) ⩽ 
0Ì
i
Ui ⧵B
1
= (H ⧵B)=0 .
By Corollary 18.10, the setF ⧵B is contained in aG-setG= ⋂
iVi (where theVi are open sets)
such that(G)=0= (F ⧵B). Thus,
F ⧵G=F ∩
˝
i
Vc
i =
˝
i
F ∩Vc
i
«ﬂ‹
closed
is anF-set insideB – we haveF ⧵G⊂F ⧵(F ⧵B)⊂B – and
(F ⧵G) ⩾ (F)− (G) ⩾ (B)− .
Now consider = 1
n and take unions of the thus obtainedF-sets. But, clearly, countable unions
ofF-sets are stillF.
■■
Problem 18.4 Solution: FixA⊂ Rn. We have to show that for anyQ⊂ Rn the equality
#Q=#(Q∩A)+#( Q ⧵A)
holds. We distinguish between two cases.
Case 1:#Q=∞ . Then at least one of the terms#(Q∩A),#(Q ⧵A) on the right-hand side must
be inﬁnite, so the equality is clear.
Case2: #Q< ∞. Thenbothsets (Q∩A),(Q ⧵A)areﬁniteand,assuch,theyaremetricallysepar-
ated. Therefore we can use the fact that
0
(A)=#( A) is a metric outer measure (Theorem 18.5)
to get equality.
■■
Problem 18.5 Solution: Use Lemma 18.17 to see0 ⩽ dimB ⩽ dim Rn as B ⊂ Rn. From
Example 18.18 we know thatdim Rn=n.
IfBcontainsanopenset U (orasetofnon-zeroLebesguemeasure),wesee n(B) ⩾ n(U)>0;
intersect with a large open ballK to make sure thatn(B∩K)<∞ andU∩K ⊂B∩K. This
showsn=dim (B∩K) ⩽dim(B) ⩽n.
■■
224

Solution Manual. Last update 18th July 2019
Problem 18.6 Solution: By self-similarity, we see for the Sierpinski triangle of generationi,Si−1
and its follow-up stageSi = Si
1∪Si
2∪Si
3 that theSi
k’s are scaled versions ofS with a factor1
2.
So,
s(Si−1)= s(Si
1)+ s(Si
2)+ s(Si
3)=3 ⋅2−ss(Si−1)
anddividingby s(Si−1)andsolvingtheequality 1=3 ⋅2−s ⇐ ⇒2s=3 ⇐ ⇒s=log3∕log2
Koch’s snowﬂakeS has in each subsequent generation stage4new parts, each scaled by1∕3, so
s(S)= s(S1)+ s(S2)+ s(S3)+ s(S4)=4 ⋅3−ss(S)
and dividing bys(S)and solving the equality1=4 ⋅3−s ⇐ ⇒3s=4 ⇐ ⇒s=log4∕log3 .
■■
Problem 18.7 Solution: Let(Si)i∈N be an-cover ofA. Then we have
∞É
i=1
(diamUi)=
∞É
i=1
(diamUi)
 (diamUi) (diamUi)
⩽
∞É
i=1
sup
x⩽
(x)
 (x) (diamUi)
=sup
x⩽
(x)
 (x)
∞É
i=1
 (diamUi).
Taking the inf over all admissible-covers shows


(A) ⩽sup
x⩽
(x)
 (x) 
 
(A) ⩽sup
x⩽
(x)
 (x) 
 
(A).
Letting →0yields


(A)=lim
→0


(A) ⩽lim
→0
sup
x⩽
(x)
 (x) 
 
(A)=limsup
x→0
(x)
 (x) 
 
(A)=0 .
■■
225



19 The Fourier transform.
Solutions to Problems 19.119.9
Problem 19.1 Solution:
(a) By deﬁnition,
ƒ1[−1,1]()= 1
2 ˚ 1[−1,1](x)e−ix dx
= 1
2
4
−e−ix
i
51
x=−1
= 1
2
1
i
 ei −e−i
= 1

sin

for ≠0. Here we use thatsin=Im ei = 1
2i(ei−e−i). For=0 we have
ƒ1[−1,1](0)= 1
2 ˚ 1[−1,1](x)dx= 1
.
(Notethat sin
 →1as →0,i.e.theFouriertransformiscontinuousat =0 –asonewould
expect.)
(b) Theconvolutiontheorem,Theorem19.11,showsthat £f ∗g=(2) ̂f⋅̂ g. Becauseofpart(a)
we get
ℱ(1[−1,1]∗ 1[−1,1])()=(2 )
0
1

sin

12
= 2

sin2
2 .
(c) We get from the deﬁnition that
ℱ(e−(⋅)1[0,∞)(⋅))()= 1
2 ˚
∞
0
e−xe−ix dx
= 1
2 ˚
∞
0
e−x(1+i)dx
=− 1
2
1
1+ i
e−x(1+i)∞
x=0
= 1
2
1
1+ i.
(d) Obviously, we have
˚ e−ixe−ðxð= ˚(−∞,0)
e−ixexdx+ ˚(0,∞)
e−ixe−xdx
227

R.L. Schilling: Measures, Integrals & Martingales
= ˚(0,∞)
eiye−ydy+ ˚(0,∞)
e−ixe−xdx.
Thus,
ℱ(e−ð⋅ð)()= ℱ(e−⋅1[0,∞))(−)+ ℱ(e−⋅1[0,∞))()
(c)
= 1
2
0
1
1− i + 1
1+ i
1
= 1

1
1+ 2.
(e) From (d) andℱ◦ℱ u(x)=(2 )−1u(−x)(cf. Corollary 19.24) we ﬁnd
ℱ
0
1
1+ x2
1
()
(d)
= ⋅ℱ◦ℱ (e−ð⋅ð)()= 1
2e−ð−ð= 1
2e−ðð.
(f) Note that
˚[−1,1]
(1− ðxð)e−ix dx= ˚[−1,1]
e−ix dx+ ˚[−1,0]
xe−ix dx− ˚[0,1]
xe−ix dx
= ˚[−1,1]
e−ix dx+ ˚[0,1]
(−y)eiy dy− ˚[0,1]
xe−ix
= ˚[−1,1]
e−ix dx− ˚[0,1]
x(eix +e−ix)
«›››››ﬂ›››››‹
2cos(x)
dx.
The ﬁrst expression is as in part (a). For the second integral we use integration by parts:
˚
1
0
xcos(x)dx=
4
xsin(x)

51
x=0
−1
 ˚
1
0
sin(x)dx
= sin()
 −1

4cos(x)

51
x=0
= sin()
 −cos()
2 + 1
2.
Thus,
ℱ(1[−1,1](1− ð⋅ð))()= 1

sin
 − 1

0sin
 −cos
2 + 1
2
1
= 1

1−cos 
2 .
(g) By deﬁnition,
ℱ
H ∞É
k=0
tk
k!e−tk
I
()= 1
2 ˚ e−ix
∞É
k=0
tk
k!e−tk(dx)= 1
2
∞É
k=0
tk
k!e−te−ik.
Sincee−ik =(e−i)k, we conclude that
ℱ
H ∞É
k=0
tk
k!e−tk
I
()= 1
2
∞É
k=0
(te−i)k
k! e−t= 1
2e−tete−i
= 1
2et(e−i−1).
228

Solution Manual. Last update 18th July 2019
(h) The same calculation as in (g) yields
ℱ
H kÉ
n=0
0
n
k
1
pkqn−kk
I
()= 1
2 ˚ e−ix
nÉ
k=0
0
n
k
1
pkqn−kk(dx)
= 1
2
nÉ
k=0
0
n
k
1
pkqn−ke−ik
= 1
2
nÉ
k=0
0
n
k
1
(pe−i)kqn−k
= 1
2
 pe−i+qn
.
In the ﬁnal step we use the binomial theorem.
■■
Problem 19.2 Solution: Observe that for complex numbersu,v ∈ C
ðu+vð2=(u+v)(u+v)
=(u+v)(̄ u+ ̄ v)
=ū u+ū v+v̄ u+v̄ v
= ðuð2+2Re ū v+ðvð2
and so, settingv ⇝−v
ðu−vð2= ðuð2−2Re ū v+ðvð2
and so, settingv ⇝iv
ðu+ivð2= ðuð2+2Im ū v−ðvð2
and so, settingv ⇝−iv
ðu−ivð2= ðuð2−2Im ū v−ðvð2
And this gives
ðu+vð2−ðu−vð2+iðu+ivð2−iðu−ivð2=4Re ū v+4iImū v=4ū v.
Thus, we have the following ‘polarization’ formula
˚ ū vdx= 1
4
4
˚ ðu+vð2dx− ˚ ðu−vð2dx+i ˚ ðu+ivð2dx−i ˚ ðu−ivð2dx
5
= 1
4
‖u+v‖2
2−‖u−v‖2
2+i‖u+iv‖2
2−i‖u−iv‖2
2

and now the claim follows directly from the statement of Plancherel’s theorem.
Alternativesolution: MimictheproofofTheorem19.20: Wehave u,v, u, v∈L2(n)(asaresult
of Theorem 19.20), and sou⋅ ̄ vand u⋅ vare integrable. Therefore,
˚  u() v()d = (2)−n
˚  u()v()d
229

R.L. Schilling: Measures, Integrals & Martingales
19.12
= (2)−n
˚ u(x)ℱv(x)dx
19.9
= (2)−n
˚ u(x)v(x)dx.
■■
Problem 19.3 Solution: Assume that =. We have
() = ˚ e−ix(dx)
 =
= ˚ e−ix  (dx)
15.1
= ˚ e−i(−x)(dx)
= ˚ e−ix(dx)
= ˚ e−ix(dx)
= ().
Therefore, is real-valued. On the other hand, the above calculation shows that
()= ˚ e−ix (dx).
This means that = entailsℱ=ℱ , and so=  because of the injectivity of the Fourier
transform.
■■
Problem 19.4 Solution: From linear algebra we know that a symmetric positive deﬁnite matrix has
a unique symmetric positive square root, i.e. there is someB ∈ Rn×n which is symmetric and
positive deﬁnite such thatB2 = A. Sincedet(B2) = (detB)2, we see thatdetB =
√
detA >0.
Now we change coordinates according toy∶=Bx
˚ e−i⟨x,⟩e−⟨x,Ax⟩dx= ˚ e−i⟨x,⟩e−⟨Bx,Bx⟩dx
= 1
detB ˚ e−i⟨B−1y,⟩e−ðyð2
dy
= 1√
detA ˚ e−i⟨y,B−1⟩e−ðyð2
dy.
If we set
g1∕2(x)∶= 1
n∕2exp −ðxð2,
cf. Example 19.2(iii), then the calculation from above gives
ℱ(e−⟨⋅,A⋅⟩)()= n∕2
√
detA
ℱ(g1∕2) B−1.
230

Solution Manual. Last update 18th July 2019
Example 19.2(iii) now shows
ℱ(e−⟨⋅,A⋅⟩)()= n∕2
√
detA
1
(2)nexp
0
−ðB−1ð2
4
1
.
Finally, sinceB−1=(B−1)⊤,
ðB−1ð2= ⟨B−1,B −1⟩= ⟨,(B−1B−1
«›ﬂ›‹
A−1
)⟩,
we infer that
ℱ(e−⟨⋅,A⋅⟩)()= 1√
detA
1
2n∕2
1
(2)n∕2exp
0
−⟨,A−1⟩
4
1
.
■■
Problem 19.5 Solution: gt(x) = (2t)−1∕2e−x2∕2t and  gt() = (2)−1e−t2∕2. By Plancherel’s the-
orem (Theorem 19.20, plus polarization) or by Problem 19.2 we see that
˚  u()e−tðð2∕2d =(2) ˚  u() gt()d
= ˚ u(x)gt(x)dx
= ˚ u(x)(2t)−1∕2e−x2∕2tdx
=(2)−1∕2
˚ u(ty)e−y2∕2dy
⩽c‖u‖∞.
(In fact,c =1 , see Example 14.11). Now lett ↑0 using monotone convergence and use that, by
assumption, u⩾0.
The same argument holds forL2-functions sincegt∈L2.
■■
Problem 19.6 Solution: We follow the hint and ﬁnd using Fubini’s theorem
2
R
2
n
˚
1∕R
−1∕R
⋯ ˚
1∕R
−1∕R ˚Rn
(1− ei⟨x,⟩)(dx)d1…dd
=2 ˚Rn
R
2
n
˚
1∕R
−1∕R
⋯ ˚
1∕R
−1∕R
(1− ei⟨x,⟩)d1…dd(dx)
=2 ˚Rn
R
2 ˚
1∕R
−1∕R
…R
2 ˚
1∕R
−1∕R
(1− ei⟨x,⟩)d1…dd(dx)
=2 ˚Rn
H
1− R
2 ˚
1∕R
−1∕R
…R
2 ˚
1∕R
−1∕R
ei⟨x,⟩d1…dd
I
(dx)
=2 ˚Rn
H
1−
n˙
n=1
R
2 ˚
1∕R
−1∕R
eixnndn
I
(dx)
231

R.L. Schilling: Measures, Integrals & Martingales
=2 ˚Rn
H
1−
n˙
n=1
R
2
4
eixnn
ixn
5n=1∕R
n=−1∕R
I
(dx)
=2 ˚Rn
H
1−
n˙
n=1
eixn∕R−e−ixn∕R
2ixn∕R
I
(dx)
=2 ˚Rn
H
1−
n˙
n=1
sin(xn∕R)
xn∕R
I
(dx)
⩾2 ˚Rn⧵[−2R,2R]n
H
1−
n˙
n=1
sin(xn∕R)
xn∕R
I
(dx).
In the last step we use that the integrand is positive sinceðsiny∕yð ⩽1. Observe that
x∈ Rn ⧵[−2R,2R]n ⇐ ⇒∃n=1,…,n ∶ ðxnð>2R
and so
n˙
n=1
sin(xn∕R)
xn∕R ⩽ 1
2
hence
2
R
2
n
˚
1∕R
−1∕R
⋯ ˚
1∕R
−1∕R ˚Rn
(1− ei⟨x,⟩)(dx)d1…dd
⩾2 ˚Rn⧵[−2R,2R]n
H
1−
n˙
n=1
sin(xn∕R)
xn∕R
I
(dx)
⩾2 ˚Rn⧵[−2R,2R]n

1− 1
2

(dx)
⩾ ˚Rn⧵[−2R,2R]n
(dx).
Remark. A similar inequality exists for the Fourier transform (instead of the inverse Fourier
transform). This has the form
(Rn ⧵[−2R,2R]n) ⩽2(R)n
˚[−1∕R,1∕R]n
  (0)−Re  () d.
■■
Problem 19.7 Solution:
(i) Let1,…,n ∈ Rn and1,…,n ∈ C. From the deﬁnition of the Fourier transform
we get
nÉ
i,k=1
(j−k)j̄k= 1
(2)n
nÉ
j,k=1
j̄k ˚ e−ix(j−k)d(x)
= 1
(2)n
nÉ
j,k=1
j̄k ˚ e−ixje−ixkd(x)
= 1
(2)n ˚
H nÉ
j=1
je−ixj
IH nÉ
k=1
ke−ixk
I
d(x)
232

Solution Manual. Last update 18th July 2019
= 1
(2)n ˚
óóóóóó
nÉ
j=1
je−ixj
óóóóóó
2
d(x) ⩾0.
Note that this already implies that(−) =(). The argument is as follows: If we
have for a matrix(ajk)that∑
jkajkj̄j ⩾0, then
0 ⩽
É
jk
ajkj̄k=
É
jk
ajkj̄k=
É
jk
ajk̄jk=
É
kj
akj̄kj
which means thatajk =akj. Apply this to the matrixajk =(j−k) withm=2 and
1= and2=0 to infer that()= (−).
(ii) We want to use the diﬀerentiability lemma for parameter-dependent integrals. For this
we deﬁne
u(,x)∶= 1
(2)ne−ix.
Since is a ﬁnite measure andðu(x,)ð ⩽(2)−n, we ﬁndu(,⋅)∈ L1(). Moreover,
ð)ju(,x)ð=(2)−dðxjð ⩽(2)−dðxð
⩽(2)−d 1[−1,1](x)+ ðxðm1R⧵[−1,1](x)=∶w(x)∈ L1()
is an integrable majorant. With Theorem 12.5 we ﬁnd
)j()= )j ˚ u(,x)(dx)= 1
(2)n ˚ (−ixj)e−ix(dx).
Iterating this argument, we see that)exists for any∈ Nn
0 such thatðð ⩽m.
(iii) We follow the hint and consider ﬁrst the cased = 1andn = 1. We can rewrite the
expression(2ℎ)−2 (0)+ (−2ℎ)using Fourier transforms:
(2ℎ)−2 (0)+ (−2ℎ)= 1
2 ˚ (e−i2ℎx−2+ ei2ℎx)(dx)
= 1
 ˚ (cos(2ℎx)−1) (dx).
L’Hospital’s theorem applies and gives
1−cos(2 y)
4y2
y→0
, , , , , , , , , , , , , , , , , →1
2.
Now we can use Fatou’s lemma
˚ x21
2(dx)= ˚ x2lim
ℎ→0
1−cos(2 ℎx)
4(ℎx)2 (dx)
⩽liminf
ℎ→0
1
4ℎ2 ˚ (1−cos(2 ℎx))(dx)
=−liminf
ℎ→0
1
4ℎ2
 (2ℎ)−2 (0)+ (−2ℎ))
=−‡‡(0)<∞.
233

R.L. Schilling: Measures, Integrals & Martingales
Ifn ⩾ 1, we use induction. Assume that ∈ C2n(R) and that the assertion has been
provedforn−1. Since∈C2n(R) ⇒∈C2(n−1),weseebytheinductionassumption
that ∫ ðxð2(n−1)d(x)<∞. Thus,(dx)∶= x2(n−1)(dx)is a measure and
 ()= 1
2 ˚ x2(n−1)e−ix d(x)
= 1
2
1
(−i)2(n−1)
d2(n−1)
d2(n−1) ˚ e−ix d(x).
Consequently, we see that̂ ∈C2(R). The ﬁrst part of the proof (n=1 ) gives
˚ ðxð2nd(x)= ˚ ðxð2d(x)<∞.
Ifd ⩾1, then we setj(x)∶= xj,x∈ Rn,j∈{1,…,d}. Apply the cased=1 to the
measuresj().
(iv) Assumethat z∈ Cn. IfK ∶=supp iscompact,thenweget,becauseofthecontinuity
ofe−izx, thatM ∶=sup x∈K ðe−izxð<∞. From
˚ ud = ˚supp
ud for anyu ⩾0
we conclude that
˚ ðe−izxðd(x) ⩽M(Rn)<∞,
i.e.
(z)= 1
(2)n ˚ e−izx d(x)
is well-deﬁned. Setting
un(x)∶= 1
(2)n
nÉ
k=0
(−izx)k
k! , x ∈ Rn,
we get
ðun(x)ð ⩽ 1
(2)n
nÉ
k=0
ðzxðk
k! ⩽ 1
(2)neðzxð ⩽ 1
(2)n sup
x∈K
eðzxð<∞.
Since is a ﬁnite measure, we can use the dominated convergence theorem to get
(z)= ˚ lim
n→∞
un(x)(dx)
= lim
n→∞ ˚ un(x)d(x)
= 1
(2)n
∞É
k=0
1
k! ˚ (zx)kd(x).
This proves that is analytic.
■■
234

Solution Manual. Last update 18th July 2019
Problem 19.8 Solution: Note thateix∕n n→∞
, , , , , , , , , , , , , , , , , , , , →1 for allx ∈ R. On the other hand, we gather from
∫Beix∕ndx = 0that 1Bei⋅∕n ∈ 1(dx). As ðeix∕nð = 1, we get1(B) < ∞. By dominated
convergence
0= lim
n→∞ ˚B
eix∕ndx= ˚B
lim
n→∞
eix∕n
«››ﬂ››‹
1
dx=1(B).
Alternative solution:Setf(x) ∶=1B(x); by assumption,̂f(1∕n) = 0. Since the Fourier trans-
form is continous, cf. 19.3, we get
̂f(0)= lim
n→∞
̂f
1
n

=0.
On the other hand,̂f(0)=(2 )−11(B).
■■
Problem 19.9 Solution:
(i) ⇐: Since(R ⧵ 2
 Z)=0 we ﬁnd
=
É
j∈Z
pj2
 Z
withpj ∶=(2
 j). From the deﬁnition of the Fourier transform we get
̂ ()= 1
2 ˚ e−ix(dx)
= 1
2
É
j∈Z
pjexp
4
−i
0
2
 j
1

5
for all∈ R. Setting=, we see
̂ ()= 1
2
É
j∈Z
pjexp(−i2j)
«›››ﬂ›››‹
1
= 1
2
É
j∈Z
pjexp(−i0)= ̂ (0).
⇒: From̂ ()= ̂ (0)we conclude
2(̂ (0)− ̂ ())= ˚ (1− e−ix)(dx)=0 .
In particular,∫(1− e−ix)(dx)∈ R, i.e.
˚ (1− e−ix)(dx)=Re ˚ (1− e−ix)(dx)= ˚ (1−cos( x))(dx)=0 .
Since1−cos( x) ⩾0, this implies
{x∈ R;1−cos( x)>0}=0.
Consequently,
0= {x∈ R;cos(x) ≠1}=
0
R ⧵2
 Z
1
.
235

R.L. Schilling: Measures, Integrals & Martingales
(ii) Because ofð (1)ð=  (0)there is somez1∈ R such that
 (1)=  (0)eiz11.
Therefore,
1
2 ˚ e−i1(x+z1)(dx)= ̂ (0).
Observethattheleft-handsideisjusttheFouriertransformofthemeasure (B)∶= (B−
z1),B∈ℬ(R), and so
̂ (1)= ̂ (0)= ̂ (0).
From part (i) we get that(R ⧵ 2
1
Z)=0 . This is the same as

<
R ⧵
0
z1+2
1
Z
1=
=0.
Using the same argument we ﬁnd somez2∈ R, such that

<
R ⧵
0
z2+2
2
Z
1=
=0.
Setting
A∶=
0
z1+2
1
Z
1
∩
0
z2+2
2
Z
1
we see that(R ⧵A)=0 . Let us show thatA contains at most one element: Assume, on
thecontrary,thattherearetwodistinctpointsin A,thenthereare n,n‡∈ Zandm,m‡∈ Z
such that
z1+2
1
n=z2+2
2
n‡,
z1+2
1
m=z2+2
2
m‡.
Subtracting these identities, we get
2
1
(n−m)= 2
2
(n‡−m‡)
⇒ 2
1
= n‡−m‡
n−m ∈ Q.
This is clearly contradicting the assumption1
2
∉ Q.
■■
236

20 The RadonNikodým theorem.
Solutions to Problems 20.120.9
Problem 20.1 Solution: The assumption ⩽ immediately implies ≪. Indeed,
(N)=0 - ⇒0 ⩽(N) ⩽(N)=0 - ⇒(N)=0 .
Using the Radon–Nikodým theorem we conclude that there exists a measurable functionf ∈
+(A) such that = f ⋅. Assume thatf >1 on a set of positive-measure. Without loss
of generality we may assume that the set has ﬁnite measure, otherwise we would consider the
intersectionAk∩{f >1}with some exhausting sequenceAk ↑X and(Ak)<∞.
Then, for suﬃciently small >0we know that({f ⩾1+ })>0 and so
({f ⩾1+ })= ˚{f ⩾1+}
fd
⩾(1+ ) ˚{f ⩾1+}
d
⩾(1+ )({f ⩾1+ })
⩾({f ⩾1+ })
which is impossible.
■■
Problem 20.2 Solution: Because of our assumption both ≪ and ≪ which means that we
know
=f and =g
for positive measurable functionsf,g which are a.e. unique. Moreover,
=f =f⋅g
so thatf⋅g is almost everywhere equal to1 and the claim follows.
Because of Problem 20.4 (which is just Corollary 25.6) it is clear thatf,g < ∞ a.e. and, by the
same argument,f,g >0 a.e.
Note that we do not have to specifyw.r.t. which measurewe understand the ‘a.e.’ since their null
sets coincide anyway.
■■
237

R.L. Schilling: Measures, Integrals & Martingales
Problem 20.3 Solution: Take Lebesgue measure ∶= 1 on(R,ℬ(R)) and the functionf(x) ∶=
x+∞ ⋅ 1[0,1]c(x). Thenf⋅is certainly not-ﬁnite.
■■
Problem 20.4 Solution: See the proof of Corollary 25.6.
■■
Problem 20.5 Solution: See the proof of Theorem 25.9.
■■
Problem 20.6 Solution: (i) IfF is AC, continuity is trivial, just takeN =2 in the very deﬁnition of
AC functions.
To see thatF is also BV, we take = 1and choose >0 such that for any subcollectiona ⩽
x1 < y1 < ⋯ < xN < yN ⩽ b with ∑
n(yn−xn) < we have∑
nðF(yn)− F(xn)ð < 1. Let
M =[(b−a)∕]+1 andai=a+i(b−a)∕M fori=0,1,…,M . Clearly,ai−ai−1=(b−a)∕M <
and, in particular,V(f,[ai−1,ai])<1for alli=0,1,…M. Thus,
V(f;[a,b]) ⩽
MÉ
i=1
V(f,[ai−1,ai])<M.
(ii)Following thehint, wesee thatf isincreasing. Deﬁneg∶=F−f. Wehaveto showthat g is
increasing. Letx<y . Obviously,
V(f;[a,x])+ F(y)− F(x) ⩽V(f;[a,x])+ ðF(y)− F(x)ð ⩽V(f;[a,y])
(since the pointsx<y can be added to extend any partition of[a,x] to give a partition of[a,y]).
This givesg(x) ⩽g(y).
(iii) Fix >0 and pickR=R()in such a way that
˚{ðfð>R}
ðfðd< 
2.
This is possible sincef is integrable: use, e.g. monotone convergence. Now pickx1<y 1<x 2<
y2 <⋯ < xN < yN with ∑N
n=1ðyn−xnð < where = () ∶=∕(2R) with theR we’ve just
chosen. Then
ðF(yn)− F(xn)ð ⩽ ˚[xn,yn)
ðf(t)ð(dt)
= ˚[xn,yn)∩{ðfð⩽R}
ðf(t)ð(dt)+ ˚[xn,yn)∩{ðfð>R}
ðf(t)ð(dt).
Summing overn=1,…,N gives
NÉ
n=1
ðF(yn)− F(xn)ð ⩽R
NÉ
n=1
ðyn−xnð+
NÉ
n=1 ˚[xn,yn)∩{ðfð>R}
ðfðd. ⩽R+ ˚{ðfð>R}
ðfðd ⩽.
238

Solution Manual. Last update 18th July 2019
(iv) WriteF = f1−f2 with fi increasing (see part (ii)). From (ii) we know that we can pick
f1(x)= V(F,[a,x]). SinceF is absolutely continuous, so isf1, hencef2. This follows from the
observation that
V(F,[a,y])− V(F,[a,x])= V(F,[x,y]) ∀ x<y.
Sincethe fiarecontinuous,theset-functions i[a,x)∶= fi(x)−fi(a)arepre-measuresandextend
to measures on the Borel-algebra – see also Problem 6.1.
Now letN be a Lebesgue null-set. For every >0 we can coverN by ﬁnitely many intervals
[xi,yi] such that∑
i(yi −xi) < . Without loss of generality we can make the intervals non-
overlapping and their length is still< . Since thefi are AC, we ﬁnd for every some such
that
É
n
ðfi(yn)− fi(xn)ð<.
In particular,
i(N) ⩽
É
n
i([xn,yn])<,
which shows that the Lebesgue null-set is also ai-null set, i.e.i ≪ and therefore the claim
follows from the Radon–Nikodým theorem.
■■
Problem 20.7 Solution: Thisproblemissomewhatill-posed. Weshouldﬁrstembeditintoasuitable
context, say, on the measurable space(R,ℬ(R)). Denote by = 1 one-dimensional Lebesgue
measure. Then
= 1[0,2] and = 1[1,3]
and from this it is clear that
= 1[1,2]+ 1(2,3]= 1[1,2]+ 1(2,3]
and from this we read oﬀ that
1[1,2] ≪
while
1(2,3]⊥.
It is interesting to note how ‘big’ the null-set of ambiguity for the Lebesgue decomposition is—it
is actuallyR ⧵[0,3] a, from a Lebesgue (i.e.) point of view, huge and inﬁnite set, but from a
--perspective a negligible, namely null, set.
■■
239

R.L. Schilling: Measures, Integrals & Martingales
Problem 20.8 Solution: Sincewedealwithaboundedmeasurewecanuse F(x)∶= (−∞,x)rather
than the more cumbersome deﬁnition forF employed in Problem 6.1 (which is good for locally
ﬁnite measures!).
Withrespecttoone-dimensionalLebesguemeasure wecandecompose  accordingtoTheorem
20.4 into
=◦+⊥ where ◦≪,  ⊥⊥.
Nowdeﬁne2 ∶=◦ andF2 ∶=◦(−∞,x). We have to prove property (2). For this we observe
that◦ isaﬁnitemeasure(since ◦ ⩽ andthat,therefore, ◦=f⋅withafunction f ∈L1().
Thus, for everyR> 0
F(yj)− F(xj)= ◦(xj,yj)
= ˚(xj,yj)
f(t)(dt)
= ˚{f<R}∩(xj,yj)
f(t)(dt)+ ˚{f ⩾R}∩(xj,yj)
f(t)(dt)
⩽R ˚(xj,yj)
(dt)+ ˚{f ⩾R}∩(xj,yj)
f(t)(dt).
Summing overj=1,2,…,N gives
NÉ
j=1
ðF2(yj)− F2(xj)ð ⩽R⋅+ ˚{f ⩾R}
f(t)(dt)
since⨃
j(xj,yj)⊂ R. Now we choose for given >0
• FirstR=R()such that∫{f ⩾R}f(t)(dt) ⩽∕2
• and then∶=∕(2R)
to conﬁrm that
NÉ
j=1
ðF2(yj)− F2(xj)ð ⩽
this settles b).
Now consider the measure⊥. Its distribution functionF⊥(x) ∶=⊥(−∞,x) is increasing, left-
continuousbutnotnecessarilycontinuous. Suchafunctionhas,byLemma14.14atmostcountably
many discontinuities (jumps), which we denote byJ. Thus, we can write
⊥=1+3
with the jump (or saltus)ΔF(y)∶= F(y+)− F(y−) ify∈J.
1∶=
É
y∈J
ΔF(y)⋅y, and 3∶=⊥−1;
240

Solution Manual. Last update 18th July 2019
1 is clearly a measure (the sum being countable) with1 ⩽⊥ and so is, therefore,2 (since the
deﬁning diﬀerence is always positive). The corresponding distribution functions are
F1(x)∶=
É
y∈J,y<x
ΔF(y)
(called the jump or saltus function) and
F2(x)∶= F⊥(x)− F1(x).
It is clear thatF2 is increasing and, more importantly, continuous so that the problem is solved.
Itisinterestingtonotethatourproblemshowsthatwecandecomposeeveryleft-orright-continuous
monotonefunctionintoanabsolutelycontinuousandsingularpartandthesingularpartagaininto
a continuous and discontinuous part:
g=gac+gsc+gsd
where
g —is a monotone left- or right-continuous function;
gac —is a monotone absolutely continuous (and in particular continuous) function;
gsc —is a monotone continuous but singular function;
gsd —isamonotonediscontinuous(even: purejump),butneverthelessleft-orright-continuous,
and singular function.
■■
Problem 20.9 Solution:
(i) Inthefollowingpicture F1 isrepresentedbyablackline, F2 byagreylineand F3 isadotted
black line.
(ii),(iii) The construction of theFn’s also shows that
ðFn(x)− Fn+1(x)ð ⩽ 1
2n+1
since we modifyFn only on a setIl
n+1 by replacing a diagonal line by a combination of
diagonal-ﬂat-diagonalandallthishappensonlywithinarangeof 2−n units. Sincetheﬂatbit
is in the middle, we get that the maximal deviation betweenFn andFn+1 is at most1
2 ⋅2−n.
Just look at the pictures!
Thus the convergence ofFn →F is uniform, i.e. it preserves continuity andF is continuous
as all theFn’s are. ThatF is increasing is already inherited from the pointwise limit of the
Fn’s:
x<y - ⇒∀n∶Fn(x) ⩽Fn(y)
- ⇒F(x)=lim
n
Fn(x) ⩽lim
n
Fn(y)= F(y).
241

R.L. Schilling: Measures, Integrals & Martingales
(iv) LetC denotetheCantorset. Thenfor x∈[0,1] ⧵C weﬁndnandl suchthat x∈Il
n (which
is an open set!) and, since on those piecesFn andF do not diﬀer any more
Fn(x)= F(x) - ⇒F‡(x)= F‡
n(x)=0
where we use thatFnðIl
n is constant. Since(C)=0 (see Problem 7.12) we have([0,1] ⧵
C)=1 so thatF‡exists a.e. and satisﬁesF‡=0 a.e.
(v) We haveIl
n = (al,bl) (we suppress the dependence ofal,bl on n with, because of our
ordering of the middle-thirds sets (see the problem):
a1<b 1<a 2<⋯<a 2n−1<b 2n−1
and
2n−1É
l=1
F(bl)− F(al)=F(b2n−1)− F(a1) , , , , , , , , , , , , , , , , , , , , →
n→∞
F(1)− F(0)=1
while (with the convention thata0∶=0 )
2n−1É
l=1
(al−bl−1) , , , , , , , , , , , , , , , , , , , , →
n→∞
0.
This leads to a contradiction since, because of the ﬁrst equality, the sum
2n−1É
l=1
F(al)− F(bl−1)
will never become small.
■■
242

Solution Manual. Last update 18th July 2019
✻
✲
1
3
4
1
2
1
4
1
3
2
3 1
1
243



21 Riesz representation theorems.
Solutions to Problems 21.121.7
Problem 21.1 Solution:
(i) Letf ∈Lp()andg∈Lq()such that‖g‖q ⩽1. Hölder’s inequality (13.5) gives
‖f⋅g‖1 ⩽ ‖f‖p‖g‖q ⩽ ‖f‖p.
Therefore
‖f‖p ⩾sup
<
˚ fgd ∶g∈Lq(), ‖g‖q ⩽1
=
.
For the converse inequality ‘⩽’ we useg∶=sgn(f)⋅ðfðp−1. Sinceq= p
p−1, we have
ðgðq = ðfð(p−1)q = ðfðp∈L1(),
andso g∈Lq()and‖g‖q = ‖f‖p∕q
p . Setting g∶=g∕‖g‖q ∈Lq()weﬁnd‖ g‖q ⩽1
as well as
˚ f gd= 1
‖g‖q ˚ ðfðpd = 1
‖f‖p∕q
p
‖f‖p
p= ‖f‖(p(1−1∕q)
p = ‖f‖p.
In the last stepe we use1
p+ 1
q =1 .
(ii) Let ⊂L q()be a dense subset. Since⊂L q()we obviously have
‖f‖p ⩾sup
<
˚ fgd ∶g∈ , ‖g‖q ⩽1
=
.
Converesly, let >0. Because of (i) there is someg∈Lq(),‖g‖q ⩽1 such that
˚ fgd ⩾ ‖f‖p−.
Since  is dense, there is someℎ∈  with ‖g−ℎ‖q ⩽. The Hölder inequality now
shows
˚ fℎd = ˚ f(ℎ−g)d+ ˚ fgd
⩾−‖f‖p‖ℎ−g‖q+ ˚ fgd
⩾−‖f‖p+ ˚ fgd
⩾−‖f‖p+‖f‖p−
= ‖f‖p(1− )− .
Letting →0 proves the claim.
245

R.L. Schilling: Measures, Integrals & Martingales
(iii) Iffg ∈L1()forall g∈Lq(),then If(g)∶= ∫ ðfðgd isapositivelinearfunctional
onLq(). From Theorem 21.5 we know that there exists a uniquef ∈Lq()such that
If(g)= ˚
fgd ∀g∈Lq().
Therefore,f = f ∈Lq().
■■
Problem 21.2 Solution:
(i) We use a classical diagonal argument (as in the proof of Theorem 21.18). Let(gn)n∈N
denote an enumeration ofq. Hölder’s inequality (13.5) tells us
óóóó˚ ungid
óóóó
⩽ ‖un‖p‖gi‖q ⩽
0
sup
n∈N
‖un‖p
1
‖gi‖q
for alli,n ∈ N. If i = 1, the sequence(∫ ung1d)n∈N is bounded. Therefore, the
Bolzano–Weierstraß theorem shows the existence of a subsequence(u1
n)n∈N such that
the limit
lim
n→∞ ˚ u1
ng1d
exists. We pick recursively subsequences(ui+1
n )n∈N⊂(ui
n)n∈N such that the limits
lim
n→∞ ˚ ui+1
n gi+1d
exist. Because of the recursive thinning, we see that
lim
n→∞ ˚ ui
ngkd
exists for allk = 1,2,…,i. Thus, for the diagonal sequencevn ∶= un
n the limits
limn→∞ ∫ vngid exist for eachi∈ N.
(ii) Letg ∈ Lq() and(un(i))i∈N be the diagonal sequence constructed in (i). SinceR is
complete, it is enough to show that ∫ un(i)gd 
i∈N is a Cauchy sequence. Fix >0.
Byassumption, q isdensein Lq(),i.e.thereexistssome ℎ∈ q suchthat ‖g−ℎ‖q ⩽
. Part (i) shows that we can takeN ∈ N with
óóóó˚ un(i)ℎd − ˚ un(k)ℎd
óóóó
⩽ ∀i,k ⩾N. (⋆)
Hölder’s inequality and the triangle inequality show
óóóó˚ un(i)gd − ˚ un(k)gd óóóó
= óóóó˚ (un(i)−un(k))(g−ℎ)d+ ˚ (un(i)−un(k))ℎdóóóó
⩽ óóóó˚ (un(i)−un(k))(g−ℎ)dóóóó
+óóóó˚ (un(i)−un(k))ℎdóóóó«›››››››››››››ﬂ›››››››››››››‹
⩽ b/o (⋆)
246

Solution Manual. Last update 18th July 2019
⩽ ‖un(i)−un(k)‖p‖g−ℎ‖q+
⩽(‖un(i)‖p+‖un(k)‖p)‖g−ℎ‖q+
⩽2sup
n∈N
‖un‖p‖g−ℎ‖q+
⩽
0
2sup
n∈N
‖un‖p+1
1

for anyi,k ⩾N. This proves that ∫ un(i)gd 
i∈N is Cauchy.
(iii) Without loss of generality we may assume that the limits
I(g)∶= lim
i→∞ ˚ u+
n(i)gd, and J(g)∶= lim
i→∞ ˚ u−
n(i)gd
exist for allg ∈ Lq(). Indeed: From (i),(ii) we see that there is a subsequence such
thatI(g) exists for allg ∈ Lq(). Thinning out this subsequence once again, we see
that J(g) exists for allg ∈ Lq(). Since I and J are positive linear functionals on
Lq(), Theorem 21.5 proves that there are unique functionsv,w ∈ Lq(),v,w ⩾ 0
representing these functionals:
I(g)= ˚ vgd and J(g)= ˚ wgd.
Therefore,
lim
i→∞ ˚ un(i)gd = lim
i→∞ ˚ u+
n(i)gd − lim
i→∞ ˚ u−
n(i)gd
= ˚ (v−w)gd.
The claim follows if we useu∶=v−w∈Lq().
■■
Problem 21.3 Solution:
(i) By Problem 19.7(i) or 21.4(a), k is positive semideﬁnite, i.e. for any choice ofm∈ N,
1,…,m∈ C and1,…,m∈ Rn we have
mÉ
i,k=1
 k(i−k)īk ⩾0.
Sincelimi→∞ i()= (), we see
mÉ
i,k=1
(i−k)īk ⩾0.
Since  i(−)=  i(), this also holds for the limit
(−)= lim
i→∞
 i(−)= lim
i→∞
 i()= () ∀∈ Rn.
Thisshowsthat ispositivesemideﬁnite. Ifm=1 resp.m=2 ,weseethatthematrices

(0)

and
H
(0) (−)
() (0)
I
247

R.L. Schilling: Measures, Integrals & Martingales
are positve hermitian for all ∈ Rn. Since determinants of positive hermitian matrices
are positive, we ﬁnd(0) ⩾0 and
0 ⩽(0)2−()(−)= (0)2−()()= (0)2−ð()ð2.
(ii) First of all we show that the limit exists. Picku∈C∞
c (Rn). Because of Theorem 19.23,
−1u∈ (Rn)and we can use Plancherel’s theorem (Theorem 19.12), to get
˚ udi= ˚ (−1u)di= ˚ −1u() i()d.
Sinceð i()ð ⩽  i(0) →(0) is uniformly bounded, we can use dominated convergence
and ﬁnd that
Λ(u)∶= lim
i→∞ ˚ udi= ˚ −1u()()d
is well-deﬁned. The linearity ofΛfollows from the linearity of the integral Moreover, if
u ⩾0, then
Λu= lim
i→∞ ˚ udi ⩾0.
(iii) The continuity ofΛfollows from
ðΛuð ⩽limsup
i→∞ ˚ ðuðdi ⩽ ‖u‖∞limsup
i→∞
i(Rn)
«ﬂ‹
(2)n i(0)
=(2)n(0)‖u‖∞.
SinceC∞
c (Rn)isuniformlydensein Cc(Rn),(seeProblem15.13,theproofresemblesthe
argumentofTheorem15.11),wecanextend Λtoapositivelinearfunctionalon Cc(Rn):
Foru∈Cc(Rn)we take(ui)i∈N⊂C ∞
c (Rn), such that‖ui−u‖∞ →0. Since
ðΛ(ui)−Λ( uk)ð= ðΛ(ui−uk)ð ⩽(2)n(0)‖ui−uk‖∞,
we conclude that(Λui)i∈N is a Cauchy sequence inR. Therefore, the limit Λu ∶=
limi→∞Λui exists and deﬁnes a positive linear functional onCc(Rn). By Riesz’s rep-
resentation theorem, Theorem 21.8, there exists a unique regular measure representing
the functionalΛ
Λu= ˚ ud ∀u∈Cc(Rn).
(iv) Let >0. Since is continuous at=0 , there is some >0 such that
ð()− (0)ð< ∀ðð ⩽.
Because of Lévy’s truncation inequality, Problem 19.6,
i(Rn ⧵[−R,R]n) ⩽2(R)n
˚[−1∕R,1∕R]n
( i(0)−Re  i())d
(note that i()=(2 )n i(−)). With the dominated convergence theorem we get
limsup
i→∞
i(Rn ⧵[−R,R]n) ⩽2(R)n
˚[−1∕R,1∕R]n
((0)−Re ())d
248

Solution Manual. Last update 18th July 2019
⩽2(2)n
forR ⩾ 1
. In particular we ﬁnd fori ⩾n0(),i(Rn ⧵[−R,R]n) ⩽3(2)n. In order to
geti(Rn ⧵[−R,R]n) ⩽3(2)n fori=1,…,n0(), we can increaseR, if needed.
(v) Let(k)k∈N ⊂ Cc(Rn) be a sequence of functions such that0 ⩽ k ⩽ 1 andk ↑ 1Rn
(use, e.g. Urysohn functions, cf. page 239, or construct thek directly). Because of (iii)
we have
˚ kd =Λ(k) ⩽(2)n(0).
The monotone convergence theorem shows that is a ﬁnite measure:
(Rn)= sup
k∈N ˚ kd ⩽(2)n(0).
Moreover,M ∶=sup i∈Ni(Rn)<∞ sincei(Rn)=(2 )n i(0) →(0). It remains to
show thati converges weakly to. First of all,
˚ udi , , , , , , , , , , , , , , , , , , , →
i→∞ ˚ ud ∀u∈Cc(Rn). (⋆)
Let u ∈ Cc(Rn). Since C∞
c (Rn) is dense inCc(Rn), there is a sequence(fk)k∈N ⊂
C∞
c (Rn)such that‖fk−u‖∞ →0. Thus,
óóóó˚ udi− ˚ udóóóó
⩽ óóóó˚ (u−fk)di
óóóó
+óóóó˚ fkdi− ˚ fkdóóóó
+óóóó˚ (fk−u)dóóóó
⩽ ‖u−fk‖∞i(Rn)+ óóóó˚ fkdi− ˚ fkdóóóó
+‖fk−u‖∞(Rn)
⩽ ‖u−fk‖∞(M+(Rn))+ óóóó˚ fkdi− ˚ fkdóóóó
(ii)
, , , , , , , , , , , , , , , , , , , →
i→∞
‖u−fk‖∞(M+(Rn)) , , , , , , , , , , , , , , , , , , , , →
k→∞
0.
Assumethat f ∈Cb(Rn). For >0,Party(iv)showsthatthereissome R> 0suchthat
withK ∶=[−R,R]n
i(Kc
n)= i(Rn ⧵K) ⩽.
Without loss of generality we may assume that(Rn ⧵K) ⩽ . Pick  ∈ Cc(Rn),
0 ⩽ ⩽1andðK =1 . Then
óóóó˚ fd i− ˚ fd óóóó
⩽ óóóó˚ fd i− ˚ fd óóóó
+óóóó˚ (1− )fd i+ ˚ (1− )fd óóóó
⩽ óóóó˚ fd i− ˚ fd óóóó
+‖f‖∞
0
˚ 1Kcdi+ ˚ 1Kcd
1
⩽
óóóó˚ fd i− ˚ fd
óóóó
+2‖f‖∞.
Sincef⋅ ∈Cc(Rn), the ﬁrst term on the right vanishes asi →∞, cf. (iii). So,
limsup
i→∞
óóóó˚ fd i− ˚ fd óóóó
⩽2‖f‖∞ , , , , , , , , , , , , , , , , , →
→0
0.
249

R.L. Schilling: Measures, Integrals & Martingales
(vi) Let(k)k∈N beaweaklyconvergentsequenceofﬁnitemeasures. Deﬁne f(x)∶= e−ix⋅,
∈ Rn, we get
 k()= 1
(2)n ˚ e−ix⋅dk(x) , , , , , , , , , , , , , , , , , , , , →
k→∞
1
(2)n ˚ e−ix⋅(dx)=  (),
i.e.theFouriertransformsconvergepointwise. Frompart(iv)weknowthatthesequence
(k)k∈N is tight. For >0 there is someR >0 such thatk(Rn ⧵K) ⩽  forK ∶=
[−R,R]n. Withoutlossofgeneralitywecanenlarge Rtomakesurethat (Rn ⧵K) ⩽,
too. Because of the (uniform) continuity of the functionR∋ r → eir on compact sets,
there is some >0 such that
ðei(−)⋅x−1ð ⩽ ∀ð−ð<, x ∈K.
Ifk∈ N,, ∈ Rn withð−ð< , then we see
ð k()−  k()ð ⩽ 1
(2)n ˚ ðei⋅x−ei⋅xðk(dx)= 1
(2)n ˚ ðei(−)⋅x−1ðk(dx)
= 1
(2)n ˚K
ðei(−)⋅x−1ð
«›››››ﬂ›››››‹
⩽
k(dx)+ 1
(2)n ˚Kc
ðei(−)⋅x−1ð
«›››››ﬂ›››››‹
⩽2
k(dx)
⩽ k(Rn)
(2)n + 2
(2)ni(Kc)
⩽ 1
(2)n(M+2)
where M ∶= supk∈Nk(Rn) < ∞. This proves the equicontinuity of the sequence
( k)k∈N.
(vii) Let∈ Rn and >0. Use equicontinuity of the sequence( k)k∈N to pick some >0.
Since  is continuous, we can ensure that is such that
ð ()−  ()ð ⩽ ∀ð−ð ⩽.
This entails for all∈ Rn satisfyingð−ð ⩽:
ð k()−  ()ð ⩽ ð k()−  k()ð
«›››››››ﬂ›››››››‹
⩽
+ð k()−  ()ð+ð ()−  ()ð
«›››››ﬂ›››››‹
⩽
- ⇒ sup
∈B()
ð k()−  ()ð ⩽2+ð k()−  ()ð , , , , , , , , , , , , , , , , , , , , →
k→∞
2 , , , , , , , , , , , , , , , , , →
→0
0.
Hereweusethat  kconvergespointwiseto  ,cf.(vi). Thecalculationshowsthat  kcon-
vergeslocallyuniformlyto  . Sincelocallyuniformconvergenceisthesameasuniform
convergence on compact sets, we are done.
■■
Problem 21.4 Solution:
250

Solution Manual. Last update 18th July 2019
(i) Since  is a ﬁnite measure, the continuity of follows directly from the continuity
lemma, Theorem 12.4 (cf. also 19.3). In order to show positive deﬁniteness, pickm∈
N,1,…,m∈ Rn and1,…,m∈ C. We get
mÉ
j,k=1
(j−k)j̄k= 1
(2)n
mÉ
j,k=1
j̄k ˚ e−ix⋅(j−k)(dx)
= 1
(2)n
mÉ
j,k=1
j̄k ˚ e−ix⋅je−ix⋅k(dx)
= 1
(2)n ˚
H mÉ
j=1
je−ix⋅j
IH mÉ
k=1
ke−ix⋅k
I
(dx)
= 1
(2)n ˚
óóóóóó
mÉ
j=1
je−ix⋅j
óóóóóó
2
(dx) ⩾0.
(ii) Form=1 and=0 thedeﬁnitionofpositivedeﬁnitenessimpliesthatthematrix ((0))
is positive deﬁnite; in particular,(0) ⩾0.
If we have for a matrix(aik)that∑
ikaikīj ⩾0, then
0 ⩽
É
ik
aikīk=
É
ik
aikīk=
É
ik
aik̄ik=
É
ki
akīki
which means thataik =aki. Apply this to the matrixaik =(i−k) withm=2 and
1= and2=0 to infer that()= (−). Moreover, the matrix
H
(0) (−)
() (0)
I
is positive semideﬁnite; in particular its determinant is positive:
0 ⩽(0)2−(−)().
Since(−)= (), we get the inequality as claimed.
(iii) Because ofð()ð ⩽(0)we see that
óóóó¸ (−)

eix⋅e−2ðð2
 eix⋅e−2ðð2dd óóóó
⩽ ð(0)ð ¸

e−2ðð2
e−2ðð2

dd <∞,
i.e. is well-deﬁned. Let us show that ⩾ 0. For this we coverRn with countably
many disjoint cubes(Ik
i)i∈N with side-length1∕k and we pick anyk
i ∈Ik
i . Using the
dominated convergence theorem and the positive deﬁniteness of the function we get
(x)= lim
k→∞
É
m,j∈N ˚Ik
m
˚Ik
j
(k
m−k
j)

eix⋅k
je−2ðk
jð2
eix⋅k
me−2ðk
mð2

dd
= lim
k→∞
É
m,j∈N
(k
j −k
m)

k−neix⋅k
je−2ðk
jð2
k−neix⋅k
je−2ðk
jð2
251

R.L. Schilling: Measures, Integrals & Martingales
⩾0.
Because of the parallelogram identity
2ðð2+2ðð2= ð−ð2+ð+ð2
we obtain
(x)= ¸

eix⋅ eix⋅e−2ðð2−2ðð2
dd
= ¸

eix⋅(−)e−ð−ð2−ð+ð2

dd.
Changing variables according to
H
t
s
I
∶=
H
−
+
I
=
H
idn −idn
idn idn
IH


I
=∶A
H


I
leads to
(x)= 1
ðdetAð ¸ (t)eix⋅te−(ðtð2+ðsð2)dtds
= 1
c ˚ (t)e−ðtð2
eix⋅tdt
= 1
c ˚ (t)eix⋅tdt. (⋆)
(iv) Deﬁne
gt(x)∶= 1
(2t)n∕2exp
0
−ðxð2
2t
1
.
Applying Theorem 19.12 for the ﬁnite measure(dx)∶= e−tðxð2
dx yields
˚ (x)e−t
2ðxð2
dx
(⋆)
= 1
c ˚ −1()(x)e−t
2ðxð2
dx= 1
c ˚ ()−1(e−t
2ð⋅ð2
)()d
forallt> 0(observe: ∈L1(Rn)). Example19.2(iii)shows (gt)(x)=(2 )−nexp(−tðxð2∕2).
Therefore, −1(e−t
2ð⋅ð2
)() = (2)ngt(). Since ð()ð ⩽ (0) and ∫ gt(x)dx = 1we
thus get
˚ (x)e−t
2ðxð2
dx= (2)n
c ˚ ()gt()d ⩽ (2)n
c (0).
Fatou’s lemma (Theorem 9.11) ﬁnally shows
˚ (x)dx= ˚ lim
k→∞
(x)e− 1
2kðxð2
dx
⩽liminf
k→∞ ˚ (x)e− 1
2kðxð2
dx
⩽ (2)n
c (0).
Since ⩾0, see (iii), this means that ∈L1(Rn).
252

Solution Manual. Last update 18th July 2019
(v) Parts(iii)and(iv)showthat   = fortheﬁnitemeasure (dx)∶= c(x)dx. Since
 → , Lévy’s continuity theorem (Problem 21.3) shows that there exists a measure
 which is the weak limit of the family as →0 and  =.
■■
Problem 21.5 Solution:
(i) Since uniform convergence preserves continuity, we see that everyu ∈ Cc(X) is con-
tinuous. By construction, the set{ðuð ⩾} is compact since there is someu ∈Cc(X)
such that‖u−u‖∞ < . This means thatu vanishes at inﬁnity. In particularCc(X)⊂
C∞(X).
Conversely, ifu ∈ C∞(X) and >0, there is some compact setK such thatðuð ⩽ 
outsideof K. NowweuseUrysohn’slemmaandconstructafunction  ∈Cc(X)such
that 1K ⩽ ⩽1. Then we getu ∶=u∈Cc(X)as well as
ðu−uð=(1− )ðuð ⩽
uniformly for allx.
(ii) It is obvious thatC∞(X) is a vector space and that‖∙‖∞ is a norm in this space. The
completeness follows from part (i) sinceC∞(X)= Cc(X)= Cc(X).
(iii) Let u ∈ C∞(X) and  > 0. Urysohn’s lemma shows that there is a ∈ Cc(X),
0 ⩽ ⩽1, such thatðuð ⩽ on the set{ <1}={  =1} c. Therefore,
óóóó˚ udn− ˚ udóóóó
⩽ óóóó˚ ud n− ˚ ud óóóó
+óóóó˚ u(1− )dn− ˚ u(1− )dóóóó
⩽ óóóó˚ ud n− ˚ ud óóóó
+n(X)+ (X)
21.16
⩽ óóóó˚ ud n− ˚ ud óóóó
+2sup
m∈N
m(X).
Sinceu ∈Cc(X), we ﬁnd asn →∞
limsup
n→∞
óóóó˚ udn− ˚ ud
óóóó
⩽2sup
m∈N
m(X) , , , , , , , , , , , , , , , , , →
→0
0.
■■
Problem 21.6 Solution:
(i) First we consideru ∈ C∞
c (Rn). According to Theorem 19.23,−1u ∈ (Rn), and
Plancherel’s theorem (Theorem 19.12) gives
˚ udi= ˚ (−1u)di= ˚ −1u() i()d.
253

R.L. Schilling: Measures, Integrals & Martingales
Sinceð i()ð ⩽  i(0) →(0) is uniformly bounded, we can use the dominated conver-
gence theorem to see
Λ(u)∶= lim
i→∞ ˚ udi= ˚ −1u()()d
i.e.Λ(u)is well-deﬁned. Moreover,
i(Rn)=(2 )n i(0) , , , , , , , , , , , , , , , , , , , →
i→∞
(2)n(0),
i.e.M ∶=sup ii(Rn)<∞. Assume now thatu∈Cc(X). SinceC∞
c (Rn) is dense in
Cc(Rn) (with respect to uniform convergence, cf. Problem 15.13), there is a sequence
(uk)k∈N⊂C ∞
c (Rn)such that‖uk−u‖∞ →0. Thus,
óóóó ˚ udi− ˚ udj
óóóó
⩽
óóóó˚ (u−uk)di
óóóó
+
óóóó˚ (u−uk)dj
óóóó
+
óóóó˚ ukdi− ˚ ukdj
óóóó
⩽ ‖u−uk‖∞
 i(Rn)+ j(Rn)+
óóóó˚ ukdi− ˚ ukdj
óóóó
⩽2‖u−uk‖∞M+
óóóó˚ ukdi− ˚ ukdj
óóóó
, , , , , , , , , , , , , , , , , , , , , , , , →
i,j→∞
2‖u−uk‖∞M , , , , , , , , , , , , , , , , , , , , →
k→∞
0.
This shows that  ∫ udi

i∈N is a Cauchy sequence inR. Thus, the limitΛ(u) ∶=
limi→∞ ∫ udi exists. Since convergent sequences are bounded, we see
sup
i∈N
óóóó˚ udi
óóóó
<∞.
Sinceu∈Cc(Rn) - ⇒ðuð∈Cc(Rn), we get
sup
n∈N ˚ ðuðdi<∞ ∀u∈Cc(Rn),
i.e.thesequence (i)i∈N isvaguelybounded. AccordingtoTheorem21.18, (i)i∈N has
a vaguely convergent subsequencen(i) →.
(ii) Wecanusepart(i)foranysubsequenceof (i)i∈N. Wewillshowthethesubsequential
limits do not depend on the subsequence. Pick any two subsequences(n(i))i∈N and
(m(i))i∈N of(i)n∈N and assume thatn(i)
v
, , , , , , , , , , →,m(i)
v
, , , , , , , , , , →. By deﬁnition, we ﬁnd
for allu∈Cc(Rn)
lim
i→∞ ˚ udn(i)= ˚ ud,
lim
i→∞ ˚ udm(i)= ˚ ud.
On the other hand, we have seen in (i) thatΛ(u)=lim i→∞ ∫ udi. Thus,
˚ ud =Λ(u)= ˚ ud.
254

Solution Manual. Last update 18th July 2019
Since this holds for allu ∈ Cc(Rn), we can use the regularity of the measures and
 to conclude that = . Since the limit does not depend on the subsequence, we
already have vague convergence of thefull sequence(i)i∈N. (Compare this with the
following subsequence principle: A sequence(ai)i∈N ⊂ R converges if, and only if,
everysubsequenceof (ai)i∈Nhasaconvergentsubsequence,andallsubsequentiallimits
coincide.)
(iii) In view of Theorem 21.17 it is enough to show that the sequence(i)i∈N is tight
Fix >0. Since is continuous at=0 , there is some >0 such that
ð()− (0)ð< ∀ðð ⩽.
From Lévy’s truncation inequality, Problem 19.6, we get
i(Rn ⧵[−R,R]n) ⩽2(R)n
˚[−1∕R,1∕R]n
( i(0)−Re  i())d
(observe, that i()=(2 )n i(−)). Now we can use dominated convergence to get
limsup
i→∞
i(Rn ⧵[−R,R]n) ⩽2(R)n
˚[−1∕R,1∕R]n
((0)−Re ())d
⩽2(2)n
for allR ⩾ 1
. In particular, we ﬁndi(Rn ⧵[−R,R]n) ⩽ 3(2)n fori ⩾ n0(). In
order to ensurei(Rn ⧵[−R,R]n) ⩽3(2)n fori=1,…,n0(), we can enlargeR, if
need be.
■■
Problem 21.7 Solution: Since
˚B
udn= ˚B∩suppu
udn
wecanassume,withoutlossofgenerality,that Biscontainedinacompactset. Denoteby K ∶=B
the closure ofB and byU ∶=B◦ the open interior ofB. Moreover, we can assume thatu ⩾0 –
otherwise we consideru± separately.
According to Urysohn’s lemma (Lemma B.2 or (21.6) & (21.7)), there are sequences(wk)k∈N ⊂
Cc(X),(vk)k∈N ⊂ Cc(X),0 ⩽vk ⩽1,0 ⩽wk ⩽1, withwk ↑ 1U andvk ↓ 1K. By assumption
n
v
, , , , , , , , , , → and so
˚B
udn ⩽ ˚K
udn ⩽ ˚ u⋅vkdn , , , , , , , , , , , , , , , , , , , , →
n→∞ ˚ u⋅vkd.
Beppo Levi’s theorem implies
limsup
n→∞ ˚B
udn ⩽ inf
k∈N ˚ u⋅vkd = ˚K
ud.
255

R.L. Schilling: Measures, Integrals & Martingales
Similarly, we get from
˚B
udn ⩾ ˚U
udn ⩾ ˚ u⋅wkdn , , , , , , , , , , , , , , , , , , , , →
n→∞ ˚ u⋅wkd.
and the monotone convergence theorem
liminf
n→∞ ˚B
udn ⩾ sup
k∈N ˚ u⋅wkd = ˚U
ud.
Finally, since(K ⧵U)= ()B)=0 , we see that
limsup
n→∞ ˚B
udn ⩽ ˚K
ud = ˚U
ud ⩽liminf
n→∞ ˚B
udn.
■■
256

22 Uniform integrability and Vitali's
convergence theorem.
Solutions to Problems 22.122.17
Problem 22.1 Solution: First, observe that
lim
j
uj(x)=0 ⇐ ⇒lim
j
ðuj(x)ð=0.
Thus,
x∈{lim
j
uj =0} ⇐ ⇒∀ >0 ∃ N ∈ N ∀j ⩾N ∶ ðuj(x)ð ⩽
⇐ ⇒∀ >0 ∃ N ∈ N ∶ sup
j⩾N
ðuj(x)ð ⩽
⇐ ⇒∀ >0 ∃ N ∈ N ∶x∈{sup
j⩾N
ðujð ⩽}
⇐ ⇒∀ >0∶ x∈
˝
N∈N
{sup
j⩾N
ðujð ⩽}
⇐ ⇒∀k∈ N∶x∈
˝
N∈N
{sup
j⩾N
ðujð ⩽1∕k}
⇐ ⇒x∈
Ì
k∈N
˝
N∈N
{sup
j⩾N
ðujð ⩽1∕k}.
Equivalently,
{lim
j
uj =0} c =
˝
k∈N
Ì
N∈N
{sup
j⩾N
ðujð>1∕k}.
By assumption and the continuity of measures,

0 Ì
N∈N
{sup
j⩾N
ðujð>1∕k}
1
=lim
N


{sup
j⩾N
ðujð>1∕k}

=0
and, since countable unions of null sets are again null sets, we conclude that
{lim
j
uj =0} has full measure.
■■
Problem 22.2 Solution: Note that
x∈ sup
j⩾k
ðujð>  ⇐ ⇒sup
j⩾k
ðuj(x)ð>
257

R.L. Schilling: Measures, Integrals & Martingales
⇐ ⇒∃j ⩾k∶ ðuj(x)ð>
⇐ ⇒x∈
˝
j⩾k
{ðujð>}
and since
˝
j⩾k
{ðujð>} ↓
Ì
k∈N
˝
j⩾k
{ðujð>}
def
= limsup
j→∞
{ðujð>}
we can use the continuity of measures to get
lim
k


sup
j⩾k
ðujð>

=lim
k

0˝
j⩾k
{ðujð>}
1
=
0 Ì
k∈N
˝
j⩾k
{ðujð>}
1
.
This, and the result of Problem 22.1 show that either of the following two equivalent conditions
lim
k→∞


sup
j⩾k
ðujð ⩾

=0 ∀  >0;


limsup
j→∞
{ðujð ⩾}

=0 ∀  >0;
ensure the almost everywhere convergence oflimjuj(x)=0 .
■■
Problem 22.3 Solution:
• Assume ﬁrst thatuj →u in-measure, that is,
∀ >0, ∀A∈A, (A)<∞∶lim
j
 {ðuj−uð>}∩ A=0.
Since
ðuj−ukð ⩽ ðuj−uð+ðu−ukð ∀j,k ∈ N
we see that
{ðuj−ukð>2}⊂{ðuj−uð>}∪{ ðu−ukð>}
(since,otherwise ðuj−ukð ⩽+=2). Thus,wegetforeverymeasurableset Awithﬁnite
-measure that
 {ðuj−ukð>2}∩ A
⩽({ðuj−uð>}∩ A)∪({ ðuk−uð>}∩ A)
⩽{ðuj−uð>}∩ A+{ðuk−uð>}∩ A
and each of these terms tend to inﬁnity asj,k →∞.
• Assume now thatðuj −ukð → 0 in-measure asj,k → ∞. Let (Al)l be an exhausting
sequence such thatAl ↑X and(Aj)<∞.
The problem is to identify the limiting function.
258

Solution Manual. Last update 18th July 2019
Fixl. By assumption, we can chooseNj ∈ N,j∈ N, such that
∀m,n ⩾Nj ∶ {ðum−unð>2−j}∩ Al
<2−j.
(Notethat Nj maydependon l,butwesuppressthisdependencyas lisﬁxed.) Byenlarging
Nj, if needed, we can always assume that
N1<N 2<⋯<N j <N j+1 →∞.
Consequently, there is an exceptional setEj ⊂A l with(Ej∩Al)<2−j such that
ðuNj+1(x)− uNj(x)ð ⩽2−j ∀x∈Al ⧵Ej
and, ifE∗
i ∶= ⋃
j⩾iEj we have(Ei∩Al) ⩽2⋅2−i as well as
ðuNj+1(x)− uNj(x)ð ⩽2−j ∀j ⩾i, ∀x∈Al ⧵E∗
i.
This means that
É
j
(uNj+1−uNj) converges uniformly forx∈Al ⧵E∗
i
sothat limjuNj existsuniformlyon Al ⧵E∗
i forall i. Since(E∗
i ∩Al)<2⋅2−i weconclude
that
lim
j
uNj 1Al =u(l)1Al exists almost everywhere
for someu(l). Since, however, a.e. limits are unique (up to a null set, that is) we know that
u(l)=u(m)a.e.on Al∩Amsothatthereisa(uptonullsets)uniquelimitfunction usatisfying
lim
j
uNj =u exists a.e., hence in measure by Lemma 22.4. (*)
Thus, we have found a candidate for the limit of our Cauchy sequence. In fact, since
ðuk−uð ⩽ ðuk−uNjð+ðuNj−uð
we have
({ðuk−uð>}∩ Al)
⩽({ðuk−uNjð>}∩ Al)+ ({ðuNj−uð>}∩ Al)
andtheﬁrstexpressionontheright-handsidetendstozero(as k,N(j) →∞)becauseofthe
assumption, while the second term tends to zero (asN(j) →∞) because of (*))
■■
Problem 22.4 Solution:
259

R.L. Schilling: Measures, Integrals & Martingales
(i) This sequence converges in measure tof ≡0 since for∈(0,1)
(ðfn,jð>)= [(j−1)∕n,j∕n]= 1
n , , , , , , , , , , , , , , , , , , , , →
n→∞
0.
This means, however, that potential a.e. andp-limits must bef ≡ 0, too. Since for
everyx
liminf fn,j(x)=0 <∞=limsup fn,j
the sequence cannot converge at any point.
Also thep-limit (ifp ⩾1) does not exist, since
˚ ðfn,jðpd=np[(j−1)∕n,j∕n]= np−1.
(ii) As in (i) we see thatgn

, , , , , , , , , , , →g ≡0. Similarly,
˚ ðgnðpd =np(0,1∕n)= np−1
so that thep-limit does not exist. The pointwise limit, however, exists since
lim
n→∞
n1(0,n)(x)=0 .
for everyx∈(0,1).
(iii) The shape ofgn is that of a triangle with base[0,1∕n]. Thus, for every >0,
(ðℎnð>) ⩽[0,1∕n]= 1
n
which shows thatℎn

, , , , , , , , , , , →ℎ ≡ 0. This must be, if the respective limits exist, also the
limiting function for a.e. andp-convergence. Since
˚ ðℎnðpd=ap
n
1
2[0,1∕n]= ap
n
2n
we havep-convergence if, and only if, the sequenceap
n∕ntends to zero asn →∞.
We have, however, always a.e. convergence since the support of the functionℎn is
[0,1∕n]and this shrinks to{0} which is a null set. Thus,
lim
n
an(1− nx)+=0
except, possibly, atx=0 .
■■
Problem 22.5 Solution: We claim that
(i) auj+bwj →au+bw;
(ii) max(uj,wj) →max(u,w);
260

Solution Manual. Last update 18th July 2019
(iii) min(uj,wj) →min(u,w);
(iv) ðujð → ðuð.
Note that
ðauj+bwj−au−bwð ⩽ ðaððuj−uð+ðbððwj−wð
so that
{ðauj+bwj−au−bwð>2}⊂{ðuj−uð>∕ðað}∪{ ðwj−wð>∕ðbð}.
This proves the ﬁrst limit.
Since, by the lower triangle inequality,
ððujð−ðuðð ⩽ ðuj−uð
we get
{ððujð−ðuðð>}⊂{ðuj−uð>}
andðujð → ðuðfollows.
Finally, since
maxuj,wj = 1
2

uj+wj+ðuj−wjð

we getmaxuj,wj →maxu,w by using rules (i) and (iv) several times. The minimum is treated
similarly.
■■
Problem 22.6 Solution: The hint is somewhat misleading since this construction is not always pos-
sible (or sensible). Just imagineR with the counting measure. ThenXf would be all ofR...
What I had in mind when giving this hint was a construction along the following lines:
Consider Lebesgue measurein Rand deﬁnef ∶= 1F+∞ 1Fc whereF =[−1,1](or any other
set of ﬁnite Lebesgue measure). Then ∶= f ⋅ is a not-ﬁnite measure. Moreover, Take any
sequenceun

, , , , , , , , , , →u converging in-measure. Then
({ðun−uð>}∩ A)= ({ðun−uð>}∩ A)
since all setsAwith(A)<∞are contained inF and(F)= (F)<∞. Thus,un

, , , , , , , , , , , →u.
However,changing uarbitrarilyon 1Fc alsoyieldsalimitpointin -measuresince,asmentioned
above, all sets of ﬁnite-measure are withinF.
This pathology cannot happen in a-ﬁnite measure space, cf. Lemma 22.6.
■■
Problem 22.7 Solution:
261

R.L. Schilling: Measures, Integrals & Martingales
(i) Fix >0. Then
˚ ðu−ujðd = ˚A
ðu−ujðd
= ˚A∩{ðu−ujð⩽}
ðu−ujðd+ ˚A∩{ðu−ujð>}
ðu−ujðd
⩽ ˚A∩{ðu−ujð⩽}
d + ˚A∩{ðu−ujð>}
(ðuð+ðujð)d
⩽(A)+2 C  A∩{ðu−ujð>}
, , , , , , , , , , , , , , , , , , , , →
j→∞
(A)
, , , , , , , , , , , , , , , , , →
→0
0.
(ii) Note thatuj converges almost everywhere and in-measure tou ≡0. However,
˚ ðujðd=[j,j +1]=1 ≠0
so that the limit—if it exists—cannot beu ≡ 0. Since this is, however, the canonical
candidate, we conclude that there is no1 convergence.
(iii) The limit depends on the setA which is ﬁxed. This means that we are, essentially,
dealing with a ﬁnite measure space.
■■
Problem 22.8 Solution: Apseudo-metricissymmetric (d2)andsatisﬁesthetriangleinequality (d3).
(i) First we note that(,) ∈ [0,1] is well-deﬁned. That it is symmetric(d2) is obvi-
ous. For the triangle inequality we observe that for three random variables,, and
numbers, >0 we have
ð−ð ⩽ ð−ð+ð−ð
implying that
{ð−ð> +}⊂{ð−ð>}∪{ ð−ð>}
so that
P(ð−ð> +) ⩽ P(ð−ð>)+ P(ð−ð>).
If >P(,)and >P(,)we ﬁnd
P(ð−ð> +) ⩽ P(ð−ð>)+ P(ð−ð>) ⩽+
which means that
P(,) ⩽+.
Passing to the inﬁmum of all possible- and-values we get
P(,) ⩽P(,)+ P(,).
262

Solution Manual. Last update 18th July 2019
(ii) Assume ﬁrst thatP(j,) , , , , , , , , , , , , , , , , , , , , →
j→∞
0. Then
P(j,) , , , , , , , , , , , , , , , , , , , , →
j→∞
0 ⇐ ⇒∃(j)j ⊂ R+∶ P(ð−jð> j) ⩽j
- ⇒∀ >j ∶ P(ð−jð>) ⩽j.
Thus, for given >0 we pickN = N() such that > j for allj ⩾ N (possible as
j →0). Then we ﬁnd
∀ >0∃ N()∈ N∀j ⩾N()∶ P(ð−jð>) ⩽j;
this means, however, thatP(ð−jð>) , , , , , , , , , , , , , , , , , , , , →
j→∞
0for any choice of >0.
Conversely, assume thatj
P
, , , , , , , , , , , , →0. Then
∀ >0∶lim
j
P(ð−jð>)=0
⇐ ⇒∀, >0∃ N(,)∀ j ⩾N(,)∶ P(ð−jð>)<
- ⇒∀ >0∃ N()∀ j ⩾N()∶ P(ð−jð>)<
- ⇒∀ >0∃ N()∀ j ⩾N()∶ P(,j) ⩽
- ⇒lim
j
P(,j)=0 .
(iii) We have
(j,k) , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , →
j,k→∞
0
(ii)
⇐ ⇒j−k
P
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , →
j,k→∞
0
P22.3
⇐ ⇒∃∶k
P
, , , , , , , , , , , , , , , , , , , , →
k→∞

(ii)
⇐ ⇒∃∶(,k) , , , , , , , , , , , , , , , , , , , , , , , , , →
k→∞
0
(iv) Note that forx,y> 0
x+y
1+ x+y = x
1+ x+y+ y
1+ x+y ⩽ x
1+ x+ y
1+ y
and
(x+y)∧1=
⎧
⎪
⎨
⎪⎩
x+y=(x∧1)+( y∧1) ifx+y ⩽1;
1 ⩽(x∧1)+( y∧1) ifx+y ⩾1.
This means that bothgP anddP satisfy the triangle inequality, that is(d3). Symmetry,
i.e.(d2), is obvious.
Moreover, since for allx ⩾0
x
1+ x ⩽x∧1 ⩽2 x
1+ x
263

R.L. Schilling: Measures, Integrals & Martingales
(consider the casesx ⩽1andx ⩾1separately), we have
gP(,) ⩽dP(,) ⩽2gP(,)
whichshowsthat gP anddP havethesameCauchysequences. Moreover,forall  ⩽1,
P(ð−ð>)= P(ð−ð∧1 >)
⩽ 1
 ˚ ð−ð∧1 dP
= 1
 dP(,)
so that (because of (iii)) anydP Cauchy sequence is aP Cauchy sequence. And since
for all ⩽1also
dP(,)= ˚ð−ð>
ð−ð∧1 dP+ ˚ð−ð⩽
ð−ð∧1 dP
⩽ ˚ð−ð>
1dP+ ˚ð−ð⩽
d P
⩽ P(ð−ð>)+ ,
allP Cauchy sequences aredP Cauchy sequences, too.
■■
Problem 22.9 Solution:
(i) Fix >0. We have
˚ ðun−uð∧ 1Ad = ˚{ðun−uð⩽}
ðun−uð∧ 1Ad+ ˚{ðun−uð>}
ðun−uð∧ 1Ad
⩽(A)+ ({ðun−uð>}∩ A).
Letting ﬁrstn →∞and then →0 yields
limsup
n ˚ ðun−uð∧ 1Ad ⩽(A) , , , , , , , , , , , , , , , , , →
→0
0.
(ii) WLOGweshowthat (un)n containsana.e.convergentsubsequence. Let (Ak)k beasin
the hint and ﬁxi. By (i) we know thatðu−unð∧ 1Ai →0inL1. By Corollary 13.8 we
see that there is a subsequenceu(i)
n such thatðu−u(i)
n ð∧ 1Ai → 0 almost everywhere.
Now take repeatedly subsequences asi ⇝ i+1 ⇝ i+2 ⇝… etc. and then take the
diagonalsequence. Thiswillfurnishasubsequence (u‡‡
n)n⊂(un)n whichconvergesa.e.
tou on⋃
iAi=X.
(iii) WearenowinthesettingofCorollary13.8: ðunð,ðuð ⩽wforsomew∈ p()andun

, , , , , , →
u. Thus, every subsequence(u‡
n)n⊂(un)n converges in measure to the same limituand
by (ii) there is some(u‡‡
n)n ⊂(u‡
n)n such thatu‡‡
n
a.e.
, , , , , , , , , , , , , →u. Now we can use the dominated
convergencetheorem(Theorem12.2orTheorem13.9)toshowthat limn‖u‡‡
n−u‖p=0 .
264

Solution Manual. Last update 18th July 2019
Assumenowthat un doesnotconvergeto uinLp. Thismeansthat limsupn‖un−u‖p>
0, i.e. there is some subsequence such thatliminf n‖u‡
n−u‖p >0. On the other hand,
there is some(u‡‡
n)n⊂(u‡
n)n such that
0=lim
n
‖u‡‡
n −u‖p ⩾liminf
n
‖u‡
n−u‖p>0
and this is a contradiction.
■■
Problem 22.10 Solution: Note that the setsAj are of ﬁnite-measure. Observe that the functions
fj ∶=u1Aj
• converge in-measure tof ≡0:
({ðfjð>}∩ Aj) ⩽(Aj) , , , , , , , , , , , , , , , , , , , , →
j→∞
0.
• are uniformly integrable:
sup
j ˚{ðfjð>ðuð}
ðfjðd =0
sinceðfjð= ðu1Ajð ⩽ ðuðandðuðis integrable.
Therefore, Vitali’s Theorem shows thatfj →0 in 1 so that∫ fjd = ∫Aj
ud →0.
■■
Problem 22.11 Solution:
(i) Trivial. More interesting is the assertion that
A sequence(xn)n⊂ Rconverges to0if, and only if, every subsequence(xnk)k contains
some sub-subsequence( xnk)k which converges to 0.
Necessity is again trivial. Suﬃciency: assume that(xn)n does not converge to0. Then
the sequence(min{ðxnð,1})n is bounded and still does not converge to0. Since this
sequenceisbounded,itcontainsaconvergentsubsequence (xnk)kwithsomelimit  ≠0.
But then(xnk)k cannot contain a sub-subsequence( xnk)k which is a null sequence.
(ii) Ifun

, , , , , , , , , , , →u,theneverysubsequence unk

, , , , , , , , , , , →u. Thus,usingtheargumentfromtheproof
of Problem 22.3 we can extract a sub-subsequence( unk)k⊂(unk)k such that
lim
k
 unk(x)1A(x))u(x)1A(x)almost everywhere. (*)
Notethat(unlessweareina -ﬁnitemeasurespace)theexceptionalsetmaydependon
the testing setA.
Conversely,assumethateverysubsequence (unk)k⊂(un)nhasasub-subsequence ( unk)k
satisfying (*). Because of Lemma 22.4 we have
lim
k
 {ð unk−uð>}∩ A=0.
265

R.L. Schilling: Measures, Integrals & Martingales
Assume now thatun does not converge in-measure onAtou. Then
xn∶=({ðun−uð>}∩ A)̸ →0.
Since the whole sequence(xn)n is bounded (by(A)) there exists some subsequence
(xnk)k given by(unk)k such that
xnk =({ðunk−uð>}∩ A) → ≠0.
Thiscontradicts,however,thefactthat xnk hasitselfasubsequenceconvergingtozero.
(iii) Fix some setA of ﬁnite-measure. All conclusions below take place relative to resp.
on this set only.
Ifun

, , , , , , , , , , , →uwehaveforeverysubsequence (unk)kasub-subsequence ( unk)kwith unk →u
a.e. SinceΦis continuous, we getΦ◦ unk →Φ◦ua.e.
Thismeans,however,thateverysubsequence (Φ◦unk)kof(Φ◦un)nhasasub-subsequence
(Φ◦ unk)k which converges a.e. toΦ◦u. Thus, part (ii) says thatΦ◦un

, , , , , , , , , , , →Φ◦u.
■■
Problem 22.12 Solution: Since  and  are uniformly integrable, we ﬁnd for any given > 0
functionsf,g ∈ 1
+ such that
sup
f∈ ˚{ðfð>f}
ðfðd ⩽ and sup
g∈ ˚{ðgð>g}
ðgðd ⩽.
We will use this notation throughout.
(i) Sincef ∶= ðf1ð+⋯+ðfnð∈ 1
+ we ﬁnd that
˚{ðfjð>f}
ðfjðd = ˚ç
ðfjðd =0
uniformly for all1 ⩽j ⩽n. This proves uniform integrability.
(ii) Instead of{f1,…,fN} (which is uniformly integrable because of (i)) we show that
∪  is uniformly integrable.
Setℎ ∶=f+g. Thenℎ ∈ 1
+ and
{ðwð ⩾f+g}⊂{ðwð ⩾f}∩{ ðwð ⩾g}
which means that we have
˚{ðwð>ℎ}
ðwðd ⩽
⎧
⎪
⎨
⎪⎩
∫{ðwð>f}ðwðd ⩽ if w∈ 
∫{ðwð>g}ðwðd ⩽ if w∈ .
Since this is uniform for allw∈ ∪ , the claim follows.
266

Solution Manual. Last update 18th July 2019
(iii) Setℎ ∶=f+g ∈ 1
+. Sinceðf+gð ⩽ ðfð+ðgð we have
{ðf+gð>ℎ }⊂{ðfð>ℎ }∪{ ðgð>ℎ }
= {ðfð>ℎ }∩{ ðgð>ℎ }
∪{ðfð>ℎ }∩{ ðgð ⩽ℎ}
∪{ðfð ⩽ℎ}∩{ ðgð>ℎ }
which implies that
˚
{ðf+gð>ℎ}
ðf+gðd
⩽ ˚
{ðfð>ℎ}
∩{ðgð>ℎ}
 ðfð+ðgðd+ ˚
{ðfð>ℎ}
∩{ðgð⩽ℎ}
ðfð∨ðgðd+ ˚
{ðfð⩽ℎ}
∩{ðgð>ℎ}
ðfð∨ðgðd
= ˚
{ðfð>ℎ}
∩{ðgð>ℎ}
ðfðd+ ˚
{ðfð>ℎ}
∩{ðgð>ℎ}
ðgðd+ ˚
{ðfð>ℎ}
∩{ðgð⩽ℎ}
ðfðd+ ˚
{ðfð⩽ℎ}
∩{ðgð>ℎ}
ðgðd
⩽ ˚
{ðfð>ℎ}
ðfðd+ ˚
{ðgð>ℎ}
ðgðd+ ˚
{ðfð>ℎ}
ðfðd+ ˚
{ðgð>ℎ}
ðgðd
⩽ ˚
{ðfð>f}
ðfðd+ ˚
{ðgð>g}
ðgðd+ ˚
{ðfð>f}
ðfðd+ ˚
{ðgð>g}
ðgðd
⩽4
uniformly for allf ∈  andg∈ .
(iv) This follows from (iii) if we set
• t ⇝ ,
• (1− t) ⇝ ,
• tf ⇝f,
• (1− t)f ⇝g,
and observe that the calculation is uniform for allt∈[0,1].
(v) Withoutlossofgeneralitywecanassumethat  isconvex,i.e.coincideswithitsconvex
hull.
Letubeanelementofthe 1-closureof(theconvexhullof) . Thenthereisasequence
(fj)j ⊂  ∶lim
j
‖u−fj‖1=0.
We have, because ofðuð ⩽ ðu−fjð+ðfjð,
{ðuð>f }⊂{ðu−fjð>f }∪{ ðfjð>f }
= {ðu−fjð>f }∩{ ðfjð>f }
∪{ðu−fjð>f }∩{ ðfjð ⩽f}
267

R.L. Schilling: Measures, Integrals & Martingales
∪{ðu−fjð ⩽f}∩{ ðfjð>f }
that
˚
{ðuð>f}
ðuðd
⩽ ˚
{ðu−fjð>f}
∩{ðfjð>f}
ðuðd+ ˚
{ðu−fjð>f}
∩{ðfjð⩽f}
ðuðd+ ˚
{ðu−fjð⩽f}
∩{ðfjð>f}
ðuðd
⩽ ˚
{ðu−fjð>f}
∩{ðfjð>f}
ðu−fjðd+ ˚
{ðu−fjð>f}
∩{ðfjð>f}
ðfjðd
+ ˚
{ðu−fjð>f}
∩{ðfjð⩽f}
ðu−fjð∨ðfjðd+ ˚
{ðu−fjð⩽f}
∩{ðfjð>f}
ðu−fjð∨ðfjðd
⩽ ‖u−fj‖1+ ˚
{ðfjð>f}
ðfjðd+‖u−fj‖1+ ˚
{ðfjð>f}
ðfjðd
⩽2‖u−fj‖1+2
, , , , , , , , , , , , , , , , , , , , →
j→∞
2.
Since this holds uniformly for all suchu, we are done.
■■
Problem 22.13 Solution: By assumption,
∀ >0∃ w ∈ 1
+∶ sup
f∈ ˚{ðfð>w}
ðfðd ⩽.
Now observe that
˚{sup1⩽j⩽kðfjð>w}
sup
1⩽j⩽k
ðfjðd
⩽
kÉ
l=1 ˚{sup1⩽j⩽kðfjð>w}∩{ðflð=sup1⩽j⩽kðfjð}
ðflðd
⩽
kÉ
l=1 ˚{ðflð>w}
ðflðd
⩽
kÉ
l=1

=k.
Therefore,
˚ sup
1⩽j⩽k
ðfjðd
⩽ ˚{sup1⩽j⩽kðfjð⩽w}
sup
1⩽j⩽k
ðfjðd+ ˚{sup1⩽j⩽kðfjð>w}
sup
1⩽j⩽k
ðfjðd
268

Solution Manual. Last update 18th July 2019
⩽ ˚ wd+k
and we get
lim
k→∞
1
k ˚ sup
1⩽j⩽k
ðfjðd ⩽ lim
k→∞
1
k ˚ wd+=
which proves our claim as >0 was arbitrary.
■■
Problem 22.14 Solution: Sincethefunction u ≡R,R> 0,isintegrablew.r.t.theprobabilitymeasure
P, we get
˚{ðujð>R}
ðujðdP ⩽ ˚{ðujð>R}
ðujð
ðujðp−1
Rp−1 dP
= 1
Rp−1 ˚{ðujð>R}
ðujðpdP
⩽ 1
Rp−1 ˚ ðujðpdP
⩽ 1
Rp−1sup
k ˚ ðukðpdP
= 1
Rp−1sup
k
‖uk‖p
p
which converges to zero asR →∞. This proves uniform integrability.
Counterexample:
Vitali’s theorem implies that a counterexample should satisfy
uj
P
, , , , , , , , , , , , , , , , , , , , →
j→∞
u, ‖uj‖1=1, u j does not converge in1.
Consider, for example, the probability space((0,1),ℬ(0,1),dx)and the sequence
uj ∶=j⋅ 1(0,1∕j).
Thenuj →0 pointwise (everywhere!), hence in measure. This is also the expected1 limit, if it
exists. Moreover,
‖uj‖1= ˚ ujdx=1
which meansthatuj cannotconverge in 1 to theexpected limitu ≡0, i.e. itdoes notconverge in
1.
Vitali’s theorem shows now that(uj)j cannot be uniformly integrable.
We can verify this fact also directly: forR> 0 and allj >Rwe get
˚{ðujð>R}
ðujðdx= ˚ ujdx=1
269

R.L. Schilling: Measures, Integrals & Martingales
which proves
sup
j ˚{ðujð>R}
ðujðdx=1 ∀ R> 0
and(uj)j cannot be uniformly integrable (in view of the equivalent characterizations of uniform
integrability on ﬁnite measure spaces, cf. Theorem 22.9)
■■
Problem 22.15 Solution: We have
∞É
j=k
j(j <ðfð ⩽j+1)=
∞É
j=k ˚{j<ðfð⩽j+1}
jd
⩽
∞É
j=k ˚{j<ðfð⩽j+1}
ðfðd
= ˚{ðfð>k}
ðfðd,
and, since2j ⩾j+1 for allj∈∈ N, also
2
∞É
j=k
j(j <ðfð ⩽j+1)=
∞É
j=k
2j(j <ðfð ⩽j+1)
=
∞É
j=k ˚{j<ðfð⩽j+1}
2jd
⩾
∞É
j=k ˚{j<ðfð⩽j+1}
ðfðd
= ˚{ðfð>k}
ðfðd.
This shows that
˚{ðfð>k}
ðfðd ⩽2
∞É
j=k
j(j <ðfð ⩽j+1) ⩽2 ˚{ðfð>k}
ðfðd
and this implies
sup
f∈ ˚{ðfð>k}
ðfðd ≃ sup
f∈
∞É
j=k
j(j <ðfð ⩽j+1).
Thisprovestheclaim(sinceweareinaﬁnitemeasurespacewhere u ≡kisanintegrablefunction!)
■■
Problem 22.16 Solution: Fix >0. By assumption there is somew=w ∈ 1
+ such that
sup
i ˚{ðfið>w}
ðfiðd ⩽.
Sinceðuið ⩽ ðfiðwe infer that{ðuið>w}⊂{ðfið>w}, and so
˚{ðuið>w}
ðuiðd ⩽ ˚{ðfið>w}
ðfiðd ⩽ uniformly for alli∈I.
■■
270

Solution Manual. Last update 18th July 2019
Problem 22.17 Solution: Letg∈ 1
+(). Then
0 ⩽ ˚ (ðuð−g∧ðuð)d = ˚{ðuð⩾g}
(ðuð−g)d ⩽ ˚{ðuð⩾g}
ðuðd.
Thisimpliesthatuniformintegrabilityofthefamily  impliesthattheconditionofProblem22.17
holds. On the other hand,
˚{ðuð⩾g}
ðuðd = ˚{ðuð⩾g}
(2ðuð−ðuð)d
⩽ ˚{ðuð⩾g}
(2ðuð−g)d
⩽ ˚{2ðuð⩾g}
(2ðuð−g)d
=2 ˚{ðuð⩾1
2g}
 ðuð− 1
2gd
=2 ˚{ðuð⩾1
2g}
 ðuð−1
2g∧ðuðd
andsince g∈ 1 if,andonlyif, 1
2g∈ 1,weseethattheconditiongiveninProblem22.17entails
uniform integrability.
In ﬁnite measure spaces this conditions is simpler: constants are integrable functions in ﬁnite
measure spaces; thus we can replace the condition given in Problem 22.17 by
lim
R→∞
sup
u∈ ˚ (ðuð−R∧ðuð)d =0.
■■
271



23 Martingales.
Solutions to Problems 23.123.16
Problem 23.1 Solution: SinceA0 ={ç,X} anA0-measurable functionu must satisfy{u=s}=ç
or=X, i.e. allA0-measurable functions are constants.
So if(uj)j∈N0 is a martingale,u0 is a constant and we can calculate its value because of the mar-
tingale property:
˚X
u0d = ˚X
u1d - ⇒u0=(X)−1
˚X
u1d. (*)
Conversely, sinceA0={ç,X} and since
˚ç
u0d = ˚ç
u1d
always holds, it is clear that the calculation and choice in (*) is necessary and suﬃcient for the
claim.
■■
Problem 23.2 Solution: We consider only the martingale case, the other two cases are similar.
(a) Sinceℬj ⊂Aj we get
˚A
ujd = ˚A
uj+1d ∀A∈Aj
- ⇒ ˚B
ujd = ˚B
uj+1d ∀B∈ℬj
showing that(uj,ℬj)j is a martingale.
(b) Itisclearthattheaboveimplicationcannotholdifweenlarge Aj tobecome Cj. Justconsider
the following ‘extreme’ case (to get a counterexample):Cj = A for allj. Any martingale
(uj,C)j must satisfy,
˚A
ujd = ˚A
uj+1d ∀A∈A.
Considering the setsA∶={uj <u j+1}∈ A andA‡∶={uj >u j+1}∈ A we conclude that
0= ˚{uj>uj+1}
(uj−uj+1)d - ⇒({uj >u j+1})=0
and, similarly({uj < uj+1}) = 0so thatuj = uj+1 almost everywhere and for allj. This
means that, if we start with a non-constant martingale(uj,Aj)j, then this can never be a
martingale w.r.t. the ﬁltration(Cj)j.
273

R.L. Schilling: Measures, Integrals & Martingales
■■
Problem 23.3 Solution: For the notation etc. we refer to Problem 4.15. Since the completionAj is
given by
Aj =(Aj,N), N ∶= M ⊂X∶∃ N ∈A, N ⊃M, (N)=0 
we ﬁnd that for allA∗
j ∈A∗
j there exists someAj ∈Aj such that
A∗
j ⧵Aj∪Aj ⧵A∗
j ∈N.
Writing ̄ for the unique extension of ontoA (and thus ontoAj for allj) we get forA∗
j,Aj as
above
óóóóóó˚A∗
j
ujd̄ − ˚Aj
ujd
óóóóóó
=
óóóóóó˚A∗
j
ujd̄ − ˚Aj
ujd̄ 
óóóóóó
= óóóó˚ (1A∗
j
− 1Aj)ujd̄ óóóó
⩽ ˚
óóó1A∗
j
− 1Aj
óóóujd̄ 
= ˚ 1A∗
j ⧵Aj∪Aj ⧵A∗
j
ujd̄ 
⩽ ˚ 1Nujd =0
for a suitable-null-setN ⊃A∗
j ⧵Aj∪Aj ⧵A∗
j. This proves that
˚A∗
j
ujd̄ = ˚Aj
ujd
andweseeeasilyfromthisthat (uj,A∗
j)j isagaina(sub-, super-)martingaleif (uj,Aj)j isa(sub-,
super-)martingale.
■■
Problem 23.4 Solution: To see that the condition is suﬃcient, setk = j +1 . For the necessity,
assume thatk = j+m. SinceAj ⊂ Aj+1 ⊂ ⋯ ⊂ Aj+m = Ak we get from the submartingale
property
˚A
ujd ⩽ ˚A
uj+1d ⩽ ˚A
uj+2d ⩽⋯ ⩽ ˚A
uj+md = ˚A
ukd.
For supermartingales resp. martingales the conditions obviously read:
˚A
ujd ⩾ ˚A
ukd ∀j <k, ∀A∈Aj
resp.
˚A
ujd = ˚A
ukd ∀j <k, ∀A∈Aj.
■■
274

Solution Manual. Last update 18th July 2019
Problem 23.5 Solution: We haveSj = {A ∈ Aj ∶ (A) < ∞} and we have to check conditions
(S1)–(S3) for a semiring, cf. page 39. Indeed
ç∈ Aj,(ç)=0 - ⇒ç∈ Sj - ⇒(S1);
and
A,B ∈Sj - ⇒A∩B∈Aj, (A∩B) ⩽(A)<∞
- ⇒A∩B∈Sj - ⇒(S2);
and
A,B ∈Sj - ⇒A ⧵B∈Aj, (A ⧵B) ⩽(A)<∞
- ⇒A ⧵B∈Sj - ⇒(S3).
SinceSj ⊂Aj also(Sj) ⊂Aj. On the other hand, ifA∈Aj with(A) = ∞we can, because
of -ﬁniteness ﬁnd a sequence(Ak)k ⊂ A0 ⊂ Aj such that(Ak) < ∞ and Ak ↑ X. Thus,
Ak∩A∈Sj for allkandA= ⋃
k(Ak∩A). This shows thatAj ⊂(Sj).
The rest of the problem is identical to remark 23.2(i) when combined with Lemma 16.6.
■■
Problem 23.6 Solution: UsingLemma17.2wecanapproximate uj ∈ 2(Aj)bysimplefunctionsin
(Aj),i.e.withfunctionsoftheform fl
j = ∑
mcl,m
j 1Al,m
j
(thesumisaﬁnitesum!) where cl
j ∈ R
andAl
j ∈Aj. Using the Cauchy–Schwarz inequality we also see that
˚ (fl
j −uj)ujd ⩽ ‖fl
j −uj‖L2⋅‖uj‖L2
l→∞
, , , , , , , , , , , , , , , , , , , , , , , →
j ﬁxed
0.
Using the martingale property we ﬁnd forj ⩽k:
˚ 1Al,m
j
ukd = ˚ 1Al,m
j
ujd ∀l, m
and therefore
˚ fl
j ukd = ˚ fl
j ujd ∀l
and since the limitl →∞exists
˚ ujukd =lim
l ˚ fl
j ukd =lim
l ˚ fl
j ujd = ˚ u2
jd.
■■
Problem 23.7 Solution: Since thefj’s are bounded, it is clear that(f ∙u)k is integrable. Now take
A∈Ak. Then
˚A
(f∙u)k+1d = ˚A
k+1É
j=1
fj−1(uj−uj−1)d
275

R.L. Schilling: Measures, Integrals & Martingales
= ˚A
(f∙u)k+fk(uk+1−uk)d
= ˚A
(f∙u)kd+ ˚ (1A⋅fk)(uk+1−uk)d
Using Remark 23.2(iii) we ﬁnd
˚ (1A⋅fk)(uk+1−uk)d = ˚ 1A⋅fkuk+1d− ˚ 1A⋅fkukd
= ˚ 1A⋅fkukd− ˚ 1A⋅fkukd
=0
and we conclude that
˚A
(f∙u)k+1d = ˚A
(f∙u)kd ∀A∈Ak.
■■
Problem 23.8 Solution:
(i) Note that
S2
n+1−S2
n =(Sn+n+1)2−S2
n =2
n+1+n+1Sn.
IfA∈An, then1ASn is independent ofn+1 and we ﬁnd, therefore,
˚A
(S2
n+1−S2
n)dP= ˚A
2
n+1dP+ ˚A
n+1SndP
⩾ ˚A
n+1SndP
= ˚ n+1(1ASn)dP
= ˚ n+1dP
«›››ﬂ›››‹
=0
˚ 1ASndP
=0.
(ii) Observe, ﬁrst of all, that due to independence
˚ S2
ndP=
nÉ
j=1 ˚ 2
j dP+
É
j≠k ˚ jkdP
=n ˚ 2
1dP+
É
j≠k ˚ jdP
«›ﬂ›‹
=0
˚ kdP
=n ˚ 2
1dP
276

Solution Manual. Last update 18th July 2019
so that ∶= ∫ 2
1dP is a reasonable candidate for the assertion. Using the calculation of
part (i) of this problem we see
[S2
n+1−(n+1)]−[ S2
n−n]= 2
n+1+n+1Sn−
and integrating over∫A…dP for anyA∈An gives, just as in (i), because of independence
of 1A andn+1 resp. 1ASn andn+1
˚A

[S2
n+1−(n+1)]−[ S2
n−n]

dP
= ˚ 1A⋅2
n+1dP+ ˚ n+1dP ˚ 1A⋅SndP− ˚A
dP
= P(A) ˚ 2
n+1dP− ˚A
dP
=0
since1 andn+1 are identically distributed implying that= ∫ 2
n+1dP= ∫ 2
1dP.
■■
Problem 23.9 Solution: As in Problem 23.8 we ﬁnd
Mn+1−Mn=2
n+1+Snn+1−2
n+1.
Integrating overA∈An yields
˚A
(Mn+1−Mn)dP
= ˚A
2
n+1dP+ ˚A
Snn+1dP−2
n+1 ˚A
dP
= P(A) ˚Ω
2
n+1dP
«›››ﬂ›››‹
=2
n+1
+ ˚A
SndP ˚Ω
n+1dP
«›››ﬂ›››‹
=0
−2
n+1P(A)
=0,
where we use the independence of1A andn+1 resp. of1ASn andn+1 and the hint given in the
statement of the problem.
■■
Problem 23.10 Solution: We ﬁnd that forA∈An
˚A
un+1d = ˚A
(un+dn+1)d = ˚A
und+ ˚A
dn+1d = ˚A
und
whichshowsthat (un,An)nisamartingale,hence (u2
n,An)nisasubmartingale—cf.Example23.3(vi).
Now
˚ u2
nd =
É
j ˚ d2
j d+2
É
j<k ˚ djdkd
277

R.L. Schilling: Measures, Integrals & Martingales
but, just as in Problem 23.6, we can approximatedj byAj-measurable simple functions(fl
j)l∈N
which shows, since∫Adkd =0 for anyA∈Aj andk>j :
˚ djdkd =lim
l ˚ fl
j dkd =0.
■■
Problem 23.11 Solution: ForA∈An we ﬁnd
˚A
401− p
p
1Sn+1
−
01− p
p
1Sn5
dP
= ˚A
01− p
p
1Sn401− p
p
1n+1
−1
5
dP
= ˚A
01− p
p
1Sn
dP⋅ ˚Ω
401− p
p
1n+1
−1
5
dP
where we use that1A
 1−p
p
Sn and  1−p
p
n+1−1 are independent, see formulae (23.6) and (23.7).
But sincen+1 is a Bernoulli random variable we ﬁnd
˚Ω
401− p
p
1n+1
−1
5
dP
=
401− p
p
11
−1
5
⋅p+
401− p
p
1−1
−1
5
⋅(1− p)
=[1−2 p]+[2 p−1]
=0.
The integrability conditions for martingales are obviously satisﬁed.
■■
Problem 23.12 Solution: AsolutioninamoregeneralcontextcanbefoundinExample25.4onpage
297 of the textbook.
■■
Problem 23.13 Solution: By deﬁnition, a supermartingale satisﬁes
˚A
ujd ⩾ ˚A
uj+1d ∀j∈ N, A∈Aj.
If we takeA=X and ifuk=0 , then this becomes
0= ˚X
ukd ⩾ ˚X
uk+1d ⩾0
and since, by assumption,uk+1 ⩾0, we conclude thatuk+1=0 .
■■
278

Solution Manual. Last update 18th July 2019
Problem 23.14 Solution: By deﬁnition,
A∈A ⇐ ⇒A∈A and ∀j∶A∩{ ⩽j}∈ Aj.
Thus,
• ç∈ A is obvious;
• ifA∈A, then
Ac∩{ ⩽j}={  ⩽j} ⧵A={ ⩽j}
«ﬂ‹
∈Aj
⧵(A∩{ ⩽j})
«››››››ﬂ››››››‹
∈Aj
∈Aj
thusAc ∈A.
• ifAl ∈A,l∈ N, then
4˝
l
Al
5
∩{ ⩽j}=
˝
l
Al∩{ ⩽j}
«›››››››ﬂ›››››››‹
∈Aj
∈Aj
thus⋃Al ∈A.
■■
Problem 23.15 Solution: By deﬁnition, is a stopping time if
∀n∈ N0∶{ ⩽n}∈ An.
Thus, if is a stopping time, we ﬁnd forn ⩾1
{ <n}={  ⩽n−1}∈ An−1⊂An
and, therefore, for alln∈ N0
{ =n}={  ⩽n} ⧵{ <n}∈ An.
Conversely, if{ =n}∈ An for alln, we get
{ ⩽k}={  =0}∪{  =1}∪ ⋯∪{ =k}∈ A0∪⋯∪Ak⊂Ak.
■■
Problem 23.16 Solution: Since∧ ⩽ and∧ ⩽, we ﬁnd from Lemma 23.6 that
ℱ∧ ⊂ℱ∩ℱ.
Conversely, ifA∈ℱ∩ℱ we know that
A∩{ ⩽j}∈ ℱj and A∩{ ⩽j}∈ ℱj ∀j∈ N0.
Thus,
A∩{∧ ⩽j}= A∩ { ⩽j}∪{  ⩽j}∈ℱj
and we getA∈ℱ∧.
■■
279



24 Martingale convergence theorems.
Solutions to Problems 24.124.9
Problem 24.1 Solution: We have0=0 which is clearly a stopping time and since
1∶=inf{ j >0∶ uj ⩽a}∧ N (infç=+∞)
it is clear that
{1>l}={ u1>a}∩ ⋯∩{ul >a}∈ Al.
Theclaimfollowsbyinductiononcewehaveshownthat k andk arestoppingtimesforageneric
value ofk. Since the structure of their deﬁnitions are similar, we show this fork only.
By induction assumption, let0,1,1,…,k−1,k be stopping times. By deﬁnition,
k∶=inf{ j >k−1∶uj ⩽a}∧ N (infç=+∞)
and we ﬁnd forl∈ N andl<N
{k>l}={ k−1 ⩽l}∈ Al
while, by deﬁnition
{k=N}=ç∈ AN.
■■
Problem 24.2 Solution: Theorem24.7becomesforsupermartingales: Let(ul)l∈−N beabackwards
supermartingaleandassumethat ðA−∞ is-ﬁnite. Thenlimj→∞u−j =u−∞∈(−∞,∞]existsa.e.
Moreover,L1-limj→∞u−j =u−∞ if, and only if,supj ∫ u−jd <∞; in this case(ul,Al)l∈−N is
a supermartingale andu−∞ is ﬁnitely-valued.
Using this theorem the claim follows immediately from the supermartingale property:
−∞< ˚A
u−1d ⩽ ˚A
u−jd ⩽ ˚A
u−∞d< ∞ ∀ j∈ N, A∈A−∞
and, in particular, forA=X∈A−∞.
■■
281

R.L. Schilling: Measures, Integrals & Martingales
Problem 24.3 Solution: Corollary 24.3 shows pointwise a.e. convergence. Using Fatou’s lemma we
get
0= lim
j→∞ ˚ ujd =liminf
j→∞ ˚ ujd
⩾ ˚ liminf
j→∞
ujd
= ˚ u∞d ⩾0
so thatu∞=0 a.e.
Moreover, since∫ ujd , , , , , , , , , , , , , , , , , , , , →
j→∞
0= ∫ u∞d, Theorem 24.6 shows thatuj →u∞ inL1-sense.
■■
Problem 24.4 Solution: FromL1-limj→∞uj =f we conclude thatsupj ∫ ðujðd <∞ and we get
thatlimj→∞uj exists a.e. SinceL1-convergence also implies a.e. convergence of a subsequence,
the limiting functions must be the same.
■■
Problem 24.5 Solution: The quickest solution uses the famous Chung-Fuchs result that a simple
random walk (this is justSj ∶=1+⋯+j withk iid Bernoullip=q = 1
2) does not converge
and that−∞=liminf jSj <limsupjSj =∞ a.e. Knowing this we are led to
P(uj converges)= P(0+1=0)= 1
2.
It remains to show thatuj is a martingale. ForA∈(1,…,j)we get
˚A
uj+1dP = ˚A
(0+1)(1+⋯+j+j+1)dP
= ˚A
(0+1)(1+⋯+j)dP + ˚A
(0+1)j+1dP
= ˚A
ujdP + ˚A
(0+1) dP ˚Ω
j+1dP
= ˚A
ujdP
where the last step follows because of independence.
IfyoudonotknowtheChung-Fuchsresult,youcouldargueasfollows: assumethatforsomeﬁnite
random variableS the limitSj(!) →S(!) takes place on a setA⊂ Ω. Since thej’s are iid, we
have
2+3+⋯ →S
and
1+2+⋯ →S
which means thatS andS+1 have the same probability distribution. But this entails thatS is
necessarily±∞, i.e.,Sj cannot have a ﬁnite limit.
■■
282

Solution Manual. Last update 18th July 2019
Problem 24.6 Solution:
(i) Cf. the construction in Scholium 23.4.
(ii) Note thatn2−(n−1)2−1=2 n−2 is even.
The functionf ∶ R2n−2 → R,f(x1,…,x2n−2)= x1+⋯+xn2−(n−1)2 is clearly Borel
measurable, i.e. the function
f((n−1)2+2,…,n2)= (n−1)2+2+⋯+n2
isAn-measurable and so is the setAn.
Moreover,x∈An if, and only if, exactly half of(n−1)2+2,…,n2 are+1 and the other
half is−1. Thus,
(An)=
0
2n−2
n−1
10
1
2
1n−10
1
2
1n−1
=
0
2n−2
n−1
10
1
2
12n−2
Using Stirling’s formula, we get
1
22k
0
2k
k
1
= (2k)!
k!k!
∼
√
22k(2k)2kekek
22k
√
2k
√
2kkkkke2k
= 1√
k
, , , , , , , , , , , , , , , , , , , , →
k→∞
0.
Settingk=n−1 this shows both
lim
n
(An)=0 and
É
n
(An)∼
É
n
1√
n
=∞.
Finally,limsupn 1An = 1limsupnAn =1 a.e. while, by Fatou’s lemma
0 ⩽ ˚ liminf
n
1And ⩽liminf
n ˚ 1And=liminf
n
(An)=0 ,
i.e.,liminf n 1An =0 a.e. This means that1An does not have a limit asn →∞.
(iii) ForA∈An we have because of independence
˚A
Mn+1d
= ˚A
Mn(1+ n2+1)d+ ˚A
1Ann2+1d
= ˚A
Mnd ˚[0,1]
(1+ n2+1)d+ ˚A
1And ˚[0,1]
n2+1d
= ˚A
Mnd.
(iv) We have
{Mn+1 ≠0}
={Mn+1 ≠0,n2+1=−1}∪{ Mn+1 ≠0,n2+1=+1}
⊂A n∪{Mn ≠0,n2+1=+1}.
283

R.L. Schilling: Measures, Integrals & Martingales
(v) By deﬁnition,
Mn+1−Mn=Mnn2+1+ 1Ann2+1=(Mn+ 1An)n2+1
so that
ðMn+1−Mnð= ðMn+ 1Anð⋅ðn2+1ð= ðMn+ 1Anð.
This shows that forx∈{lim nMn exists} the limitlimn 1An(x) exists. But, because of
(ii), the latter is a null set, so that the pointwise limit ofMn cannot exist.
On the other hand, using the inequality (iv), shows
(Mn+1 ≠0) ⩽ 1
2(Mn ≠0)+ (An)
and iterating this gives
(Mn+k ≠0) ⩽ 1
2k(Mn ≠0)+ (An)+ ⋯(An+k−1)
⩽ 1
2k +(An)+ ⋯(An+k−1).
Letting ﬁrstn →∞and thenk →∞yields
limsup
j
(Mj ≠0)=0
so thatlimj(Mj =0)=0 .
■■
Problem 24.7 Solution: Note that forA∈ {1},{2},…,{n},{n+1,n +2,…}we have
˚A
n+1dP = ˚A
(n+2) 1[n+2,∞)∩NdP
=
⎧
⎪
⎨
⎪⎩
0 ifA is a singleton
˚[n+1,∞)∩N
(n+2) 1[n+2,∞)∩NdP else
and in the second case we have
˚[n+1,∞)∩N
(n+2) 1[n+2,∞)∩NdP = ˚[n+2,∞)∩N
(n+2) dP
=(n+2)
∞É
j=n+2
P({j})
=(n+2)
∞É
j=n+2
0
1
j − 1
j+1
1
=1,
The same calculation shows
˚A
ndP = ˚A
(n+1) 1[n+1,∞)∩NdP
284

Solution Manual. Last update 18th July 2019
=
⎧
⎪
⎨
⎪⎩
0 ifAis a singleton
˚[n+1,∞)∩N
(n+1) 1[n+1,∞)∩NdP =1 else
so that
˚A
n+1dP = ˚A
ndP
for allA from a generator of the-algebra which contains an exhausting sequence. This shows,
by Remark 23.2(i) that(n)n is indeed a martingale.
The second calculation from above also shows that∫ ndP =1 while
sup
n
n=∞ and lim
n
n=0
are obvious.
■■
Problem 24.8 Solution:
(i) Using Problem 23.6 we get
˚ (uj−uj−1)2d = ˚ u2
jd−2 ˚ ujuj−1d+ ˚ u2
j−1d
= ˚ u2
jd−2 ˚ u2
j−1d+ ˚ u2
j−1d
= ˚ u2
jd− ˚ u2
j−1d
which means that
˚ u2
Nd =
NÉ
j=1 ˚ (uj−uj−1)2d
and the claim follows.
(ii) Because of Example 23.3(vi),p=2 , we conclude that(u2
j)j is a submartingale which,
due toL2-boundedness, satisﬁes the assumptions of Theorem 24.2 on submartingale
convergence. This means thatlimju2
j =u2 exists a.e. This is, alas, not good enough to
getuj →ua.e., it only shows thatðujð → ðuða.e.
The following trick helps: let(Ak)k ⊂ A0 be an exhausting sequence withAk ↑ X
and(Ak)<∞. Then(1Akuj)j is anL1-bounded martingale: indeed, ifA∈An then
A∩Ak∈An and it is clear that
˚A
1Akund = ˚A∩Ak
und = ˚A∩Ak
un+1d = ˚A
1Akun+1d
while, by the Cauchy–Schwarz inequality,
˚ ð1Akunðd ⩽
√
(Ak)⋅
v
sup
n ˚ u2
nd ⩽ck.
285

R.L. Schilling: Measures, Integrals & Martingales
Thus, we can use Theorem 24.2 and conclude that
1Akun , , , , , , , , , , , , , , , , , , , , →
n→∞
1Aku
almost everywhere with, because of almost-everywhere-uniqueness of the limits on
each of the setsAk, a single functionu. This showsun →ua.e.
(iii) Following the hint and using the arguments of part (i) we ﬁnd
˚ (uj+k−uj)2d = ˚ (u2
j+k−u2
j)d
=
j+kÉ
l=j+1 ˚ (u2
l−u2
l−1)d
=
j+kÉ
l=j+1 ˚ (ul−ul−1)2d.
Now we use Fatou’s lemma and the result of part (ii) to get
˚ liminf
j
(u−uj)2d ⩽liminf
j ˚ (u−uj)2d
⩽limsup
j ˚ (u−uj)2d
⩽limsup
j
∞É
l=j+1 ˚ (ul−ul−1)2d
=0
since, byL2-boundedness,∑∞
k=1 ∫(uk−uk−1)2d< ∞.
(iv) Since() < ∞, constants are integrable and we ﬁnd using the Cauchy–Schwarz and
Markov inequalities
˚ðukð>R
ðukðd ⩽
√
(ðukð>R)⋅
v
˚ u2
kd
⩽ 1
R
v
˚ u2
kd⋅
v
˚ u2
kd
⩽ 1
R sup
k ˚ u2
kd
fromwhichwegetuniformintegrability; theclaimfollowsnowfromparts(i)–(iii)and
Theorem 24.6.
■■
Problem 24.9 Solution:
(i) Note that∫ jdP = 0and ∫ 2
j dP = 1. Moreover,n ∶= ∑n
j=1jyj is a martingale
w.r.t. the ﬁltrationAn∶=(1,…,n)and
˚ 2
ndP =
nÉ
j=1
y2
j.
286

Solution Manual. Last update 18th July 2019
Problem 24.8 now shows that∑∞
j=1y2
j < ∞ means that the martingale(n)n is L2-
bounded, i.e.n converges a.e. The converse follows from part (iii).
(ii) This follows with the same arguments as in part (i) withAn=(1,…,n).
(iii) We show thatS2
n−An is a martingale. Now forA∈An
˚A
Mn+1dP = ˚A
(S2
n+1−An+1)dP
= ˚A
(S2
n+2n+1Sn+2
n+1−An−2
n+1)dP
= ˚A
(S2
n−An)dP + ˚A
(2n+1Sn+2
n+1−2
n+1)dP
= ˚A
MndP + ˚A
(2n+1Sn+2
n+1−2
n+1)dP
But, because of independence,
˚A
(2n+1Sn+2
n+1−2
n+1)dP
= ˚A
2n+1dP ˚Ω
SndP +P(A) ˚ 2
n+1dP −P(A)2
n+1
=0+ P(A)2
n+1−P(A)2
n+1
=0.
and the claim is established.
Now deﬁne
 ∶= ∶=inf{ j∶ ðMjð>}.
By optional sampling,(Mn∧)n is again a martingale and we have
ðMn∧ð=Mn1{n<}+ðMð1{n⩾}
⩽1{n<}+ðMð1{n⩾}
⩽1{n<}+ðM−M−1ð1{n⩾}+ðM−1ð1{n⩾}
=1{n<}+ðð1{n⩾}+ðM−1ð1{n⩾}
⩽1{n<}+ðð1{n⩾}+1{n⩾}
⩽+C
where we use, for the estimate ofM−1, the deﬁnition of for the last estimate. Since
(Mn∧)n is a martingale, this gives
˚ (S2
n∧−An∧)dP = ˚ (S2
0−A0)dP =0
so that
˚ An∧dP = ˚ S2
n∧dP ⩽(+C)2
287

R.L. Schilling: Measures, Integrals & Martingales
uniformly inn.
Thus, by Beppo Levi’s theorem,
˚ AdP ⩽(+C)2<∞
which means thatA < ∞ almost surely. But since∑
jj converges almost surely,
P( =∞)=1 for suﬃciently large, and we are done.
■■
288

25 Martingales in action.
Solutions to Problems 25.125.15
Problem 25.1 Solution: This problem is intimately linked with problem 25.7.
Without loss of generality we assume that and are ﬁnite measures, the case for-ﬁnite and
arbitrary is exactly as in the proof of Theorem 25.2.
Let(Ai)i be as described in the problem and deﬁne the ﬁnite-algebrasAn ∶= (A1,…,An).
Using the hint we can achieve that
An= Cn
1,…,C n
l(n)

withmutuallydisjoint Ck
i ’sandl(n) ⩽2n+1 and⨃
iCn
i =X. ThentheconstructionofExample
25.4 yields a countably-indexed martingale since the-algebrasAi are increasing.
This means, that the countable version of the martingale convergence theorem is indeed enough
for the proof.
■■
Problem 25.2 Solution: “⇒”: Assume ﬁrst that (25.1) holds, i.e. that ≪ . If(A▵B) = 0for
someA,B ∈A we get(A▵B)=0 . By deﬁnition,
(A▵B)= (A ⧵B)+ (B ⧵A)= (A ⧵(A∩B))+ (B ⧵(A∩B))=0
so that
(A ⧵(A∩B))= (B ⧵(A∩B))=0 .
Assume that(A)<∞. Then(A∩B) ⩽(A)<∞and we see that
(A)= (A∩B) and (B)= (A∩B)
which means that(A)= (B).
If (A) = ∞the condition(A ⧵(A∩ B)) = 0shows that(A∩ B) = ∞, otherwise0 =
(A ⧵(A∩B))= (A)− (A∩B)=∞ which is impossible. Again we have(A)=∞= (B).
“⇐”: Assume now that the condition stated in the problem is satisﬁed. IfN ∈ A is any-null
set, we chooseA∶=N andB∶=ç and observe thatA▵B=N. Thus,
(N)= (A▵B)=0 - ⇒ (A)= (B)
289

R.L. Schilling: Measures, Integrals & Martingales
but this is just(N)= (A)= (ç)=0 . Condition (25.1) follows.
■■
Problem 25.3 Solution: Using simply the Radon–Nikodým theorem, Theorem 25.2, gives
∀t ∃pt(x) such thatt(dx)= pt(x)⋅t(dx)
with a measurable functionx → pt(x); it is, however, far from being clear that(t,x) → pt(x) is
jointly measurable.
A slight variation of the proof of Theorem 25.2 allows us to incorporate parameters provided the
families of measures are measurable w.r.t. these parameters. Following the hint we set (notation
as in the proof of 25.2)
p(t,x)∶=
É
A∈
t(A)
t(A)IA(x)
with the agreement that0
0 ∶= 0(note thata
0 witha ≠ 0 will not turn up because of the absolute
continuity of the measures!). Sincet → t(A) andt → t(A) are measurable, the above sum is
measurable so that
(t,x) →p(t,x)
is a jointly measurable function. If we can show that
lim

p(t,x)= p(t,x)
exists (say, inL1,tbeing ﬁxed) then the limiting function is again jointly measurable.
Using exactly the arguments of the proof of Theorem 25.2 witht ﬁxed we can conﬁrm that this
limit exists and deﬁnes a jointly measurable function with the property that
t(dx)= p(t,x)⋅t(dx).
Because of the a.e. uniqueness of the Radon–Nikodým density the functionsp(t,x) andpt(x) co-
incide, for everyt a.e. as functions ofx; without additional assumptions on the nature of the de-
pendence on the parameter, the exceptional set may, though, depend ont!
■■
Problem 25.4 Solution:  ≪ . We show that(N) = 0- ⇒ (N) = 0. LetN ∈ ℬ(Rn) be a
Lebesgue null set. Using the invariance of Lebesgue measure under shifts we get
0= ˚ (N)
«ﬂ‹
=0
(dy) = ˚ (N−y)(dy)
= ¸ 1N(x+y)(dx)(dy)
Tonelli
= ¸ 1N(x+y)(dy)(dx)
290

Solution Manual. Last update 18th July 2019
= ˚ (N−y)(dy).
Therefore,(N−y)=0 forLebesguealmostevery y,i.e.thereissome x0suchthat (N+x0)=0 .
Now we use the quasi-invariance to get(N)= ((N+x0)− x0)=0 .
≪ . Weshow that(N)=0 - ⇒(N)=0 . LetN ∈ℬ(Rn)bea nullset forthe measure.
Similar to the ﬁrst part of the proof we get
0= ˚ (N−x)
«››ﬂ››‹
=0
(dx)= ˚ (N−y)(dy)
= ˚ (N)(dy)= (N)(Rn).
This shows that(N)=0 (unless is trivial....).
■■
Problem 25.5 Solution: Have a look at the respective solutions for Chapter 20.
■■
Problem 25.6 Solution: We writeu± for the positive resp. negative parts ofu ∈ 1(A), i.e.u =
u+−u− andu± ⩾0. Fix such a functionuand deﬁne
±(F)∶= ˚F
u±(x)(dx), ∀F ∈ℱ.
Clearly,± are measures on the-algebraℱ. Moreover
∀N ∈ℱ, (N)=0 - ⇒±(N)= ˚N
u±d =0
which means that± ≪ . By the Radon–Nikodým theorem we ﬁnd (up to null-sets unique)
positive functionsf±∈ 1(ℱ)such that
±(F)= ˚F
f±d ∀F ∈ℱ.
Thus,uℱ ∶=f+−f−∈ 1(ℱ)clearly satisﬁes
˚F
uℱ d = ˚F
ud ∀F ∈ℱ.
To see uniqueness, we assume thatw∈ 1(ℱ)also satisﬁes
˚F
wd = ˚F
ud ∀F ∈ℱ.
Since then
˚F
uℱ d = ˚F
wd ∀F ∈ℱ.
we can choosef ∶={w>u ℱ}and ﬁnd
0= ˚{w>uℱ}
(w−uℱ)d
291

R.L. Schilling: Measures, Integrals & Martingales
which is only possible if({w > uℱ})= 0. Similarly we conclude that({w < uℱ})= 0from
which we getw=uℱ almost everywhere.
Reformulation of the submartingale property.
Recall that(uj,Aj)j is a submartingale if, for everyj,uj ∈ 1(Aj)and if
˚A
ujd ⩽ ˚A
uj+1d ∀A∈Aj, ∀j.
We claim that this is equivalent to saying
uj ⩽u
Aj
j+1 almost everywhere, ∀j.
The direction ‘⇒’ is clear. To see ‘⇐’ we ﬁxj and observe that, since
˚A
ujd ⩽ ˚A
uj+1d = ˚A
u
Aj
j+1d ∀A∈Aj,
we get, in particular, forA∶={u
Aj
j+1<u j}∈ Aj,
0 ⩽ ˚{u
Aj
j+1<uj}
(u
Aj
j+1−uj)d
which is only possible if({u
Aj
j+1<u j})=0 .
■■
Problem 25.7 Solution: Sinceboth andare-ﬁnite,wecanrestrictourselves,usingthetechnique
of the Proof of Theorem 25.2 to the case where and are ﬁnite. All we have to do is to pick an
exhaustion(Kl)l,Kl ↑ X such that(Kl),(Kl) <∞ and to consider the measures1Kl and
1Kl which clearly inherit the absolute continuity from and.
Using the Radon–Nikodým theorem (Theorem 25.2) we get that
j ≪ j - ⇒j =uj⋅j
with anAj-measurable positive densityuj. Moreover, since is a ﬁnite measure,
˚X
ujd = ˚X
ujdj = ˚X
dj =j(X)<∞
so that all the(uj)j are-integrable. Using exactly the same argument as at the beginning of the
proofofTheorem25.2(ii) ⇒(i), wegetthat (uj)j isevenuniformly -integrable. Finally,(uj)j isa
martingale (given the measure), since forj,j +1 andA∈Aj we have
˚A
uj+1d = ˚A
uj+1dj+1
= ˚A
dj+1 (uj+1⋅j+1=j+1)
= ˚A
dj (A∈Aj)
292

Solution Manual. Last update 18th July 2019
= ˚A
ujdj (j =uj⋅j)
= ˚A
ujd
andweconcludethat uj →u∞ a.e.andin L1()forsomelimitingfunction u∞ whichisstill L1()
and alsoA∞ ∶=(⋃
j∈NAj)-measurable. Since, by assumption,A∞ =A, this argument shows
also that
=u∞⋅
and it reveals that
u∞= d
d =lim
j
dj
dj
.
■■
Problem 25.8 Solution: We can assume thatVj <∞, otherwise the inequality would be trivial.
Note that the random variablesj − Ej, j = 1,2,…,n are still independent and, of course,
centered (= mean-zero). Thus, by Example 23.3(x) we get that
Mk∶=
kÉ
j=1
(j− Ej) is a martingale
and, because of Example 23.3(v),(ðMkð)k is a submartingale. Applying (25.10) in this situation
proves the claimed inequality since
VMn= E(M2
n) (since EMn=0 )
=
nÉ
j=1
E(2
j)
whereweuse,forthelastequality,whatprobabilistscall TheoremofBienaymé fortheindependent
random variablesj:
E(M2
n)=
nÉ
j,k=1
E(j− Ej)(k− Ek)
=
nÉ
j=k=1
E(j− Ej)2+
É
j≠k
E(j− Ej)E(k− Ek) (by independence)
=
nÉ
j=k=1
E(j− Ej)2
=
nÉ
j=1
EM2
j

=
nÉ
j=1
VMj.
■■
293

R.L. Schilling: Measures, Integrals & Martingales
Problem 25.9 Solution:
(i) As in the proof of Theorem 25.12 we ﬁnd
˚ upd
(14.9)
= p ˚
∞
0
sp−1({u ⩾s}) ds
⩽ p ˚
∞
0
sp−2
0
˚ 1{u⩾s}(x)w(x)(dx)
1
ds
= p ˚
0
˚
∞
0
1[0,u(x)](s)sp−2ds
1
w(x)(dx)
= p ˚
u(x)p−1
p−1 w(x)(dx)
= p
p−1 ˚ up−1wd
Notethatthisinequalityismeantin [0,+∞],i.e.weallowthecases a ⩽+∞and+∞ ⩽+∞.
(ii) Pick conjugate numbersp,q ∈(1,∞), i.e.q= p
p−1. Then we can rewrite the result of (i) and
then apply Hölder’s inequality to get
‖u‖p
p ⩽ p
p−1 ˚ up−1wd
⩽ p
p−1
0
˚ u(p−1)qd
11∕q0
˚ wpd
11∕p
= p
p−1
0
˚ upd
11−1∕p
‖w‖p
= p
p−1 ‖u‖p−1
p ⋅‖w‖p
andtheclaimfollowsupondividingbothsidesby ‖u‖p−1
p . (Hereweusetheﬁnitenessofthis
expression, i.e. the assumptionu∈ p).
■■
Problem 25.10 Solution: Only the ﬁrst inequality needs proof. Note that
max
1⩽j⩽N ˚ ðujðpd ⩽ ˚ max
1⩽j⩽N
ðujðpd = ˚ u∗
Nd
from which the claim easily follows.
■■
Problem 25.11 Solution: Let(Ak)k ⊂A0 be an exhausting sequence, i.e.Ak ↑X and(Ak)<∞.
Since(uj)j isL1-bounded, we know that
sup
j
‖uj‖p ⩽c <∞
and we ﬁnd, using Hölder’s inequality with1
p+ 1
q =1
˚ ð1Akujðd ⩽  (Ak)1∕q
⋅‖uj‖p ⩽c (Ak)1∕q
294

Solution Manual. Last update 18th July 2019
uniformly for allj ∈ N. This means that the martingale(1Akuj)j (see the solution to Problem
24.8) isL1-bounded and we get, as in Problem 24.8 that for some unique functionu
lim
j
1Akuj = 1Aku ∀k
a.e., henceuj , , , , , , , , , , , , , , , , , , , , →
j→∞
ua.e. Using Fatou’s Lemma we get
˚ ðuðpd = ˚ liminf
j
ðujðpd
⩽liminf ˚ ðujðpd
⩽sup
j ˚ ðujðpd < ∞
which means thatu∈Lp.
Foreach k∈ Nthemartingale (1Akuj)j isalsouniformlyintegrable: usingHölder’sandMarkov’s
inequalities we arrive at
˚{1Akðujð>1AkR}
1Akðujðd ⩽ ˚{ðujð>R}
1Akðujðd
⩽  {ðujð>R}1∕q
‖uj‖p
⩽
0
1
Rp ‖uj‖p
p
11∕q
‖uj‖p
⩽ cp∕q+1
Rp∕q
and the latter tends, uniformly for allj, to zero asR →∞. Since 1Ak⋅R is integrable, the claim
follows.
Thus,Theorem24.6appliesandshowsthatfor u∞∶=uandevery kthefamily (uj1Ak)j∈N∪{∞} is
a martingale. Because of Example 23.3(vi)(ðujðp1Ak)j∈N∪{∞} is a submartingale and, therefore,
for allk∈ N
˚ ð1Akujðpd ⩽ ˚ ð1Akuj+1ðpd ⩽ ˚ ð1Aku∞ðpd = ˚ ð1Akuðpd,
Since, by Fatou’s lemma
˚ ð1Akuðpd = ˚ liminf
j
ð1Akujðpd ⩽liminf
j ˚ ð1Akujðpd
we see that
˚ ð1Akuðpd =lim
j ˚ ð1Akujðpd =sup
j ˚ ð1Akujðpd.
Since suprema interchange, we get
˚ ðuðpd =sup
k ˚ ð1Akuðpd
=sup
k
sup
j ˚ ð1Akujðpd
295

R.L. Schilling: Measures, Integrals & Martingales
=sup
j
sup
k ˚ ð1Akujðpd
=sup
j ˚ ðujðpd
and Riesz’s convergence theorem, Theorem 13.10, ﬁnally proves thatuj →uinLp.
■■
Problem 25.12 Solution: Sincefk is a martingale and since
˚ ðfkðd ⩽
É
z∈2−kZZn
1
n(Qk(z)) ˚Qk(z)
ðfðdn
˚ 1Qk(z)dn
=
É
z∈2−kZZn ˚Qk(z)
ðfðdn
= ˚ ðfðdn<∞
we get from the martingale convergence theorem 24.2 that
f∞∶=lim
k
fk
exists almost everywhere and thatf∞∈ 1(ℬ). The above calculation shows, on top of that, that
for any setQ∈A[0]
k
˚Q
fkdn= ˚Q
fd n
and
˚Q
ðfkðdn ⩽ ˚Q
ðfðdn
which means that, using Fatou’s Lemma,
˚Q
ðf∞ðdn ⩽liminf
k ˚Q
ðfkðdn ⩽ ˚Q
ðfðdn
forall Q∈A[0]
k andany k. SinceS = ⋃
kA[0]
k isasemi-ringandsinceonbothsidesoftheabove
inequality we have measures, this inequality extends toℬ=(S)(cf. Lemma 16.6) and we get
˚B
ðf∞ðdn ⩽ ˚B
ðfðdn.
Sincef∞ andf areℬ-measurable,wecantake B={ ðf∞ð> ðfð}andwegetthat f =f∞ almost
everywhere. This shows that(fk)k∈N∪{∞} is a martingale.
Thus all conditions of Theorem 24.6 are satisﬁed and we conclude that(fk)k is uniformly integ-
rable.
■■
296

Solution Manual. Last update 18th July 2019
Problem 25.13 Solution: As one would expect, the derivative atx turns out to beu(x). This is seen
as follows (without loss of generality we can assume thaty>x ):
óóóó
1
x−y
0
˚[a,x]
u(t)dt− ˚[a,x]
u(t)dt
1
−u(x)óóóó
= óóóó
1
x−y ˚[x,y]
 u(t)− u(x)dtóóóó
⩽ 1
ðx−yð ˚[x,y]
óóóu(t)− u(x)óóódt
⩽ 1
ðx−yð ðx−yð sup
t∈[x,y]
óóóu(t)− u(x)óóó
= sup
t∈[x,y]
óóóu(t)− u(x)óóó
and the last expression tends to0asðx−yð →0sinceuis uniformly continuous on compact sets.
Ifuisnotcontinuousbutmerelyofclass L1,wehavetorefertoLebesgue’sdiﬀerentiationtheorem,
Theorem 25.20, in particular formula (25.19) which reads in our case
u(x)=lim
r→0
1
2r ˚(x−r,x+r)
u(t)dt
for Lebesgue almost everyx∈(a,b).
■■
Problem 25.14 Solution: We follow the hint: ﬁrst we remark that by Lemma 14.14 we know that
f has at most countably many discontinuities. Since it is monotone, we also know thatF(t) ∶=
f(t+)=lim s>t,s→tf(s)existsandisﬁniteforevery tandthat {f ≠F}isatmostcountable(since
it is contained in the set of discontinuities off), hence a Lebesgue null set.
Iff is right-continuous,(a,b] ∶=f(b)− f(a) extends uniquely to a measure on the Borel-sets
and this measure is locally ﬁnite and-ﬁnite. If we apply Theorem 25.9 to and=1 we can
write=◦+⊥ with◦≪ and⊥⊥. By Corollary 25.22D⊥=0 a.e. andD◦ exists a.e.
and we get a.e.
D(x)=lim
r→0
(x−r,x +r)
2r =lim
r→0
◦(x−r,x +r)
2r +0
and we can setf‡(x)= D(x)which is a.e. deﬁned. Where it is not deﬁned, we put it equal to0.
Now we get
f(b)− f(a)= (a,b]
⩾(a,b)
= ˚(a,b)
d
⩾ ˚(a,b)
d◦
= ˚(a,b)
D(x)(dx)
297

R.L. Schilling: Measures, Integrals & Martingales
= ˚(a,b)
f‡(x)(dx).
The above estimates show that we get equality iff is continuous and also absolutely continuous
w.r.t. Lebesgue measure.
■■
Problem 25.15 Solution: Without loss of generality we may assume thatfj(a) = 0, otherwise we
would consider the (still increasing) functionsx →fj(x)− fj(a)resp. their sumx →s(x)− s(a).
Thederivativesarenotinﬂuencedbythisoperation. Asindicatedinthehintcall sn(x)∶= f1(x)+
⋯+fn(x)thenth partial sum. Clearly,s,sn are increasing
sn(x+ℎ)− sn(x)
ℎ ⩽ sn+1(x+ℎ)− sn+1(x)
ℎ ⩽ s(x+ℎ)− s(x)
ℎ .
and possess, because of Problem 25.14, almost everywhere positive derivatives:
s‡
n(x) ⩽s‡
n+1(x) ⩽⋯s‡(x), ∀x∉E
Note that the exceptional null-sets depend originally on the functionsn etc. but we can consider
their (countable!!) union and get thus a universal exceptional null setE. This shows that the
formally diﬀerentiated series
∞É
j=1
f‡
j(x) converges for allx∉E.
Since the sequence of partial sums is increasing, it will be enough to check that
s‡(x)− s‡
nk
(x) , , , , , , , , , , , , , , , , , , , , →
k→∞
0 ∀x∉E.
Since, by assumption the sequencesk(x) → s(x) we can choose a subsequencenk in such a way
that
s(b)− snk(b)<2−k ∀k∈ N.
Since
0 ⩽s(x)− snk(x) ⩽s(b)− snk(b)
the series
∞É
k=1
(s(x)− snk(x)) ⩽
∞É
k=1
2−k<∞ ∀ x∈[a,b].
By the ﬁrst part of the present proof, we can diﬀerentiate this series term-by-term and get that
∞É
k=1
(s‡(x)− s‡
nk
(x)) converges ∀x∈(a,b) ⧵E
and, in particular,s‡(x)− s‡
nk
(x) , , , , , , , , , , , , , , , , , , , , →
k→∞
0 for allx∈(a,b) ⧵E which was to be proved.
■■
298

26 Abstract Hilbert space.
Solutions to Problems 26.126.19
Problem 26.1 Solution: If we set=1+⋯+n,X={1,2,…,n},A =P(X) or= ∑
j∈Nj,
X= N,A =P(X), respectively, we can deduce 26.5(i) and (ii) from 26.5(iii).
Let us, therefore, only verify (iii). Without loss of generality (see the complexiﬁcation of a real
inner product space in Problem 26.3) we can consider the real case whereL2=L2
R.
• L2 is a vector space — this was done in Remark 13.5.
• ⟨u,v⟩ is ﬁnite onL2×L2 — this is the Cauchy–Schwarz inequality 13.3.
• ⟨u,v⟩ is bilinear — this is due to the linearity of the integral.
• ⟨u,v⟩ is symmetric — this is obvious.
• ⟨v,v⟩ is deﬁnite, and‖u‖2 is a Norm — cf. Remark 13.5.
■■
Problem 26.2 Solution:
(i) We prove it for the complex case—the real case is simpler. Observe that
⟨u±w,u ±w⟩= ⟨u,u⟩±⟨u,w⟩±⟨w,u⟩+⟨w,w⟩
= ⟨u,u⟩±⟨u,w⟩±⟨u,w⟩+⟨w,w⟩
= ⟨u,u⟩±2Re ⟨u,w⟩+⟨w,w⟩.
Thus,
⟨u+w,u +w⟩+⟨u−w,u −w⟩=2 ⟨u,u⟩+2⟨w,w⟩.
Since‖v‖2= ⟨v,v⟩ we are done.
(ii) (SP1): Obviously,
0<(u,u)= 1
4 ‖2v‖2= ‖v‖2 - ⇒v ≠0.
(SP1): is clear.
(iii) Using at the point (*) below the parallelogram identity, we have
4(u+v,w)=2( u+v,2w)
= 1
2
 ‖u+v+2w‖2−‖u+v−2w‖2
299

R.L. Schilling: Measures, Integrals & Martingales
= 1
2
 ‖(u+w)+( v+w)‖2−‖(u−w)+( v−w)‖2
∗
= 1
2

2 ‖u+w‖2+‖v+w‖2−‖u−w‖2−‖v−w‖2
=4(u,w)+4( v,w)
and the claim follows.
(iv) We show(qv,w) =q(v,w) for allq ∈ Q. Ifq = n∈ N0, we iterate (iii)n times and
have
(nv,w)= n(v,w) ∀ n∈ N0 (*)
(the casen=0 is obvious). By the same argument, we get form∈ N
(v,w)=  m 1
mv,w=m 1
mv,w
which means that
 1
mv,w= 1
m(v,w) ∀ m∈ N. (**)
Combining (*) and (**) then yields(n
mv,w)= n
m(v,w). Thus,
(pu+qv,w)= p(u,w)+ q(v,w) ∀ p,q ∈ Q.
(v) By the lower triangle inequality for norms we get for anys,t ∈ R
óóó‖tv±w‖−‖sv±w‖óóó ⩽ ‖(tv±w)−( sv±w)‖
= ‖(t−s)v‖
= ðt−sð⋅‖v‖.
This means that the mapst →tv±w are continuous and so ist →(tv,w) as the sum
of two continuous maps. Ift ∈ R is arbitrary, we pick a sequence(qj)j∈N ⊂ Q such
thatlimjqj =t. Then
(tv,w)=lim
j
(qjv,w)=lim
j
qj(qv,w)= t(v,w)
so that
(su+tv,w)=( su,w)+( tv,w)= s(u,w)+ t(v,w).
■■
Problem 26.3 Solution: This is actually a problem on complexiﬁcation of inner product spaces... .
Sincevandiw are vectors inV ⊕iV and since‖v‖= ‖±iv‖, we get
(v,iw)R= 1
4
 ‖v+iw‖2−‖v−iw‖2
= 1
4
 ‖i(w−iv)‖2−‖(−i)(w+iv)‖2
= 1
4
 ‖w−iv‖2−‖w+iv‖2
=(w,−iv)R
=−(w,iv)R.
(*)
300

Solution Manual. Last update 18th July 2019
In particular,
(v,iv)=−( v,iv) - ⇒(v,iv)=0 ∀ v,
and we get
(v,v)C=(v,v)R>0 - ⇒v=0.
Moreover, using (*) we see that
(v,w)C=(v,w)R+i(v,iw)R
∗
=(w,v)R−i(w,iv)R
=(w,v)R+̄i⋅(w,iv)R
=(w,v)R+i(w,iv)R
=(w,v)C.
Finally, for real, ∈ R the linearity property of the real scalar product shows that
(u+v,w)C=(u,w)R+(v,w)R+i(u,iw)R+i(v,iw)R
=(u,w)C+(v,w)C.
Therefore to get the general case where, ∈ C we only have to consider the purely imaginary
case:
(iv,w)C=(iv,w)R+i(iv,iw)R
∗
=−(v,iw)R−i(v,−w)R
=−(v,iw)R+i(v,w)R
=i i(v,iw)R+(v,w)R

=i(v,w)C,
where we use twice the identity (*). This shows complex linearity in the ﬁrst coordinate, while
skew-linearity follows from the conjugation rule(v,w)C=(w,v)C.
■■
Problem 26.4 Solution: The parallelogram law (stated forL1)would say:
0
˚
1
0
ðu+wðdx
12
+
0
˚
1
0
ðu−wðdx
12
=2
0
˚
1
0
ðuðdx
12
+2
0
˚
1
0
ðwðdx
12
.
Ifu±w,u,w have always only ONE sign (i.e.+ve or−ve), we could leave the modulus signsð∙ð
away, and the equality would be correct! To show that there is no equality, we should therefore
choose functions where we have some sign change. We try:
u(x)=1∕2 , w (x)= x
301

R.L. Schilling: Measures, Integrals & Martingales
(note:u−w does change its sign!) and get
˚
1
0
ðu+wðdx= ˚
1
0
(1
2+x)dx=[ 1
2(x+x2)]1
0=1
˚
1
0
ðu−wðdx= ˚
1∕2
0
(1
2−x)dx+ ˚
1
1∕2
(x− 1
2)dx
=[ 1
2(x−x2)]1∕2
0 +[ 1
2(x2−x)]1
1∕2
= 1
4− 1
8− 1
8+ 1
4 = 1
4
˚
1
0
ðuðdx= ˚
1
0
1
2dx= 1
2
˚
1
0
ðwðdx= ˚
1
0
xdx =[ 1
2x2]1
0= 1
2
This shows that
12+( 1
4)2= 17
16 ≠1=2( 1
2)2+2( 1
2)2.
We conclude, in particular, thatL1 cannot be a Hilbert space (since in any Hilbert space the Par-
allelogram law is true....).
■■
Problem 26.5 Solution:
(i) Ifk=0 we have=1 and everything is obvious. Ifk ≠0, we use the summation formula
for the geometric progression to get
S ∶= 1
n
nÉ
j=1
jk = 1
n
nÉ
j=1
 kj
= 
n
1−( k)n
1− k
but(k)n=exp(2i
n⋅k⋅n)=exp(2 ik)=1 . ThusS =0 and the claim follows.
(ii) Note thatj =−j so that
‖v+jw‖2= ⟨v+jw,v +jw⟩
= ⟨v,v⟩+⟨v,jw⟩+⟨jw,v⟩+⟨jw,jw⟩
= ⟨v,v⟩+−j⟨v,w⟩+j⟨w,v⟩+j−j⟨w,w⟩
= ⟨v,v⟩+−j⟨v,w⟩+j⟨w,v⟩+⟨w,w⟩.
Therefore,
1
n
nÉ
j=1
j‖v+jw‖2
= 1
n
nÉ
j=1
j⟨v,v⟩+1
n
nÉ
j=1
⟨v,w⟩+1
n
nÉ
j=1
2j⟨w,v⟩+1
n
nÉ
j=1
j⟨w,w⟩
=0+ ⟨v,w⟩+0+0
where we use the result from part (i) of the exercise.
302

Solution Manual. Last update 18th July 2019
(iii) Since the function → ei‖v+eiw‖2 is bounded and continuous, the integral exists as
a (proper) Riemann integral, and we can useany Riemann sum to approximate the integral,
see12.6–12.12inChapter12orCorollaryI.6andTheoremI.8ofAppendixI. Beforewedo
that, we change variables according to =(+)∕2 so thatd =d∕2 and
1
2 ˚(−,]
eiôôôv+eiwôôô
2
d=− ˚(0,1]
e2i ôôôv−e2i wôôô
2
d .
Now using equidistant Riemann sums with step1∕n and nodesj
n =e2i⋅1
n⋅j,j =1,2,…,n
yields, because of part (ii) of the problem,
− ˚(0,1]
e2i ôôôv−e2i wôôô
2
d =− lim
n→∞
1
n
nÉ
j=1
j
n‖v−j
nw‖2
=− lim
n→∞
⟨v,−w⟩
= ⟨v,w⟩.
■■
Problem 26.6 Solution: We assume thatV is aC-inner product space. Then,
‖v+w‖2= ⟨v+w,v +w⟩
= ⟨v,v⟩+⟨v,w⟩+⟨w,v⟩+⟨w,w⟩
= ‖v‖2+⟨v,w⟩+⟨v,w⟩+‖w‖2
= ‖v‖2+2Re ⟨v,w⟩+‖w‖2.
Thus
‖v+w‖2= ‖v‖2+‖w‖2 ⇐ ⇒Re⟨v,w⟩=0 ⇐ ⇒v⊥w.
■■
Problem 26.7 Solution: Let(ℎk)k⊂  such thatlimk‖ℎk−ℎ‖=0 . By the triangle inequality
‖ℎk−ℎl‖ ⩽ ‖ℎk−ℎ‖
«›ﬂ›‹
→0
+‖ℎ−ℎl‖
«››ﬂ››‹
→0
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , →
k,l→∞
0.
■■
Problem 26.8 Solution: Letg, g∈ . By the Cauchy–Schwarz inequality 26.3
óó⟨g,ℎ⟩−⟨ g,ℎ⟩óó ⩽ óó⟨g− g,ℎ⟩óó ⩽ ‖ℎ‖⋅‖ g−g‖
which proves continuity. Incidentally, this calculation shows also that, sinceg → ⟨g,ℎ⟩ is linear,
it would have been enough to check continuity at the pointg=0 (think about it!).
■■
303

R.L. Schilling: Measures, Integrals & Martingales
Problem 26.9 Solution: Deﬁniteness(N1)andpositivehomogeneity( N2)areobvious. Thetriangle
inequality reads in this context (g,g‡,ℎ,ℎ ‡∈ ):
‖ð(g,ℎ)+( g‡,ℎ‡)ð‖ ⩽ ‖ð(g,ℎ)ð‖+‖ð(g‡,ℎ‡)ð‖ ⇐ ⇒
 ‖g+g‡‖p+‖ℎ+ℎ‡‖p1∕p
⩽  ‖g‖p+‖ℎ‖p1∕p
+ ‖g‡‖p+‖ℎ‡‖p1∕p
.
Since
 ‖g+g‡‖p+‖ℎ+ℎ‡‖p1∕p
⩽  ‖g‖‖g‡‖p
+‖ℎ‖+‖ℎ‡‖p1∕p
wecanusetheMinkowskiinequalityforsequencesresp.in R2—whichreadsfornumbers a,A,b,B ⩾
0
 (a+b)p+(A+B)p1∕p
⩽  ap+Ap1∕p
+ bp+Bp1∕p
—and the claim follows.
Since R2 isonlywiththeEuclideannormaHilbertspace—theparallelogramidentityfailsforthe
norms(ðxðp+ðyðp)1∕p—this shows that also in the case at hand onlyp=2 will be a Hilbert space
norm.
■■
Problem 26.10 Solution: Forthescalarproductwehaveforall g,g‡,ℎ,ℎ ‡∈  suchthat ‖g−g‡‖2+
‖ℎ−ℎ‡‖2<1
óóó⟨g−g‡,ℎ −ℎ‡⟩óóó ⩽ ‖g−g‡‖⋅‖ℎ−ℎ‡‖ ⩽ ‖g−g‡‖2+‖ℎ−ℎ‡‖21∕2
where we use the elementary inequality
ab ⩽ 1
2(a2+b2) ⩽a2+b2 ⩽
√
a2+b2
«››››ﬂ››››‹
if a2+b2⩽1
.
Since(g,ℎ) → ‖g‖2+‖ℎ‖21∕2
is a norm on×  we are done.
Essentially the same calculation applies to(t,ℎ) →t⋅ℎ.
■■
Problem 26.11 Solution: Assume that has a countable maximal ONS, say(ej)j. Then, by deﬁni-
tion,everyvector ℎ∈  canbeapproximatedbyasequencemadeupofﬁnitelinearcombinations
of the(ej)j:
ℎk∶=
n(k)É
j=1
j⋅ej
(note thatj =0 is perfectly possible!). In view of problem 26.10 we can even assume that thej
are rational numbers. This shows that the set
∶=
$ nÉ
j=1
j⋅ej ∶j ∈ Q,n ∈ N
%
304

Solution Manual. Last update 18th July 2019
is a countable dense subset of.
Conversely, if ⊂  is a countable dense subset, we can use the Gram-Schmidt procedure and
obtain froman ONS. Then Theorem 26.24 proves the claim.
■■
Problem 26.12 Solution: Let us, ﬁrst of all, show that for a closed subspaceC ⊂  we haveC =
(C⊥)⊥.
Because of Lemma 26.12 we know thatC ⊂(C⊥)⊥ and thatC⊥ is itself a closed linear subspace
of . Thus,
C⊕C ⊥= =C⊥⊕(C⊥)⊥.
ThusC cannot be a proper subspace of(C⊥)⊥ and thereforeC =(C⊥)⊥.
Applyingthistotheobviouslyclosedsubspace C ∶= K⋅w=span(w)weconcludethat span(w)=
span(w)⊥⊥.
By assumption,Mw={w}⊥ andM⊥
w ={w}⊥⊥ and we havew∈{w}⊥⊥. The last expression is
a (closed) subspace, so
w∈{w}⊥⊥ - ⇒span(w)⊂{w}⊥⊥
also. Further
{w}⊂span(w) - ⇒{w}⊥⊃span(w)⊥
- ⇒{w}⊥⊥⊂span(w)⊥⊥=span(w)
and we conclude that
{w}⊥⊥=span(w)
which is either{0}or a one-dimensional subspace.
■■
Problem 26.13 Solution:
(i) By Pythagoras’ Theorem 26.19
‖ej−ek‖2= ‖ej‖2+‖ek‖2=2 ∀ j ≠k.
This shows that no subsequence(ej)j∈⟋ can ever be a Cauchy sequence, i.e. it cannot
converge.
Ifℎ∈  we get from Bessel’s inequality 26.19 that the series
É
j
ð⟨ej,ℎ⟩ð2 ⩽ ‖ℎ‖2
is ﬁnite, i.e. converges. Thus the sequence with elements⟨ej,ℎ⟩ must converge to0 as
j →∞.
305

R.L. Schilling: Measures, Integrals & Martingales
(ii) Parseval’s equality 26.19 shows that
‖ℎ‖2=
∞É
j=1
ð⟨ej,ℎ⟩ð2=
∞É
j=1
ðcjð2 ⩽
∞É
j=1
1
j2 <∞
uniformly for allℎ∈Q, i.e.Qis a bounded set.
Let(ℎl)l ⊂ Qbe a sequence withlimlℎl = ℎ and writecj ∶= ⟨ej,ℎ⟩ andcl
j ∶=
⟨ej,ℎl⟩. Because of the continuity of the scalar product
ðcjð= ð⟨ej,ℎ⟩ð=lim
l
ð⟨ej,ℎl⟩ð=lim
l
ðcl
j ð ⩽ 1
j
which means thatℎ∈Qand thatQ is closed.
Let(ℎl)l ⊂Q be a sequence and setcj(l)∶= ⟨ej,ℎl⟩. Using the Bolzano-Weierstraß
theorem for bounded sequences we get
ðc1(l)ð ⩽1 - ⇒∃ c1(l1
j)
j ⊂  c1(l)
l ∶lim
j
c1(l1
j)= 1
and
ðc2(l1
j)ð ⩽ 1
2 - ⇒∃ c2(l2
j)
j ⊂  c2(l1
j)
j ∶lim
j
c2(l2
j)= 2
and, recursively,
ðck(lk−1
j )ð ⩽ 1
k - ⇒∃ ck(lk
j)
j ⊂  ck(lk−1
j )
j ∶lim
j
ck(lk
j)= k
and since we have considered sub-sub-etc.-sequences we get
ck(lm
m) , , , , , , , , , , , , , , , , , , , , , , →
m→∞
k ∀k∈ N.
Thus, we have constructed a subsequence(ℎlm
m
)m⊂(ℎl)l with
⟨ek,ℎlm
m
⟩ , , , , , , , , , , , , , , , , , , , , , , →
m→∞
k ∀k∈ N (*)
so thatj ⩽ 1∕j. Setting ℎ = ∑
jjej we see (by Parseval’s relation) thatℎ ∈ Q.
Further,
‖ℎ−ℎlm
m
‖2=
∞É
j=1
ðj−cj(lm
m)ð2
⩽
NÉ
j=1
ðj−cj(lm
m)ð2+
∞É
j=N+1
4
j2.
Letting ﬁrstm →∞we get, because of (*)
NÉ
j=1
ðj−cj(lm
m)ð2 , , , , , , , , , , , , , , , , , , , , , , →
m→∞
0,
and lettingN →∞gives
limsup
m
‖ℎ−ℎlm
m
‖2 ⩽
∞É
j=N+1
4
j2 , , , , , , , , , , , , , , , , , , , , , , , , →
N→∞
0
so thatlimm‖ℎ−ℎlm
m
‖2=0 .
306

Solution Manual. Last update 18th July 2019
(iii) R cannot be compact since(ej)j ⊂ Rdoes not have any convergent subsequence, see
part (i).
Ris bounded sincer∈Rif, and only if, there is somej∈ N such that
‖r−ej‖ ⩽ 1
j ⩽1.
Thus, everyr∈Ris bounded by
‖r‖ ⩽ ‖r−ej‖+‖ej‖ ⩽2.
Ris closed. Indeed, ifxj ∈B1∕j(ej)we see that forj ≠k
‖xj−xk‖= ‖(xj−ej)+( ej−ek)+( ek−xk)‖
⩾ ‖ej−ek‖−‖xj−ej‖−‖xk−ek‖
(i)
⩾
√
2− 1
j − 1
k.
This means that any sequence(rj)r ⊂R withlimjrj =r is in at most ﬁnitely many of
the setsB1∕j(ej). But a ﬁnite union of closed sets is closed so thatr∈R.
(iv) Assume that∑
j2
j < ∞. Then closedness, boundedness and compactness follows
exactly as in part (ii) of the problem withj replacing1∕j.
Conversely, assume thatS is compact. Then the sequence
ℎl =
lÉ
j=1
jej ∈S
and, by compactness, there is a convergent subsequence
ℎlk =
lkÉ
j=1
jej , , , , , , , , , , , , , , , , , , , , →
k→∞
ℎ.
By Parseval’s identity we get:
‖ℎlk‖2=
lkÉ
j=1
2
j , , , , , , , , , , , , , , , , , , , , →
k→∞
∞É
j=1
2
j = ‖ℎ‖2<∞.
■■
Problem 26.14 Solution:
(i) Note that for allg ≠0
ð⟨g,ℎ⟩ð ⩽ ‖g‖⋅‖ℎ‖ - ⇒ ð⟨g,ℎ⟩ð
‖g‖ ⩽ ‖ℎ‖
so that
sup
g≠0
ð⟨g,ℎ⟩ð
‖g‖ ⩽ ‖ℎ‖.
307

R.L. Schilling: Measures, Integrals & Martingales
Since forg=ℎ the supremum is attained, we get equality.
Further, sinceôôô
g
‖g‖
ôôô=1 , we have
sup
g≠0
ð⟨g,ℎ⟩ð
‖g‖ =sup
g≠0
óóó
( g
‖g‖,ℎ
)óóó= sup
, ‖‖=1
ð⟨,ℎ⟩ð.
Finally,
‖ℎ‖= sup
g, ‖g‖=1
ð⟨g,ℎ⟩ð ⩽ sup
g, ‖g‖⩽1
ð⟨g,ℎ⟩ð ⩽ sup
g, ‖g‖⩽1
‖g‖⋅‖ℎ‖ ⩽ ‖ℎ‖.
(ii) Yes, since we can, by a suitable rotationei achieve that
⟨eig,ℎ⟩= ð⟨g,ℎ⟩ð
while‖g‖= ‖eig‖.
(iii) Yes. IfD ⊂ is dense andℎ ∈  we ﬁnd a sequence(dj)j ⊂ Dwithlimjdj = ℎ.
Since the scalar product and the norm are continuous, we get
lim
j
⟨dj,ℎ⟩
‖dj‖ = ⟨ℎ,ℎ⟩
‖ℎ‖ = ‖ℎ‖
and we conclude that
‖ℎ‖ ⩽sup
j
ð⟨dj∕‖dj‖,ℎ⟩ð ⩽ sup
d∈D, ‖d‖=1
ð⟨d,ℎ⟩ð.
The reverse inequality is trivial.
■■
Problem 26.15 Solution: Letx,y ∈span{ej, j∈ N}. By deﬁnition, there exist numbersm,n ∈ N
and ‘coordinates’1,…,m,1,…,n∈ K such that
x=
mÉ
j=1
jej and y=
nÉ
k=1
kek.
Without loss of generality we can assume thatm ⩽n. By deﬁning
m+1∶=0,…,n∶=0
we can write for all, ∈ K
x=
nÉ
j=1
jej and y=
nÉ
k=1
kek and x+y=
nÉ
l=1
(l+l)ek.
This shows thatspan{ej, j∈ N}⊂  is a linear subspace.
■■
Problem 26.16 Solution:
308

Solution Manual. Last update 18th July 2019
(i) Since∑∞
j=1a2
j =∞ there is some numberj1∈ N such that
j1É
j=1
a2
j >1.
Since the remaining tail of the series∑
j>j1
a2
j = ∞we can construct recursively a
strictly increasing sequence(jk)k∈N0 ⊂ N,j0∶=1 , such that
É
j∈Jk
a2
j >1 where Jk∶=(jk,jk+1]∩ N.
(ii) Deﬁne the numbersk as, say,
k∶= 1
k
t∑
j∈Jk
a2
j
.
Then
É
j
b2
j =
É
k
É
j∈Jk
2
ka2
j
=
É
k
2
k
É
j∈Jk
a2
j
=
É
k
∑
j∈Jk
a2
j
k2∑
j∈Jk
a2
j
=
É
k
1
k2 <∞.
Moreover, since
∑
j∈Jk
a2
j
t∑
j∈Jk
a2
j
⩾1,
we get
É
j
ajbj =
É
k
É
j∈Jk
ka2
j
=
É
k
k
É
j∈Jk
a2
j
=
É
k
1
k
∑
j∈Jk
a2
j
t∑
j∈Jk
a2
j
⩾
É
k
1
k =∞.
(iii) Wewanttoshow(notethatwerenamed ∶=aand∶=bfornotationalreasons)that
for any sequence=(j)j we have:
∀∈l2∶ ⟨, ⟩<∞ - ⇒∈l2.
309

R.L. Schilling: Measures, Integrals & Martingales
Assume, to the contrary, that ∉ l2. Then∑
j2
j = ∞and, by part (i), we can ﬁnd
a sequence ofjk with the properties described in (i). Because of part (ii) there is a
sequence =(j)j ∈l2 such that the scalar product⟨, ⟩=∞ . This contradicts our
assumption, i.e. should have been inl2 in the ﬁrst place.
(iv) Since, by Theorem 26.24 every separable Hilbert space has a basis(ej)j∈N ⊂ , we
can identifyℎ∈  with the sequence of ‘coordinates’(⟨ℎ,ej⟩)j∈N and it is clear that
(iii) implies (iv).
■■
Problem 26.17 Solution:
(i) SinceP2=P isobviousbytheuniquenessoftheminimizingelement,thispartfollows
already from Remark 26.15.
(ii) Note that foru,v ∈  we have
∀ℎ∈ ∶ ⟨u,ℎ⟩= ⟨v,ℎ⟩ - ⇒u=v.
Indeed, considerℎ∶=u−v. Then
⟨u,ℎ⟩= ⟨v,ℎ⟩ - ⇒0= ⟨u−v,ℎ⟩= ⟨u−v,u −v⟩= ðu−vð2
so thatu=v.
Linearity ofP: Let, ∈ K andf,g,ℎ ∈ . Then
⟨P(f +g),ℎ⟩= ⟨f +g,Pℎ ⟩
=⟨f,Pℎ ⟩+⟨g,Pℎ ⟩
=⟨Pf,ℎ ⟩+⟨Pg,ℎ ⟩
= ⟨Pf +Pg,ℎ ⟩
and we conclude thatP(f +g)= Pf +Pg .
Continuity ofP: We have for allℎ∈ 
‖Pℎ‖2= ⟨Pℎ,Pℎ ⟩= ⟨P2ℎ,ℎ⟩= ⟨Pℎ,ℎ ⟩ ⩽ ‖Pℎ‖⋅‖ℎ‖
and dividing by‖Pℎ‖ shows thatP is continuous, even a contraction.
Closedness ofP(): Note thatf ∈ P() if, and only if,f = Pℎ for someℎ ∈ .
SinceP2=P we get
f =Pℎ ⇐ ⇒f−Pℎ =0
⇐ ⇒f−P2ℎ=0
⇐ ⇒f−Pf =0
⇐ ⇒f ∈(id− P)−1({0})
310

Solution Manual. Last update 18th July 2019
andsince P iscontinuousand {0}isaclosedset, (id−P)−1({0})isclosedandtheabove
line showsP()=(id− P)−1({0})is closed.
Projection: In view of Corollary 26.14 we have to show thatPℎ −ℎis for anyℎ∈ 
orthogonal tof ∈P(). But
⟨Pℎ −ℎ,f ⟩= ⟨Pℎ,f ⟩−⟨ℎ,f ⟩
= ⟨ℎ,Pf ⟩−⟨ℎ,f ⟩
= ⟨ℎ,f ⟩−⟨ℎ,f ⟩ = 0.
(iii) Since, by assumption,‖Pℎ‖ ⩽ ‖ℎ‖,P is continuous and closedness follows just as in
(ii). It is, therefore, enough to show thatP is an orthogonal projection.
We will show thatN ∶={ℎ∈ ∶Pℎ =0} satisﬁesN ⊥=P().
For this we observe that ifℎ ∈ ,P(Pℎ −ℎ) =P2ℎ−Pℎ = Pℎ −Pℎ = 0so that
Pℎ −ℎ∈N. In particular
ℎ∈N ⊥ - ⇒y=Pℎ −ℎ∈N
- ⇒Pℎ =ℎ+y with ℎ⊥y. (*)
Thus,
‖ℎ‖2+‖y‖2= ‖Pℎ‖2 ⩽ ‖ℎ‖2 - ⇒‖y‖2 - ⇒y=0.
We conclude that
ℎ∈N ⊥ - ⇒Pℎ −ℎ=0 - ⇒Pℎ =ℎ - ⇒ℎ∈P()
and we have shown thatN ⊥⊂P ().
Toseetheconversedirectionwepick ℎ∈P()andﬁndPℎ =ℎ. Since=N ⊕N ⊥
we haveℎ=x+x⊥ withx∈N andx⊥∈N ⊥. Thus,
Pℎ =Px +P(x⊥)= P(x⊥)
(∗)
= x⊥,
thus
ℎ=Pℎ =x⊥ - ⇒P()⊂N ⊥.
We have seen thatP()= N ⊥⊥N = kernel(P). This means that
⟨Pℎ −ℎ,Pℎ ⟩=0
and we conclude thatP is an orthogonal projection.
■■
Problem 26.18 Solution:
311

R.L. Schilling: Measures, Integrals & Martingales
(i) Pickuj ∈Yj anduk∈Yk,j ≠k. Then
˚Am
ujukd ⩽
v
˚Am
u2
jd
v
˚Am
u2
kd
=
⎧
⎪
⎪
⎨
⎪
⎪⎩
0⋅0 if m∉{j,k}
√⋯⋅ 0 if m=j,m ≠k
0⋅√⋯ if m ≠j,m =k
=0.
(ii) Letu∈L2() and setwj ∶=w1A1∪⋯∪Aj. Since(A1∪⋯∪Aj)c =Ac
1∩⋯∩Ac
j ↓ç
we get by dominated convergence
‖u−wj‖2
2= ˚(A1∪⋯∪Aj)c
u2d = ˚Ac
1∩⋯∩Ac
j
u2d , , , , , , , , , , , , , , , , , , , , →
j→∞
0.
(iii) P is given byPj(u)= u1Aj. Clearly,Pj ∶L2() →Yj is linear andP2=P, i.e. it is a
projection. Orthogonality follows from
⟨u−u1Aj,u 1Aj⟩= ˚ u1Ac
j
⋅u1Ajd = ˚ u1çd =0.
■■
Problem 26.19 Solution:
(i) See Lemma 27.1 in Chapter 27.
(ii) Setun∶=EAnu. Then
un=
nÉ
j=0
j⋅ 1Aj,  j ∶= 1
(Aj) ˚Aj
ud, 0 ⩽j ⩽n.
whereA0∶=(A1∪⋯∪An)c and1∕∞∶=0 . Thisfollowssimplyfromtheconsideration
thatun, as an element ofL2(An), must be of the form∑n
j=0j⋅ 1Aj while thej’s are
calculated as
⟨EAju, 1Aj⟩= ⟨u,EAj 1Aj⟩= ⟨u, 1Aj⟩= ˚Aj
ud
(resp.=0 if(A0)=∞ ) so that, because of disjointness,
j(Aj)=
( nÉ
k=0
k⋅ 1Ak, 1Aj
)
= ⟨EAju, 1Aj⟩= ˚Aj
ud.
Clearly this is a linear map andun ∈ L2(An). Orthogonality follows because all the
A0,…,An are disjoint so that
⟨u−un,un⟩=
(
u−
nÉ
j=0
j1Aj,
nÉ
k=0
k1Ak
)
312

Solution Manual. Last update 18th July 2019
=
nÉ
j=0 ˚Aj
(u−j)jd
=
nÉ
j=0
0
j ˚Aj
ud −(Aj)2
j
1
=
nÉ
j=0
0 = 0.
(iii) We have
L2(An)⊥=
<
u−
nÉ
j=0
j1Aj =
nÉ
j=0
(u−j)1Aj ∶u∈L2()
=
(iv) In view of Remark 23.2 we have to show that
˚Aj
EAnud = ˚Aj
EAn+1ud, ∀A0,A1,…,An.
Thus
˚Aj
EAnud = ⟨EAnu, 1Aj⟩= ⟨u,EAn1Aj⟩= ⟨u, 1Aj⟩= ˚Aj
ud
for all0 ⩽j ⩽n. The same argument shows also that
˚Aj
EAn+1ud = ˚Aj
ud ∀j=1,2,…,n.
Sincethe A1,A2,…arepairwisedisjointand A0=(A1∪⋯∪An)c,wehave An+1⊂A 0
andAj∩A0=ç ,1 ⩽j ⩽n; ifj=0 we get
˚A0
EAn+1ud
= ˚A0
0
1An+1
∫An+1
ud
(An+1) + 1A0⧵An+1
∫A0⧵An+1
ud
(A0 ⧵An+1)
1
d
=(A0∩An+1)
∫An+1
ud
(An+1) +(A0 ⧵An+1)
∫A0⧵An+1
ud
(A0 ⧵An+1)
=(An+1)
∫An+1
ud
(An+1) +(A0 ⧵An+1)
∫A0⧵An+1
ud
(A0 ⧵An+1)
= ˚An+1
ud + ˚A0⧵An+1
ud
= ˚A0
ud.
The claim follows.
Remark. It is, actually, better to show that forun ∶= EAnu the sequence(u2
n)n is a
sub-Martingale. (The advantage of this is that we do not have to assume thatu ∈ L1
and thatu∈L2 is indeed enough....). O.k.:
313

R.L. Schilling: Measures, Integrals & Martingales
We have
An
0∶=(A1⊍⋯⊍An)c =Ac
1∩⋯∩Ac
n
An+1
0 ∶=(A1⊍⋯⊍An⊍An+1)c =An
0∩Ac
n+1
and
EAnu=
nÉ
j=1
1Aj ˚Aj
u d
(Aj)+ 1An
0 ˚An
0
u d
(An
0)
EAn+1u=
n+1É
j=1
1Aj ˚Aj
u d
(Aj)+ 1An+1
0 ˚An+1
0
u d
(An+1
0 )
with the convention that1∕∞=0 . Since theAj’s are mutually disjoint,
 EAnu2
=
nÉ
j=1
1Aj
4
˚Aj
u d
(Aj)
52
+ 1An
0
4
˚An
0
u d
(An
0)
52
 EAn+1u2
=
n+1É
j=1
1Aj
4
˚Aj
u d
(Aj)
52
+ 1An+1
0
4
˚An+1
0
u d
(An+1
0 )
52
.
We have to show that EAnu2
=u2
n ⩽u2
n+1=  EAn+1u2
. If(An+1
0 )=∞ this follows
trivially since in this case
 EAnu2
=
nÉ
j=1
1Aj
4
˚Aj
u d
(Aj)
52
 EAn+1u2
=
n+1É
j=1
1Aj
4
˚Aj
u d
(Aj)
52
.
If(An+1
0 )<∞we get
 EAnu2
− EAn+1u2
= 1An
0
4
˚An
0
u d
(An
0)
52
− 1An+1
4
˚An+1
u d
(An+1)
52
+ 1An+1
0
4
˚An+1
0
u d
(An+1
0 )
52
= 1An+1
H4
˚An+1
u d
(An
0)
52
−
4
˚An+1
u d
(An+1)
52I
+ 1An+1
0
H4
˚An+1
0
u d
(An
0)
52
−
4
˚An+1
0
u d
(An+1
0 )
52I
and each of the expressions in the brackets is negative since
An
0⊃A n+1 - ⇒(An
0) ⩾(An+1) - ⇒ 1
(An
0) ⩽ 1
(An+1)
and
An
0⊃A n+1
0 - ⇒(An
0) ⩾(An+1
0 ) - ⇒ 1
(An
0) ⩽ 1
(An+1
0 )
.
314

Solution Manual. Last update 18th July 2019
(v) Setun∶=EAnu. Since(un)n isamartingale, u2
n isasubmartingale. Infact, (u2
n)n iseven
uniformly integrable. For this we remark that
un=
nÉ
j=1
1Aj ˚Aj
u(x)(dx)
(Aj) + 1An
0 ˚An
0
u(x)frac(dx)(An
0)
(1∕∞∶=0 ) and that the function
v∶=
∞É
j=1
1Aj ˚Aj
u(x)(dx)
(Aj)
is inL2(A∞). Only integrability is a problem: since theAj’s are mutually disjoint, the
square of the series deﬁningv factorizes, i.e.
˚ v2(y)(dy)= ˚
0 ∞É
j=1
1Aj(y) ˚Aj
u(x)(dx)
(Aj)
12
(dy)
=
∞É
j=1 ˚ 1Aj(y)(dy)
0
˚Aj
u(x)(dx)
(Aj)
12
⩽
∞É
j=1 ˚ 1Aj(y)(dy) ˚Aj
u2(x)(dx)
(Aj)
=
∞É
j=1 ˚Aj
u2(x)(dx)
= ˚ u2(x)(dx)
where we use Beppo Levi’s theorem (twice) and Jensen’s inequality. In fact,
v=EA∞u.
Sinceun(x)= v(x)for allx∈A1∪⋯∪An, and sinceAn
0=(A1∪⋯∪An)c ∈An we
ﬁnd by the submartingale property
˚{u2
n>(2v)2}
u2
nd ⩽ ˚An
0
u2
nd
⩽ ˚An
0
u2d
, , , , , , , , , , , , , , , , , , , , →
n→∞
0
by dominated convergence sinceAn
0 →ç andu2∈L1().
Using the convergence theorem for UI (sub)martingales, Theorem 24.6, we conclude
thatu2
j convergespointwiseandin L1-sensetosome u2
∞∈L1(A∞)andthat(u2
j)j∈N∪{∞}
is again a submartingale. By Riesz’s convergence theorem 13.10 we conclude that
uj →u∞ inL2-norm.
Remark: We can also identifyu∞ withv: sinceEAjv = uj = EAju∞ it follows that
fork=1,2,…,j and allj
0= ⟨EAjv−EAju∞, 1Ak⟩= ⟨v−u∞,EAj 1Ak⟩= ⟨v−u∞, 1Ak⟩
315

R.L. Schilling: Measures, Integrals & Martingales
i.e.v=u∞ on all sets of the∩-stable generator ofA∞ which can easily be extended to
contain an exhausting sequenceA1⊍⋯⊍An of sets of ﬁnite-measure.
(vi) The above considerations show that the functions
D∶=
T
01An
0
+
nÉ
j=1
j1Aj ∶n∈ N,j ∈ R
U
(if(An
0)=∞ , then0=0 ) are dense inL2(A∞). It is easy to see that
E∶=
T
q01An
0
+
nÉ
j=1
qj1Aj ∶n∈ N,j ∈ Q
U
(if(An
0)=∞ , thenq0=0 ) is countable and dense inD so that the claim follows.
■■
316

27 Conditional expectations.
Solutions to Problems 27.127.19
Problem 27.1 Solution: In Theorem 27.4(vii) we have seen that
Eℋ EGu= Eℋu.
Since, by 27.4(i) and 27.1Eℋu∈L2(ℋ)⊂L 2(G)we have, because of 27.4
EG Eℋu= Eℋu.
■■
Problem 27.2 Solution: Note that by the Markov inequality{u> 1} ⩽ ∫ u2d <∞, i.e.u1{u>1}
is an integrable function (use Cauchy-Schwarz).
We have
1{u> 1}= ˚{u>1}
1d
(*)
< ˚{u>1}
ud
assumption
⩽ {u> 1}.
In the step marked (*) we really (!) need that{u> 1}>0— otherwise we could not get a strict
inequality. Thus,{u >1} < {u >1} which is a contradiciton. Therefore,{u >1} = 0and
we haveu ⩽1 a.e.
Ifyouareunhappywithstrictinequalities,youcanextendtheargumentasfollows: Byassumption
{u> 1}>0. Since{u> 1}= ⋃
n⩾1{u ⩾1+1∕n},thereissome N suchthat {u ⩾1+1∕n}>0
for alln ⩾N — use a continuity of measure argument. Now we get for alln ⩾N
˚
u⩾1+1
n
1d =u ⩾1+ 1
n

<  1+ 1
n
u ⩾1+ 1
n

= ˚
u⩾1+1
n

 1+ 1
n
d
⩽ ˚
u⩾1+1
n
ud.
Observe that
˚{u>1}
1d =
∞É
n=N+1 ˚
1+1∕n⩽u<1+1∕(n−1)
1d+ ˚
u⩾1+ 1
N
1d
317

R.L. Schilling: Measures, Integrals & Martingales
⩽
∞É
n=N+1 ˚
1+1∕n⩽u<1+1∕(n−1)
ud + ˚
u⩾1+ 1
N
1d
<
∞É
n=N+1 ˚
1+1∕n⩽u<1+1∕(n−1)
ud + ˚
u⩾1+ 1
N
ud
= ˚{u>1}
ud.
With our assumption we thus get the contradiction{u> 1}<{u> 1}.
Alternative: From ∫{u>1}ud ⩽(u> 1)we get
˚{u>1}
(u−1) d ⩽0.
Observe that(u−1)1{u>1} ⩾0 implies
˚{u>1}
(u−1) d ⩾0.
Therefore, ∫{u>1}(u−1) d =0 and we see that(u−1)1{u>1}=0 a.e., hence1{u>1}=0 a.e.
■■
Problem 27.3 Solution: Note that, sinceEG is (currently...) only deﬁned forL2-functions the prob-
lem implicitly requires thatf ∈ L2(A,). (A look at the next section reveals that this is not
really necessary...). Below we will write⟨∙,∙⟩L2() resp. ⟨∙,∙⟩L2() to indicate which scalar product
is meant.
We begin with a general consideration: Letu,w be functions such thatu2,v2 ∈ L2(). Then we
haveðu⋅wð ⩽ 1
2(u2+w2)∈ L2()and, using again the elementary inequality
ðxyð ⩽ x2
2 + y2
2
forx = ðuð∕
t
EG
(u2) and y = ðwð∕
t
EG
(w2) we conclude that onGn ∶= {EG
(u2) > 1
n}∩
{EG
(w2)> 1
n}
ðuð⋅ðwðt
EG
(w2)
t
EG
(w2)
1Gn ⩽
L
u2
2 EG
(u2)+ w2
2 EG
(w2)
M
1Gn.
Taking conditional expectations on both sides yields, sinceGn∈G:
EG

 ðuð⋅ðwð
t
EG
(w2)
t
EG
(w2)
1Gn ⩽ 1Gn.
Multiplying through with the denominator of the lhS and lettingn →∞gives
óóóEG
(uw)óóó1G∗ ⩽ EG

 ðuwð1G∗ ⩽
t
EG
(u2)
t
EG
(w2)
on the setG∗∶=Gu∩Gw∶={ EG
u2>0}∩{ EG
w2>0}.
318

Solution Manual. Last update 18th July 2019
(i) SetG∗∶={ EG
f >0} andGn∶={ EG
f >1
n}. Clearly, using the Markov inequality,
(Gn) ⩽n2
˚ (EG
f)2d ⩽n ˚ f2d< ∞
so that by monotone convergence we ﬁnd for allG∈G ∩G∗
(G)= ⟨f, 1G⟩L2()
=sup
n
⟨f, 1G∩Gn⟩L2()
=sup
n
⟨f, EG
 1G∩Gn⟩L2()
=sup
n
⟨EG
f, 1G∩Gn⟩L2()
= ⟨EG
f, 1G⟩L2()
which means thatðG∩G∗ = EGf⋅ðG∩G∗.
(ii) We deﬁne forboundedu∈L2()
Pu ∶=
EG
(fu)
EG
f 1G∗.
Let us show thatP ∈ L2(). Set G√
fu ∶= {EG

 f ⋅u2 > 0}. Then, forbounded
u∈L2()
ôôôô
EG
(fu)
EG
f 1G∗∩G√
fu∩G√
f
ôôôô
2
L2()
= ˚G∗∩G√
fu∩G√
f
EG
(fu)2
EG
f2 d
= ˚G∗∩G√
fu∩G√
f
EG
(fu)2
EG
f2 fd
= ˚G∗∩G√
fu∩G√
f
EG
(fu)2
EG
f2 EG
fd
= ˚G∗∩G√
fu∩G√
f
EG
(fu)2
EG
f d
= ˚G∗∩G√
fu∩G√
f
EG

√
f(
√
fu)2
EG
f d
⩽ ˚G∗∩G√
fu∩G√
f
EG
f⋅ EG

fu2
EG
f d
= ˚G∗∩G√
fu∩G√
f
EG

fu2d
=sup
n ˚ 1Gn∩G√
fu∩G√
f
EG

fu2d
319

R.L. Schilling: Measures, Integrals & Martingales
=sup
n ˚ EG
 1Gn∩G√
fu∩G√
f
fu2d
=sup
n ˚ 1Gn∩G√
fu∩G√
f
fu2d
= ˚ 1G∗∩G√
fu∩G√
f
fu2d
⩽ ˚ fu2d = ôôô
√
fuôôô
2
L2()
= ‖u‖2
L2()<∞.
Still for boundedu∈L2(),
˚Gn∩{f<n}∩{EG(fu2)=0}
EG
(fu)d
= ˚Gn∩{EG(
√
fu)=0}
fud
⩽
v
˚Gn∩{f<n}
fd
v
˚Gn∩{EG(fu2)=0}
fu2d
=
v
˚Gn∩{f<n}
fd
v
˚Gn∩{EG(fu2)=0}
EG
fu2d
=0
and, using monotone convergence, we have
‖Pu‖2
L2() ⩽ ‖u‖2
L2()
forallbounded u∈L2(),hence–throughextensionbycontinuity–forall u∈L2().
(iii) Since
u−Pu,Pu 
L2()
= fu−fPu,Pu 
L2()
=
(
fu−f
EG
(fu)
EG
f 1G∗,
EG
(fu)
EG
f 1G∗
)
L2()
=
(
EG


fu−f
EG
(fu)
EG
f 1G∗

,
EG
(fu)
EG
f 1G∗
)
L2()
=
(
EG
(fu)− EG


f
EG
(fu)
EG
f 1G∗

,
EG
(fu)
EG
f 1G∗
)
L2()
=
(
EG
(fu)− EG
(f)
EG
(fu)
EG
f 1G∗,
EG
(fu)
EG
f 1G∗
)
L2()
=
(
EG
(fu)− EG
(fu)1G∗,
EG
(fu)
EG
f 1G∗
)
L2()
=0
which shows thatP is the (uniquely determined) orthogonal projection ontoL2(,G),
i.e.P = EG
 .
320

Solution Manual. Last update 18th July 2019
(Note that we have, implicitly, extendedEG
 ontoL1....)
(iv) The condition thatf 1G∗ isG-measurable will do. Indeed, sinceG∗∈G:
EG
u=
EG
(fu)
EG
f 1G∗ =
EG
((f 1G∗)u)
EG
(f 1G∗) =
(f 1G∗)EG
(u)
(f 1G∗) = EG
u.
In fact, iff ∈L4(,A)this is also necessary:
EG
f = EG
f
implies, because of (i), that
EG
f =
EG
(f2)
EG
f 1{EG
f>0} ⇐ ⇒ EG
f2
= EG
(f2)1{EG
f>0}
⇐ ⇒ EG
f2
= EG
(f2).
Thus,
EG

 f− EG
f2
=0,
which means that on the setG∗= ⋃
nGn with(Gn)<∞, see above,
0= ˚Gn
EG
(f− EG
f)2d = ˚Gn
(f− EG
f)2d
i.e.f = EG
f onG∗={ EG
f >0}
■■
Problem 27.4 Solution: SinceG ={G1,…,Gn}suchthatthe Gj’sformamutuallydisjointpartition
of the whole spaceX, we have
L2(G)=
T nÉ
j=1
j1Gj ∶j ∈ R
U
.
Itis,therefore,enoughtodeterminethevaluesofthe j. Usingthesymmetryandidempotencyof
the conditional expectation we get fork∈{1,2,…,n}
⟨EGu, 1Gk⟩= ⟨u, EG 1Gk⟩= ⟨u, 1Gk⟩= ˚Gk
ud.
On the other hand, using thatEGu∈L2(G)we ﬁnd
⟨EGu, 1Gk⟩=
( nÉ
j=1
j1Gj, 1Gk
)
=
nÉ
j=1
j⟨1Gj, 1Gk⟩=k(Gk)
and we conclude that
k= 1
(Gk) ˚Gk
ud = ˚Gk
u(x)(dx)
(Gk).
■■
321

R.L. Schilling: Measures, Integrals & Martingales
Problem 27.5 Solution: We follow the hint. Letu∈Lp()and deﬁneun=[(−n)∨ u∧n]1{ðuð⩾1∕n}.
Clearly,un is bounded, and by the Markov inequality (11.4)
{ðuð ⩾1∕n}= {ðuðp ⩾1∕np} ⩽np
˚ ðuðpd< ∞.
Therefore,un∈Lr()for allr ⩾1:
˚ ðunðrd = ˚{ðunð⩾1∕n}
(ðuð∧n)r ⩽nr{ðunð ⩾1∕n} ⩽nr+p
˚ ðuðpd< ∞.
Sinceun →ua.e., dominated convergence (use the majorantðuðp) shows thatun →uinLp. Thus,
weseeasintheremarkbeforeTheorem27.5that (Tun)n∈N isaCauchysequencein Lp(),i.e.the
limitLp-limnTun exists. If(wn)n isafurtherapproximatingsequencesuchthat wn →uinLp(),
we get
‖Tun−Twn‖p= ‖T(un−wn)‖p ⩽c‖un−wn‖p ⩽c‖un−u‖p+c‖u−wn‖p , , , , , , , , , , , , , , , , , , , , →
n→∞
0
whichshowsthat limnTun=lim nTwn,i.e. Tu ∶=lim nTun (asan Lp-limit)iswell-deﬁnedsince
it is independent of the approximating sequence. Linearity is clear from the linearity of the limit.
Assume now that0 ⩽un ↑u whereun ∈Lp()∩ L2(). By the ﬁrst part,Tu =lim nTun inLp,
so there is a subsequence such thatTu =lim kTunk a.e. Because of monotonicity we have
Tunk ⩽Tun ∀n ⩾n(k) - ⇒0 ⩽ Tu −Tun ⩽ Tu −Tunk.
So,
0 ⩽limsup
n→∞
(Tu −Tun) ⩽ Tu −Tunk , , , , , , , , , , , , , , , , , , , , →
k→∞
0,
which shows thatlimn(Tu −Tun)=0 .
■■
Problem 27.6 Solution: LetGu ∶= {EGðuðp > 0}, Gw ∶= {EGðwðq > 0} andG ∶= Gu∩Gw.
Following the hint we get
ðuð
EG(ðuðp)1∕p
ðwð
EG(ðwðq)1∕q 1G ⩽ ðuðp
p EG(ðuðp) 1G+ ðuðq
q EG(ðwðq) 1G
Since 1G is bounded andG-measurable, we can applyEG on both sides of the above inequality
and get
EG(ðuððwð)
EG(ðuðp)1∕pEG(ðwðq)1∕q 1G ⩽ EG(ðuðp)
p EG(ðuðp) 1G+ EG(ðuðq)
q EG(ðwðq) 1G= 1G
or
EG(ðuððwð)1G ⩽ EG(ðuðp)1∕pEG(ðwðq)1∕q
1G
⩽ EG(ðuðp)1∕pEG(ðwðq)1∕q
.
322

Solution Manual. Last update 18th July 2019
Denote byGn an exhaustion ofX such thatGn∈G,Gn ↑X and(Gn)<∞. Then
˚Gc
u
ðuðpd =sup
n ˚Gc
u∩Gn
ðuðpd
=sup
n
⟨1Gc
u∩Gn,ðuðp⟩
=sup
n
⟨EG 1Gc
u∩Gn,ðuðp⟩
=sup
n
⟨1Gc
u∩Gn, EG(ðuðp)⟩
=0
which means that1Guu=ualmost everywhere. Thus,
EG(ðuððwð)1G= EG(ðuððwð1G)= EG(ðuð1Guðwð1Gw)= EG(ðuððwð)
and the inequality follows since
óóóEG(uw)óóó ⩽ EG(ðuwð).
■■
Problem 27.7 Solution: In this problem it is helpful to keep the distinction betweenEG deﬁned on
L2(A)and the extensionEG deﬁned onLG(A).
SinceðA is-ﬁnitewecanﬁndanexhaustingsequenceofsets An ↑X with(An)<∞. Setting
foru,w ∈LG(A)withuEGw∈L1(A)un∶=  (−n)∨u∧n⋅ 1An andwn∶=  (−n)∨w∧n⋅ 1An
we have found approximating sequences such thatun,wn ∈ L1(A)∩ L∞(A) and, in particular,
∈L2(A).
(iii): Foru,w ⩾0weﬁndbymonotoneconvergence,usingthepropertieslistedinTheorem27.4:
⟨EGu,w⟩=lim
n
⟨EGun,w⟩
=lim
n
lim
m
⟨EGun,wm⟩
=lim
n
lim
m
⟨un, EGwm⟩
=lim
n
⟨un,EGw⟩
= ⟨u,EGw⟩.
In the general case we write
⟨EGu,w⟩= ⟨EGu+,w+⟩−⟨EGu−,w+⟩−⟨EGu+,w−⟩+⟨EGu−,w−⟩
and consider each term separately.
The equality⟨EGu,w⟩= ⟨EGu,EGw⟩ follows similarly.
(iv): we have
u=w - ⇒uj =wj ∀j - ⇒ EGuj = EGwj ∀j
323

R.L. Schilling: Measures, Integrals & Martingales
and we get
EGu=lim
j
EGuj =lim
j
EGwj =w.
(ix): we have
0 ⩽u ⩽1 - ⇒0 ⩽un ⩽1 ∀ n
- ⇒0 ⩽ EGun ⩽1 ∀ n
- ⇒0 ⩽EGu=lim
n
EGun ⩽1.
(x):
u ⩽w - ⇒0 ⩽w−u - ⇒0 ⩽EG(u−w)= EGu−EGw.
(xi):
±u ⩽ ðuð - ⇒±EGu ⩽EGðuð - ⇒óóóEGuóóó ⩽EGðuð.
■■
Problem 27.8 Solution: (Mind the typo in the hint:EG = EG should readEG =EG.) Assume ﬁrst
thatðG is-ﬁniteanddenoteby Gk∈G,Gk ↑X and(Gk)<∞anexhaustingsequence. Then
1Gk ∈L2(G), 1Gk ↑1 and
EG1=sup
k
EG 1Gk =sup
k
1Gk =1.
Conversely,letEG1=1 . BecauseofLemma27.7thereisasequence (uk)k⊂L 2(A)withuk ↑1.
By the very deﬁnition ofEG we have
EG1=sup
k
EGuk=1,
i.e. there is a sequencegk ∶= EGuk ∈ L2(G) such thatgk ↑ 1. SetGk ∶= {gk > 1−1∕ k} and
observe thatGk ↑X as well as
(Gk) ⩽ 1
(1− 1
k)2 ˚ g2
kd
= 1
(1− 1
k)2
‖EGuk‖2
L2
⩽ 1
(1− 1
k)2
‖uk‖2
L2
<∞.
This shows thatðG is-ﬁnite.
324

Solution Manual. Last update 18th July 2019
IfG is not-ﬁnite, e.g. ifG ={ç,G,G c,X}where(G)<∞and(Gc)=∞ we ﬁnd that
L2(G)={ c1G∶c∈ R}
which means thatEG1= 1G since for everyA⊂G c,A∈A and(A)<∞we ﬁnd
EG 1A⊍G=EG(1A+ 1G)= EG 1A+EG 1G=EG 1A+ 1G
Since this must be an element ofL2(G), we have necessarilyEG 1A=c1G or
⟨c1G, 1G⟩= ⟨EG 1A, 1G⟩= ⟨1A,EG 1G⟩= ⟨1A, 1G⟩=(A∩G)=0 ,
hencec=0 orEG 1A=0 .
This shows that
EG1= 1G ⩽1
is best possible.
■■
Problem 27.9 Solution: Forthisproblemitishelpfultodistinguishbetween EG (deﬁnedonL2)and
the extensionEG.
Without loss of generality we may assume thatg ⩾0—otherwise we would consider positive and
negative parts separately. Sinceg∈Lp(G)we have that
{g >1∕j} ⩽jp
˚ gpd< ∞
which means that the sequencegj ∶= (j∧g)1{g>1∕j} ∈ L2(G). Obviously,gj ↑ g pointwise as
well as inLp-sense. Using the results from Theorem 27.4 we get
EGgj =gj - ⇒EG =sup
j
EGgj =sup
j
gj =g.
■■
Problem 27.10 Solution: For this problem it is helpful to distinguish betweenEG (deﬁned onL2)
and the extensionEG.
Foru ∈ Lp(A) we getEℋEGu = Eℋu because of Theorem 27.11(vi) while the other equality
EGEℋu=Eℋu follows from Problem 27.9.
Ifu ∈ M+(A) (mind the misprint in the problem!) we get a sequenceuj ↑ u of functionsuj ∈
L2
+(A). FromTheorem27.4weknowthat EGuj ∈L2(G)increasesand,bydeﬁnition,itincreases
towardsEGu. Thus,
Eℋ EGuj = Eℋuj ↑Eℋu
325

R.L. Schilling: Measures, Integrals & Martingales
while
Eℋ EGuj ↑Eℋ sup
j
EGuj
=EℋEGu.
The other equality is similar.
■■
Problem 27.11 Solution: We know that
Lp(An)=
T nÉ
j=1
cj1[j−1,j)∶cj ∈ R
U
sincec01[n,∞)∈Lp if, and only if,c0=0 . Thus,EAnuis of the form
EAnu(x)=
nÉ
j=1
cj1[j−1,j)(x)
and integrating over[k−1,k)yields
˚[k−1,k)
EAnu(x)dx=ck.
Since
˚[k−1,k)
EAnu(x)dx= ⟨EAnu, 1[k−1,k)⟩
= ⟨u,EAn1[k−1,k)⟩
= ⟨u, 1[k−1,k)⟩
= ˚[k−1,k)
u(x)dx
we get
EAnu(x)=
nÉ
j=1 ˚[j−1,j)
u(t)dt1[j−1,j)(x).
■■
Problem 27.12 Solution: For this problem it is helpful to distinguish betweenEG (deﬁned onL2)
and the extensionEG.
If(X)=∞ andif G ={ç,X},then L1(G)={0} whichmeansthat EGu=0 foranyu∈L1(A).
Thus for integrable functionsu> 0 andðG not-ﬁnite we can only have ‘⩽’.
IfðG is-ﬁnite and ifGj ↑X,Gj ∈G,(Gj)<∞ is an exhausting sequence, we ﬁnd for any
u∈L1
+(A)
˚ EGud =sup
j ˚Gj
EGud
=sup
j
⟨EGu, 1Gj⟩
326

Solution Manual. Last update 18th July 2019
=sup
j
⟨u,EG 1Gj⟩
=sup
j
⟨u, 1Gj⟩
= ⟨u,1⟩
= ˚ ud.
IfðG is not-ﬁnite and ifu ⩾0, we perform a similar calculation with an exhausting sequence
Aj ∈ A, Aj ↑ X, (Aj) < ∞ (it is implicit thatðA is -ﬁnite as otherwise the conditional
expectation would not be deﬁned!):
˚ EGud =sup
j ˚Aj
EGud
=sup
j
⟨EGu, 1Aj⟩
=sup
j
⟨u,EG 1Aj⟩
⩽ ⟨u,1⟩
= ˚ ud.
■■
Problem 27.13 Solution:
Proof of Corollary 27.14: Since
liminf
j→∞
uj =sup
k
inf
j⩾k
uj
we get
EG inf
j⩾k
uj
 ⩽ EGum ∀m ⩾k
thus
EG inf
j⩾k
uj
 ⩽ inf
m⩾k
EGum ⩽sup
k
inf
m⩾k
EGum=liminf
m→∞
EGum.
Sinceontheotherhandthesequence infj⩾kuj increases,as k →∞,towards supkinfj⩾kuj wecan
use the conditional Beppo Levi theorem 27.13 on the left-hand side and ﬁnd
EG liminf
j→∞
uj
= EG sup
k
inf
j⩾k
uj
=sup
k
EG inf
j⩾k
uj
 ⩽liminf
m→∞
EGum.
The Corollary is proved.
Proof of Corollary 27.15: Sinceðujð ⩽ w we conclude thatðuð = limjðujð ⩽ w and that2w−
ðu−ujð ⩾0. Applying the conditional Fatou lemma 27.14 we ﬁnd
EG(2w)= EG liminf
j
2w−ðu−ujð
327

R.L. Schilling: Measures, Integrals & Martingales
⩽liminf
j
EG 2w−ðu−ujð
= EG(2w)−limsup
j
EG(ðu−ujð)
which shows that
limsup
j
EG(ðu−ujð)=0 - ⇒lim
j
EG(ðu−ujð)=0 .
Since, however,
óóóEGuj− EGuóóó= óóóEG(uj−u)óóó ⩽ EGðuj−uð , , , , , , , , , , , , , , , , , , , , →
j→∞
0
the claim follows.
■■
Problem 27.14 Solution: (i) - ⇒(ii): Let A ∈ A∞ be such that(A) < ∞. Then, by Hölder’s
inequality with1∕p+1∕q=1 ,
óóóó ˚A
ujd− ˚A
udóóóó
⩽ ˚A
ðuj−uðd ⩽ ‖uj−u‖p(A)1∕q , , , , , , , , , , , , , , , , , , , , →
j→∞
0.
Thus, ifu∞ ∶= EA∞u, we ﬁnd by the martingale property for allk > jandA ∈ Aj such that
(A)<∞
˚A
ujd = ˚A
ukd = lim
k→∞ ˚A
ukd = ˚A
ud = ˚A
u∞d,
and since we are in a-ﬁnite setting, we can apply Theorem 27.12(i) and ﬁnd thatuj = EAju∞.
(ii) - ⇒(iii): Assume ﬁrst thatu∞∈L1∩Lp. Thenuj = EAju∞∈L1∩Lp and Theorem 27.19(i)
shows thatuj , , , , , , , , , , , , , , , , , , , , →
j→∞
u∞ both inL1 and a.e. In particular, we get
⟨u∞−uj,⟩ ⩽ ‖u∞−uj‖1‖‖∞ →0 ∀ ∈L∞.
In the general case whereu∞ ∈ Lp(A∞) we ﬁnd for every >0 an elementu
∞ ∈ L1(A∞)∩
Lp(A∞)such that
‖u∞−u
∞‖p ⩽
(indeed, since we are working in a-ﬁnite ﬁltered measure space, there is an exhaustionAk ↑X
such thatAk ∈ A∞ and for large enoughk = k the functionu
∞ ∶= u∞1Ak will to the job).
Similarly, we can approximate any ﬁxed∈Lq by ∈Lq∩L1 such that‖−‖q ⩽.
Now we setu
j ∶= EAju
∞ and observe that
‖uj−u
j‖p= ‖EAju∞− EAju
∞‖p ⩽ ‖u∞−u
∞‖p ⩽.
Thus, for any∈Lq,
⟨uj−u∞,⟩
328

Solution Manual. Last update 18th July 2019
= ⟨uj−u
j−u∞+u
∞,⟩+⟨u
j−u
∞,⟩
= ⟨uj−u
j−u∞+u
∞,⟩+⟨u
j−u
∞, −⟩+⟨u
j−u
∞,⟩
⩽  ‖uj−u
j‖p+‖u∞−u
∞‖p
‖‖q
+‖u
j−u
∞‖p‖−‖q+⟨u
j−u
∞,⟩
⩽2‖‖q+ ‖u
j−u
∞‖p
«›››ﬂ›››‹
⩽2‖u
∞‖p⩽2(+‖u∞‖p)
+⟨u
j−u
∞,⟩
«›››››ﬂ›››››‹
, , , , , , , , , , , , , , , , , , , , →
j→∞
0
⩽ const.
for suﬃciently largej’s, and the claim follows.
(iii) - ⇒(ii): Letun(j) be a subsequence converging weakly to someu∈Lp, i.e.,
lim
k
⟨un(k)−u,⟩=0 ∀ ∈Lq.
Then, in particular,
lim
k
⟨un(k)−u, EAn⟩=0 ∀ ∈Lq, n∈ N
or
lim
k
⟨EAnun(k)− EAnu,⟩=0 ∀ ∈Lq, n∈ N.
Sinceuj is a martingale, we ﬁnd thatEAnun(k) ifn<n (k), i.e.,
⟨un− EAnu,⟩=0 ∀ ∈Lq, n∈ N.
and we conclude thatun = EAnu. Because of the tower property we can always replaceu by
u∞∶= EA∞u:
un= EAnu= EAnEA∞u= EAnu∞
and the claim follows.
(ii) - ⇒(i): Weshowthatwecantake u=u∞. First, ifu∞∈L1∩L∞ weﬁndbytheclosabilityof
martingales, Theorem 27.19(i), that
lim
j
‖uj−u‖1=0.
Moreover, using thatða−bðr ⩽(ðað+ðbð)r ⩽2r(ðaðr+ðbðr), we ﬁnd
‖uj−u‖p
p= ˚ ðuj−uðpd
= ˚ ðuj−uð⋅ðuj−uðp−1d
⩽2p−1(‖uj‖p−1
∞ +‖u‖p−1
∞ ) ˚ ðuj−uðd
⩽2p‖u‖p−1
∞ ⋅‖uj−u‖1
329

R.L. Schilling: Measures, Integrals & Martingales
, , , , , , , , , , , , , , , , , , , , →
j→∞
0
where we use that
‖uj‖∞= ‖EA
j u‖∞ ⩽ EA
j
 ‖u‖∞
 ⩽ ‖u‖∞.
Now for the general case whereu∞ ∈ Lp. Since we are in a-ﬁnite setting, we can setu ∶=
(u⋅ 1Aj)∧ j,j=j()suﬃcientlylargeand Aj →X anexhaustingsequenceofsetsfrom A∞, and
can guarantee that
‖u−u‖p ⩽.
At the same time, we get foru
j ∶= EAju ∈L1∩L∞ that
‖uj−u
j‖p= ‖EAju− EAju‖p ⩽ ‖u−u‖p ⩽.
Thus, by the consideration for the special case whereu ∈L1∩L∞,
‖uj−u‖p ⩽ ‖uj−u
j‖p+‖u
j−u‖p+‖u−u‖p
⩽+‖u
j−u‖p+
, , , , , , , , , , , , , , , , , , , , →
j→∞
2 , , , , , , , , , , , , , , , , , →
→0
0.
■■
Problem 27.15 Solution: Obviously,
mk=mk−1+(uk−EAk−1uk).
Sincem1=u1∈L1A1,thisshows,byinduction,that mk∈L1(Ak). ApplyingEAk−1 tobothsides
of the displayed equality yields
EAk−1mk=EAk−1mk−1+EAk−1(uk−EAk−1uk)
=mk−1+EAk−1uk−EAk−1uk
=mk−1
which shows thatmk is indeed a martingale.
■■
Problem 27.16 Solution: Problem27.15showsthat sk isamartingale,sothat s2
k isasub-martingale
(use Jensen’s inequality for conditional expectations). Now
˚ s2
kd =
É
j ˚ u2
kd+2
É
j<k ˚ ujukd
and ifj <k
˚ ujukd = ˚ EAj(ujuk)d = ˚ ujEAj(uk)
«ﬂ‹
=0
d =0.
■■
330

Solution Manual. Last update 18th July 2019
Problem 27.17 Solution: Problem 27.15 shows thatmj is a martingale.
Since a1 = EA0u1−u0 = E{ç,X}u1 = ∫ u1d is constant, i.e.,A0-measurable, the recursion
formula
aj+1=aj+EAjuj+1−uj
implies thataj+1 isAj-measurable.
Sinceuj is a submartingale, we get
EAjuj+1 ⩾uj - ⇒aj+1−aj ⩾0
i.e., the sequenceaj increases.
Finally, ifmj+aj =uj =  mj+ aj are two such decompositions we ﬁnd thatmj−  mj =aj− aj is
Aj−1 measurable. Using the martingale property we ﬁnd
mj−  mj =EAj−1(mj−  mj)
Martingale
= mj−1−  mj−1
and applying this recursively forj=1,2,3,…yields
m1−  m1=0, m 2−  m2=0, m 3−  m3=0,…
so thatmj =  mj and, consequently,aj = aj.
■■
Problem 27.18 Solution: Assume thatMk = EAkM. Then we know from Theorem 27.19 that
M =lim kMk exists a.e. and inL1. Moreover,∫ MkdP =1 so thatM cannot be trivial. On the
other hand,
P(M >0) ⩽P(Mk>0)= P(Xj >0 ∀j=1,2,…,k)=2 −k , , , , , , , , , , , , , , , , , , , , →
k→∞
0
which yields a contradiction.
■■
Problem 27.19 Solution: (ComparethisproblemwithProblem22.16.) Recallthatinﬁnitemeasure
spaces uniform integrability follows from (and is actually equivalent to)
lim
R→∞
sup
n ˚{ðunð>R}
ðunðd =0;
this is true since in a ﬁnite measure space the constant functionw ≡Ris integrable.
Observe now that
˚{ðunð>R}
ðunðd ⩽ ˚{ðunð>R}
EAnfd
= ˚{ðunð>R}
fd
331

R.L. Schilling: Measures, Integrals & Martingales
= ˚{ðunð>R}∩{f ⩽R∕2}
fd + ˚{ðunð>R}∩{f>R∕2}
fd
⩽ ˚{ðunð>R}∩{f ⩽R∕2}
1
2ðunðd+ ˚{ðunð>R}∩{f>R∕2}
fd
⩽ ˚{ðunð>R}
1
2ðunðd+ ˚{f>R∕2}
fd
This shows that
1
2 ˚{ðunð>R}
ðunðd ⩽ ˚{f>R∕2}
fd
R→∞
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , →
uniformly for alln
0.
■■
332

28 Orthonormal systems and their
convergence behaviour.
Solutions to Problems 28.128.11
Problem 28.1 Solution: SinceJ(,)
k is a polynomial of degreek, it is enough to show thatJ(,)
k is
orthogonal inL2(I,(x)dx) to any polynomialp(x) of degreej < k. We write)k for dk
dxk and
u(x)=( x−1)k+(x+1)k+. Then we get by repeatedly integrating by parts
˚
1
−1
J(,)
k (x)p(x)(x−1)(x+1)dx
= (−1)k
k!2k ˚
1
−1
p(x))ku(x)dx
=

p(x)⋅)k−1u(x)− )1p(x)⋅)k−2u(x)+ ⋯+(−1)k−1)k−1p(x)⋅u(x)
1
−1
+(−1)k
˚
1
−1
u(x))kp(x)dx.
Obviously,)lu(−1) =)lu(1) = 0for all0 ⩽l ⩽ k−1 and)kp ≡0 sincep is a polynomial of
degreej <k.
■■
Problem 28.2 Solution: It is pretty obvious how to go about this problem. The calculations them-
selves are quite tedious and therefore omitted.
■■
Problem 28.3 Solution: Theorem28.6: Thepolynomialsaredensein C[a,b]withrespecttouniform
convergence.
Proof 1: mimic the proof of 28.6 with the obvious changes;
Proof 2: Letf ∈ C[a,b]. Then f(y) ∶=f(a+(b−a)y),y ∈ [0,1] satisﬁesf ∈ C[0,1] and,
because of Theorem 28.6, there is a sequence of polynomials pn such that
lim
n→∞
sup
y∈[0,1]
ðf(y)−  pn(y)ð=0.
Deﬁnepn(x)∶=  pn
 x−a
b−a
,x ∈[a,b]. Clearlypn is a polynomial and we have
sup
x∈[a,b]
ðpn(x)− f(x)ð= sup
y∈[0,1]
ð pn(y)− f(y)ð.
333

R.L. Schilling: Measures, Integrals & Martingales
Corollary 28.8:The monomials are complete inL1([a,b],dt).
Proof 1: mimic the proof of 28.8 with the obvious changes;
Proof 2: assume that for allj∈ N0 we have
˚
b
a
u(x)xjdx=0.
Since
˚
1
0
u((b−a)t+a)tjdx= ˚
b
a
u(x)
4
x−a
b−a
5j
dx
=
jÉ
k=0
ck ˚
b
a
u(x)xkdx
=0
we get from Corollary 28.8 that
u((b−a)t+a)=0 Lebesgue almost everywhere on[0,1]
and since the map[0,1] ∋t → x = (b−a)t+a ∈ [a,b] is continuous, bijective and with a
continuous inverse, we also get
u(x)=0 Lebesgue almost everywhere on[a,b].
■■
Problem 28.4 Solution: Observe that
Re

ei(x−y)−ei(x+y)

=Re

eix

e−iy−eiy

=Re

−2ieixsiny

=2sin xsiny,
and that
Re

ei(x+y)+ei(x−y)

=Re

eix

eiy+e−iy

=Re

2eixcosy

=2cos xcosy.
Moreover, we see that forN ∈ N0
˚

−
eiNxdx=
⎧
⎪
⎨
⎪⎩
eiNx
iN
óóó

−
=0, ifN ≠0;
2, ifN =0.
Thus, ifk ≠l
˚

−
2cos kxcoslxdx =Re
0
˚

−
ei(k+l)xdx+ ˚

−
ei(k+l)xdx
1
=0
334

Solution Manual. Last update 18th July 2019
and ifk=l ⩾1
˚

−
2cos kxcoskxdx =Re
0
˚

−
e2ikxdx+ ˚

−
1dx
1
=2
and ifk=l=0 ,
˚

−
2cos kxcoskxdx = ˚ 2dx=4.
The proof for the pure sines integral is similar while for the mixed sine-cosine integrals the integ-
rand
x →coskxsinlx
is always an odd function, the integral over the symmetric (w.r.t. the origin) interval(−,) is
always zero.
■■
Problem 28.5 Solution:
(i) We have
2kcosk(x)=2 k
eix+e−ix
2
k
=
eix+e−ix
2
k
=
kÉ
j=0
0
k
j
1
eijxe−i(k−j)x
=
kÉ
j=0
0
k
j
1
ei(2j−k)x
Addingtheﬁrstandlastterms,secondandpenultimateterms,termno. j andk−j,etc.under
the sum gives, since the binomial coeﬃcients satisfy k
j
=   k
k−j
,
–ifk=2nis even
22ncos2n(x)=
n−1É
j=0
0
2n
j
1
(ei(2j−2n)x+ei(2n−2j)x)+
0
2n
n
1
=
nÉ
j=0
0
2n
j
1
2cos(2j−2n)+
0
2n
n
1
–ifk=2n−1 is odd
22n−1cos2n−1(x)=
n−1É
j=0
0
2n−1
j
1
(ei(2j−2n+1)x+ei(2n−2j−1)x)
=
n−1É
j=0
0
2n−1
j
1
2cos(2n−2j−1)x.
335

R.L. Schilling: Measures, Integrals & Martingales
In a similar way we computesinkx:
2ksink(x)=2 k
eix−e−ix
2i
k
=i−k
eix−e−ix
2
k
=i−k
kÉ
j=0
0
k
j
1
(−1)k−jeijxe−i(k−j)x
=i−k
kÉ
j=0
0
k
j
1
(−1)k−jei(2j−k)x.
Addingtheﬁrstandlastterms,secondandpenultimateterms,termno. j andk−j,etc.under
the sum gives, since the binomial coeﬃcients satisfy k
j
=   k
k−j
,
–ifk=2nis even
22nsin2n(x)
=(−1) n
n−1É
j=0
0
2n
j
1 (−1)2n−jei(2j−2n)x+(−1)jei(2n−2j)+
0
2n
n
1
=
n−1É
j=0
0
2n
j
1
(−1)n−j ei(2j−2n)x+ei(2n−2j)+
0
2n
n
1
=
n−1É
j=0
0
2n
j
1
(−1)n−j2cos(2n−2j)x+
0
2n
n
1
–ifk=2n−1 is odd
22n−1sin2n−1(x)
=i(−1)n
n−1É
j=0
0
2n−1
j
1 (−1)2n−1−jei(2j−2n+1)x+(−1)−jei(2n−2j−1)
=i
n−1É
j=0
0
2n−1
j
1
(−1)n−j −ei(2j−2n+1)x+ei(2n−2j−1)
=i
n−1É
j=0
0
2n−1
j
1
(−1)n−j2isin(2n−2j+1)x
=
n−1É
j=0
0
2n−1
j
1
(−1)n−j−12sin(2n−2j+1)x.
(ii) We have
coskx+isinkx=eikx=  eixk
=  cosx+isinxk
and we ﬁnd, using the binomial formula,
coskx+isinkx=
kÉ
j=0
0
k
j
1
cosjx⋅ik−jsink−jx
and the claim follows by separating real and imaginary parts.
336

Solution Manual. Last update 18th July 2019
(iii) Since a trigonometric polynomial is of the form
Tn(x)= a0+
nÉ
k=1
 akcoskx+bksinkx
it is a matter of double summation and part (ii) to see thatTn(x)can be written likeUn(x).
Conversely, part (i) enables us to rewrite any expression of the formUn(x)asTn(x).
■■
Problem 28.6 Solution: By deﬁnition,
DN(x)= 1
2+
NÉ
j=1
cosjx.
Multiplying both sides bysin x
2 and using the formula
cosaxsinbx= 1
2

sin(a+b)x
2 −sin (a−b)x
2

wherej=(a+b)∕2and1∕2=( a−b)∕2, i.e.a=(2j+1)∕2 andb=(2j−1)∕2 we arrive at
DN(x)sin x
2 = 1
2sin x
2 + 1
2
NÉ
j=1

sin (2j+1)x
2 −sin (2j−1)x
2

=sin (2N+1)x
2 .
■■
Problem 28.7 Solution: We have
ðsinxð= 2
 − 4

0
cos2x
1⋅3 +cos4x
3⋅5 +cos6x
5⋅7 +⋯
1
.
Indeed, let us calculate the Fourier coeﬃcients 28.8. First,
bk= 1
 ˚

−
ðsinxðsinkxdx =0, k ∈ N,
sincetheintegrandisanoddfunction. SonosinesappearintheFourierseriesexpansion. Further,
using the symmetry properties of the sine function
a0∕2= 1
2 ˚

−
ðsinxðdx
= 1
 ˚

0
ðsinxðdx
= 1
(−cos x)óóó

0
= 2

and using the elementary formula2sin acosb=sin(a−b)+sin( a+b)we get
aj = 1
 ˚

−
ðsinxðcosjxdx
337

R.L. Schilling: Measures, Integrals & Martingales
= 2
 ˚

0
sinxcosjxdx
= 2
 ˚

0
1
2
 sin((j+1)x)−sin(( j−1)x)dx
= 1

4cos((j−1)x)
j−1 −cos((j+1)x)
j+1
5
0
= 1

4cos((j−1))
j−1 −cos((j+1))
j+1 − 1
j−1 + 1
j+1
5
.
Ifj is odd, we getaj =0 and ifj is even, we have
aj = 1

4
−1
j−1 − −1
j+1 − 1
j−1 + 1
j+1
5
=− 4

1
(j−1)(j+1) .
This shows that we have only evenly indexed cosines in the Fourier series.
■■
Problem 28.8 Solution: This is not as trivial as it looks in the ﬁrst place! Sinceu is itself a Haar
function, we have
sN(u,x)= u(x) ∀ N ∈ N
(it is actually the ﬁrst Haar function) so thatsN converges in anyLp-norm,1 ⩽p< ∞tou.
Thesameappliestothe righttail oftheHaarwaveletexpansion. Thelefttail,however,converges
only for1<p< ∞ inLp. The reason is the calculation of Step 5 in the proof of Theorem 28.20
which goes in the casep=1 :
EAΔ
−Mu=2 −M
˚[−2M,0)
u(x)dx1[−2M,0)+2−M
˚[0,2M)
u(x)dx1[0,2M)
=2 −M 1[0,2M),
but this is notL1-convergent to0 as it would be required. Forp> 1 all is ﬁne, though....
■■
Problem 28.9 Solution: Assume thatuis uniformly continuous (Cc andC∞-functions are!). Since
sn(u;x)= EAH
n u(x)
is the projection onto the sets inAH
n , see e.g. Step 2 in the proof of Theorem 28.17, we have
sn(u;x)= 1
(I) ˚I
u(y)dx1I(x)
whereI isandyadicintervalfromthegeneratorof AH
n asinStep2oftheproofofTheorem28.17.
Thus, ifxis fromI we get
ðsn(u;x)− u(x)ð=
óóóó
1
(I) ˚I
(u(y)− u(x))dx
óóóó
⩽ 1
(I) ˚I
ðu(y)− u(x)ðdx
338

Solution Manual. Last update 18th July 2019
⩽ 1
(I) ˚I
dx
=
if(I)< for small enough >0. This follows from uniform continuity: for given >0 there
is some >0 such that forx,y ∈I (this entailsðx−yð ⩽!) we haveðu(x)− u(y)ð ⩽.
The above calculation holds uniformly for allx and we are done.
■■
Problem 28.10 Solution: The calculation for the right tail is more or less the same as in Problem
28.9. Only the left tail diﬀers. Here we argue as in Step 5 of the proof of Theorem 28.20: if
u∈Cc(R)we can assume thatsuppu⊂ [−R,R]and we see
EAΔ
−Mu(x)=2 −M
˚[−R,0]
u(x)dx1[−2M,0)+2−M
˚[0,R]
u(x)dx1[0,2M)
⩽2−MR‖u‖∞1[−2M,0)+2−MR‖u‖∞1[0,2M)
=2 −MR‖u‖∞1[−2M,2M)
⩽2−MR‖u‖∞
M→∞
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , →
uniformly for allx
0
Ifu ∈ C∞ we can use the fact thatCc is dense inC∞, i.e. we can ﬁnd for every >0 functions
v=v ∈Cc andw=w ∈C∞ such that
u=v+w and ‖w‖∞ ⩽.
Then
óóóEAΔ
−Mu(x)óóó ⩽ óóóEAΔ
−Mv(x)óóó+óóóEAΔ
−Mw(x)óóó
⩽ óóóEAΔ
−Mv(x)óóó+ EAΔ
−M‖w‖∞
⩽ óóóEAΔ
−Mv(x)óóó+
and, by the ﬁrst calculation forCc-functions, the right-hand side converges, sincev∈Cc, to0+ 
uniformly for allx, and letting →0 we conclude the proof.
■■
Problem 28.11 Solution: See the picture at the end of this solution. Since the functionu(x) ∶=
1[0,1∕3)(x)ispiecewiseconstant,andsinceforeachHaarfunction ∫ k,jdx=0 unlessj=k=1 ,
we see that only a single Haar function contributes to the value ofsN(u; 1
3), namely where1
3 ∈
suppn,j.
The idea of the proof is now pretty clear: take valuesN wherex= 1
3 is in the left ‘half’ ofN,k,
i.e. whereN,k(1
3)=1 and valuesM such thatx= 1
3 is in the opposite, negative ‘half’ ofM,l,
i.e.where M,l(1
3)=−1 . Ofcourse,k,l dependon x,N andM respectively. Oneshouldexpect
thatthepartialsumsforthesediﬀerentpositionsleadtodiﬀerentlimits, hencediﬀerentupperand
lower limits.
339

R.L. Schilling: Measures, Integrals & Martingales
The problem is to pickN’s andM’s. We begin with the simple observation that the dyadic (i.e.
base-2) representation of1∕3is the periodic, inﬁnite dyadic fraction
1
3 =0.01010101⋯=
∞É
k=1
1
22k
and that the ﬁnite fractions
dn∶=0.0101⋯01«›››ﬂ›››‹
2n
=
nÉ
k=1
1
22k
approximate1∕3 from the left in such a way that
1
3−dn=
∞É
k=n+1
1
22k <
∞É
l=2n+2
1
2l = 1
22n+2
1
1− 1
2
= 1
22n+1
Now consider those Haar functions whose support consists of intervals of the length2−2n, i.e.
the2n,j’s and agree thatj = j(1∕3,n) is the one value where1
3 ∈ supp2n,j. By construction
supp2n,j =[dn,dn+1∕22n]and we get for the Haar-Fourier partial sum
s2n(u, 1
3)− 1
3 = ˚
1∕3
dn
2ndx⋅2n,j(1
3)
=2 2n 1
3−dn

=4 n
∞É
k=n+1
1
22k
=4 n
∞É
k=n+1
1
4k
=4 n4−n−1 1
1− 1
4
= 1
3.
Theshiftby −1∕3comesfromthestarting‘atypical’Haarfunction0,0since⟨u,0,0⟩= ∫ 1∕3
0 dx=
1
3.
UsingthenextsmallerHaarfunctionswithsupportoflength 2−2n−1, i.e.the2n+1,k’s, weseethat
withj as above2n+1,2j−1(1
3) = −1(since twice as many Haar functions appear in the run-up to
dn) and that
s2n+1(u, 1
3)− 1
3
=
4
˚
dn+1∕22n+2
dn
2n+1dx− ˚
1∕3
dn+1∕22n+2
2n+1dx
5
⋅2n+1,2j−1(1
3)
=
4
dn+ 1
22n+2 −dn−1
3+dn+ 1
22n+2
5
2n+1⋅(−2n+1)
=
4
dn−1
3+ 2
22n+2
5
⋅(−22n+2)
340

Solution Manual. Last update 18th July 2019
=4 ⋅22n
1
3−dn

−2
=4 ⋅1
3−2 (using the result above)
=− 2
3
This shows that
s2n(u; 1
3)= 2
3 >−1
3 =s2n+1(u, 1
3)
and the claim follows since because of the above inequality,
liminf
N
sN(u; 1
3) ⩽−1
3 ⩽ 2
3 ⩽limsup
N
sN(u; 1
3).
■■
341

R.L. Schilling: Measures, Integrals & Martingales
✻
✲
/u1D451 /u1D45B /u1D451 /u1D45B + 1
22/u1D45B+1 /u1D451 /u1D45B + 1
22/u1D45B
2
2/u1D45B
2
2
2/u1D45B+1
2
/u1D451 /u1D45B+1
1
3
/u1D712 2/u1D45B,/u1D457 and /u1D712 2/u1D45B+1,2/u1D457−1
Picture is not to scale!
2
342

