11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 1/27
My Solutions to Old Analysis Quals
Jacob S Townson
August-December 2017
Prelude
This document is written in reference to qualifying exams given at the University of Louisville in past years. These solutions are not given fromthe University, but of my work alone as a way to study for my own qualifying exam. If any tips or recommendations come up and you feel youshould share, feel free to raise an issue on GitHub where I have this document saved and open to the public here(https://github.com/obewanjacobi/gradwork/tree/master/Classes/Old%20Qualifying%20Exams/My%20Solutions). To see the qualifying exams foryourself, visit this link (http://www.math.louisville.edu/GraduateFAQ/qualifiers/QualifierStudyGuides/). When referencing the Royden book, this isin reference to the Real Analysis; 4th Edition. Special thanks to Trevor Leach for sharing his solutions with me for reference on this document.Thank you for reading, and for all advice.
Jacob Townson
What to Expect:
differentiation and Riemann integration of functions of one real variable, sequences of functions, uniform convergence, Lebesgue’scharacterization of Riemann integrability
topology of the line, countable and uncountable sets, Borel sets, Cantor sets and Cantor functions, Baire category theorem
Lebesgue measure and integration on the line, measurable functions, convergence theorems
AC and BV functions, fundamental theorem of calculus, Lebesgue differentiation theorem
Hilbert spaces, Lp spaces, lp spaces, Hölder and Minkowski (like triangle) inequalities, completeness
There are a few types of problems that are consistently on exams as well, and may be good to know. These include that when asked to proveuniform convergence, using the Wierstass M-test is the easiest method; when a problem involves absolute continuity, it will often be used toimply bounded variation, which then implies that we can use the fundamental theorem of calculus; and finally, if we have two functions that arein conjugate  spaces, Holder’s inequality will help us. Using these tricks and others contained in this document should guarantee a passingscore on the qualifier!
My Solutions from Quals
Spring 2017
Prove that if  has Lebesgue measure , then .
My Solution:
Let  and . First note that we know  is continuous on . Let , then
Also,  for all . By definition of Lebesgue measure, for all , there exists a sequence of intervals  such that  is the empty set for all  and . Also,  such that  since . Let 
, , then . Then
Since  is continuous, we know that . Since  is a closed interval and  is continuous, we
can find  and  such that  and . WLOG we can assume that . Then,
where 
Since  and , we find that . This implies  which implies
Lp
A⊂R 0 m({ |x∈A})=0ex
m(A)=0 E={ |x∈A}ex f(x)=ex R =[−N,N]∩AAN
A=⋃
N=1
∞
AN
m(A)=0⟹m( )=0AN N∈N ϵ>0{In}∞n=1 ∩Ii Ij i j ⊂∪AN In l( )<ϵ∑n In m( )=0AN=( , )In anbn =[ , ]I∗n anbn m( )=m( )In I∗n
m(f( ))< m(f( ))= m(f( ))AN ∑n In ∑n I∗n
f m(f( ))= f(x)− f(x)I∗n maxx∈I∗n minx∈I∗n I∗n fx1 ∈x2 I∗n f( )= f(x)x1 maxx∈I∗n f( )= f(x)x2 minx∈I∗n ≤x1 x2
m(f( ))=f( )−f( )≤| (α)|( − )I∗n x1 x2 f′ x1 x2
≤ (x)×l( )≤ (x)ϵmaxx∈I∗n
f′ In maxx∈I∗n
f′
α∈( , )x1x2
(x)<∞maxx∈I∗nf′ ϵ→0 m(f( ))=0In m(f( ))=0AN

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 2/27
Thus, . QED
Prove that if  is absolutely continuous, then so is .
My Solution:
Given that  is absolutely continuous, we know then that for all , there exists a  such that if  is a finite collection of
disjoint intervals of  with  implies that . Also, because  is absolutely continuous, weknow then that it must also be continuous. Hence,  must be bounded on . Let  on  and choose  such that 
 gives us
Then note that
Hence,  is absolutely continuous as well. QED
Prove that if  is absolutely continuous on  and there is a  suchthat  a.e., then  is differentiable on  and .
My Solution:
Using Lebesgue’s fundamental theorem of calculus, we know that
Then, because  a.e.;
This implies that , thus by the fundamental theorem of calculus, if we take the derivative of both sides, we can see that 
 for all . Note, the reason that we can use the fundamental theorem of calculus here is because the function  is absolutelycontinuous, which implies it’s of bounded variation. QED
Prove that the series  converges uniformly for  andthen evaluate the following series:
My Solution:
Recall the Weierstrass M Test: Let  be a series of real valued functions on a subset . Suppose there exists a convergent
series  where  such that for all  and , . Then  converges uniformly.
Now, for ,  for all . Note,  converges because it is a geometric series. Thus by the
Weierstrass M test, the series converges uniformly for . QED
Because the series converges uniformly on a compact set,
m(f(A))=m(f( ))≤ m(f( ))=0∪∞NAN ∑
N
∞
AN
m(f(A))=m(E)=0
f:[0,1]→(0,∞) 1/f
f ϵ>0 δ>0 {( , )aibi }ni=1[0,1] | − |<δ∑ni=1bi ai |f( )−f( )|<ϵ∑ni=1 bi ai ff [0,1] m=min(f) [0,1] δ| − |<δ∑ni=1bi ai
|f( )−f( )|< ϵ∑
i=1
n
bi ai m2
− =∑
i=1
n ∣∣∣ 1f( )bi
1f( )ai
∣∣∣ ∑
i=1
n ∣∣∣f( )−f( )bi ai
f( )f( )ai bi
∣∣∣
≤ |f( )−f( )|< =ϵ1
m2∑
i=1
n
bi ai ϵm2
m2
1f
f [0,1] g∈C([0,1])=gf′ f [0,1] =gf′
f(x)=f(0)+∫
x
0 f′
=gf′
f(x)=f(0)+ g∫
x
0
= g∫x0f′ ∫x0(x)=g(x)f′ x f
t∑∞k=0sink t∈[−π/4,π/4]
(t)dt∑
k=0
∞
∫
π/4
−π/4sink
∑∞n=1fn A⊂R∑∞n=1Mn ≥0Mn n∈N x∈A| (x)|≤fn Mn ∑∞n=1fn
t∈[−π/4,π/4] (t)≤sink ( )12√
k k ∑∞k=1( )12√
k
t∈[−π/4,π/4]
(t)dt= (t)dt= dt∑
k=1
∞
∫
π/4
−π/4sink ∫
π/4
−π/4∑
k=1
∞
sink ∫
π/4
−π/4
11−sin(t)

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 3/27
QED
Let  be a sequence of Lebesgue measurable subsets of . Prove:(a) If  then ; and (b) If  it maynot be true that 
My Solution:
a. Let , since , there exists an  such that . So,
Hence,
This implies that .
b. Let , , , , , , , ,… We repeat
these definitions in this pattern, giving us that . But for all ,  implying that . Thus it may not be true that if  that . QED
Prove that if , , then 
My Solution:
Let  and . Note, since ,  (because , , which implies
that  must be finite). So,
where
and
since . This argument works for any . As for , this argument still works, however rather than saying the above, weargue . So for any  such that , we can see that the integral is indeed bounded. Thus
by the Lebesgue Dominated Convergence Theorem,
QED
Define the function  by  if  is irrational, and by 
if  is rational and  when written in least terms. Decide whether or not  is
Riemann integrable on  and if so, evaluate its integral.
My Solution:
Let , then . Thus . Also  is clearly measurable as 
. Hence  is Lebesgue measurable and  with  since  a.e. QED
= dt= (t)dt+ tan(t)sec(t)dt∫
π/4
−π/4
1+sin(t)(t)cos2 ∫
π/4
−π/4sec2 ∫
π/4
−π/4
=tan(t) +sec(t) =1−(−1)+ − =2|π/4−π/4 |π/4−π/4 2–√ 2–√
{ }⊂MEn [0,1]∑m( )<∞En m(limsup )=0En m( )→0Enm(limsup )=0En
ϵ>0 ∑m( )<∞En N ∑m( )<ϵEN
limsup( )= ⊂En ⋂
n=1
∞
⋃
k=n
∞
Ek ⋃
k=n
∞
Ek
m(limsup( ))≤m( )≤ m( )<ϵEn ⋃
k=N
∞
Ek ∑
k=n
∞
Ek
m(limsup )=0En
=[0,1]E1 =[0, ]E2 12 =[ ,1]E3 12 =[0, ]E4 14 =[ , ]E5 14 12 =[ , ]E6 12 34 =[ ,1]E7 34 =[0, ]E8 18m( )=0limn→∞ En n∈N =[0,1]⋃∞k=nEklimsup( )=[0,1]En m( )→0En m(lim sup( ))=0En
f∈ ([0,∞))Lp 1≤p≤∞ f(x) dx=0limn→∞∫∞0 e−nx
A={x|f(x)<1} B={x|f(x)≥1} f∈Lpm(B)<∞ f∈Lp <∞(∫|f )|p 1/p
m(B)
f(x) dx=∫(f(x) +f(x) )dx∫∞
0 e−nx e−nxχA e−nxχB
f(x) dx< =1∫∞
0 e−nxχA ∫∞
0 e−x
∫f(x) dx≤∫|f <∞e−nxχB |pχB
f∈Lp 1≤p<∞ p=∞∫f(x) dx≤esssupf <∞e−nxχB χB p 1≤p≤∞
f(x) dx= f(x) dx=∫0dx=0limn→∞∫
∞
0 e−nx ∫
∞
0 limn→∞ e−nx
f:[0,1]→R f(x)=0x f(x)=1qx x=pq f[0,1]
A={x| f(x)≠f(a)}limx→a A={x|x∈Q} m(A)=0 f{x|f(x)≥a}={(0,∞)} f ∫f=Rf ∫f=0 f=0

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 4/27
Let  be a sequence of polynomials. Suppose that for every point there exists an index  satisfying . Prove at least one of the polynomialsis identically zero.
My Solution:
Suppose there does not exist an  such that  for all . Let’s define . Note,  has to be finite
since each polynomial can only have a finite number of zeros. Now consider  since for each  there exists apolynomial such that . But a countable collection of finite sets is countable. But  is uncountable, thus giving us a contradiction.This implies that one of the polynomials must indeed be identically zero. QED
Let . Prove that the following are equivalent to each other: (a)  is notLebesgue measurable; and (b) There is an  such that whenever  ismeasurable and , then .
My Solution:
Let  not be Lebesgue measurable and suppose that for all  there exists  such that  and . So for every ,
let  and . Then  and . Since  which implies 
 is measurable (because Lebesgue measure is complete). Hence,  is measurable. This is acontradiction, thus we have proven the desired result. QED
Let . Define a functional  by .Prove that 
My Solution:
Will show :
Note, by Holder’s since we have ,
Will show :
We may assume .  is -finite, so there exists  increasing towards  such that . Define 
 for , to be fixed. Hence . Define , which implies 
for all  and  for all . Thus  for all . This implies .
Thus we have proven the desired result. QED
August 2016
Let  be a closed set. Prove that  is Riemann integrable iff  hasLebesgue measure zero.
My Solution:
Assume that  has Lesbegue measure zero. This implies that . Thus the Riemann integral exists andagrees with the Lebesgue integral.
Now assume that  is Riemann integrable. This is true iff the Lesbegue integral exists and . So  isdiscontinuous at its boundary points, which implies that . QED
Let  Prove the following statements are equivalent: (a)  is Lebesguemeasurable and (b) There is a  set  and a set  of measure zero such that .
My Solution:
{ }pn x∈[0,1]n (x)=0pn
n =0pn n∈N ={x∈[0,1]| (x)=0}Sn Pn Sn⊇[0,1]⋃∞n=1Sn x∈[0,1](x)=0pn [0,1]
A⊂R Aϵ>0 BA⊂B (B/A)≥ϵm∗
A ϵ>0 B A⊂B (B−A)<ϵm∗ 1n⊃ABn ( −A)<m∗Bn 1n A⊂∩Bn ((∩ )−A)=0m∗ Bn ((∩ )−A)=0m∗ Bn(∩ )−ABn A=[(∪( ))∪(∩( )−A)Bcn Bn ]c
h∈ (R)L∞ T: (R)→RL1 Tf= (fh)dm∫RTf=||h|sup||f| ≤1|1 |∞
≤
Tf= ∫fh≤ ||f| ||h|sup||f| ≤1|1
sup||f| ≤1|1
sup||f| ≤1|1
|1 |∞
1,∞
≤1⋅||h| =||h||∞ |∞
≥
||h| =M>0|∞ Rσ Fn x m( )<aFn
={x∈ ||h(x)|>a}An Fn 0<a<M m( )>0An (x)=gn sgn(h)−χAn
m( )An || | =1gn|1
n ∫h =agn n a<∫hgn n a< ∫hsup0<a<M sup|| | ≤1gn|1 gn
||f| =M< ∫fh= Tf|∞ sup||f| ≤1|1
sup||f| ≤1|1
C⊂[0,1] χC ∂C
∂C m({x| f(x)≠f(a)})=0limx→a
χC m({x| f(x)≠f(a)})=0limx→a χCm(∂C)=0
S⊂R SGδ G NS=G−N

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 5/27
( ): Given  is a  set,  must then be Borel measurable. Thus it is also Lebesgue measurable.  must be Lebesguemeasurable as well since the Lebesgue -algebra is complete. Thus  is Lebesgue measurable.
( ): This follows directly from a proposition stating that if  is a Lebesgue measurable set, and  is a Lebesgue measure,then there exists a set  which contains  that is the countable intersection of a decreasing sequence of open sets and .QED
If  is nonnegative and integrable on , then 
My Solution:
where . Thus,
Since  is integrable, we know that , and  must be bounded, thus  is integrable as well.
So,
by the D.C.T., and thus,
QED
Let . If  for all rational numbers  and  with , then  a.e.
My Solution:
We will claim here that  integrates to  over arbitrary open sets. Thus for any , choose an open set  such that and . Hence
because . Thus the integral is  since this is true for all .
We must now prove our claim in order to complete the problem. For any , there exists  such that decreases to  and  increases to  as  goes to infinity. Thus . Using this, and the dominated convergence theorem,
we find that
with  as the majorant since . Now let  with  being arbitrary disjoint intervals. Then
By the dominated convergence theorem,
with  as the majorant because . Thus  for any open set . A similar proof holds for . Hence 
 a.e. QED
b⟹a G Gδ G Nσ S=G−N
a⟹b A⊂[0,1] mH A m(H−A)=0
f [0,1]=m{x|f(x)>0}limn→∞∫10 f−−√n
= ⋅ + ⋅∫
1
0 f−−√n ∫
1
0 f−−√n χf=0 ∫
1
0 f−−√n χf>0
⋅ = =0∫10 f−−√n χf=0 ∫10 0–√n
= ⋅∫
1
0 f−−√n ∫
1
0 f−−√n χf>0
f ⋅ < f<∞∫10 f−−√n χf>1 ∫10 ⋅∫10 f−−√n χ0<f<1 f−−√n
⋅ = ⋅limn→∞∫
1
0 f−−√n χf>0 ∫
1
0 limn→∞ f−−√n χf>0
= 1⋅ =m({x|f(x)>0})∫
1
0 χf>0
f∈ (R)L1 f=0∫ba a b a<bf=0
f 0 ϵ>0 B A={f>0}⊂Bm(B−A)<δ
f≤ f− f= f≤ |f|<ϵ∣∣∣∫A
∣∣∣ ∣∣∣∫B ∫A
∣∣∣ ∣∣∣∫B−A
∣∣∣ ∫B−A
m(B−A)<δ 0 ϵ
(a,b)∈R×R { },{ }∈Qan bn ana bn b n f= f∫(a,b) ∫∪( , )anbn
f= f=0∫∪( , )anbn
limn→∞∫( , )anbn
|f| f∈L1 B= ( , )⋃∞n=1anbn ( , )anbn
f=∫ f⋅∫B ∑
n=1
∞
χ( , )anbn
∫ f⋅ = ∫f⋅ =∑0=0∑
n=1
∞
χ( , )anbn ∑
n=1
∞
χ( , )anbn
|f| f∈L1 f=0∫B B m({x|f(x)<0})=0f=0

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 6/27
Suppose that  and . Define . Prove that 
 and that .
My Solution:
For , we have
So . Given this, we can see that
by Holders’ because  and  are conjugate. Then,
QED
Let  be a sequence of real numbers with the property that  for all .Prove that both series ,  convergeuniformly on every compact subinterval of  and that  for all .
My Solution:
Since ,
which converges uniformly because  by the Weirstrass-M test (and because it’s a geometric series). Let  be a compact
interval of  and let . Then  which converges because it’s a geometric sequence. Now weapply the Weirstrass M-test to give us the desired result.
As for proving that , we simply note that by definition of differentiation on power series that this is true (with simple calculus IIlogic). QED
Give an example of a continuous function  with the property that , , yet  for almost every .
My Solution:
Let  be the Cantor function on . Consider . Then  and . Also,almost everywhere the derivative of the Cantor function is 0 (because almost everywhere it is constant). Then the derivative almost everywhereof  would be  almost everywhere.
Let  be a sequence of measurable subsets of  with the propertythat . Show almost every  is contained in only finitelymany of the .
My Solution:
By way of contradiction, suppose there exists an  such that . Also assume that  for all  where  is asubsequence of . But
which diverges because . Thus by contradiction, we have proven the desired result. QED
f∈ ([0,1])L2 ||f| =1|2 g(x)=xf(x)g∈ ([0,1])L1 ||g| ≤|1 13√
x∈ ([0,1])L2
= <∞( |f )∫1
0 |2 1/2
( )13x3|10
1/2
x∈L2
||x⋅f(x)| ≤||x| ||f||1 |2 |2
2 2
||x| ||f| ≤ ⋅1≤|2 |2 ( )13x3|10
1/2 1
3–√
{ }ak | |≤1ak kf(x)=∑∞k=1akxkg(x)= k∑∞k=1akxk−1
(−1,1) (x)=g(x)f′
x∈(−1,1)
| |≤1ak
≤∑
k=1
∞
akxk ∑
k=1
∞
xk
|x|<1 C⊂[0,1](−1,1) a=max{|x|:x∈C} ∑|x ≤∑|k ak
(x)=g(x)f′
f:[0,1]→Rf(0)=0f(1)=1 (x)≤−1f′ x∈[0,1]
C(x) [0,1] f(x)=2C(x)−x f(0)=2⋅0−0=0 f(1)=2⋅1−1=1
f(x) (x)=−1f′
, , ,...E1E2E3 Rm( )<∞∑∞n=1 En x∈REn
I⊂R m(I)=c>0 I⊂E∗n n { }E∗n{ }En
m( )≥ m(I)= c∑
n=1
∞
E∗n ∑
n=1
∞
∑
n=1
∞
c>0

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 7/27
Let  be Lebesgue measurable. Prove that if  for all , then  exists and .
My Solution:
First off, it is known that . Since , and since we’re integrating between  and , we can easily see then that 
. Let , then  which implies that . Thus  is integrable. QED
Define a sequence of functions  by  if  and 
 if . Does  converge in ? If so, to what function?
My Solution:
Suppose  in . Then . But  for all . Hence . However, this is a contradiction
because , thus it does not converge in . QED
January 2016
Let  be dense in  and . Prove or give a counterexample:  ismeasurable iff  is measurable for all .
My Solution:
First assume  is measurable. This implies that  is Lebesgue measurable for all . Hence  is Lebesguemeasurable for all .
Now assume that  is measurable for all . It suffices to show that  is measurable for all . So, let, given that  is dense in . Let  such that  decreases to . Thus,
is the union of measurable sets. Hence  is measurable. QED
Suppose  denotes the Lebesgue measure of the set . Let  be absolutely continuous and  be such that .Prove that .
My Solution:
Given  with , let  be a collection of disjoint intervals covering  with .  is absolutelycontinuous, which implies that it must also be continuous. Thus for each , let  such that 
. Also, recall that because  is continuous, this implies that for all , there exists a 
such that  where . Now notice that
because . Thus
because . Thus . QED
Let  for each . Prove that the sequence  convergesuniformly on  for each , and converges non-uniformly on .
My Solution:
Before we begin, note that if , then
f:[0,1]→R p≤f(x)≤qx∈[0,1] f∫[0,1] p≤ f≤q∫[0,1]
1=1∫[0,1] p≤f≤q 0 1p≤ f≤q∫[0,1] a=max{|p|,|q|} |f|<a |f|<a∫[0,1] f
∈ [0,1]fn L1 (x)=nfn x≤1nf(x)=0x>1n fn ([0,1])L1
→ffn Lp || | →||f|fn|1 |1 ∫| |= ⋅n=1fn 1n n ||f||=1=0limn→∞fn ([0,1])L1
S R f:R→R f{x:f(x)≥s} s∈S
f {x|f(x)≥a} a∈R {x|f(x)≥s}s∈S
{x:f(x)≥s} s∈S {x:f(x)>s} s∈Sc
t∈Sc S R { }⊂Stn tn t
{x:f(x)>t}= {x|f(x)≥ }⋃
n=1
∞
tn
f
λ(S) S⊂Rg:[0,1]→R E⊂[0,1] λ(E)=0λ(g(E))=0
E⊂[0,1] λ(E)=0 {( , )}aibi E | − |<δ∑ni=1bi ai g( , )aibi ( , )⊆( , )cidi aibi{f( ),f( )}∈{min(f ,max(f }ci di )( , )aibi )( , )aibi g ϵ>0 δ|f( )−f( )|<ϵai bi | − |<δai bi
| − |< | − |<δ∑
i=1
n
ci di ∑
i=1
n
bi ai
( , )⊆( , )cidi aibi
λ(g(E))≤λ(g( ( , )))=λ( g( , ))⋃
i=1
∞
aibi ⋃
i=1
∞
aibi
≤ λ(g( , ))≤ |f( )−f( )|<ϵ∑
i=1
∞
aibi ∑
i=1
∞
ci di
∑| − |<δci di λ(g(E))=0
(x)=fn xn n≥1 { }fn[−δ,δ] 0<δ<1 (−1,1)
|x <ϵ|n

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 8/27
. This will be useful in our proof.
Let  and . Also let . Hence for  (thus ),  which implies that .
The reason that the inequality changes directions here is because for  and for very small  (specifically less than ), . Thus, we can see that , which implies that  for all . Thus  converges uniformly on .
If we fix , this implies that  by our previous point in the proof. However, it is not uniform since  depends on . Thus wehave proven the desired result. QED
Let  denote the Lebesgue measure of the set . Find an open set  which isdense in  such that  and  for any interval .
My Solution:
Let  represent the rationals in . For each  define  as an interval containing ,  and . Let 
 with
Since  contains the rationals on , it is also dense on .  is open because it is the countable union of open intervals on . let . It must contain a rational, which implies that it intersects any  non-trivially, thus . Thus  is a dense open set on  such that the measure of  is less than  and intersects any interval of  non-trivially. QED
Is  separable, where ?
My Solution:
Yes! First note that separable means that it contains a countable subset that is dense in .
Let  be step functions on  and let  be step functions of  with rational endpoints. Since is dense in ,  is dense in  thus it’s dense in . QED
Suppose that  and that . Prove that if  in 
and  in , then  in .
My Solution:
Here it is sufficient to show that . Well,
by Holder’s Inequality, where , , and . Thus we have proven the desired
result. QED
Assume that . Prove that  for each  andthat .
My Solution:
To complete this proof, we will divide the problem into a group of lemmas and prove them to get the desired result.
ln(|x )<ln(ϵ) ⟹nln(|x|)<ln(ϵ)|n
⟹n<ln(ϵ)ln(|x|)
δ∈(0,1) ϵ>0 N=ln(ϵ)ln(δ) n≥N n≥ln(ϵ)ln(δ) nln(δ)≤ln(ϵ) ln( )≤ln(ϵ)δn
δ∈(0,1) ϵ 1ln(δ),ln(ϵ)<0 ≤ϵδn < <ϵxn δn x∈(−δ,δ) { }fn[−δ,δ]
x∈(−1,1) <ϵxn N x
m(G) G G[0,1] m(G)<1 m(G∩I)>0I⊂[0,1]
{qi}∞i=1 Q∩[0,1] n In qnm( )<In 14⋅2n ⊂[0,1]In
G=⋃∞i=1In
m(G)=m( )≤ m( )⋃
i=1
∞
In ∑
i=1
∞
In
< = ⋅ =∑
i=1
∞ 14⋅2n
14 11−(1/2) 12
G [0,1] [0,1]G [0,1]I⊂[0,1] In m(I∩G)>0 G[0,1] G 1 [0,1]
([a,b])Lp 1<p<∞
X
S[a,b]⊂ ([a,b])Lp [a,b] [a,b]⊂S[a,b]SQ [a,b] QR [a,b]SQ S[a,b] ([a,b])Lp
1<p,q<∞ + =11p 1q →ffn (R)Lp
→ggn (R)Lq →fgfngn (R)L1
|| −fg||=0limn→∞fngn
|| −fg| = || − g+ g−fg|limn→∞fngn |1 limn→∞fngn fn fn |1
= || − g| +|| g−fg|limn→∞fngn fn |1 fn |1
≤ || | ⋅|| −g| +|| −f| ⋅||g| =0limn→∞fn|p gn |q fn |p |q
|| | →||f| <∞limn→∞fn|p |p || −g| →0gn |q || −f| →0fn |p
f∈ ([0,1])L∞ f∈ ([0,1])Lp 1≤p<∞||f| = ||f||∞ limp→∞ |p

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 9/27
Lemma 1:  Proof: Assume . Then  a.e. Then 
. Thus .
Lemma 2: Assume . Then  for . Proof: Consider .
where for ,  since .
where . Thus , which implies .
Lemma 3:  Proof:  a.e. This implies that , which implies 
. Hence .
Lemma 4:  Proof: Let . Then . Then 
. Hence . This implies that 
. Thus  for all . It follows that by our claims then
that . Thus we have proven the desired result. QED
August 2015
Let  denote the Cantor set. Let  if  and  otherwise.
Explain why  is Riemann integrable and compute .
My Solution:
Given that ,  a.e. which implies that  and since  is bounded with 
. Thus . QED
Let  be a Lebesgue measurable set with . Prove there exists aLebesgue measurable set  with .
My Solution:
. This implies that . Pick a sufficiently large  such that 
. Consider  for . Since  is continuous with  and , there exists 
 such that  by the Intermediate Value Theorem. Thus  is a Lebesgue measurable set with 
. QED
Let  be a measure space. If  is a sequence of functions suchthat  converges, then prove that  almost everywhere.
My Solution:
by the M.C.T. since  is increasing. Thus  almost everywhere because it’s integrable when  approaches . Hence  almost everywhere. QED
Prove that  if  and  if  is continuous but
not absolutely continuous on .
My Solution:
Consider , which is constructed of functions that are continuous everywhere on their domains. So it is continuous on  excluding 
. To show continuity at , consider that  which implies that  with 
 Hence by the squeeze theorem, .
f∈ ([0,1]) ⟹f∈ ([0,1])L∞ L1 f∈L∞ f≤m=essup(f)|f|≤ m=m<∞∫[0,1] ∫[0,1] f∈L1
f∈ ([0,1])L∞ f∈ ([0,1])Lp 1≤p≤∞ ∫|f = |f + |f|p ∫{|f|<1} |p ∫{|f|≥1} |p
p>1 |f < |f|<∞∫{|f|<1} |p ∫{|f|<1} f∈L1
|f ≤ = ⋅m({|f|≥1})<∞∫{|f|≥1} |p ∫{|f|≥1}mp mp ∫|f <∞|p f∈Lp
limsup||f||≤||f||∞ |f|≤||f||∞ |f ≤||f||p |p∞( |f ≤( ||f| =||f| <∞∫[0,1] |p)1/p ∫[0,1] |p∞)1/p |∞ limsup||f| ≤||f||p |∞
||f| ≤lim inf||f||∞ |p t∈[0,m=||f| )|∞ ∫|f|= |f|+ |f|∫{|f|<t} ∫{|f|≥t}
∫|f ≥ |f ≥|p ∫{|f|<1} |p ∫{|t|<1}tp (∫|f ≥( =t⋅m({|f|<t}|p)(1/p) ∫{|f|<t}tp)1/p )1/p
lim inf||f| ≥lim inft⋅m({|f|<t} =t⋅1|p )1/p lim inf||f| ≥t|p t∈[0,||f| )|∞limsup||f| ≤||f| ≤lim inf||f||p |∞ |p
C⊂R (x)=1χC x∈C 0χC (x)dx∫10χC
m(C)=0 (x)=0χC ∫ =0χC (x)χC
m({x| f(x)≠f(a)})=m(C)=0limx→a Rf=∫f=0
E⊂R m(E)=1F⊂E m(F)=12
E= E∩[n,n+1]⋃∞n=1 m(E)= m(E∩[−n,n])=1limn→∞ n∈Nm(E∩[−n,n])>12 f(x)=∫x−nχE x∈[−n,n] f f(−n)=0 f(n)>12c∈[−n,n] f(c)=12 (−n,n)∩Em((−n,c)∩E)=12
(X,A,μ) :X→Rfn| |dμ∑∞n=1∫Xfn →0fn
| |dμ= | |dμ= | |dμ∑
n=1
∞
∫Xfn limk→∞∑
n=1
k
∫Xfn limk→∞∫X∑
n=1
k
fn
= | |dμ= | |dμ<∞∫Xlimk→∞∑
n=1
k
fn ∫X∑
n=1
∞
fn
| |∑ki=1fn | |→0fn n ∞→0fn
f(x)=0x=0 f(x)= cos( )x2 1x2 x≠0[−1,1]
cos( )x2 1x2 R
{0} x=0 −1≤cos( )≤11x2 − ≤ cos( )≤x2 x2 1x2 x2
− = =0limx→0 x2 limx→0x2 cos( )=f(0)=0limx→0x2 1x2

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 10/27
Suppose  is absolutely continuous on . Hence it is of bounded-variation on , thus . Consider the partition with
endpoints
Hence for ,
because  is even and  is odd. The above sum is equal to  which diverges because it’s a harmonic series. Thus 
. This is a contradiction to the assumption of  being absolutely continuous, thus we have proven the desired result. QED
Let  be a finite measure space. If  is -measurable and for all , then prove that  exists and .
My Solution:
Since  is finite, and , . This implies that .
Now, we must show that  is integrable. Consider . Hence . This implies that 
. Hence  is integrable. QED
Suppose that  and that . Prove that if  in 
and  in , then  in .
My Solution:
It is sufficient to show that the . Well,
by Holder’s Inequality where . Thus  and . So the above limit does in fact
imply that  in . QED
Evaluate . Justify your computations.
My Solution:
Here we will use Leibniz’s integral rule, stating that
Thus we find that
where . QED
If  and , then prove that .
My Solution:
f [−1,1] [−1,1] [0,1]<∞Vf
P={−1}∪[{± :n∈N}∩[−1,1]]∪{1}1nπ
−−−√
, ∈Pxixi+1
|f( )−f( )|= f( )−f( )∑
n=1
∞
xi xi+1 ∑
n=1
∞∣
∣∣∣ 1nπ
−−−√ 1(n+1)π
− −−−−−−−√ ∣
∣∣∣
= ⋅cos − ⋅cos∑
n=1
∞∣
∣
∣∣∣
⎡
⎣
⎢⎢( )1nπ
−−−√
2 ⎛
⎝
⎜⎜ 1
1(n+1)π
− −−−−√ 2
⎞
⎠
⎟⎟
⎤
⎦
⎥⎥
⎡
⎣
⎢⎢( )1(n+1)π
− −−−−−−−√
2 ⎛
⎝
⎜⎜ 1
1(n+1)π
− −−−−√ 2
⎞
⎠
⎟⎟
⎤
⎦
⎥⎥
∣
∣
∣∣∣
= ( cos(nπ))−( cos((n+1)π))= −∑
n=1
∞∣∣∣ 1nπ 1(n+1)π ∣∣∣ ∑
n=1
∞∣∣∣ 1nπ −1(n+1)π∣∣∣
n n+1 1π∑∞n=1∣∣2n+1+nn2 ∣∣[0,1]≮∞Vf f
(X,A,μ) f μ p≤f(x)≤qx∈X fdμ∫X pμ(X)≤ fdμ≤qμ(X)∫X
X p≤f≤qμ(X)= 1dμ∫X p⋅μ(X)≤ fdμ≤qμ(X)∫X
fdμ∫X |f|≤max{|p|,|q|}=M |f|≤M|f|dμ≤μ(X)⋅M<∞∫X f
1<q,p<∞ + =11p 1q →ffn (R)Lp
→ggn (R)Lq →fgfngn (R)L1
|| −fg| =0limn→∞fngn |1
|| −fg| = || − g| +|| g−fg|limn→∞fngn |1 limn→∞fngn fn |1 fn |1
≤ || | || −g| +||g| || −f|limn→∞fn|pgn |q |qfn |p
|| | →||f| <∞limn→∞fn|p |p || −g| →0gn |q || −f| →0fn |p
→fgfngn (R)L1
dxddt∫10 sin(xt)x
( f(x,t)dx)= f(x,t)dxddt ∫
b
a ∫
b
a
∂∂t
dx= x⋅ dx= cos(xt)dx=ddt∫
1
0
sin(xt)x ∫
1
0
cos(xt)x ∫
1
0
sin(t)t
t>0
f∈ (R)∩ (R)L1 L∞ p≥1 f∈ (R)Lp

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 11/27
Given . This implies that  and . So,
For , . Thus
where  and  thus the entire equation is less than . So 
 for all . Thus . QED
If  is measurable, then .
My Solution:
Since  is positive,  is a sequence of increasing positive functions. Thus
with the step of moving the limit inside the integral is by the Monotone Convergence Theorem. QED
January 2013
Show that every dense subset of  is uncountable.
My Solution:
Let . Then for any  such that . So,
Without loss of generality, , then  on  respectively. This is where we get the above
equality, as
Consider  which is an uncountable collection of disjoint balls. And given any dense set  has elements in each
ball by definition of density. Thus  is uncountable. QED
Let  be a Lebesgue measurable function on  with the property that . Prove that  and .
My Solution:
For every , let
and let . Also define the linear functional  such that
Clearly  is a bounded functional in , since, by Holder’s inequality,
Since
we can thus conclude that . Moreover,  increases to  as . So
f∈ (R)∩ (R)L1 L∞ m=essup(f)<∞ ∫|f|<∞
∫|f = |f + |f|p ∫{x:|f|<1} |p ∫{x:|f|>1} |p
p>0 |f < |f|∫{x:|f(x)<1} |p ∫{x:|f(x)<1}
|f + |f ≤ |f|+∫{x:|f|<1} |p ∫{x:|f|>1} |p ∫{x:|f|<1} ∫{x:|f|>1}mp
|f|<∞∫{x:|f|<1} = ⋅m({x:|f(x)>1})<∞∫{x:|f|>1}mp mp ∞
(∫|f <∞|p)1/p p f∈Lp
f:R→[0,∞) f= flimn→∞∫n−n ∫R
f f⋅χ[−n,n]
∫f⋅ =∫ f⋅ = flimn→∞ χ[−n,n] limn→∞ χ[−n,n] ∫R
([0,1])L∞
A={ :t∈(0,1)}χ(0,t) , ∈Aχ(0, )t1 χ(0, )t2 ≠t1 t2
|| − | =1χ(0, )t1 χ(0, )t2 |∞
<t1 t2 − =0,1,0χ(0, )t1 χ(0, )t2 (0, ),( , ),( ,1)t1 t1t2 t2
= (x)− (x) =1−∥∥χ(0, )t2 χ(0, )t1∥∥∞ supx∈[0,1]∣∣χ(0, )t2 χ(0, )t1 ∣∣
{ }B( , )χ(0,t) 13
S⊂ ([0,1])L∞
S
f R|fg|dλ≤1sup{g∈ (R):||g| ≤1}L2 |2 ∫R f∈ (R)L2 ||f| ≤1|2
n∈N
={x∈[−n,n]:|f(x)|≤n}An
=ffn χAn : →RTn L2
(g)= gTn ∫Rfn
Tn L2
| (g)|≤ | g|≤|| | ||g|Tn ∫Rfn fn|2 |2
| ( )|= = =|| |Tnfn ∣∣∣∫Rf2χAn
∣∣∣ ∫Rf2n fn|22
|| ||=|| |Tn fn|2 | g|fn |fg| n→∞

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 12/27
By the uniform boundedness principle, we can conclude that the sequence  converges to a bounded linear functional  and that
On the other hand, by the monotone convergence theorem,
hence . Finally, taking  in the assumption, we find that
Thus we have proven the desired result. QED
Let  and  for all . If  for all 
, then there is a set  such that  a.e.
My Solution:
We know  for all . Suppose . Pick  such that . Then
since .
Consider , which we claim is equal to zero. To prove this, pick . Then
as . Hence  or  almost everywhere. If we use this to define , then  almost everywhere. QED
If  is a measurable subset of , then there is an interval  such that  or .
My Solution:
Suppose not! Then for all ,  and . Suppose  has finite measure and let .
Then
Thus for all covers of , . But, by definition
Hence
Now for  with any measure,
Hence  for all  where
| (g)|≤ |fg|<∞supn Tn ∫R
( )Tn T
||T||≤ || ||<∞lim infn Tn
|| ||= || | =lim infn Tn lim infn fn|2 ( |f )∫R |2 1/2
f∈L2 g=f||f||2
|fg|=||f| ≤1∫R |2
f≥0 f∈ [0,1]Lp p∈[1,∞) ||f| =||f||pp |1p∈[1,∞) S f=χS
||f| =∫|f|1 |p p∈[1,∞) m({x|f>1})≠0 ϵ∈(1,∞) 1<ϵ≤f<∞
||f| =∫|f ≥ |f ≥∫ →∞|1 |p ∫{1<|f|} |p ϵp
ϵ>1
m({x|0<f<1}) 0<|f|≤ϵ<1
||f| =∫|f ≤ →0|1 |p ∫{0<|f|≤ϵ<1}ϵp
p→∞ f=0 1 S={x|f(x)=1} f=χS
E R Im(E∩I)> m(I)910 m( ∩I)> m(I)Ec 910
Im(E∩I)≤ m(I)910 m( ∩I)≤ m(I)Ec 910 E E⊂⋃∞n=1In
m(E)=m(E∩ )=m( E∩ )≤ m(E∩ )≤ m( )⋃
n=1
∞
In ⋃
n=1
∞
In ∑
n=1
∞
In 910∑
n=1
∞
In
Em(E)≤ m( )910∑∞n=1 In
m(E)=inf{ m( ):E⊂ }∑n In ⋃
n=1
∞
In
m(E)≤ m(E) ⟹m(E)=0910
E
m(E∩(−n,n)∩ )≤m(E∩ )≤ m( )In In 9n In
m(E∩(−n,n))=0 n
m(E)=m( (E∩(−n,n)))≤ m(E∩(−n,n))=0⋃
n=1
∞
∑
n=1
∞

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 13/27
Note the same proof works for . Thus the desired result is proven. QED
A measure space  is -finite iff there is an  such that .
My Solution:
Assume that  such that . Then
where
since  and by Chebyshev’s Inequality.
Now assume  is -finite. We have , a union of disjoint sets with . Define  where 
 when  and  when . Then
Thus proving the desired result. QED
(a) Find a sequence  such that  for all  and  for all . (b) If the  are as in part (a), then prove 
.
My Solution:
a. 
b. Given  as defined above, we can simply integrate to get this answer. So, given  defined as in part (a),
Thus
QED
Show that  is open in . (Assume has the uniform metric.)
My Solution:
The function  is continuous. Thus  must be open. QED
m( )=0Ec
(X,μ) σ f:X→(0,∞)f∈ (X,μ)L1
f:X→(0,∞) f∈ (X,μ)L1
X={f>0}= {f> }⋃
n=1
∞ 1n
μ({f> })≤∫ dμ≤n⋅∫|f|<∞1n |f|
1(1/n)
f∈L1
Xσ X=⋃∞i=1An μ( <∞)An f=∑∞n=1an
= ⋅an 1μ( )⋅Ann2 χAn μ( )>0An =an 1n2χAn μ( )=0An
∫f= ∫ ⋅ = ∫ = <∞∑
n=1
∞ 1μ( )⋅An n2 χAn ∑
n=1
∞ 1μ( )⋅An n2 χAn ∑
n=1
∞ 1n2
:[0,1]→Rfn | (x)|=2∫10fn n∈N(x)=1limn→∞fn x∈[0,1] fn
| (x)−1|dx=1limn→∞∫10fn
(x):=4 x+1 for x∈[0, ]fn n2 12n
(x):=−4 x+1+4n for x∈[ ,]and f(x)=1 otherwise.fn n2 12n 1n
fn fn
(x)−1=4 x for x∈[0, ]fn n2 12n
(x)−1=−4 x+4n for x∈[ , ]and f(x)=0 otherwise.fn n2 12n 1n
| −1|dx= [ 4 xdx+ (−4 x+4n)dx]limn→∞∫
1
0 fn limn→∞∫
1/2n
0 n2 ∫
1/n
1/2n n2
= [ −0− + + − ]= 1=1limn→∞
2n2
4n2
2n2
n2
4nn 2n2
4n2
4n2n limn→∞
G={f∈C[0,1]: >1}∫10f2 C[0,1] C[0,1]
ϕ(f)=∫10f2 ((1,∞))ϕ−1

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 14/27
Let  be a metric space and suppose  and  are nonempty disjoint subsetsof  with  compact and  closed. (a) Prove there is a  such that  for all  and . (b) Show that part (a) may fail if  is closed,but not compact.
My Solution:
a. By way of contradiction, assume for every  we can find an  and  such that . Since  is compact,
there is a convergent subsequence  whose limit is . By the triangle inequality, . If wejuggle the ’s around a bit, we find that  giving us a contradiction, thus we have proven the desired result. The problem here isthat this question is not written that well in regards to our qualifying exam, so for the most part this one should be ignored. It leaves outimportant details of what exactly  is. However, if you would like to check out other solutions on this, follow these links:
[https://math.stackexchange.com/questions/185656/show-that-exists-delta-0-such-thatdx-y-geq-delta(https://math.stackexchange.com/questions/185656/show-that-exists-delta-0-such-thatdx-y-geq-delta)]
[http://www.math.ucsd.edu/~benchow/F16/HW7-140A-F16-ans.pdf (http://www.math.ucsd.edu/~benchow/F16/HW7-140A-F16-ans.pdf)] (check#8)
b. Consider an example in  with the standard metric. Take  as the -axis and  as the graph of the exponential function , that is, 
. These are clearly non-empty and mutually disjoint. Both  and  are closed, but neither is compactbecause they are both unbounded. It is easy then to see that their distance is zero and a strictly positive  of the desired result does notexist. Thus we can see then that if  is not compact and still closed that our proof in part (a) may not hold.
The limit superior of a sequence of sets  is defined as . Let  be a sequence of sets in . (a)
Prove that if , then . (b) Is it true ingeneral that ?
My Solution:
(a): Let . Given , there exists  such that .
Hence
which implies that . QED
(b): Consider the sequence of functions: 
, and so on. Then 
 but for all , . This implies that . Thus it may not be true that . QED
Show that  where  and  where  is in 
, but  where  and  where  isnot.
My Solution:
Because , it is sufficient to show this is true for  as  follows from it. Well,
Then if we let  and , then
(X,ρ) K FX K F δ>0ρ(x,y)≥δ x∈K y∈F K
n ∈Kxn ∈Fyn ρ( , )<xnyn 1n Kxnk x ρ(x, )≤ρ(x, )+ρ( , )ynk xnk xnkynk
ϵ x∈F
ρ
R2 K x F ex
F={(x,y)∈ |y= }R2 ex K F δK
{ }Eklimsup =Ek ⋂∞j=1⋃∞k=jEk { :k∈N}Ek Lλ( )<∞∑k∈N Ek λ(limsup( ))=0Ekλ(limsup( ))=limsupλ( )Ek Ek
ϵ>0 m( )<∞∑∞k=1 Ek N m( )<ϵ∑∞k=N Ek
limsup( )= ⊂Ek ⋂
n=1
∞
⋃
k=n
∞
Ek ⋃
k=N
∞
Ek
m(limsup( ))≤m( )≤ m( )<ϵEk ⋃
k=N
∞
Ek ∑
k=N
∞
Ek
m(limsup( ))=0Ek
=[0,1], =[0, ], =[ ,1], =[0, ], =[ , ], =[ , ], =[ ,1]E1 E2 12 E3 12 E4 14 E5 14 12 E6 12 34 E7 34m( )=0limn→∞ Ek n∈N =[0,1]⋃∞k=nEk lim sup( )=[0,1]Enλ(limsup( ))=limsupλ( )Ek Ek
f(x)= sin()x2 1x x≠0 f(x)=0 x=0BV[−1,1] g(x)= sin()x2 1x2 x≠0 g(x)=0 x=0
f(−x)=−f(x) (0,1) (−1,0)
T.V.(f)= | (x)|dx= dx∫
1
0 f′ ∫
1
0
cos()−2xsin()ln(x)∣∣ 1x 1x ∣∣
1x2
u=1x du=ln(x)dx
T.V.(f)= du≤ =1<∞∫
∞
1
cos(u)− sin(u)∣∣ 2u ∣∣u2 ∫
∞
1
duu2

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 15/27
Thus the total variation is finite, thus proving that  is of bounded variation.
Now we must show that  is not of bounded variation.
Well, let
. Hence for ,
Notice that this is a harmonic series, thus it diverges, implying that , thus it cannot be of bounded variation. QED
Extra Problems
Let  be an outer measure on a set . Prove that if  is a sequence of subsetsof  and , then 
My Solution:
Since , for any  there exists an  such that  from sub-additivity. Thus
But by monotonicity,
Since  is arbitrary, we see that . QED
Let  be a measure space and let  be measurable. Provethat  is measurable.
My Solution:
Let  and note that for ,  which is in . So assume , and note that  is equivalent to 
. But since  this is also a measurable set. QED
Let  and  be finite measures on a measurable space  with the propertythat  for all . Prove that  for everybounded measurable function .
My Solution:
Let  be a simple non-negative measurable function. Then
QED
f(x)
g(x)
P={−1}∪[{± :n∈N}∩[−1,1]]∪{1}1nπ
−−−√
, ∈Pxnxn+1
|f( )−f( )|= f( )−f( )∑
n=1
∞
xn xn+1 ∑
n=1
∞∣
∣∣∣ 1nπ
−−−√ 1(n+1)π
− −−−−−−−√ ∣
∣∣∣
= ( sin(nπ)− sin(nπ+π))∑
n=1
∞∣∣∣ 1nπ 1nπ+π ∣∣∣
= ( + )sin(nπ) ≤∑
n=1
∞∣∣∣ 1(n+1)π 1nπ ∣∣∣ 1π∑
n=1
∞∣∣∣2n+1+nn2
∣∣∣
[0,1]≮∞Vg
μ∗ X { }EkX ( )<∞∑∞k=1μ∗Ek ( )=0μ∗⋂∞k=1⋃∞n=kEn
( )<∞∑∞k=1μ∗Ek ϵ>0 N ( )<ϵ∑∞k=Nμ∗Ek
( )≤ ( )<ϵμ∗ ⋃
n=N
∞
En ∑
k=N
∞
μ∗Ek
( )≤ ( )<ϵμ∗ ⋂
k=1
∞
⋃
n=k
∞
En μ∗ ⋃
n=N
∞
En
ϵ ( )=0μ∗⋂∞k=1⋃∞n=kEn
(X,A,μ) f:X→(0,∞)1/f
g=1f a≤0{g>a}=X A a>0 {g>a}
{0<f< }1a ∈R1a
μn μ (X,A)(A)→μ(A)μn A∈A fd → fdμ∫X μn ∫Xf:X→R
f
fd = (x)d = ( )= μ( )= fdμlimn→∞∫X μn limn→∞∫X∑
i=1
L
aiχAi μn limn→∞∑
i=1
L
aiμnAi ∑
i=1
L
ai Ai ∫X

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 16/27
Suppose that  with Lebesgue measure. Prove that .
My Solution:
We note that  for . Since , we may apply the DCT with  as the majorant. Thus
. QED
Let  and  be finite (positive) measures on a measurable space . Define . Prove that  for every set .
My Solution:
Let  and  be a Hahn decomposition with respect to . So
But . Since all of these terms are non-negative and finite by
comparisons of signs, we can clearly see that  for all . QED
Let  be a normed vector space and let  be linear. Define what is meantby  and prove that  if and only if  is continuous.
My Solution:
First off, .
Now we just need to prove that  implies continuity, or that if it’s not continuous that . Let  be such that thereexists  such that in any  there exists  such that
This implies that . Take . Clearly,  is unbounded here.
Now to prove that continuous implies bounded. Let , then there exists a  such that  so that . We
see  for all . Since any  can be expressed as , we then see our desired result, that 
. QED
Important Notes
Undergrad
For reference, these notes are gathered from the book Real Analysis; A First Course by Russell A. Gordon. These notes consist of basic realanalysis ideas based off of my past undergraduate class taught by Dr. Christine Leverenz at Georgetown College.
Gordon Chapter 1 (Real Numbers)
A field is a nonempty set  of objects that has two operations defined on it. These operations are usually defined as addition andmultiplication. These operations follow a set of properties which will not be listed here as you should know them.
Triangle Inequality: . It follows from this that 
If  and  are real numbers, then
Cauchy-Schwarz Inequality: Let  be a positive integer. If  and  are real numbers, then
Equality occurs iff there is a constant  such that  for all integers 
f∈ (R)L1
fdm=0limn→∞12n∫n−n
f(x) (x) ≤|f(x)|∣∣ 12n χ{|x|≤n} ∣∣ x∈R f∈L1 |f(x)|
f(x) dm= dm= 0dm=0limn→∞∫R
12n χ{|x|≤n} ∫Rlimn→∞
f(x)2nχ{|x|≤n} ∫R
μ ν (X,A)ρ=μ−ν |ρ|(E)≤μ(E)+ν(E) E∈A
Pρ Nρ ρ
|ρ|(A)=ρ(A∩ )−ρ(A∩ )=μ(A∩ )−ν(A∩ )−μ(A∩ )+ν(A∩ )Pρ Nρ Pρ Pρ Nρ Nρ
μ(A)+ν(A)=μ(A∩ )+ν(A∩ )+μ(A∩ )+ν(A∩ )Pρ Pρ Nρ Nρ|ρ|(E)≤μ(E)+ν(E) E∈A
V L:V→R||L|| ||L||<∞ L
||L||= {|L(V)|}sup||V||≤1
||L||<∞ ||L||=∞ X∈Vϵ>0 B(x, )rn yn
|L(x)−L( )|=|L(x− )|>ϵyn yn
||L||≥ϵrn =r′n ()12n ||L||
ϵ>0 δ>0 y∈B(x,δ) |L(x)−L(y)|<ϵ
L( )<∣∣ x−yδ ∣∣ ϵδ y∈B(x,δ) v∈B(0,1) x−yδ
|L(v)|<sup||v||≤1 ϵδ
F
|a+b|≤|a|+|b| ||a|−|b||≤|a−b|
a≠0 r≠1
a+ar+a +a +...+a =a⋅r2 r3 rn 1−rn+1
1−r
n , ,...,a1a2 an , ,...,b1b2 bn
≤( )( )( )∑
k=1
n
akbk
2
∑
k=1
n
a2k ∑
k=1
n
b2k
c =cak bk k

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 17/27
The set  is bounded if there is a number  such that  for all . The number  is called a bound for S.
Suppose that  is bounded above. A number  is the supremum of  if  is an upper bound of  and any number less than  is not anupper bound of . We write 
Suppose that  is bounded below. A number  is the infimum of  if  is an lower bound of  and any number greater than  is not anlower bound of . We write 
Archimedean Property of the Real Numbers: If  and  are positive real numbers, then there exists a positive integer  such that .
Between any two distinct real numbers, there exists a rational and an irrational number.
A countable union of countable sets is countable.
Let  be an interval and  be a function such that , and let  be a subinterval of . The function  is increasing on  if  for all  such that ; and strictly increasing on  if  for all  such that . Thefunction  is decreasing on  if  for all  that satisfy ; and strictly decreasing on  if  forall  such that . The function  is monotone on  if it is either increasing or decreasing on  and strictly monotone on  if it is either strictly increasing or decreasing on .
Gordon Chapter 2 (Sequences)
A sequence is a function whose domain is the set of positive integers. A sequence of real numbers is a sequence whose codomain isthe set . Although a sequence is a function, the standard notation for a sequence of real numbers is  where the subscript denotes the index of the sequence.
A sequence  converges to a number  if for all  there exists a positive integer  such that  for all .The sequence is convergent if there exists a number  that the sequence converges to, otherwise it is divergent.
The limit of a convergent sequence is unique.
Suppose that  converges to  and  converges to . Then:
— 
— 
— 
A monotone sequence converges iff it is bounded
A sequence  is a Cauchy Sequence if for all  there exists a positive integer  such that  for all .
A sequence of real numbers converges iff it is a Cauchy sequence
Let  be a sequence and let  be a strictly increasing sequence of positive integers. The sequence  is called a
subsequence of 
If a sequence  converges to , then every subsequence must converge to  as well.
Bolzano-Weierstrass Theorem: Every bounded sequence has a convergent subsequence.
Gordon Chapter 3 (Limits and Continuity)
Let  be an open interval that contains the point  and suppose that  is a function that is defined on  except possibly at . The function has limit  at point  if for all  there exists  such that  for all  such that . We thenwrite .
We have linearity for limits.
Let  be an interval and , and let . The function  is continuous at  if for each  there exists a  such that  for all  such that . The function is continuous on  if  is continuous on every point of .
Intermediate Value Theorem: Suppose that  is continuous on . If  is a number between  and , thenthere is a point  such that .
Extreme Value Theorem: If  is continuous on , then there exist points  and  in  such that  for all .
Let  be an interval. A function  is uniformly continuous on  if for each  there exists a  such that  for all  such that .
If  is continuous on , then  is uniformly continuous on .
A partition  of an interval  is a finite set of points  such that
S M |x|≤M x∈S M
S β Sβ S βS β=sup(S)
S α Sα S αS α=inf(S)
a b nna>b
I f f:I→R J I f Jf(x)≤f(y) x,y∈J x<y Jf(x)<f(y) x,y∈J x<yf Jf(x)≥f(y) x,y∈J x<y Jf(x)>f(y)x,y∈J x<y f J JJ J
R { }xn n
{ }xn L ϵ>0 N | −L|<ϵxn n≥NL
{ }an a { }bn b
{c }→caan
{ ± }→a±ban bn
{ }→abanbn
{ }xn ϵ>0 N | − |<ϵxm xnm,n≥N
{ }xn { }pn { }xpn
{ }xn
{ }xn L L
I c f I cf L c ϵ>0 δ>0 |f(x)−L|<ϵ x∈I |x−c|<δf(x)=Llimx→c
I f:I→R c∈I f c ϵ>0 δ>0|f(x)−f(c)|<ϵ x∈I |x−c|<δ If I
f:[a,b]→R [a,b] v f(a) f(b)c∈(a,b) f(c)=v
f:[a,b]→R [a,b] c d [a,b]f(c)≤f(x)≤f(d) x∈[a,b]
I f:I→R I ϵ>0 δ>0|f(y)−f(x)|<ϵ x,y∈I |y−x|<δ
f:[a,b]→R [a,b] f [a,b]
P [c,d] { |0≤i≤n}xi
c= < < <...< < =dx0 x1 x2 xn−1 xn

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 18/27
Let  be a function and let  be any closed subinterval of . The variation of  on  is defined by 
. Note that the integer  is not fixed; the supremum is over all possible partitions of . The function  is of bounded variation on  if  is finite.
Gordon Chapter 4 (Differentiation)
Let  be an interval, let , and let . The function  id differentiable at  provided that the limit
exists. The derivative of  at  is the value of the aforementioned limit denoted by .
Rolle’s Theorem: Let  be continuous on  and differentiable on . If , then there exists a point  such that .
Mean Value Theorem: If  is continuous on  and differentiable on , then there exists a point  suchthat
Gordon Chapter 5 (Integration)
A tagged partition  of an interval  consists of a partition  of  along with a set  ofpoints, known as tags, that satisfy  for .
Let  and let  be a tagged partition of . The Riemann sum  of 
associated with  is defined by
A function  is Riemann integrable on  if there exists a number  with the following property: for all  there
exists  such that  for all tagged partitions  of  that satisfy . The number  is called theRiemann integral of  on .
Cauchy Criterion for Riemann Integrability: A bounded function  is Riemann integrable on  iff for each  there exists 
 such that  for all tagged partitions  and  of  with norms less than .
Fundamental Theorem of Calculus is a thing
Integration by Parts:
Gordon Chapter 6 (Infinite Series)
A power series is an expression of the form
where the ’s are constants
A Fourier series is an expression of the form
where the ’s and ’s are constants
An infinite series of real numbers is an expression of the form
A partial sum of an infinite series is represented by 
An infinite series converges if its corresponding sequence  of partial sums converges. If  is the limit of the previous sequence,then we say the series converges to . If the sequence does not converge, we say that the series diverges.
If the series  converges, then the sequence  converges to zero.
f:[a,b]→R [c,d] [a,b] f [c,d]V(f,[c,d])=sup{ |f( )−f( )|}∑ni=1 xi xi−1 n[c,d] f [c,d] V(f,[c,d])
I f:I→R c∈I f c
limv→c
f(v)−f(c)v−c
f c (c)f′
f:[a,b]→R [a,b] (a,b) f(a)=f(b)c∈(a,b) (c)=0f′
f:[a,b]→R [a,b] (a,b) c∈(a,b)
(c)=f′ f(b)−f(a)b−a
Pt [a,b] P={ |0≤i≤n}xi [a,b] { |1≤i≤n}ti≤ ≤xi−1 ti xi 1≤i≤n
f:[a,b]→R P={( ,[ , ])|1≤i≤n}t ti xi−1xi [a,b] S(fP),t fPt
S(fP)= f( )( − ),t ∑
i=1
n
ti xi xi−1
f:[a,b]→R [a,b] L ϵ>0δ>0 |S(fP)−L|<ϵ,t Pt [a,b] |P||<δ|t Lf [a,b]
f [a,b] ϵ>0δ>0 |S(f )−S(f )|<ϵ,tP1 ,tP2 tP1 tP2 [a,b] δ
g=f(b)g(b)−f(a)g(a)− f∫
b
af′ ∫
b
ag′
+ x+ + +...a0 a1 a2x2 a3x3
ak
+ cos(x)+ sin(x)+ cos(2x)+ sin(2x)+...a0 a1 b1 a2 b2
ak bk
= + +...∑
k=1
∞
ak a1 a2
∑nk=1ak
{ }sn SS
∑∞k=1ak { }ak

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 19/27
The series  converges iff for all  there exists a positive integer  such that  for all positive integers 
 and  that satisfy 
A series with nonnegative terms converges iff its sequence of partial sums is bounded
Linearity is preserved
Geometric Series: Suppose that . The geometric series  converges if  and diverges if . If ,
The -series  converges if  and diverges if .
Let  be a series of real numbers. If the series  converges, then so does .
Rearrangement stuff is cool, but unnecessary for this study guide.
Gordon Chapter 7 (Sequences and Series of Functions)
Let  be a sequence of functions defined on an interval  and let  be a function defined on . The sequence  convergespointwise to  on  if the sequence  converges to  for each . In other words,  for all .
Let  be a sequence of functions defined on an interval  and let  be a function defined on . The series  converges
pointwise to  on  if the sequence  of partial sums converges pointwise to  on .
Let  be a sequence of functions defined on an interval  and let  be a function defined on . The sequence  convergesuniformly to  on  if for all  there exists a positive integer  such that  for all  and for all .
A lot more information is here, may add later. I just don’t think it will help much for the Qual
Gordon Chapter 8 (Point-Set Topology)
A point  is an interior point of  if there exists a positive number  such that 
A point  is an isolated point of  if there exists a positive number  such that 
A point  is a limit point of  if for each positive number , the set  contains a point of  other than 
The set  is open if all of its points are interior points
The set  is closed if it contains all of its limit points
Every open interval is an open set and every closed interval is a closed set
Let  be a set of real numbers. A collection  of sets is an open cover of  if each set in  is open and  is contained in the union ofall the sets in . The open cover  has a finite subcover if  is contained in the union of a finite number of sets in 
A set  is compact if every open cover of  has a finite subcover
A compact set is closed and bounded
A closed subset of a compact set is compact
A set of real numbers is compact iff it is closed and bounded
More is in this section. Possibly going to add more, but I don’t find it necessary for the Qual.
Graduate Notes/Royden Book
Royden Chapter 1 (Sets, Sequences, and Functions)
A nonempty set  of real numbers is said to be bounded above provided that there is a real number  such that  for all .  is known as an upper bound for . We define bounded below similarly.
The Completeness Axiom: Let  be a nonempty set of real numbers that is bounded above. Then among the set of upper bounds for  there is a smallest, or least, upper bound.
The least upper bound of  is called the supremum of  and denoted by . We define the infimum similarly as the greatest lowerbound and denote it by .
Triangle Inequality:
A set  of real numbers is said to be inductive provided it contains  and if the number , the number  as well.
Every nonempty set of natural numbers has a smallest member.
∑∞k=1ak ϵ>0 N | |<ϵ∑nk=m+1akm n n>m≥N
a≠0 a∑∞k=0rk |r|<1 |r|≥1 |r|<1
a =∑
k=0
∞
rk a1−r
p ∑∞k=1 1kp p>1 p≤1
∑∞k=1ak | |∑∞k=1ak ∑∞k=1ak
{ }fn I f I { }fnf I { (x)}fn f(x) x∈I f(x)= (x)limn→∞fnx∈I
{ }fk I f I ∑∞k=1fkf I { }={ }sn ∑nk=1fk f I
{ }fn I f I { }fnf I ϵ>0 N | (x)−f(x)|<ϵfn x∈I n≥N
x E r (x−r,x+r)⊆E
x E r (x−r,x+r)∩E={x}
x E r (x−r,x+r)∩E E x
E
E
E G E G EG G E G
E E
E b x≤b x∈Eb E
EE
E E supEinfE
|a+b|≤|a|+|b|
E 1 x∈E x+1∈E

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 20/27
Archimedean Property: For each pair of positive real numbers  and , there is a natural number  for which .
A set  of real numbers is said to be dense in  provided between any two real numbers there lies a member of .
The rational numbers are dense in .
A set  is said to be finite provided either it is empty or there is a natural number  such that  is equipotent to .
We say that  is countably infinite provided  is equipotent to the set  (the natural numbers). A set that is either finite or countablyfinite is said to be countable. A set that is not countable is uncountable.
A subset of a countable set is countable.
A nonempty set is countable iff it is the image of a function whose domain is a nonempty countable set.
The union of countable sets is countable.
A set  of real numbers is called open provided for each , there is a  for which the interval  is contained in.
The set of real numbers and the empty set are open; the intersection of any finite collection of open sets is open; and the union of anycollection of open sets is open.
Every nonempty open set is the disjoint union of a countable collection of open intervals.
For a set  of real numbers, a real number  is called a point of closure of  provided every open interval that contains  alsocontains a point in . The collection of points of closure of  is called the closure of .
A set of real numbers is open iff its complement in  is closed.
A collection of sets  is said to be a cover of a set  provided . By a subcover of a cover of  we mean asubcollection of the cover that itself also is a cover of . If each set  in a cover is open, then we call  an open cover of .If the cover  contains only a finite number of sets, we call it a finite cover.
Let  be a closed and bounded set of real numbers. Then every open cover of  has a finite subcover.
We say that a countable collection of sets  is descending or nested provided that  for every natural number .
It is said to be ascending provided  for every natural number .
-algebra: Given a set , a collection  of subsets of  is called a -algebra provided
– the empty set belongs to 
– the complement in  of a set in  also belongs to 
– the union of a countable collection of sets in  also belongs to .
Let  be a collection of subsets of a set . Then the intersection  of all -algebras of subsets of  that contain  is a -algebra thatcontains . Moreover, it is the smallest -algebra of subsets  that contains  in the sense that any -algebra that contains  alsocontains .
The collection  of Borel sets of real numbers is the smallest -algebra of sets of real numbers that contains all of the open sets of realnumbers. (every open set is a Borel set)
Royden Chapter 2 (Lebesgue Measure)
The measure of an interval is its length. Each nonempty interval  is Lebesgue measurable and
Measure is translation invariant. If  is Lebesgue measurable and  is any number, then the translate of  by , , also is Lebesgue measurable and
Measure is countably additive over countable disjoint unions of sets. If  is a countable disjoint collection of Lebesgue
measurable sets, then
The outer measure of an interval is its length, it is translation invariant, however the outer measure is not finitely additive. Instead:
Let  be a nonempty interval of real numbers. For a set  of real numbers, consider the countable collections  of nonempty
open, bounded intervals that cover , that is, collections for which . We define the outer measure of , , to be
a b n na>b
E R E
R
E n E {1,2,3,...,n}
E E N
O x∈O r>0 (x−r,x+r)O
E x E xE E E
R
{Eλ}λ∈Λ E E⊆∪λ∈ΛEλ EE Eλ {Eλ}λ∈Λ E{Eλ}λ∈Λ
F F
{En}∞n=1 ⊆En+1 En n⊆En En+1 n
σ x A X σ
A
X A A
A A
F X A σ X F σF σ X F σ FA
B σ
I
m(I)=l(I)
E y E yE+y={x+y|x∈E}
m(E+y)=m(E)
{Ek}∞k=1
m( )= m( )⋃
k=1
∞
Ek ∑
k=1
∞
Ek
( )≤ ( )m∗ ⋃
k=1
∞
Ek ∑
k=1
∞
m∗Ek
I A {Ik}∞k=1A A⊆⋃∞k=1Ik A (A)m∗

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 21/27
A measure is monotone if for all , then .
A set  is said to be measurable provided for any set  that
Any set of outer measure zero is measurable. In particular, any countable set is measurable.
The union of a finite collection of measurable sets is measurable.
The union of a countable collection of measurable sets is measurable.
Every interval is measurable.
The collection  of measurable sets is a -algebra that contains the -algebra  of Borel sets. Each interval, each open set, eachclosed set, and each clopen set is measurable.
The translate of a measurable set is measurable.
If  is a measurable set of finite outer measure that is contained in , then
and
The restriction of the set function outer measure to the class of measurable sets is called Lebesgue Measure. It is denoted by , sothat if  is a measurable set, its Lebesgue measure will be , defined by
The Lebesgue measure defined on the -algebra of Lebesgue measurable sets assigns length to any interval, is translation invariant,and is countably additive.
The Continuity of Measure: Lebesgue measure possesses the following continuity properties:
a. If  is an ascending collection of measurable sets, then,
b. If  is a descending collection of measurable sets and , then
For a measurable set , we say that a property holds almost everywhere on , or it holds for almost all , provided there is asubset  of  for which  and the property holds for all  ~ .
Let  be a countable collection of measurable sets for which . Then almost all  belong to at most
finitely many of the ’s.
Let  be a bounded measurable set of real numbers. Suppose there is a bounded, countably infinite set of real numbers  for which thecollection of translates of , , is disjoint. Then 
Any set  of real numbers with positive outer measure contains a subset that fails to be measurable.
There are disjoint sets of real numbers  and  for which
The Cantor set  is a closed, uncountable set of measure zero
The Cantor-Lebesgue function  is an increasing continuous function that maps  onto . Its derivative exists on the open set , the complement in  of the Cantor set  on  while 
There is a measurable set, a subset of the Cantor set, that is not a Borel set.
Royden Chapter 3 (Lebesgue Measurable Functions)
Let the function  have a measurable domain . Then the following statements are equivalent:
i. For all , the set  is measurable
(A)=inf{ l( )|A⊆ }m∗ ∑
k=1
∞
Ik ⋃
k=1
∞
Ik
A⊆B (A)≤ (B)m∗ m∗
E A
(A)= (A∩E)+ (A∩ )m∗ m∗ m∗ EC
M σ σ B
A B
(B/A)= (B)− (A)m∗ m∗ m∗
(B)= (A)+ (B/A)m∗ m∗ m∗
mE m(E)
m(E)= (E)m∗
σ
{Ak}∞k=1
m( )= m( )⋃
k=1
∞
Ak limk→∞ Ak
{Bk}∞k=1 m( )<∞B1
m( )= m( )⋂
k=1
∞
Bk limk→∞ Bk
E E x∈EE0 E m( )=0E0 x∈EE0
{Ek}∞k=1 m( )<∞∑∞k=1 Ek x∈REk
E ΛE{λ+E}λ∈Λ m(E)=0
E
A B
(A∪B)< (A)+ (B)m∗ m∗ m∗
C
ϕ [0,1] [0,1]O [0,1] =0ϕ′ O m(O)=1
f E
c∈R {x∈E|f(x)>c}

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 22/27
ii. For all , the set  is measurable
iii. For all , the set  is measurable
iv. For all , the set  is measurable
An extended real-valued function  defined on  is said to be Lebesgue measurable, or simply measurable, provided its domain  ismeasurable and it satisfies one of the four above statements.
Let the function  be defined on a measurable set . Then  is measurable iff for all open sets , the inverse image of  under , , is measurable
A real valued function that is continuous on its measurable domain is measurable
A monotone function that is defined on an interval is measurable
Let  be an extended real-valued function . Then if  is measurable on  and  a.e. on , then  is measurable on . For ameasurable subset  of ,  is measurable on  iff the restrictions of  to  and ~  are measurable.
Let  and  be measurable functions on  that are finite a.e. on . For any  and ,  is measurable on  and  ismeasurable on .
Let  be a measurable real-valued function defined on  and  a continuous real-valued function on all of . Then the composition  is a measurable function on 
For a sequence  of functions with common domain , a function  on  and a subset  of , we say that the sequence converges to  pointwise on  provided  for all ; and the sequence  converges to  pointwisea.e. on  provided it converges to  pointwise on ~  where ; and the sequence  converges to  uniformly on provided for each , there is an index  for which  on  for all .
Let  be a sequence of measurable functions on  that converges pointwise a.e. on  to the function . Then  is measurable.
If  is any set, the characteristic function of , , is the function on  defined by
A real-valued function  defined on a measurable set  is called simple provided it is measurable and takes only a finite number ofvalues
Let  be a measurable real-valued function on . Assume  is bounded on , that is there exists an  for which  on .Then for all , there are simple functions  and  defined on  which have the following approximation properties on :
An extended real-valued function  on a measurable set  is measurable iff there is a sequence  of simple functions on  whichconverges pointwise on  to  and has the property that  on  for all . If  is nonnegative, we may choose  to beincreasing
Egoroff’s Theorem: Assume  has finite measure. Let  be a sequence of measurable functions on  that converges pointiwse on to the real-valued function . Then for all , there is a closed set  contained in  for which  uniformly on  and ~
Under the assumptions of Egoroff’s Thm, for all  and , there is a measurable subset  of  and an index  for which  on  for all  and ~ .
Let  be a simple function defined on . Then for each , there is a continuous function  on  and a closed set  contained in for which  on  and ~
Let  be a real-valued measurable function on . Then for all , there is a continuous function  on  and a closed set contained in  for which  on  and ~
Royden Chapter 4 (Integration)
The upper and lower sums for  with respect to a partition  are
where  is the infimum on the given partition, and  is the supremum
The lower and upper Riemann integrals of  over  are defined by (respectively)
c∈R {x∈E|f(x)≥c}
c∈R {x∈E|f(x)<c}
c∈R {x∈E|f(x)≤c}
f E E
f E f O O f(O)={x∈E|f(x)∈O}f−1
f E f E f=g E g EDEf E f D ED
f g E E α βαf+βg E fgE
g E f Rf∘g E
{ }fn E f E AE { }fnf A (x)=f(x)limn→∞fn x∈A { }fn fA f AB m(B)=0 { }fn f Aϵ>0 N |f− |<ϵfn A n≥N
{ }fn E E f f
A AχA R
={1|x∈A&0|x∉A}χA
ϕ E
f E f E M≥0 |f|≤M Eϵ>0 ϕϵ ψϵ E E
≤f≤ ;0≤ − <ϵϕϵ ψϵ ψϵ ϕϵ
f E { }ϕn EEf | |≤|f|ϕn E n f { }ϕn
E { }fn EE f ϵ>0 F E { }→ffn Fm(EF)<ϵ
ν>0 δ>0 AE N| −f|<νfn A n≥N m(EA)<δ
f E ϵ>0 g R F Ef=g F m(EF)<ϵ
f E ϵ>0 g R FE f=g F m(EF)<ϵ
f P
L(f,P)= ×( − )∑
i=1
n
mi xi xi−1
U(f,P)= ×( − )∑
i=1
n
Mi xi xi−1
mi Mi
f [a,b]
f=sup{L(f,P)}∫
b
a

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 23/27
where  is a partition of .
If the two above mentioned integrals are equal, then we say that  is Riemann integrable over .
For a simple function  defined on a set of finite measure , we define the integral of  over  by
where  and each 
Let  be a finite disjoint collection of measurable subsets of a set of finite measure . For , let  be a real number.
If  on , then
Linearity and Monotonicity of Integration: Let  and  be simple functions defined on a set of finite measure . Then for any  and ,
Moreover, if  on , then
A bounded function  on a domain  of finite measure is said to be Lebesgue integrable over  provided its upper and lowerLebesgue integrals over  are equal. The common value of the upper and lower integrals is called the Lebesgue integral.
Let  be a bounded function defined on the closed, bounded interval . If  is Riemann integrable over , then it is Lebesgueintegrable over  and the two integrals are equal.
Let  be a bounded measurable function on a set of finite measure . Then  is integrable over .
Let  and  be bounded measurable functions on a set of finite measure . Then for any  and ,
Moreover, if  on , then
Let  be a bounded measurable function on a set of finite measure . Suppose  and  are disjoint measurable subsets of . Then
Let  be a bounded measurable function on a set of finite measure . Then,
Let  be a sequence of bounded measurable functions on a set of finite measure . If  uniformly on , then 
The Bounded Convergence Theorem: Let  be a sequence of measurable functions on a set of finite measure . Suppose is uniformly pointwise bounded on , that is, there exists a number  for which  on  for all . If  pointwise
on , then 
Chebychev’s Inequality: Let  be a nonnegative measurable function on . Then for any ,
Let  be a nonnegative measurable function on . Then  iff  a.e. on .
Linearity and Monotonicity follow for nonnegative measurable functions.
f=inf{U(f,P)}∫
b
a
P [a,b]
f [a,b]2
ψ E ψ E
ψ= ×m( )∫E ∑
i=1
n
ai Ei
ψ= ×∑ni=1ai χEi ={x∈E|ψ(x)= }Ei ai
{Ei}ni=1 E 1≤i≤n ai
ϕ= ×∑ni=1ai χEi E
ϕ= ×m( )∫E ∑
i=1
n
ai Ei
ϕ ψ E αβ
(αϕ+βψ)=α ϕ+β ψ∫E ∫E ∫E
ϕ≤ψ E
ϕ≤ ψ∫E ∫E
f E EE
f [a,b] f [a,b][a,b]
f E f E
f g E α β
(αf+βg)=α f+β g∫E ∫E ∫E
f≤g E
f≤ g∫E ∫E
f E A B E
f= f+ f∫A∪B ∫A ∫B
f E
f≤ |f|∣∣∣∫E
∣∣∣ ∫E
{ }fn E { }→ffn E= flimn→∞∫Efn ∫E
{ }fn E { }fnE M≥0 | |≤Mfn E n { }→ffnE = flimn→∞∫Efn ∫E
f E λ>0
m({x∈E|f(x)≥λ})≤ f1λ∫E
f E f=0∫E f=0 E

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 24/27
Fatou’s Lemma: Let  be a sequence of nonnegative measurable functions on . If  pointwise a.e. on , then 
Monotone Convergence Theorem: Let  be an increasing sequence of nonnegative measurable functions on . If pointwise a.e. on , then
A nonnegative measurable function  on a measurable set  is said to be integrable over  provided 
Let the nonnegative function  be integrable over . Then  is finite a.e. on .
Let  be a measurable function on . Then  and  are integrable over  iff  is integrable over .
A measurable function  on  is said to be integrable over  provided . When this is so, we define the integral by
Let  be integrable over . Then  is finite a.e. on  and  if  such that .
The Integral Comparison Test: Let  be a measurable function on . Suppose there is a nonnegative function  that is integrable over  and dominates  in the sense that  on . Then  is integrable over  and
If  and  are integrable functions on , then linearity and monotonicity follow.
Let  be integrable over . Assume  and  are disjoint measurable subsets of . Then
Dominated Convergence Theorem: Let  be a sequence of measurable functions on . Suppose there is an integrable function on  and dominates  on  in the sense that  on  for all . If  pointwise a.e. on , then  is integrable over 
 and .
General Dominated Convergence Theorem: Let  be a sequence of measurable functions on  that converges pointwise a.e. on  to . Suppose there is a sequence  of nonnegative measurable functions on  that converges pointwise a.e. on  to  anddominates  on  in the sense that  on  for all . If
then,
Let  be a set of finite measure and . Then  is the disjoint union of a finite collection of sets, each of which has measure lessthan .
A family  of measurable functions on  is said to be uniformly integrable over  provided for each , there is a  such thatfor each , if  is measurable and , then .
Let  be a finite collection of functions, each of which is integrable over . Then  is uniformly integrable.
Vitali COnvergence Theorem: Let  be of finite measure. Suppose the sequence of functions  is uniformly integrable over . If  a.e. on , then  is integrable over  and
Let  be a bounded function on a set of finite measure . Then  is Lebesgue integrable over  iff it is measurable.
Let  be a bounded function on the closed, bounded interval of . Then  is Riemann integrable over  iff the set of points in  at which  fails to be continuous has measure zero.
Royden Chapter 6 (Differentiation)
Let  be a monotone function on the open interval . Then  is continuous except possibly at a countable number of points in .
If the function  is monotone on the open interval , then it is differentiable almost everywhere on 
{ }fn E { }→ffn Ef≤liminf∫E ∫Efn
{ }fn E { }→ffnE
= flimn→∞∫Efn ∫E
f E E f<∞∫E
f E f E
f E f+ f− E |f| E
f E E |f|<∞∫E
f= −∫E ∫Ef+ ∫Ef−
f E f E f= f∫E ∫E/E0 ⊆EE0 m( )=0E0
f E gE f |f|≤g E f E
f≤ |f|∣∣∣∫E
∣∣∣ ∫E
f g E
f E A B E
f= f+ f∫A∪B ∫A ∫B
{ }fn E gE { }fn E | |≤gfn E n { }→ffn E fE = flimn→∞∫Efn ∫E
{ }fn EEf { }gn E Eg{ }fn E | |≤fn gn E n
= g<∞limn→∞∫Egn ∫E
= flimn→∞∫Efn ∫E
E δ>0 Eδ
F E E ϵ>0 δ>0f∈FA⊆E m(A)<δ |f|<ϵ∫A
{fn}nk=1 E {fn}nk=1
E { }fn E{ }→ffn E f E
= flimn→∞∫Efn ∫E
f E f E
f [a,b] f [a,b][a,b] f
f (a,b) f(a,b)
f (a,b) (a,b)

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 25/27
Define the variation of  with respect to  (a partition) by , and the total variation of  on  by  where  is a partition on 
A real valued function  on the closed and bounded interval  is said to be of bounded variation on  provided 
Jordan’s Thm: A function  is of bounded variation on the closed, bounded interval  iff it is the difference of two increasingfunctions on 
If the function  is of bounded variation on the closed and bounded interval  then it is differentiable almost everywhere on the openinterval  and  is integrable over 
A real valued function  on a closed and bounded interval  is said to be absolutely continuous on  provided for each 
there is a  such that for every finite disjoint collection  of open intervals in , if , then
If the function  is Lipschitz on a closed, bounded interval , then it is absolutely continuous on 
Let the function  be absolutely continuous on the closed, bounded interval . Then  is the difference of increasing absolutelycontinuous functions and, in particular, is of bounded variation
Let the function  be absolutely continuous on the closed, bounded interval . Then  is differentiable almost everywhere on ,its derivative  is integrable over  and
We call a function  on a closed, bounded interval  the indefinite integral of  over  provided that  is Lebesgue integrableover  and for all 
A function  on a closed, bounded interval  is absolutely continuous on  iff it is an indefinite integral over 
Let the function  be monotone on the closed, bounded interval . Then  is absolutely continuous on  iff 
Let  be integrable over the closed, bounded interval . Then  for almost all  iff  for all 
Let  be integrable over the closed, bounded interval . Then for almost all 
Royden Chapter 7 (  Spaces)
For most of this section, unless otherwise stated, define  to be a measurable set of real numbers, and  to be the collection of allmeasurable extended real-valued functions on  that are finite a.e. on . Define  and  to be equivalent and  iff  for almost all .
We call a function  essentially bounded provided there is some  called an essential upper bound for  for which  for almost all 
functionals are real-valued functions that have as their domain linear spaces of functions
Let  be a linear space. A real-valued functional  on  is called a norm provided for each  and  in , and each real number ,  and  iff ,
By a normed linear space we mean a linear space together with a norm. If  is a linear space normed by  we say that a function in is a unit function provided 
For any , , the function  is a unit function: it is a scalar multiple of  which we call the normalization of 
The Normed Linear Space 
f P V(f,P)= |f( )−f( )|∑ki=1 xi xi−1 f[a,b] TV(f)=sup{V(f,P)} P [a,b]
f [a,b] [a,b] TV(f)<∞
f [a,b][a,b]
f [a,b](a,b) f′ [a,b]
f [a,b] [a,b] ϵ>0δ>0 {( , )akbk}nk=1 (a,b) [ − ]<δ∑nk=1bk ak
|f( )−f( )|<ϵ∑
k=1
n
bk ak
f [a,b] [a,b]
f [a,b] f
f [a,b] f (a,b)f′ [a,b]
=f(b)−f(a)∫
a
b f′
f [a,b] g [a,b] g[a,b] x∈[a,b]
f(x)=f(a)+ g∫
x
a
f [a,b] [a,b] [a,b]
f [a,b] f [a,b]=f(b)−f(a)∫baf′
f [a,b] f(x)=0 x∈[a,b] f=0∫x2
x1
( , )⊆[a,b]x1x2
f [a,b] x∈(a,b)
[ f]=f(x)ddx∫
x
a
Lp
E FE E f g∈F f≅gf(x)=g(x) x∈E
f∈F M≥0 f|f(x)|≤M x∈E
X ||⋅|| X f g X c||f||≥0 ||f||=0 f=0
||f+g||≤||f||+||g||
||cf||=|c|||f||
X ||⋅||X ||f||=1
f∈Xf≠0 f||f|| f f
(E)L1
||f| = |f||1 ∫E

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 26/27
The Normed Linear Space : For a function , define  to be the infimum of the essential upper bounds for .We call  the essential supremum of  and claim that  is a norm on 
 is a norm and is called the maximum norm
For a measurable set  where  and a function  in , define
The conjugate of a number  is the number , which is the unique number  for which
Note, the conjugate of  is defined to be  and vice versa.
Young’s Inequality: For ,  is the conjugate of  and any two positive numbers  and ,
Let  be a measurable set , and  be the conjugate of . If  belongs to  and  belongs to , then theirproduct  is integrable over  and
This is known as Holder’s Inequality.
Let  be a measurable set and . If the functions  and  belong to , then so does their sum  and moreover,
Cauchy-Schwarz Inequality: Let  be a measurable set and  and  measurable functions on  for which  and  are integrableover . Then their product  is also integrable over  and
Let  be a measurable set and . Suppose  is a family of functions in  that is bounded in  in the sense thatthere is a constant  for which  for all  in . Then the family  is uniformly integrable over .
Let  be a measurable set of finite measure and . Then . Furthermore  for
all  in  where  if  and  if 
A sequence  in a linear space  that is normed by  is said to converge to  in  provided . Thiscan also be written as  in  or  in .
A sequence  in a linear space  that is normed by  is said to be Cauchy in  provided for each , there is a naturalnumber  such that  for all .
A normed linear space  is said to be complete provided every Cauchy sequence in  converges to a function in . A completenormed linear space is called a Banach space
Let  be a normed linear space. Then every convergent sequence in  is Cauchy. Moreover, a Cauchy sequence in  converges if ithas a convergent subsequence.
Let  be a linear space normed by . A sequence  in  is said to be rapidly Cauchy provided there is a convergent series of
positive numbers  for which  for all 
Let  be a normed linear space. Then every rapidly Cauchy sequence in  is Cauchy. Furthermore, every Cauchy sequence has arapidly Cauchy subsequence.
Let  be a measurable set and . Then every rapidly Cauchy sequence in  converges both wrt the  norm andpointwise a.e. on  to a function in .
Let  be a measurable set and . Then  is a Banach space. Moreover, if  in , a subsequence of  converges pointwise a.e. on  to 
Let  be a measurable set and . Suppose  is a sequence in  that converges pointwise a.e. on  to the
function  which belongs to . Then  in  iff 
Let  be a measurable set and . Suppose  is a sequence in  that converges pointwise a.e. on  to thefunction  which belongs to . Then  in  iff  is uniformly integrable and tight over .
(E)L∞ f∈ (E)L∞ ||f||∞ f||f||∞ f ||⋅|| (E)L∞
||f| = |f(x)||max maxx∈[a,b]
E 1<p<∞ f (E)Lp
||f| =|p [ |f ]∫E |p 1/p
p∈(1,∞) q=pp−1 q∈(1,∞)
+ =11p 1q
1 ∞
1<p<∞q p a b
ab≤ +ap
p bq
q
E 1≤p<∞ q p f (E)Lp g (E)Lq
f⋅g E
|f⋅g|≤||f| ⋅||g|∫E |p |q
E 1≤p<∞ f g (E)Lp f+g
||f+g| ≤||f| +||g||p |p |p
E f g E f2 g2
E f⋅g E
|fg|≤ ⋅∫E ∫Ef2− −−−−√ ∫Eg2− −−−−√
E 1<p<∞ F (E)Lp (E)Lp
M ||f| ≤M|p f F F E
E 1≤ < ≤∞p1 p2 (E)⊆ (E)Lp2 Lp1 ||f| ≤c||f||p1 |p2
f (E)Lp2 c=[m(E)]
−p2p1p1p2 <∞p2 c=[m(E)]
1p1 =∞p2
{ }fn X ||⋅|| f X ||f− ||=0limn→∞ fn{ }→ffn X =flimn→∞fn X
{ }fn X ||⋅|| X ϵ>0N || − ||<ϵfn fm m,n≥N
X X X
X X X
X ||⋅|| { }fn X∑∞k=1ϵk || − ||≤fk+1 fk ϵ2k k
X X
E 1≤p≤∞ (E)Lp (E)Lp
E (E)Lp
E 1≤p≤∞ (E)Lp { }→ffn (E)Lp
{ }fn Ef
E 1≤p<∞ { }fn (E)Lp Ef (E)Lp { }→ffn (E)Lp | = |flimn→∞∫Efn|p ∫E |p
E 1≤p<∞ { }fn (E)Lp Ef (E)Lp { }→ffn (E)Lp {|f }|p E

11/9/21, 5:35 PM My Solutions to Old Analysis Quals
https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dﬀ45fead17af37236a76c8.html 27/27
Let  be a normed linear space with norm . Given two subsets  and  of  with , we say that  is dense in , providedfor each function  and , there is a function  for which 
Let  be a measurable set and . Then the subspace of simple functions in  is dense in 
Let  be a closed, bounded interval and . Then the subspace of step functions on  is dense in 
A normed linear space  is said to be separable provided there is a countable subset that is dense in .
Let  be a measurable set and . Then the normed linear space  is separable.
Royden Chapter 8 (  Spaces Continued)
A linear functional on a linear space  is a real-valued function  on  such that for  and  in  and  and  real numbers,
For a normed linear space , a linear functional  on  is said to be bounded provided there is an  for which  for all . The infimum of all such  is called the norm of  and denoted by 
Let  be a normed linear space. Then the collection of bounded linear functionals on  is a linear space on which  is a norm. Thisnormed linear space is called the dual space of  and denoted by 
Let  be a measurable set, ,  be the conjugate of , and  belong to . Define the functional  on  by 
 for all . Then  is a bounded linear functional on  and 
Let  and  be bounded linear functionals on a normed linear space . If  on a dense subset  of , then 
Let  be a closed, bounded interval and . Suppose  us a bounded linear functional on . Then there is a
function  in , where  is the conjugate of  for which  for all 
Let  be a measurable set,  and  the conjugate of . For each , define the bounded linear functional  on 
 by  for all  in . Then for each bounded linear functional  on , there is a unique function 
 for which  and 
Let  be a normed linear space. A sequence  in  is said to converge weakly in  to  in  provided  for all 
Let  be a measurable set, , and  the conjugate of . Then  converges weakly in  to  in  iff 
 for all 
Let  be a measurable set and . Suppose  converges weakly in  to . Then  is bounded in  and 
Let  be a measurable set, , and  the conjugate of . Suppose  converges weakly to  in  and 
converges strongly to  in . Then 
The linear span of a subset  of a linear space  is the linear space consisting of all linear combinations of functions in , that is, thelinear space of functions of the form  where each  is a real number and each  belongs to 
Let  be a measurable set and . Suppose  is a bounded sequence in  and  belongs to . Then 
converges weakly to  in  iff for every measurable subset  of , . If , it is sufficient to consider
sets  of finite measure.
Let  be a closed and bounded interval and . Suppose  is a bounded sequence in  and  belongs to . Then  converges weakly to  in  iff
for all . This theorem is false for 
Let  be a measurable set and . Suppose  converges weakly to  in . Then  in  iff 
Let  be a measurable set and . Suppose  converges weakly  in . Then a subsequence of  convergesstrongly in  to  iff 
Let  be a measurable set and . Then every bounded sequence in  has a subsequence that converges weakly in  to a function in 
X ||⋅|| F G X F⊆G F Gg∈G ϵ>0 f∈F ||f−g||<ϵ
E 1≤p≤∞ (E)Lp (E)Lp
[a,b] 1≤p<∞ [a,b] [a,b]Lp
X X
E 1≤p<∞ (E)Lp
Lp
X T X g h X α β
T(α⋅g+β⋅h)=α⋅T(g)+β⋅T(h)
X T X M≥0|T(f)|≤M⋅||f|| f∈X M T ||T||∗
X X ||⋅||∗X X∗
E 1≤p<∞q p g (E)Lq T (E)Lp
T(f)= g⋅f∫E f∈ (E)Lp T (E)Lp ||T| =||g||∗ |q
T S XT=S X0 X T=S
I=[a,b] 1≤p<∞ T [a,b]Lp
g [a,b]Lq q p T(f)= g⋅f∫I f∈ [a,b]Lp
E 1≤p<∞ q p g∈ (E)Lq Rg(E)Lp (f)= g⋅fRg ∫E f (E)Lp T (E)Lp
g∈ (E)Lq =TRg ||T| =||g||∗ |q
X { }fn X Xf XT( )=T(f)limn→∞ fn T∈X∗
E 1≤p<∞ q p { }fn Xf (E)Lp
g⋅ = g⋅flimn→∞∫E fn ∫E g∈ (E)Lq
E 1≤p<∞ { }fn (E)Lp f { }fn (E)Lp
||f| ≤liminf|| ||p fn|p
E 1≤p<∞ q p { }fn f (E)Lp { }gng (E)Lq ⋅ = g⋅flimn→∞∫Egnfn ∫E
S X Sf= ⋅∑nk=1αkfk αk fk S
E 1≤p<∞ { }fn (E)Lp f (E)Lp { }fnf (E)Lp AE = flimn→∞∫Afn ∫A p>1A
[a,b] 1<p<∞ { }fn [a,b]Lp f[a,b]Lp { }fn f [a,b]Lp
[ ]= flimn→∞∫
x
a fn ∫
x
a
x∈[a,b] p=1
E 1<p<∞ { }fn f (E)Lp { }→ffn (E)Lp
|| | =||f|limn→∞fn|p |p
E 1<p<∞ { }fn f (E)Lp { }fn(E)Lp f ||f| =liminf|| ||p fn|p
E 1<p<∞ (E)Lp
(E)Lp (E)Lp

