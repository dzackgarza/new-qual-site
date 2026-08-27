UCLA Analysis Qualifying Exam Solutions
Last updated: January 25, 2019
Contents
1 Spring 2009 2
2 F all 2009 7
3 Spring 2010 12
4 F all 2010 16
5 Spring 2011 22
6 F all 2011 26
7 Spring 2012 33
8 F all 2012 40
9 Spring 2013 47
10 F all 2013 55
11 Spring 2014 63
12 F all 2014 69
13 Spring 2015 76
14 F all 2015 84
15 Spring 2016 95
16 F all 2016 104
17 Spring 2017 114
18 F all 2017 121
19 Spring 2018 127
20 F all 2018 137
1

1 Spring 2009
Problem 1. Let f and g be real-valued integrable functions on a measure space pX, B,µq and deﬁne
Ft “ txPX :fpxqą tu, G t “ txPX :gpxqą tu.
Prove ż
|f´g|dµ “
ż8
´8
µppFtzGtqYp GtzFtqq.
Solution. First assume that X is σ-ﬁnite. Then we have
ż8
´8
µppFtzGtqYp GtzFtqq “
ż8
´8
ż
X
χtxPX:minpfpxq,gpxqqďtămaxpfpxq,gpxqqupxqdµpxqdt
“
ż
X
ż8
´8
χtxPX:minpfpxq,gpxqqďtămaxpfpxq,gpxqqupxqdtdµpxq by Tonelli
“
ż
X
|fpxq´ gpxq|dµpxq,
which is the desired result. Now drop the assumption that X isσ-ﬁnite. Let Y “txPX :|fpxq´gpxq|‰ 0u
and let ν“µ|Y . Note that Y “ Ť8
n“1txPX :|fpxq´ gpxq|ą 1{nu, and since f and g are both integrable,
each of those sets must have ﬁnite measure. Thus pY,νq is aσ-ﬁnite measure space. Thus by the work above
we have ż
Y
|f´g|dν “
ż8
´8
νppFtXYzGtXYqYp GtXYzFtXYqq.
But note that
ş
X|f´g|dµ“
ş
Y |f´g|dµ`
ş
Yc|f´g|dµ“
ş
Y |f´g|dν by deﬁnition of Y and ν. Also
note that FtzGt,GtzFtĎ Y for every t, so pFtXYzGtXYqYp GtXYzFtXYq“p FtzGtqYp GtzFtq, and
νppFtzGtqYp GtzFtqq “µppFtzGtqYp GtzFtqq. Substituting all of this into the above equation gives the
desired result.
Problem 2. Let H be an inﬁnite dimensional real Hilbert space.
(a) Prove the unit sphere S“txPH :||x||“ 1u is weakly dense in the unit ball B“txPH :||x||ď 1u.
(b) Prove there is a sequence Tn of bounded linear operators from H toH such that||Tn||“ 1 for all n but
limnÑ8Tnpxq“ 0 for all xPH.
Solution. (a) Fix x P B. We may assume ||x|| ă 1 because if x P S the result is obvious. Using a
standard Zorn’s Lemma/Gram-Schmidt argument, together with the fact that H is inﬁnite-dimensional, we
can construct an orthonormal set tx{||x||,e 1,e 2,... u. Let xn “ x`
b
1´||x||2en. By the Pythagorean
theorem we have||xn||2“||x||2`p1´||x||2q||en||2“ 1, soxnPS. Now we claim thattxnu converges weakly
to x. For yPH ﬁxed, we have
xxn´x,yy “
b
1´||x||2xen,yy.
This goes to 0 as nÑ8 because sincetenu is an orthonormal set, Bessel’s inequality gives ř8
n“1 |xen,yy|2ď
||y||2 and the terms of a convergent series must go to 0.
(b) Fix an inﬁnite orthonormal set te1,e 2,... u. Deﬁne Tnpxq :“ xx,enyen. It’s clear that Tn is a linear
operatorHÑH. We have||Tnpxq||“ |xx,eny|||en||ď|| x|| by Cauchy-Schwarz, so||Tn||ď 1. Also it’s clear
that Tnpenq“ en, so ||Tn||“ 1. Finally, for any xPH we have limnÑ8||Tnpxq||“ limnÑ8 |xx,eny|“ 0 by
the same Bessel’s inequality argument in part (a).
Problem 3. Let X be a Banach space. Prove that if X˚ is separable then X is separable.
Solution. See Fall 2014 # 6.
2

Problem 4. Let fpxq be a non-decreasing function on r0, 1s.
(a) Prove that
ş1
0f1pxqdxďfp1q´ fp0q.
(b) Let tfnu be a sequence of non-decreasing functions on r0, 1s such that the series Fpxq “ř8
n“1fnpxq
converges for all xPr 0, 1s. Prove that F1pxq“ ř8
n“1f1
npxq almost everywhere.
Solution. (a) First we extend the deﬁnition of f by setting fpxq “fp1q for x ą 1. Note that f is
diﬀerentiable almost everywhere because it is non-decreasing. So for almost every x, the representation
f1pxq “ lim
hÑ0`
fpx`hq´ fpxq
h
is valid. Since f is non-decreasing, the diﬀerence quotient is non-negative for every x and every h. Thus by
Fatou’s lemma we have
ż 1
0
f1pxqdx “
ż 1
0
lim
hÑ0`
fpx`hq´ fpxq
h dx ď lim inf
hÑ0`
ż 1
0
fpx`hq´ fpxq
h dx
“ lim inf
hÑ0`
1
h
ż 1`h
1
fpxqdx´ 1
h
żh
0
fpxqdx ď fp1q´ fp0q
where we used the fact that f is non-decreasing again in the last inequality.
(b) First note that since each fn is non-decreasing, F also is, so F is diﬀerentiable almost everywhere.
Let rNpxq“ ř8
n“N`1fnpxq and write Fpxq“ řN
n“1fnpxq` rNpxq. Since rN is also non-decreasing, we can
write F1pxq “řN
n“1f1
npxq` r1
Npxq for all x at which all three of those functions are diﬀerentiable, which
is still almost everywhere. Thus to show the desired result it’s enough to show that r1
Npxq Ñ0 almost
everywhere asNÑ8 . First note that for almost every x,r1
Npxq´ r1
N`1pxq“p rN´rN`1q1pxq“ f1
Npxqě 0
becausefN is non-decreasing so its derivative is non-negative wherever it exists. Sotr1
Npxqu is monotonically
decreasing inN for almost everyx. So the limit limNÑ8r1
Npxq exists almost everywhere and is non-negative
(as a limit of non-negative terms). Thus by the monotone convergence theorem we have
ż 1
0
lim
NÑ8
r1
Npxqdx “ lim
NÑ8
ż 1
0
r1
Npxqdx ď lim
NÑ8
rNp1q´ rNp0q “ 0
where the second to last inequality uses part (a) because each rN is non-decreasing and the last equality is
by the hypothesis that the series deﬁning F converges everywhere. Thus lim NÑ8r1
Npxq is a non-negative
function which integrates to 0, so it must be zero almost everywhere.
Problem 5. Let I0,0“r 0, 1s and for ně 0, 0ďjď 2n´ 1, let
In,j “ rj2´n,pj` 1q2´ns.
Forf P L1pr0, 1sq deﬁne Enf “ ř2n´1
j“0
´
2nş
In,j
fptqdt
¯
χIn,j. Prove that Enf Ñ f almost everywhere on
r0, 1s.
Solution. For a ﬁxed xPr 0, 1s, Enfpxq is simply the average value of f over the interval In,jpn,xq that x
lies in. It’s clear that the family of intervals tIn,jpn,xqu8
n“1 shrinks nicely to x, so it’s a direct consequence
of the Lebesgue diﬀerentation theorem that Enfpxq Ñfpxq for all Lebesgue points of f, which is almost
everywhere.
Problem 6. ForIn,j as in Problem 5, deﬁne the Haar function hn,j“ 2n{2`
χIn`1,2j´χIn`1,2j`1
˘
.
(a) Draw I2,1 and graph h2,1.
(b) Prove that if fPL2pr0, 1sq and
ş1
0fptqdt“ 0, then
ż 1
0
|fpxq|2dx “
ÿ
ně0,0ďjď2n´1
⏐⏐⏐⏐
ż 1
0
fptqhn,jptqdt
⏐⏐⏐⏐
2
.
3

(c) Prove that if fPL1pr0, 1sq and
ş1
0fptqdt“ 0, then almost everywhere on r0, 1s,
fpxq “
8ÿ
n“0
2n´1ÿ
j“0
ˆż 1
0
fptqhn,jptqdt
˙
hn,jpxq.
Solution. (a)
(b) Let M “
!
fPL2pr0, 1sq :
ş1
0f“ 0
)
. First note that M is a closed subspace of L2: if fn P M and
fn Ñ f in L2, then by Cauchy-Schwarz we also have fn Ñ f in L1, so in particular
ş
fn Ñ
ş
f, so
ş
f “ 0
as well. Thus we can consider M as a Hilbert space. Next note that thn,jun,j form an orthonormal set
in M: It’s clear that
ş
h2
n,j “ 1 for each n,j . Now consider
ş
hn,jhm,k. Suppose without loss of generality
that m ě n. There are only two possibilities, either hn,j and hm,k have disjoint supports, in which case
the integral is clearly zero, or the support of hm,k is contained in a set on which hn,j is constant, in which
case the integral is just a constant multiple of
ş
hm,k, which is 0. Thus they form an orthonormal set. We
want to show they form an orthonormal basis for M. If we show this, then the desired conclusion is just the
statement of Parseval’s identity and we will be done. Let f P M and suppose that
ş
fhn,j “ 0 for all n,j .
It’s enough to show this implies f “ 0. First note that we have
ş1
0f “
ş1{2
0 f`
ş1
1{2f “ 0. We also have
by assumption
ş
fh0,0 “
ş1{2
0 f´
ş1
1{2f “ 0. Combining these two yields
ş1{2
0 f “
ş1
1{2f “ 0. Continuing,
we have 0 “
ş1{2
0 f “
ş1{4
0 f`
ş1{2
1{4, and by assumption, 0 “
ş
fh1,0 “
ş1{4
0 f´
ş1{2
1{4f, and combining these
gives
ş1{4
0 f “
ş1{2
1{4f “ 0. Continuing in this way inductively shows that
ş
In,jf “ 0 for all n,j . Any closed
interval can be written as a countable disjoint union of the In,j, so the integral of f over any closed interval
vanishes, which implies f“ 0.
(c) Let
SNfpxq “
Nÿ
n“0
2n´1ÿ
j“0
ˆż 1
0
fptqhn,jptqdt
˙
hn,jpxq.
In light of problem 5 above, it’s enough to show that SNfpxq“ EN`1fpxq for almost every x. We show this
holds for any x which is not an endpoint of any In,j. Fix such an x. Deﬁne jpnq to be the unique j such
that xPIn,j and deﬁne jpnqc to be the unique j‰jpnq such that In,jpnqYIn,jpnqc “In´1,jpn´1q. Then we
have
SNfpxq “
Nÿ
n“0
ˆż 1
0
fptqhn,jpnqptqdt
˙
hn,jpnqpxq
“
Nÿ
n“0
2n
˜ż
In`1,jpn`1q
f´
ż
In`1,jpn`1qc
f
¸
“
Nÿ
n“0
2n
˜
2
ż
In`1,jpn`1q
f´
ż
In,jpnq
f
¸
“
Nÿ
n“0
2n`1
ż
In`1,jpn`1q
f´ 2n
ż
In,jpnq
f
“ 2N`1
ż
IN`1,jpN`1q
f´
ż
I0,0
f
“ 2N`1
ż
IN`1,jpN`1q
f “ EN`1fpxq.
Problem 7. Let µ be a ﬁnite positive Borel measure on C.
4

(a) Prove that Fpzq “
ş
C
1
z´wdµpwq exists for almost all z P C and that
ş
K|Fpzq|dxdy ă 8for every
compact KĎ C.
(b) Prove that for almost every horizontal line L and all compact KĎL,
ş
K|Fpx`iyq|dxă8 .
(c) Prove that for almost all open squares S with sides parallel to the axes,
µpSq “ 1
2πi
ż
BS
Fpzqdz.
Solution. (a) The second half of the assertion implies the ﬁrst half, so we focus on the second. It’s
enough to show that
ş
|z|ďR|Fpzq|dApzqă8 for each R. We estimate
ż
|z|ďR
|Fpzq|dApzq ď
ż
|z|ďR
ż
wPC
1
|z´w|dµpwqdApzq “
ż
wPC
ż
|z|ďR
1
|z´w|dApzqdµpwq by Tonelli
“
ż
|w|ď2R
ż
|z|ďR
1
|z´w|dApzqdµpwq`
ż
|w|ą2R
ż
|z|ďR
1
|z´w|dApzqdµpwq
ď
ż
|w|ď2R
ż
|z´w|ď3R
1
|z´w|dApzqdµpwq`
ż
|w|ą2R
ż
|z|ďR
1
RdApzqdµpwq
ď
ż
|w|ď2R
CRdµpwq`
ż
|w|ą2R
πRdµpwq where CR is some constant depending on R
ă 8
because µ is a ﬁnite measure.
(b) As in part (a), it’s enough to prove the assertion with any compact set K replaced by any interval
of the form r´R,Rs. Fix some R and an integer m. Then by part (a) and Tonelli’s theorem, we knowşm`1
m
şR
R|Fpx`iyq|dxdy ă8 . This implies that there is a set Ym,R of full measure in rm,m` 1s such thatşR
R|Fpx`iyq|dxă8 for eachyPYm,R. By setting Ym“ Ş8
R“1Ym,R, we see thatY still has full measure in
rm,m`1s and now for anyyPYm,
şR
R|Fpx`iyq|dxă8 for everyR. Thus we have shown that almost every
horizontal line withy-intercept inrm,m`1s satisﬁes the desired property. Now setting Y “ Ť8
m“´8Ym, we
see that Y is an almost everywhere subset of R with the property that yPY implies
şR
R|Fpx`iyq|dxă8
for every R, which is the desired conclusion. In fact, by examining the proof of part (a) it’s clear that we
actually proved something a bit stronger, which is that yPY implies
ş
K
ş
wPC
1
|x`iy´w|dµpwqdxă8 for all
compact sets K (we’ll need this version in part (c)).
(c) The same argument as in part (b) shows that the analogous result to part (b) for vertical lines also
holds. Let S be the collection of squares S in C such that all four sides of S lie on lines for which the
conclusion of part (b) holds. It’s clear that S is almost every square in C. Thus for SP S, we have
ż
BS
Fpzqdz “
ż
BS
ż
C
1
z´wdµpwqdz “
ż
C
ż
BS
1
z´wdzdµpwq
“
ż
C
2πiχSpwqdµpwq “ 2πiµpSq,
which is the desired result. We just need to justify switching the order of integration in the ﬁrst line. Note
that by deﬁnition of S, ż
BS
ż
C
1
|z´w|dµpwqdz
is simply a sum of four integrals along horizontal or vertical lines which are known to be ﬁnite by the com-
ment at the end of part (b). Thus Fubini-Tonelli applies, so the switch is justiﬁed.
Problem 8. Let f be an entire non-constant function that satisﬁes the functional equation
fp1´zq “ 1´fpzq
5

for all zP C. Show that fpCq“ C.
Solution. The functional equation implies that w P Impfq if and only if 1 ´w P Impfq. Thus suppose
that there were somewR Impfq, then 1´wR Impfq either, sof misses two points (ifw‰ 1{2). But Picard’s
little theorem says that an entire function that misses two points is constant, a contradiction. Thus f hits
everything except possibly 1{2. But putting z“ 1{2 into the functional equation gives fp1{2q“ 1´fp1{2q,
so fp1{2q“ 1{2. Thus f is surjective.
Problem 9. Letfpzq be an analytic function on the entire complex plane C and assumefp0q‰ 0. Let tanu
be the zeros of f, counted with multiplicity.
(a) Let Rą 0 be such that |fpzq|ą 0 on |z|“ R. Prove
1
2π
ż 2π
0
log
⏐⏐fpReiθq
⏐⏐ dθ “ log|fp0q|`
ÿ
|an|ăR
log
ˆ R
|an|
˙
.
(b) Assume |fpzq|ď Ce|z|λ
for positive constants C and λ. Prove that
ÿ
n
ˆ 1
|an|
˙λ`ϵ
ă 8
for all ϵą 0.
Solution. See Spring 2017 # 9.
Problem 10. Let µ be Lebesgue measure on D. Let H be the subspace of L2pD,µq consisting of holo-
morphic functions. Show that H is complete.
Solution. See Fall 2014 #10 (not exactly the same problem, but a similar idea).
Problem 11. Suppose that f : DÑ C is holomorphic and injective in some annulustz :ră|z|ă 1u. Show
that f is injective in D.
Solution. Suppose there are z1,z 2 P D with fpz1q “fpz2q “w. Then there is a circle C of radius
sPpr, 1q containing both z1 and z2 in its interior. Then the function f´w has at least two zeros inside C,
so the argument principle tells us that the curve fpCq has winding number at least 2 around zero. But a
curve of winding number at least 2 has to intersect itself, meaning that there are two diﬀerent points on the
curve C at which f´w takes the same value. But since S lies in the annulus ră|z|ă 1, this contradicts
the fact that f is injective on the annulus.
Problem 12. Let Q be the closed unit square in C and let R be the closed rectangle in C with ver-
ticest0, 2,i, 2`iu. Prove there does not exists a surjective homeomorphism f :QÑR that is conformal on
the interior of Q and maps corners to corners.
Solution. Suppose f : Q Ñ R satisﬁes the given conditions. By continuity, it must preserve the order
of the vertices, so by precomposing with rotations and ﬂips if necessary, we may assume that f ﬁxes the
vertical line segment r0,is. By the Schwarz reﬂection principle, applied iteratively and reﬂecting over the
vertical lines, we can extend f to a map from the strip 0 ď Impzqď 1 to itself. We can then reﬂect over
the two horizontal lines to extend f to a map from the strip ´1ď Impzqď 2 to itself. This strip is simply
connected and so is conformally equivalent to D. So f has been extended to a conformal automorphism of
a region conformally equivalent to D, and f has two ﬁxed points, which implies f is the identity, a contra-
diction.
6

2 Fall 2009
Problem 1. Find a non-empty closed set in the Hilbert space L2pr0, 1sq that does not contain an element
of smallest norm.
Solution. Let fn“n¨χr0,1{n2`1{n3s. We claim tfnu8
n“2 is such a set. First note that
ż
|fn|2“
ˆ 1
n2 ` 1
n3
˙
¨n2 “ 1` 1
n,
so we see that the set has no element of smallest norm. To show it’s closed, suppose gPL2 is a limit point.
Then there is a subsequence fnk converging to g in L2. But this implies there is a further subsequence fnk𝓁
converging almost everywhere to g. But it’s clear that fnÑ 0 almost everywhere, so g“ 0. But 0 is clearly
not a limit point of tfnu because||fn||L2ą 1 for each n. Thus tfnu has no limit points so it’s closed.
Problem 2. Let v be a trigonometric polynomial in two variables, i.e.
vpx,yq “
ÿ
n,mPZ
an,me2πipnx`myq
with only ﬁnitely many nonzero an,m. If u“v´ ∆v where ∆“B 2
x`B 2
y is the Laplacian, prove that
||v||L8pr0,1s2q ď C||u||L2pr0,1s2q
for some constant C independent of v.
Solution. A straightforward computation shows that
upx,yq “
ÿ
n,m
an,mp1` 4π2pn2`m2qqe2πipnx`myq.
Thus, using orthonormality and the fact that only ﬁnitely many coeﬃcients are nonzero, we have
ż 1
0
ż 1
0
|upx,yq|2 dxdy “
ż 1
0
ż 1
0
ÿ
n,m,k,𝓁
an,mak,𝓁p1` 4π2pn2`m2qqp1` 4π2pk2`𝓁2qqe2πipnx`myqe´2πipkx`𝓁yqdxdy
“
ÿ
n,m,k,𝓁
an,mak,𝓁p1` 4π2pn2`m2qqp1` 4π2pk2`𝓁2qq
ż 1
0
e2πipn´kqxdx
ż 1
0
e2πipm´𝓁qydy
“
ÿ
n,m
|an,m|2p1` 4π2pn2`m2qq2.
Now we simply estimate v using the triangle inequality and Cauchy-Schwarz:
|vpx,yq|2 ď
˜ÿ
n,m
|an,m|
¸2
“
˜ÿ
n,m
|an,m|p1` 4π2pn2`m2qq¨ 1
p1` 4π2pn2`m2qq
¸2
ď
˜ÿ
n,m
|an,m|2p1` 4π2pn2`m2qq2
¸˜ ÿ
n,m
1
p1` 4π2pn2`m2qq2
¸
“C¨||u||2
L2pr0,1s2q
because ř
n,m
1
p1`4π2pn2`m2qq2 converges. Thus we have established ||v||2
L8pr0,1s2q ď C||u||2
L2pr0,1s2q which
implies the desired result.
Problem 3. Let f :r0, 1sÑ R be continuous with
min
xPr0,1s
fpxq “ 0.
7

Assume that for all 0 ďaăbď 1 we have
żb
a
pfpxq´ min
yPra,bs
fpyqqdx ď 1
2pb´aq.
(a) Prove that for all λě 0,
|tx :fpxqą λ` 1u| ď 1
2 |tx :fpxqą λu|.
(b) Prove that for all 1 ďcă 2, ż 1
0
cfpxqdx ď 100
2´c.
Solution. (a) Fix λ ě 0. Since f is continuous, tx : fpxq ąλu is open, and thus it can be written as
a countable union of disjoint open intervals paj,bjq (the set is only open relative to r0, 1s, so it’s possible
that one of the intervals is closed on the left at 0 and another is closed on the right at 1, but that doesn’t
change any of the following work, so we ignore it). Also by continuity, we must have min yPraj,bjsfpyq“ λ
for each j. Thus using the hypothesis on f, for each j we have
1
2pbj´ajq ě
żbj
aj
pfpxq´ λqdx “
żbj
aj
fpxqdx´λpbj´ajq.
Summing both sides from j“ 1 to 8 gives
ˆ1
2`λ
˙
|tx :fpxqą λu| ě
ż
tfąλu
fpxqdx.
We also have
ż
tfąλu
fpxqdx “
ż
tfąλ`1u
fpxqdx`
ż
tλăfďλ`1u
fpxqdx
ě pλ` 1q |tx :fpxqą λ` 1u|`λ |tx :fpxqą λ` 1uztx :fpxqą λu|
“ pλ` 1q |tx :fpxqą λ` 1u|`λp|tx :fpxqą λu|´ |tx :fpxqą λ` 1u|q
“ |tx :fpxqą λ` 1u|`λ |tx :fpxqą λu|.
Combining this with the above inequality and rearranging gives the desired result.
(b) Fix 1 ďcă 2. We can write
ż 1
0
cfpxqdx “ c0¨|tf“ 0u|`
8ÿ
j“0
ż
tjăfďj`1u
cfpxqdx ď 1`
8ÿ
j“0
cj`1 |tjăfďj` 1u| ď 1`
8ÿ
j“0
cj`1 |tfąju|.
We know that |tx :fpxqą 0u| ď 1, so by inductively applying the conclusion of part (a) we see that
|tx :fpxqą ju|ď 2´j. Thus we have
ż 1
0
cfpxqdx ď 1`
8ÿ
j“0
cj`12´j “ 1`c
8ÿ
j“0
pc{2qj “ 1` c
1´c{2 “ 2`c
2´c ď 100
2´c
where the geometric series converges because că 2.
Problem 4. Prove the following variant of the Lebesgue diﬀerentiation theorem: Let µ be a ﬁnite Borel
measure on R, singular with respect to Lebesgue measure. Then for Lebesgue almost every xP R,
lim
ϵÑ0
µprx´ϵ,x `ϵq
2ϵ “ 0.
8

Solution. See Fall 2016 #2.
Problem 5. Construct a Borel subset E of the real line R such that for all intervals ra,bs we have
0 ă mpEXra,bsq ă b´a
where m denotes Lebesgue measure.
Solution.
Problem 6. The Poisson kernel for 0 ďρă 1 is the 2π-periodic function on R deﬁned by
Pρpθq “ Re
ˆ1`ρeiθ
1´ρeiθ
˙
.
For functionsh continuous on and harmonic inside the closed disc of radius R about the origin one has
hpreiηq “ 1
2π
ż 2π
0
Pr{Rpη´θqhpReiθqdθ.
Assume that h is harmonic and positive on D. Prove that there exists a positive Borel measure µ onr0, 2πs
such that for all reiηP D one has
hpreiνq “
ż 2π
0
Prpη´θqdµpθq.
Solution. For each 0 ă R ă 1, deﬁne the measure µR by dµRpθq “hpReiθqdθ. By scaling we may
assume hp0q “1. Since h is positive and continuous, each µR is a positive Borel measure on r0, 2πs. By
the Riesz representation theorem, we may view each µR as a bounded linear functional on the Banach space
Cpr0, 2πsq. Note that by the special case of the given formula with r“ 0 (i.e. the mean value property), we
have
||µR|| “ µRpr0, 2πsq “ 1
2π
ż 2π
0
hpReiθqdθ “ hp0q.
Thus eachµR is in the unit ball of the dual spaceCpr0, 2πsq˚. By Banach-Alaoglu and the fact thatCpr0, 2πsq
is separable, this implies that we have a subsequence of Rs converging to 1 and some measure µ in the unit
ball of Cpr0, 2πsq with µRÑµ in the weak-˚ topology. A standard approximation argument shows that µ
must also be a positive measure since each µR is. We claim that µ is the desired measure. Fix reiη P D.
Note that each Pρ is continuous on r0, 2πs and Pr{RÑ Pr uniformly on r0, 2πs as RÑ 1. For each Ră 1
the given formula tells us
hpreiηq “
ż 2π
0
Pr{Rpη´θqdµRpθq.
Taking the limit as R Ñ 1 on both sides gives the desired result, where we have assumed the following
lemma: if fn are continuous andfnÑf uniformly onr0, 2πs andµnÑµ in weak-˚, then
ş
fndµnÑ
ş
fdµ .
The proof of this just follows by writing
⏐⏐⏐⏐
ż
fndµn´
ż
fdµ
⏐⏐⏐⏐ ď
⏐⏐⏐⏐
ż
fndµn´
ż
fndµ
⏐⏐⏐⏐`
⏐⏐⏐⏐
ż
fndµ´
ż
fdµ
⏐⏐⏐⏐
and noting that the ﬁrst term goes to 0 by weak-˚ convergence and the second term goes to zero by uniform
convergence.
Problem 7. (a) Deﬁne unitary operator on a complex Hilbert space.
(b) Let S be a unitary operator on a complex Hilbert space. Prove that for every complex number |λ|ă 1
9

the operator S´λI is invertible.
(c) For a ﬁxed vector v in the Hilbert space and all |λ|ă 1, deﬁne
hpλq “
@
pS`λIqpS´λIq´1v,v
D
.
Show Rephq is a positive harmonic function (you may not use the spectral theorem).
Solution. (a) S :HÑH is unitary if xSx,Syy“x x,yy for all x,y PH.
(b) Suppose pS´λIqx“ 0 but x‰ 0. Then we have
0 “ xpS´λIqx,pS´λIqxy “ xSx´λx,Sx ´λxy “ ||Sx||2`|λ|2||x||2´ 2 Repλxx,Sxyq
“ p1`|λ|2q||x||2´ 2 Repλxx,Sxyq.
Thus we have
p1`|λ|2q||x||2 “ 2 Repλxx,Sxyq ď 2|λ||xx,Sxy| ď 2|λ|||x||||Sx|| “ 2|λ|||x||2.
Since we are assuming x‰ 0 this implies p1`|λ|2qď 2|λ|, which is impossible for |λ|ă 1. Thus S´λI is
injective and therefore invertible.
(c)
Problem 8. Let Ω be an open convex region in the complex plane. Assume f is a holomorphic func-
tion on Ω and the Repf1pzqqą 0 for all zP Ω.
(a) Prove that f is one-to-one.
(b) Show by example that the word “convex” cannot be replaced by “connected and simply connected”.
Solution. (a) Let a‰ bP Ω. Let γ be a straight line from a to b, parameterized by γptq“p 1´tqb`ta.
By convexity,γ lies in Ω. So we can write
ş
γf1pzqdz “ fpbq´ fpaq. Write f“u`iv, then f1“ux`ivx.
Examining the integral above, we have
fpbq´ fpaq “
ż
γ
f1pzqdz “
ż 1
0
puxpγptqq` ivxpγptqqqpb´aqdt “ pb´aq
ż 1
0
puxpγptqq` ivxpγptqqqdt.
Note that the integral on the right side has nonzero real part because ux is always positive. Thus the whole
right side is just some nonzero complex number since b´a is a nonzero constant, so fpbq‰ fpaq.
Problem 9. Let f be a non-constant meromorphic function on C that obeys
fpzq “ fpz`
?
2q “ fpz`i
?
2q.
Assume f has at most one pole in the closed unit disc D.
(a) Prove that f has exactly one pole in D.
(b) Prove that this is not a simple pole.
Solution. (a) We just need to show f has at least one pole in D. Let Λ “ r0,
?
2sˆr 0,i
?
2s be a
fundamental domain for f and let M be the discrete lattice generated by
?
2 and i
?
2. Simple geometry
shows that every point of Λ is at most 1 away from one of the vertices. Thus every point of Λ is equivalent
mod M to some point of D. Since f is non-constant and doubly periodic, it must have a pole somewhere
(otherwise it would be holomorphic and bounded and therefore constant), so it must have a pole in Λ, and
thus must have a pole in D.
(b) The work in part (a) shows that every point of C is equivalent mod M to some point of D, so the
fact thatf has exactly one pole in D implies thatf has exactly one distinct pole mod M. The desired result
now follows from the general fact that a doubly periodic function can’t have only a single simple pole (mod
10

M), a proof of which is reproduced here (see e.g. Ahlfors Complex Analysis). Since the zeros and poles of
f are discrete, we can ﬁnd a fundamental domain Λ of M such that f has no zeros or poles on BΛ. Thus
by double periodicity, it is clear that
ş
BΛfpzqdz“ 0 because the integrals over opposite sides of Λ going in
opposite directions cancel each other out. So by the residue theorem, the sums of residues of all the poles
inside Λ is 0, implying there can’t only be one simple pole.
11

3 Spring 2010
Problem 1. (a) Let 1 ďpă8 . Show that if a sequence of real-valued functions tfnu converges in LppRq,
then it contains a subsequence that converges almost everywhere.
(b) Give an example of a sequence of functions converging to 0 in L2pRq that does not converge almost
everywhere.
Solution.
Problem 2. Let p1,...,p n be distinct points in C and let U be the domain Cztp1,...,p nu. Let A be
the vector space of real harmonic functions on U and let B Ď A be the subspace of real parts of complex
analytic functions on U. Find the dimension of the quotient space A{B and give a basis.
Solution. See Spring 2017 #10.
Problem 3. For f : R Ñ R in L1pRq, let Mf be the (centered) Hardy-Littlewood maximal function.
Prove there is a constant A such that for any λą 0,
mtxP R :Mfpxqą λu ď A
λ||f||L1
where m is Lebesgue measure. If you use a covering lemma, you should prove it.
Solution. See Fall 2011 #5.
Problem 4. Let fpzq be a continuous function on D such that f is analytic on D and fp0q‰ 0.
(a) Prove that if 0 ără 1 and if inf|z|“r|fpzq|ą 0, then
1
2π
ż 2π
0
log
⏐⏐fpreiθq
⏐⏐ dθ ě log |fp0q|.
(b) Prove that mtθPr 0, 2πs :fpeiθq“ 0u“ 0 where m is Lebesgue measure.
Solution. See Fall 2016 #8.
Problem 5. (a) ForfPL2pRq and a sequencetxnuĎ R which converges to zero, deﬁnefnpxq :“fpx`xnq.
Show thattfnu converges to f in L2.
(b) Let W Ď R be a Lebesgue measurable set of positive Lebesgue measure. Show that the set of diﬀerences
W´W “tx´y :x,y PWu contains an open neighborhood of the origin.
Solution. (a) See Fall 2011 #3.
(b) Let fpxq“ χWpxq and fypxq“ χWpx`yq. We calculate
||f´fy||2
L2 “
ż
pχWpxq´ χWpx`yqq2dx
“
ż
χWpxq2`χWpx`yq2´ 2χWpxqχWpx`yqdx
“ 2mpWq´ 2
ż
χWpxqχWpx`yqdx.
By part (a), this quantity goes to 0 as yÑ 0. Thus for all y suﬃciently small,
ż
χWpxqχWpx`yqdx ą 1
2mpWq ą 0.
In particular, there is at least onex such thatχWpxqχWpx`yq“ 1, i.e. xPW andx`yPW , soyPW´W .
ThusW´W contains all suﬃciently small y, as desired.
12

Problem 6. Let µ be a ﬁnite, positive, regular Borel measure supported on a compact subset of C and
deﬁne the Newtonian potential
Uµpzq “
ż
C
⏐⏐⏐⏐
1
z´w
⏐⏐⏐⏐ dµpwq.
(a) Prove that Uµ exists at Lebesgue almost all zP C and that
ĳ
K
Uµpzqdxdy ă 8
for every compact KĎ C.
(b) Prove that for almost every horizontal or vertical line LĎ C, µpLq“ 0 and
ş
KUµpzqdsă8 for every
compact subset KĎL, where ds denotes Lebesgue linear measure on L.
(c) Deﬁne the Cauchy potential of µ to be
ż
C
1
z´wdµpwq.
LetR be a rectangle in C whose four sides are contained in lines L having the conclusions of (b). Prove that
1
2πi
ż
BR
Sµpzqdz “ µpRq.
Solution. See Spring 2009 #7.
Problem 7. Let H be a Hilbert space and let E be a closed convex subset of H. Prove that there
exists a unique element xPE such that
||x|| “
ż
yPE
||y||.
Solution. See Fall 2012 #3
Problem 8. LetFpzq be a non-constant meromorphic function on the complex plane C such thatFpz`1q“
Fpzq“ Fpz`iq for all z. Let Q be a square with vertices z, z` 1, z`i, and z` 1`i such that F has
no zeros and no poles on BQ. Prove that inside Q the function F has the same number of zeros as poles
(counting multiplicities).
Solution.
Problem 9. Let
A “ txP𝓁2 :
ÿ
ně1
n|xn|2 ď 1u.
(a) Show that A is compact in the 𝓁2 topology.
(b) Show that the mapping from A to R deﬁned by
xÞÑ
ż 2π
0
⏐⏐⏐⏐⏐
ÿ
ně1
xneinθ
⏐⏐⏐⏐⏐
dθ
2π
achieves its maximum on A.
Solution.
13

Problem 10. Let Ω Ď C be a connected open set, let z0 P Ω, and let U be the set of positive har-
monic functions U on Ω such that Upz0q “1. Prove that for every compact set K Ď Ω there is a ﬁnite
constantM such that
sup
UPU
sup
zPK
Upzq ď M.
Solution.
Problem 11. Let φ : RÑ R be a continuous function with compact support.
(a) Prove there is a constant A such that
||f˚φ||Lq ď A||f||Lp for all 1 ďpďqď8 and all fPLp.
If you use Young’s convolution inequality you should prove it.
(b) Show by example that such a general inequality cannot hold for pąq.
Solution. (a) Deﬁne α to be the number ě 1 so that 1 {α “ 1{q´ 1{p` 1 (if q “ 8and p “ 1 then
α“8 ). Then 1{q` 1“ 1{p` 1{α, so by Young’s convolution inequality we have
||f˚φ||Lq ď ||f||Lp||φ||Lα ď sup
xPR
|φpxq|¨|| f||Lp
as desired. Now we prove Young’s convolution inequality: the statement is that if 1 {p` 1{q“ 1{r` 1, and
f P Lp and g P Lq, then ||f˚g||Lr ď||f||Lp||g||Lq. Proof: note that the condition on p,q,r implies that
1{p, 1{qě 1{r. We have
1 “ 1
p` 1
q´ 1
r “
ˆ1
p´ 1
r
˙
`
ˆ1
q´ 1
r
˙
` 1
r “ r´p
pr ` r´q
qr ` 1
r.
By H¨ older using the three conjugate exponents above, we have
|pf˚gqpxq| ď
ż
|fpx´yqgpyq| dy
ď
ż
|fpx´yq|pr´pq{r|gpyq|pr´qq{r|fpx´yqp{rgpyqq{r|dy
ď
ˆż
|fpx´yq|pdy
˙pr´pq{prˆż
|gpyq|qdy
˙pr´qq{prˆż
|fpx´yqpgpyqq|dy
˙1{r
“ ||f||pr´pq{r
Lp ||g||pr´qq{r
Lq
ˆż
|fpx´yqpgpyqq|dy
˙1{r
.
Thus
||f˚g||r
Lr “
ż
|pf˚gqpxq|rdx ď ||f||r´p
Lp ||g||r´q
Lq
ż ż
|fpx´yqpgpyqq|dydx
“||f||r´p
Lp ||g||r´q
Lq
ż ż
|fpx´yqpgpyqq|dxdy by Tonelli
“ ||f||r
Lp||g||r
Lq.
(b) Fix p ą q. Let φ be equal to 1 on r0, 1s, have support contained in r´1, 2s, and have 0 ď φ ď 1
everywhere. Fix 1 {α P pq,pq and let fpyq “1{yα for y P r10,8q and 0 otherwise. Note that f P Lp but
fRLq. We have, for all xą 100,
pf˚φqpxq “
ż
fpx´yqφpyqdy ě
ż 1
0
fpx´yqdy “
żx
x´1
fpyqdy “
żx
x´1
1
yα dy ě 1
xα.
Thusf˚φRLq, so the inequality fails.
14

Problem 12. Let F be a function from D to D such that whenever z1,z 2,z 3 are distinct points of D
there exists an analytic function fz1,z2,z3 from D into D such that Fpzjq “fz1,z2,z3pzjq. Prove that F is
analytic at every point of D.
Solution.
Problem 13. Let X and Y be Banach spaces. A bounded linear transformation A : X Ñ Y is com-
pact if for every bounded sequence txnu ĎX, the sequence tAxnu has a convergent subsequence in Y .
Suppose X is reﬂexive pX˚˚ “ Xq and X˚ is separable. Show that A : X Ñ Y is compact if and only
if for every bounded sequence txnu ĎX, there exists a subsequence txnju and a vector φP X such that
xnj “φ`rnj and Arnj Ñ 0 in Y .
Solution.
15

4 Fall 2010
Problem 1. Consider just Lebesgue measurable functiions f :r0, 1sÑ R together with Lebesgue measure.
(a) State Fatou’s lemma,
(b) State and prove the Dominated Convergence Theorem.
(c) Give an example where fnpxqÑ 0 a.e. but
ş
fnpxqdxÑ 1.
Solution. (a) If fn are non-negative, then
ş
lim infnÑ8fnď lim infnÑ8
ş
fn.
(b) If fnÑf almost everywhere and|fn|ď g for some integrable function g and all fn, then
ş
|f´fn|Ñ 0.
Proof: Since |fn| ďg and fn Ñ f almost everywhere, we also have |f| ďg almost everywhere, so the
functions 2g´|f´fn| are non-negative. Thus we can apply Fatou’s lemma to get
ż
lim inf
nÑ8
2g´|f´fn| ď lim inf
nÑ8
ż
p2g´|f´fn|q.
The left side simpliﬁes to
ş
2g and the right side simpliﬁes to
ş
2g´ lim supnÑ8
ş
|f´fn|. Thus by canceling
and rearranging we get lim sup
ş
|f´fn|ď 0, and since it’s a limsup of non-negative quantities this implies
the limit exists and equals 0.
(c) Let fn“n¨χr0,1{ns. fnÑ 0 almost everywhere but
ş
fn“ 1 for all n.
Problem 2. Prove the following form of Jensen’s inequality: if f :r0, 1sÑ R is continuous, then
ż 1
0
efpxqdx ě exp
ˆż 1
0
fpxqdx
˙
.
Moreover, if equality occurs then f is a constant function.
Solution. Let u “
ş1
0fpxqdx. Let L be the tangent line to the graph of y “ ex at x “ u. Say L has
the equation y“ax`b. Since exp is convex, we know that au`b“eu andat`băet for all t‰u. So we
have
au`b “ a
ż 1
0
fpxqdx`b “
ż 1
0
pafpxq` bqdx ď
ż 1
0
efpxqdx
by deﬁnition of the line y“ax`b. Furthermore, if equality holds in the last step, we must have fpxq“ u
for all x. This is because f is continuous, so if fpxq‰ u somewhere, then f‰u on some open interval, and
for all x in that interval we would have afpxq` băefpxq, leading to a strict inequality above.
Problem 3. Consider the following sequence of functions:
fn :r0, 1sÑ R by fnpxq “ exppsinp2πnxqq.
(a) Prove that fn converges weakly in L1pr0, 1sq.
(b) Prove that fn converges weak-˚ in L8pr0, 1sq, viewed as the dual of L1pr0, 1sq.
Solution. (a) This requires showing the existence of some f P L1 with
ş
fng Ñ
ş
fg for all g P L8.
Since L8pr0, 1sqĎ L1pr0, 1sq, this conclusion is implied by part (b) below.
(b) We need to ﬁnd some f P L8 such that
ş
fng Ñ
ş
fg for all g P L1. First note that each fn is
1{n-periodic, so we have
ż 1
0
fnpxqdx “
ż 1
0
exppsinp2πnxqqdx “ n
ż 1{n
0
exppsinp2πnxqq “
ż 1
0
exppsinp2πuqqdu “
ż 1
0
f1puqdu.
Thus the quantity
ş1
0fnpxqdx is independent of n. By viewing this as the dual pairing with the constant
function 1, we see that if the weak limit f exists it must be equal to the constant C :“
ş1
0 exppsinp2πuqqdu.
16

So we need to show that
ş1
0fng Ñ C
ş1
0g for any g P L1. We do this with a standard density argument.
Suppose we knew the desired conclusion for all φ in some family F dense in L1. Then for any gPL1, let φk
be a sequence in F converging to g, then we have
⏐⏐⏐⏐
ż
fng´C
ż
g
⏐⏐⏐⏐ ď
⏐⏐⏐⏐
ż
fng´
ż
fnφk
⏐⏐⏐⏐`
⏐⏐⏐⏐
ż
fnφk´
ż
Cφk
⏐⏐⏐⏐ ď e¨||g´φk||L1`
⏐⏐⏐⏐
ż
fnφk´
ż
Cφk
⏐⏐⏐⏐
because each fn is bounded uniformly by e. For a ﬁxed k, take nÑ8 and the second term on the right
goes to zero by assumption on the φk. Then take kÑ8 and the ﬁrst term also goes to zero by construction,
so the desired result follows. Now we just need to prove the desired result for a dense family F. We take
F to be the set of linear combinations of characteristic functions of closed intervals. Since the desired
property is linear, it’s enough to verify for the characteristic function g “ χra,bs. We need to show thatşb
a exppsinp2πnxqqdxÑCpb´aq as nÑ8 . Let an be the least number of the form q{nąa and bn be the
greatest number of the form q{năb. Then we write, using the periodicity,
żb
a
exppsinp2πnxqqdx “
˜żan
a
`
żb
bn
`ptpb´aqnu´ 2q
żan`1{n
an
¸
exppsinp2πnxqqdx
“ epan´aq` epb´bnq`p tpb´aqnu´ 2q
ż 1{n
0
exppsinp2πnxqqdx
“epan´aq` epb´bnq` tpb´aqnu´ 2
n C
which tends to pb´aqC as nÑ8 , so we’re done.
Problem 4. Let T be a linear transformation on CcpRq (continuous functions with compact support)
that has the following two properties:
||Tf||L8 ď ||f||L8 and mtxP R :|Tfpxq|ą λu ď ||f||L1
λ
where m denotes Lebesgue measure. Prove that
ż
|Tfpxq|2dx ď C
ż
|fpxq|2dx
for all fPCcpRq and some ﬁxed number C.
Solution. We mimic the proof of the Hardy-Littlewood maximal theorem, with a few annoying things
changed becauseT is only deﬁned for Cc functions. First we will establish the result when f is a real-valued,
non-negative function, and extend it at the end. We use the identity
ż
|Tf|2 “ 2
ż8
0
λ¨mtx :|Tfpxq|ą λudλ.
For each ﬁxedλ, we have the decomposition f“g`h whereh :“ minpf,λ{2q andg :“f´h“ 0 if făλ{2
and f´λ{2 if f ą λ{2. Note that both g and h are continuous and non-negative with compact support.
Then we have Tf “Tg `Th , so |Tf|ď| Tg|`| Th|, which implies that
tx :|Tfpxq|ą λu Ď tx :|Tgpxq|ą λ{2uYt x :|Thpxq|ą λ{2u.
But we have||Th||L8ď||h||L8ďλ{2 by construction, so the second set has measure zero and we just have
(up to measure zero sets)
tx :|Tfpxq|ą λu Ď tx :|Tgpxq|ą λ{2u.
17

Thus we have
ż
|Tf|2 ď 2
ż8
0
λ¨mtx :|Tgpxq|ą λ{2udλ
À
ż8
0
λ2||g||L1
λ dλ by the weak-type hypothesis
À
ż8
0
ż
R
|gpxq|dxdλ “
ż8
0
ż
tx:fpxqąλ{2u
pfpxq´ λ{2qdxdλ ď
ż8
0
ż
tx:fpxqąλ{2u
fpxqdxdλ
“
ż
R
|fpxq|
ż 2|fpxq|
0
dλdx by Tonelli
À
ż
R
|fpxq|2dx.
This establishes the result for positive real-valued f. For general real-valued f, write f“f`´f´. Then we
have
ż
|Tf|2 “
ż
|Tf`´Tf´|2 “
ż
|Tf`|2`|Tf´|2`|Tf`||Tf´|
ď
ż
|Tf`|2`
ż
|Tf´|2 À ||f`||2
L2`||f´||2
L2 “ ||f||2
L2
where the last equality is valid by the Pythagorean theorem because since f`pxqf´pxq “0 for all x, f`
and f´ are orthogonal. This establishes the result for general real-valued f. For complex-valued f, write
f“ Repfq` i Impfq, then we have
ż
|Tf|2 “
ż
|T Repfq` iT Impfq|2 “
ż
|T Repfq|2`|T Impfq|2 À
ż
| Repfq|2`| Impfq|2 “
ż
|f|2,
so we’re done.
Problem 5. Let R{Z denote the torus (whose elements we write as cosets) and ﬁx an irrational αą 0.
(a) Show that
lim
NÑ8
1
N
N´1ÿ
n“0
fpnα` Zq “
ż 1
0
fpx` Zqdx
for all continuous functions f : R{ZÑ R.
(b) Show that the conclusion is also true when f is the characteristic function of a closed interval.
Solution. (a) Deﬁne ANpfq “ 1
N
řN´1
n“0 fpnα` Zq and Ipfq “
ş1
0fpx` Zqdx. First we show the con-
clusion when f is a trig polynomial. By linearity, it’s enough to assume fpxq“ e2πikx for some k P Z. If
k“ 0 then both sides are clearly equal to 1 so assume k‰ 0. Then we have
ANpfq “ 1
N
N´1ÿ
n“0
pe2πikαqn “ 1
N
1´e2πikαN
1´e2πikα Ñ 0 as NÑ8
Ipfq “
ż 1
0
e2πikxdx “ 0.
So the result is veriﬁed for trig polynomials. Now for general f P CpR{Zq, ﬁx ϵ ą 0 and let P be a trig
polynomial with ||f´P||L8ăϵ. Then we have
|ANpfq´ Ipfq| ď |ANpfq´ ANpPq|`| ANpPq´ IpPq|`| IpPq´ Ipfq|
ď 2ϵ`|ANpPq´ IpPq|.
First take N Ñ8 , then we see that |limNÑ8ANpfq´ Ipfq|ă 2ϵ, and since this holds for arbitrary ϵ, the
desired result follows.
18

(b) Let f “χra,bs. Let gk and hk be sequences of continuous functions satisfying 0 ďgk ďf ďhk ď 1 for
all k, and gk and hk both converge almost everywhere to f as kÑ8 (it’s clear that such sequences exist
by just taking the graph of f and smoothing it out a bit). Then for each N and k we have
ANpgkq ď ANpfq ď ANphkq, I pgkq ď Ipfq ď Iphkq.
Fork ﬁxed, take NÑ8 . Since gk and hk are continuous, this implies that
Ipgkq ď lim inf
NÑ8
ANpfq ď lim sup
NÑ8
ANpfq ď Iphkq.
Since everything is dominated by 1 and we have pointwise convergence almost everywhere, by the dominated
convergence theorem we can take kÑ8 and get
Ipfq ď lim inf
NÑ8
ANpfq ď lim sup
NÑ8
ANpfq ď Ipfq,
which implies the desired result.
Problem 6. Consider the complex Hilbert space
H :“
#
f : DÑ C :fpzq“
8ÿ
k“0
pfpkqzk with ||f||2 :“
8ÿ
k“0
p1`k2q|pfpkq|2ă8
+
.
(a) Prove that the linear function L :fÞÑfp1q is bounded.
(b) Find the element gPH representingL.
(c) Show that fÞÑ ReLpfq achieves its maximal value on the set
B :“ tfPH :||f||ď 1 and fp0q“ 0u,
that this maximum occurs at a unique point, and determine this maximal value.
Solution. (a) We have
|fp1q| ď
8ÿ
k“0
|pfpkq| “
8ÿ
k“0
|pfpkq|
a
1`k2 1?
1`k2 ď
˜ 8ÿ
k“0
|pfpkq|2p1`k2q
¸1{2˜ 8ÿ
k“0
1
1`k2
¸1{2
“ C||f||
where C2“ ř8
k“0
1
1`k2 ă8 .
(b) We are implicitly assuming the inner product in H is given by
xf,gy “
8ÿ
k“0
pfpkqpgpkqp1`k2q.
If g representsL then we must have
xf,gy “
8ÿ
k“0
pfpkqpgpkqp1`k2q “ fp1q “
8ÿ
k“0
pfpkq.
It’s clear that if pgpkq“ 1
1`k2 then this would be satisﬁed. So we can just deﬁne
gpzq “
8ÿ
k“0
1
1`k2zk.
The series converges uniformly on D so this deﬁnition actually makes sense (and in fact is holomorphic, but
that’s not necessary).
19

(c) First we note that the maximum value of Re pLpfqq on B must happen when ||f|| “ 1, otherwise
we could normalize f and increase the value of Re pLpfqq. The condition that fp0q “ 0 corresponds to
having pfp0q “0. So the problem is reduced to maximizing ř8
k“1 Reppfpkqq subject to the condition thatř8
k“1p1`k2q|pfpkq|2 “ 1. Note that the constraint only depends on |pfpkq|. Thus we can always increase
Repfp1qq while keeping the norm constant if we assume that each pfpkq is real and positive. So without loss
of generality we can assume each pfpkq ě0. Using the same Cauchy-Schwarz argument from part (a), we
have
8ÿ
k“1
pfpkq ď
˜ 8ÿ
k“1
|pfpkq|2p1`k2q
¸1{2˜ 8ÿ
k“1
1
1`k2
¸1{2
“
˜ 8ÿ
k“1
1
1`k2
¸1{2
and equality holds if and only if pfpkq
?
1`k2“ α?
1`k2 for some αP R. This shows that that maximum on
B is achieved at a unique point, i.e.
fpzq “
8ÿ
k“1
α
1`k2zk.
Also, this α is determined by the condition that f has norm 1:
1 “
8ÿ
k“1
p1`k2q|pfpkq|2 “
8ÿ
k“1
α2
1`k2,
so α“
´ř8
k“1
1
1`k2
¯´1{2
. Thus the maximum value achieved is
8ÿ
k“1
α
1`k2 “
˜ 8ÿ
k“1
1
1`k2
¸1{2
.
Problem 7. Suppopse that f : C Ñ C is continuous and holomorphic on CzR. Prove that f is en-
tire.
Solution. By Morera’s theorem it’s enough to show that the integral around any rectangle with sides
parallel to the axes is zero. Let R be any rectangle. If R doesn’t intersect the real axis, the integral is
obviously zero by hypothesis. If R does intersect the real axis, break up R into two pieces, one in the upper
half plane and one in the lower, and by continuity the integral over R is equal to limit of the integrals as the
two pieces approach the real axis, so you still get zero (this is a really standard argument).
Problem 8. Let ApDq be the C-vector space of all holomorphic functions on D and suppose that L :
ApDqÑ C is a multiplicative linear functional. If L is not identically zero, show that there is a z0 P D so
that Lpfq“ fpz0q for all fPApDq.
Solution. Note that if this were true, then we would have to have Lpzq “z0. So deﬁne z0 :“ Lpzq
and we want to show that Lpfq“ fpz0q for any f PApDq. Since we are assuming that L is not identically
zero, letf be such thatLpfq‰ 0. Then because L is multiplicative we can writeLpfq“ Lpf¨1q“ LpfqLp1q,
so Lp1q“ 1. This, combined with the linear and multiplicative hypotheses again, imply that LpPq“ Ppz0q
for any polynomial P . Now let f be any element of ApDq. We can write fpzq´fpz0q“p z´z0qgpzq for some
other gPApDq. Therefore we have
Lpfq´ fpz0q “ Lppz´z0qgpzqq “ pLpzq´ z0qLpgq “ 0,
which establishes the desired result. The only thing left to check is that we actually have z0 P D. If not,
then 1{pz´z0q would be in ApDq, and so we would have
Lp1{pz´z0qq “ 1{Lpz´z0q “ 1{pz0´z0q,
20

a contradiction.
Problem 9. Let
fpzq “
8ÿ
n“0
anzn
be a holomorphic function in D. Show that if
8ÿ
n“2
n|an| ď |a1|
with a1‰ 0 then f is injective.
Solution. We havef1pzq“ ř8
n“1nanzn´1. Thus for any ﬁxed zP D we have
|f1pzq| “
⏐⏐⏐⏐⏐
8ÿ
n“1
nanzn´1
⏐⏐⏐⏐⏐ ě |a1|´
8ÿ
n“2
n|an||z|n ą |a1|´
8ÿ
n“2
a|an| ě 0,
so f1 is nonvanishing in D.
Problem 10. Prove that the punctured disc tz : 0 ă |z| ă1u and the annulus tz : 1 ă |z| ă2u are
not conformally equivalent.
Solution. Let P be the punctured disc and A be the annulus. Suppose f : P Ñ A is conformal. Then,
since A is bounded, the singularity of f at 0 must be removable. So we extend f to a holomorphic function
f : D Ñ A. If we knew that f were still conformal, this would be a contradiction because D is simply
connected but A is not. We already know f is holomorphic and surjective, so to show f is conformal we just
need to show that f is still injective when we extend it to be deﬁned at 0. Suppose fp0q“ fpzq with zPP
(this is the only possibility because f is injective on P ). Let U andV be disjoint open balls around 0 and z
respectively. By the open mapping theorem, fpUq andfpVq are open. They interset at fp0q“ fpzq, so their
intersection is open and non-empty, and therefore in particular there is some other point wPfpUqX fpVq.
So we have z1 P U, z2 P V with fpz1q“ fpz2q. But z1 ‰ 0 because w‰ fp0q, so this contradicts the fact
that f is injective on P .
Problem 11. Let Ω Ď C be a non-empty open connected set. If f : Ω Ñ C is harmonic and f2 is
also harmonic, show that either f or f is holomorphic on Ω.
Solution. Recall the Wirtinger derivates Bz “ p1{2qpBx´iByq and Bz “ p1{2qpBx`iByq. A straightfor-
ward computation veriﬁes the identity ∆ “ 4BzBz. By hypothesis, f2 is harmonic, so ∆f2“ 0. Putting this
into the above identity and using the chain and product rules and the hypothesis that f is also harmonic,
this reduces to pBzfqpBzfq“ 0. Suppose f is not holomorphic. Then there is a point in Ω at which Bzf‰ 0.
By continuity,Bzf is nonzero on an open ball, so Bzf “ 0 on an open ball. Since f is harmonic, Bz also
is (because Bx andBy both are). But then we have a harmonic function on all of Ω which vanishes on an
open ball. In particular it has a local maximum on that open ball, so the maximum principle implies Bzf is
constant and therefore identically zero, so f is holomorphic.
Problem 12. Let F be the family of functions f holomorphic on D with
ĳ
x2`y2ă1
|fpx`iyq|2dxdy ă 1.
Prove that for each compact subsetKĎ D there is a constantA so that|fpzq|ă A for allzPK and allfP F.
Solution. See e.g. the ﬁrst half of Fall 2014 #10.
21

5 Spring 2011
Problem 1.
(a) Deﬁne what it means to say that fnÑf weakly in L2pr0, 1sq.
(b) Suppose fnPL2pr0, 1sq converge weakly to fPL2pr0, 1sq and deﬁne ‘primitive’ functions
Fnpxq :“
żx
0
fnptqdt and Fpxq :“
żx
0
fptqdt.
Show that Fn,F PCpr0, 1sq and that FnÑF uniformly on r0, 1s.
Solution.
(a) For every gPL2pr0, 1sq, limnÑ8
ş1
0fnpxqgpxqdx“
ş1
0fpxqgpxqdx.
(b) First, we know that weakly convergent sequences are bounded, so we can say ||fn||L2 ď M for all n.
To show that Fn and F are continuous, note that
|Fnpx`hq´ Fnpxq| ď
żx`h
x
|fnptq|dt ď
˜żx`h
x
|fnptq|2dt
¸1{2˜żx`h
x
1dt
¸1{2
ď M|h|1{2.
Note that the above estimate for |Fnpx`hq´ Fnpxq| is independent of both n andx, so we have actu-
ally shown thattFnu is an equicontinuous family of functions. A similar estimate shows|Fpx`hq´ Fpxq|ď
||f||L2|h|1{2, so F is also continuous. Now we show FnÑF uniformly. First note that
|Fnpxq| ď
żx
0
|fnptq|dt ď
ˆżx
0
|fnptq|2dt
˙1{2
x1{2 ď M,
so Fn is also a uniformly bounded family. To show that Fn Ñ F uniformly, it’s enough to show
that any subsequence of Fn has a further subsequence converging uniformly to F . Let Fnk be any
subsequence. We have shown it is a uniformly bounded and equicontinuous family, so by Arzela-Ascoli
it has a further subsequence converging uniformly to some function g. But note that for each x,
lim
nÑ8
Fnpxq “ lim
nÑ8
żx
0
fnptqdt “ lim
nÑ8
ż 1
0
fnptqχr0,xsptqdt “
ż 1
0
fptqχr0,xsptqdt “
żx
0
fptqdt “ Fpxq
by weak convergence becauseχr0,xsPL2pr0, 1sq. Thus, since Fn converges pointwise toF , and Fnk has
a subsequence converging uniformly to some g, we must in fact have g“F . Thus every subsequence
Fnk has a further subsequence converging uniformly to F , so FnÑF uniformly.
Problem 2. Let fPL3pRq and φpxq“ sinpπxq¨ χr´1,1spxq. Show that
fnpxq :“ n
ż
fpx´yqφpnyqdyÑ 0
Lebesgue almost everywhere.
Solution. Letφnpxq“ nφpnxq. Let gpxq“´ φpxqχr´1,0s be the negative part of φ and lethpxq“ φpxqχr0,1s
be the positive part. Also deﬁne gn and hn similarly to φn. Note that φn “ hn´gn so to show that
f˚φnÑ 0 a.e. it’s enough to show that f˚gn,f ˚hnÑpπ{2qf a.e. We show it for hn and the argument
22

for gn is exactly the same. First note that
ş
hnpxqdx“
ş1{n
0 sinpnπxqdx“ 2{π. We have
⏐⏐⏐pf˚hnqpxq´ π
2fpxq
⏐⏐⏐ “
⏐⏐⏐⏐⏐
ż 1{n
0
fpx´yqn sinpnπyqdy´
ż 1{n
0
fpxqn sinpnπyqdy
⏐⏐⏐⏐⏐
ď n
ż 1{n
0
|fpx´yq´ fpxq| |sinpnπyq| dy
ď n
ż 1{n
0
|fpx´yq´ fpxq| dy,
which goes to 0 almost everywhere by the Lebesgue diﬀerentiation theorem ( fPL1
loc because fPL3).
Problem 3. Let µ be a Borel probability measure on R and deﬁne fptq“
ş
eitxdµpxq. Suppose that
lim
tÑ0
fp0q´ fptq
t2 “ 0.
Show that µ is supported at 0.
Solution. Rewrite the limit condition as
lim
tÑ0
ż 1´eitx
t2 dµpxq “ 0.
Just looking at the real part of the above gives
lim
tÑ0
ż 1´ cosptxq
t2 dµpxq “ 0.
Since the integrand is positive for all t,x , by Fatou’s lemma we have
0 “ lim
tÑ0
ż 1´ cosptxq
t2 dµpxq ě
ż
lim
tÑ0
1´ cosptxq
t2 dµpxq “
ż 1
2x2dµpxq,
and since the last term on the right is also non-negative, we have
ş
x2dµpxq “ 0. This immediately
implies that µ is supported at 0 because if µ gave nonzero measure to Rzt0u, it would have to give
positive measure to some set of the form p´8,´δsXr δ,8q for some δ ą 0, and then we would haveş
x2dµpxqą δ2µpp´8,´δsXr δ,8qqą 0, a contradiction.
Problem 4. Let fn :r0, 1sÑr 0,8q be Borel functions with
sup
n
ż 1
0
fnpxq logp2`fnpxqqdx ď M ă 8.
Suppose fnÑf Lebesgue almost everywhere. Show that fPL1 and fnÑf in L1.
Solution. By Fatou’s lemma (since everything is positive) we have
M ě lim inf
nÑ8
ż 1
0
fnpxq logp2`fnpxqqdx ě
ż 1
0
fpxq logp2`fpxqqdx ě logp2q
ż 1
0
fpxqdx,
so f PL1. Now to show fnÑf in L1, we ﬁrst want to establish the following claim: for all ϵą 0 there is
δą 0 such that for any n and any EĎr 0, 1s, mpEqă δ implies
ş
Efpxqdxăϵ. Suppose this were not true,
then there would be a sequence of sets Ek and functions fnk with mpEkqă 1{k and
ş
Ek
fnk ěϵ. Then by
Jensen’s inequality, since tÞÑt logp2`tq is convex, we would have
ˆ 1
mpEkq
ż
Ek
fnk
˙
log
ˆ
2` 1
mpEkq
ż
Ek
fnk
˙
ď 1
mpEkq
ż
Ek
fnk logp2`fnkq ď 1
mpEkqM.
23

Cancelling terms on both sides and using the fact that tÞÑt logp2`tq is also increasing, we get
M ě ϵ logp2`kϵq,
which is a contradiction for k large enough. Thus the claim is established. Now to ﬁnish the problem, ﬁx
ϵą 0. By the previous claim we can pick δą 0 so that mpEqă δ implies
ş
Efnăϵ for all n and
ş
Ef ăϵ.
By Egorov’s theorem, we can ﬁnd a set EĎr 0, 1s with fnÑf uniformly on Ec and mpEqă δ. Then
ż
|fn´f| ď
ż
Ec
|fn´f|`
ż
E
|fn|`
ż
E
|f| ď
ż
Ec
|fn´f|` 2ϵ.
First take nÑ8 , then take ϵÑ 0, and we get the desired result.
Problem 5. (a) Show that 𝓁8pZq contains continuum many functionsxα : ZÑ R obeying||xα||𝓁8“ 1 and
||xα´xβ||𝓁8ě 1 whenever α‰β.
(b) Deduce (assuming the axiom of choice) that the Banach space dual of 𝓁8pZq cannot contain a countable
dense subset.
(c) Deduce that 𝓁1pZq is not reﬂexive.
Solution. (a) For each subset α Ď Z, let xαpjq “1 if j P α and 0 otherwise. Then each ||xα||𝓁8 “ 1
and for any two distinct subsets α‰β, there is a point at which xα and xβ disagree, so ||xα´xβ||𝓁8 ě 1.
It’s standard that there are continuum many subsets of Z.
(b) Part (a) shows that the dual of 𝓁8 is not separable. So it just follows from the general fact that if
X is a Banach space and X˚ is separable, then X is also separable (see Fall 2014 #6).
(c) Recall that the dual of 𝓁1 is 𝓁8. If 𝓁1 is separable, then p𝓁1q˚˚ “ p𝓁8q˚ “ 𝓁1, which is separable,
so by part (b) 𝓁8 is also separable, a contradiction.
Problem 6. Suppose µ and ν are ﬁnite positive (regular) Borel measures on Rn. Prove the existence
and uniqueness of the Lebesgue decomposition: there are a unique pair of positive Borel measures µa and
µs such that
µ “ µa`µs, µ a!ν, µ sKν.
Solution. First we show uniqueness. Suppose that µ“ µa`µs “ µ1
a`µ1
s are two decompositions. It’s
enough to show that µs“µ1
s. Write Rn“XYY “X1YY1 whereνpYq“ νpY1q“ 0 andµspXq“ µ1
spX1q0.
By the absolute continuity of µa and µ1
a, we see that µspAq“ µ1
spAq for any A satisfying νpAq“ 0. For a
general set E, write
E “ pEXXXX1qYp EXY XX1qYp EXXXY1qYp EXY XY1q “: pEXXXX1qY rE.
Note that since νprEq“ 0 and EXXXX1 is contained in both X and X1 we have
µspEq “ µspEXXXX1q` µsprEq “ µ1
spEXXXX1q` µ1
sprEq “ µ1
spEq.
Thus the decomposition is unique. Now we show existence. Let λ“ µ`ν and note that since all of the
measures involved are positive,ν is clearly absolutely continuous with respect toλ. Let f“ dν
dλ be the Radon-
Nikodym derivative, and note that fě 0 because the measures are positive. Deﬁne X“tx :fpxq‰ 0u and
Y “t x : fpxq“ 0u. We deﬁne µspEq :“ µpEXYq and µapEq :“ µpEXXq. It’s clear that µs`µa “ µ.
We need to show that µs is singular to ν andµa is absolutely continuous with respect to ν. For the singular
part, note that X,Y are disjoint, Rn“XYY , µspXq“ 0 by deﬁnition, and
νpYq “
ż
Y
fdλ “ 0
24

by deﬁnition of X. This shows µsKν. For absolute continuity, suppose νpEq“ 0. Then we have
0 “ νpEq “
ż
E
fdλ “
ż
E
fdµ `
ż
E
fdν “
ż
E
fdµ “
ż
EXX
fdµ “
ż
EXX
fdµ a
because µs vanishes on X. But since f is strictly positive on EXX, the fact that
ş
EXXfdµ a“ 0 implies
that µapEXXq“ 0, which is the same as saying µapEq“ 0 by deﬁnition. Thus µa!ν.
Problem 7. Prove Goursat’s theorem: if f : C Ñ C is complex diﬀerentiable, then for every triangle
T Ď C ¿
BT
fpzqdz “ 0.
Solution.
Problem 10. Evaluate
sup
␣
Ref1pi{2q :f : HÑ D is holomorphic
(
.
Solution. We can freely post-compose f with a rotation, so it’s equivalent to ﬁnd |f1pi{2q| instead of
the real part. Let f be any holmorphic function HÑ D. Let ψ : DÑ D be an automorphism sending fpi{2q
to 0. Concretely, ψpzq“ z´fpi{2q
1´fpi{2qz . An easy calculation shows that
ψ1pfpi{2qq “ 1
1´|fpi{2q|2.
Let φ : DÑ H be a conformal map sending 0 to i{2. Concretely we can take φpzq“ 1
2¨ ´ipz`1q
z´1 . Another
easy calculation shows that φ1p0q“ i. Now ψ˝f˝φ is a holomorphic function D to D sending 0 to 0, so by
the Schwartz lemma we have
1 ě
⏐⏐pψ˝f˝φq1p0q
⏐⏐ “
⏐⏐ψ1pfpφp0qqqf1pφp0qqφ1p0q
⏐⏐ “ 1
1´|fpi{2q|2|f1pi{2q| ě |f1pi{2q|.
Thus the supremum in question is at most 1. Finally note that taking fpzq“ φ´1pzq“ 2z´i
2z`i, a calculation
shows that f1pi{2q“´ i. So 1 is achieved and therefore is the desired supremum.
25

6 Fall 2011
Problem 1. Prove Egorov’s theorem, that is:
Consider a sequence of measurable functions fn :r0, 1sÑ R that converges Lebesgue almost everywhere to
a measurable function f : r0, 1s ÑR. Then for any ϵ ą 0 there exists a measurable set E Ď r0, 1s with
measure λpEqă ϵ such that fn converges uniformly on r0, 1szE.
Solution. Let Z be the measure zero set of x for which fnpxq­Ñ fpxq and set I“r 0, 1szZ. Deﬁne
Enpkq :“ txPI :|fjpxq´ fpxq|ă 1{k for all jěnu.
Fix ϵą 0. First we show a lemma: For each k there is an Nk such that λpENkpkqqą 1´ϵ2´k. To see this,
ﬁx a k and note that by deﬁnition of pointwise convergence, we have Ť8
n“1Enpkq“ I. So by continuity of
measure from below we can pick Nk large enough so that λpENkpkqqą λpIq´ ϵ2´k“ 1´ϵ2´k. This proves
the lemma.
Now we upgrade to the full result. Deﬁne E :“ Ť8
k“1ENkpkqc. We have
λpEq ď
8ÿ
k“1
λpENkpkqcq ă
8ÿ
k“1
ϵ2´k “ ϵ.
We claim that fn Ñ f uniformly on Ec. Fix α ą 0. Pick k big enough so that 1 {k ă α. Then for any
xPEc, we have xPENkpkq, so něNk implies that |fnpxq´ fpxq|ă 1{kăα for all xPEc. Thus fnÑf
uniformly on Ec.
Problem 2.
(a) Let dσ denote surface measure on the unit sphere S2Ă R3. Note
ş
dσpxq“ 4π. For ξP R3, compute
ż
S2
eix¨ξdσpxq,
where¨ denotes the usual inner product on R3.
(b) Using this, or otherwise, show that the mapping
fÞÑ
ż
S2
ż
S2
fpx`yqdσpxqdσpyq
extends uniquely from the space of all C8 functions on R3 with compact support to a bounded linear
functional on L2pR3q.
Solution.
(a) It is clear that the integral in question depends only on |ξ| (a simple proof could be given if necessary,
using an orthogonal transformation and the change of variables formula). Therefore, given the mag-
nitude c“|ξ| of ξ, we are free to choose ξ so that the integral is as easy as possible to evaluate. We
choose ξ“p 0, 0,cq. Then
ż
S2
eix¨ξdσpxq“
ż
S2
cospcx3qdσpxq` i
ż
S2
sinpcx3qdσpxq“
ż
S2
cospcx3qdσpxq,
since sin is odd and S2 is symmetric about the origin. Using spherical coordinates, the last integral
equals
ż
S2
cospcx3qdσpxq“
ż 2π
0
żπ
0
cospc cosφq¨ sinφdφdθ
“´ 2π
c sinpc cosφq
ˇˇˇ
π
0
“ 4π sinc
c .
“ 4π sin|ξ|
|ξ| .
26

(b) For fPC8
c pR3q, deﬁne
Lpfq“
ż
S2
ż
S2
fpx`yqdσpxqdσpyq.
Since C8
c pR3q is dense in L2pR3q, to show that L extends uniquely to a bounded linear functional on
L2pR3q it will be enough to prove a bound of the form |Lpfq| ďC||f||2 for all f P C8
c pR3q (where
C is independent of f). Since f is smooth with compact support, it lies in the Schwartz space, and
therefore Fourier inversion applies and gives
fpxq“
ż
R3
e2πiξ¨x ˆfpξqdξ“
ż8
0
r2
ż
S2
e2πirx¨ξ ˆfprξqdσpξqdr
for all x P R3. (Note that since ˆf is in the Schwartz space as well, || ˆf||L8prS 2q decays faster than
any power of r, so the integral on the right is convergent.) Therefore, by Fubini’s theorem and the
calculation in (a),
Lpfq“
ż
S2
ż
S2
fpx`yqdσpxqdσpyq
“
ż
S2
ż
S2
ż8
0
r2
ż
S2
e2πirpx`yq¨ξ ˆfprξqdσpξqdrdσpxqdσpyq
“
ż8
0
r2
ż
S2
ˆfprξq
ż
S2
e2πirx¨ξdσpxq
ż
S2
e2πiry¨ξdσpyqdσpξqdr
“
ż8
0
r2
ż
S2
ˆfprξq
ˆsin 2πr
r
˙2
dσpξqdr
“
ż
R3
ˆfpξq
ˆsin 2π|ξ|
|ξ|
˙2
dξ.
Now, by the Plancherel theorem, ˆf P L2pR3q and || ˆf||2 “ ||f||2. Moreover, hpξq “
´
sin 2π|ξ|
|ξ|
¯2
is
in L2pR3q as well, since hpξq2 is bounded near zero and decays like |ξ|´4 near inﬁnity. Therefore,
Cauchy-Schwarz implies
|Lpfq|ď|| ˆf||2||h||2“C||f||2,
as required.
Problem 3. Let 1ăp,q ă8 with 1{p` 1{q“ 1. Let f PLppR3q and gPLqpR3q. Show (a) that f˚g is
continuous on R3 and (b) that pf˚gqpxqÑ 0 as |x|Ñ8 .
Solution. (a) Fix xP R3. We estimate
|pf˚gqpxq´p f˚gqpx`hq| “
⏐⏐⏐⏐
ż
R3
pfpx´yqgpyq´ fpx`h´yqgpyqqdy
⏐⏐⏐⏐
ď
ż
|gpyq||fpx`h´yq´ fpx´yq|dy
ď||g||Lq
ˆż
|fpx`h´yq´ fpx´yq|pdy
˙1{p
“ ||g||Lq
ˆż
|fpy`hq´ fpyq|pdy
˙1{p
.
So it suﬃces to show that
`ş
|fpy`hq´ fpyq|pdy
˘1{p
Ñ 0 as |h|Ñ 0. This is just the Lp continuity of the
translation operator, a proof of which is reproduced below.
27

For f P Lp deﬁne τhfpyq “fpy`hq. We want to show that ||τhf´f||Lp Ñ 0 as |h| Ñ0. First sup-
pose that φ P CcpR3q. Let S “ tx P R3 : distpx, supppφqq ď1u and let M “ λ3pSq ă 8. By uniform
continuity ofφ, let |h|ă 1 be small enough so that |τhφpxq´ φpxq|ă ϵ for all xP R3. Then
||τhφ´φ||p
Lp ď ϵpM,
so the result is true for CcpR3q functions. For general f PLppR3q, a standard density argument works: ﬁx
ϵą 0 and pick φPCcpR3q with||f´φ||Lpăϵ. Then
||τhf´f||Lp ď ||τhf´τhφ||Lp`||τhφ´φ||Lp`||φ´f||Lp ă 2ϵ`||τhφ´φ||Lp.
Take|h|Ñ 0 and then ϵÑ 0 and the result follows.
(b) Note that if f,g have compact support then f ˚g also does. Pick sequences fn,gk with fn Ñ f in
Lp, gkÑg inLq,||fn||Lpď||f||Lp,||gk||Lpď||g||Lp, and each fn,gk has compact support (e.g. just cut oﬀ
f andg at bigger and bigger balls). Fix ϵą 0 and pick n,k big enough so that ||fn´f||Lp,||gk´g||Lpăϵ.
Then for any xP R3 we have
|pf˚gqpxq| ď |pfn˚gkqpxq|` |ppf´fnq˚ gkqpxq|` |pf˚pg´gkqqpxq|
ď |pfn˚gkqpxq|`||pf´fnq˚ gk||L8`||f˚pg´gkq||L8
ď |pfn˚gkqpxq|`ϵ||g||Lq`ϵ||f||Lp.
Take|x|Ñ8 and conclude lim|x|Ñ8pf˚gqpxqď ϵp||f||Lp`||g||Lqq, then takeϵÑ 0 to get the desired result.
Problem 4. Let fPC8pr0,8qˆr 0, 1sq such that
ż8
0
ż 1
0
|Btfpt,xq|2p1`t2qdxdt ă8.
Prove that there exists a function gPL2pr0, 1sq such that fpt,¨q converges to gp¨q in L2pr0, 1sq as tÑ8 .
Solution. (There may be ways to make this proof more eﬃcient, but it seems correct as far as I can
tell.) For each t,fp¨,tq is inL2pr0, 1sq, so by Parseval’s theorem there exist complex numbersanptq such that
fpx,tq“
ÿ
nPZ
anptqe2πinx
in L2pr0, 1sq, where ř
n|anptq|2“||fp¨,tq||2ă8 . By Parseval again it is enough to prove the existence of a
sequencetbnunPZPl2pZq such that ÿ
nPZ
|anptq´ bn|2Ñ 0
as tÑ8 ; the function gpxq„ ř
nbne2πinx will then be the desired limit in L2pr0, 1sq. By completeness of
l2pZq, this is the same as showing that tanptqu is Cauchy in l2pZq astÑ8 . In other words, given ϵą 0, we
want to be able to ﬁnd T ą 0 so that s,t ąT implies
ÿ
nPZ
|anptq´ anpsq|2ăϵ.
Assume for the moment that the coeﬃcients anptq are continuously diﬀerentiable with respect to t and that
Btfpx,tq“
ÿ
nPZ
a1
nptqe2πinx
in L2pr0, 1sq for each t. Then by assumption, we have
ż8
0
ż 1
0
|Btfpt,xq|2p1`t2qdxdt “
ż8
0
˜ÿ
nPZ
|a1
nptq|2
¸
p1`t2qdt
“
ÿ
nPZ
ż8
0
|a1
nptq|2p1`t2qdtă8 (1)
28

(using the monotone convergence theorem to interchange the sum and integral). Since each anptq is C1, we
have
anpsq´ anptq“
żs
t
a1
npτqdτ.
Consequently, by Cauchy-Schwarz
ÿ
nPZ
|anpsq´ anptq|2“
ÿ
nPZ
⏐⏐⏐⏐
żs
t
a1
npτqdτ
⏐⏐⏐⏐
2
ď
ÿ
nPZ
ż8
t
τ 2|a1
npτq|2dτ
ż8
t
dτ
τ 2 (assuming sąt)
À
ÿ
nPZ
ż8
t
|a1
npτq|2p1`τ 2qdτ.
But by (1) above, this sum goes to 0 as t Ñ 8. Hence, tanptqun is Cauchy in l2pZq as t Ñ 8, and so
fp¨,tqÑ gp¨q in L2pr0, 1sq as tÑ8 .
Now we just have to justify the continuous diﬀerentiability of the coeﬃcientsanptq and the fact thatBtfpx,tq
equals ř
na1
nptqe2πinx in L2pr0, 1sq. For any t, let hą 0; then by smoothness of f onr0,8qˆr 0, 1s,
fpx,t `hq´ fpx,tq
h “
ÿ
nPZ
anpt`hq´ anptq
h e2πinxÑB tfpx,tq
as hÑ 0, uniformly on r0, 1s, and hence also in L2pr0, 1sq. But Btfpx,tq is also in L2pr0, 1sq, and hence has
an L2-Fourier series
Btfpx,tq“
ÿ
nPZ
αnptqe2πinx.
Thus, by Parseval’s theorem,
ÿ
nPZ
⏐⏐⏐⏐
anpt`hq´ anptq
h ´αnptq
⏐⏐⏐⏐
2
Ñ 0
as h Ñ 0, which implies anpt`hq´anptq
h Ñ αnptq for each n. Thus, anptq is diﬀerentiable with derivative
a1
nptq“ αptq, and
Btfpx,tq“
ÿ
nPZ
a1
nptqe2πinx
in L2pr0, 1sq, as desired. The same argument applied to ř
na1
nptqe2πinx shows that the a1
nptq are themselves
diﬀerentiable, and hence continuous; so the anptq are continuously diﬀerentiable, as required.
Problem 5. ForfPL1pRq, recall the Hardy-Littlewood maximal function
Mfpxq :“ sup
hą0
1
2h
żx`h
x´h
|fpyq|dy.
Prove there is a constant A such that for any αą 0,
λtxP R :Mfpxqą αu ď A
α||f||L1.
If you use a covering lemma, you should prove it.
Solution. Fix α ą 0 and let E “ tx P R : Mfpxq ąαu. For each x P E, by deﬁnition of Mf there
is a radius rx such that żx`rx
x´rx
|f| ą 2αrx.
29

Note the above implies we must have rx ă ||f||L1{p2αq for each xP E. Set Ix “ px´rx,x `rxq. Since
the radii are uniformly bounded, we may apply the Vitali covering lemma to tIxuxPE to obtain a countable
disjoint subcollection Ij“pxj´rj,xj`rjq with EĎ Ť8
j“1 5Ij. Thus we have
λpEq ď
8ÿ
j“1
λp5Ijq “ 5
8ÿ
j“1
2rj ď 5
λ
8ÿ
j“1
żxj`rj
xj´rj
|f| ď 5
λ||f||L1
because the intervals Ij are pairwise disjoint. All that remains is to prove the Vitali covering lemma.
Let tIαu be a collection of open balls with uniformly bounded radius. Let R “ supα radpIαq. Let F1
be the collection of all balls Iα with radii in pR{2,Rs. Let B1 be a maximal pairwise disjoint subcollection
of F1 (a standard Zorn’s lemma argument shows that this exists). Now let F2 be the subcollection of all
balls Iα which are disjoint from every element of B1 and have radii in pR{4,R{2s, and let B2 be a maximal
pairwise disjoint subcollection of F2 (same deal with Zorn’s lemma). Inductively, we may construct Fn
to be the collection of all balls Iα which do not intersect any ball in B1Y... Y Bn´1 and have radii in
pR{2n,R{2n´1s, and let Bn be a maximal disjoint subcollection of Fn. Let B “ Ť8
n“1 Bn. It’s clear that
B is a pairwise disjoint (and therefore countable) subcollection of the Iα. Consider some IαR B. We have
radpIαqPp R{2n,R{2n´1s for some n. By the maximality of Bn, it must be the case that Iα intersects some
Iβ P B1Y... Bn. So radpIβqą R{2n ěp 1{2q radpIαq. Thus B has the property that any Iα R B intersects
some Iβ P B with radpIβqą R{2něp 1{2q radpIαq. Thus a simple triangle inequality shows that IαĎ 5Iβ,
so Ť
αIαĎ Ť
IPB 5I.
Problem 6. Let pX,dq be a compact metric space. Let µn be a sequence of positive Borel measures
on X that converge in the weak-˚ topology to a ﬁnite positive Borel measure µ, that is
ż
X
fdµ n Ñ
ż
X
fdµ for all fPCpXq.
Show that
µpKq ě lim sup
nÑ8
µnpKq for all compact sets KĎX.
Solution. Fix K compact. First we show that the characteristic function χK is upper semicontinuous.
We need to show
χKpx0q ě lim sup
xÑx0
χKpxq
for any x0 P X. If x0 P K, then the inequality obviously holds because χKpx0q is equal to the maximum
valueχK can take. If x0RK, then since Kc is open there is a neighborhood around x0 on which χK “ 0,
so χKpx0q“ 0“ limxÑx0χKpxq. Thus χK is upper semicontinuous.
Now we prove the inequality ż
fdµ ě lim sup
nÑ8
fdµ n
for all upper semicontinuous f : X Ñ R. This ﬁnishes the problem by taking f “ χK. It’s equivalent to
show ż
fdµ ď lim inf
nÑ8
fdµ n
whenever f is lower semicontinuous (by just taking the negative). Fix such an f. Since X is compact, f
achieves a minimum onX (this is a property of lower semicontinuous functions). By an equivalent deﬁnition
of lower semicontinuous, we have a sequence φk of continuous functions with φk ď φk`1 and φk Ñ f
pointwise. By replacing φk by maxpφk, minpfqq if necessary, we may assume that all of the φk are uniformly
bounded from below. We have ż
X
φkdµn ď
ż
X
fdµ n
30

for any k,n . Taking the liminf as nÑ8 , since φk is continuous we get
ż
X
φkdµ ď lim inf
nÑ8
ż
X
fdµ n
for every k. Finally, since the right side is independent of k, apply the Monotone Convergence theorem to
get the desired conclusion.
Problem 7. Compute
ş8
0
cospxq
p1`x2q2 dx.
Solution. Let fpzq “ eiz
p1`z2q2 . Integrate f around a semicircle of radius R in the upper half plane. It’s
easy to show the contribution from the curved part of the contour vanishes as RÑ8 . The real part of the
integral over the straight part is twice the desired integral because the original function is even. f has a
double pole at z“i. Take the residue
Respf,iq “ lim
zÑi
d
dz
“
pz´iq2fpzq
‰
“ ´i
2e.
Set the two things equal to each other using the residue theorem and solve. The answer is π{2e.
Problem 8. Determine the number of solutions to
z´ 2´e´z“ 0
with z in the right half-plane H“tzP C : Rezą 0u.
Solution. Any such z satisﬁes z“ 2`e´z, and therefore |z|“| 2`e´z|ď 2`|e´z|ă 3, since Re zą 0.
Hence, we can restrict z to the half-disc U “ HXt|z| ă3u. Consider the functions fpzq “z´ 2 and
gpzq“´ e´z onBU. It is easy to see that |g|ă| f| onBU, since |g|“ e´x ă 1 everywhere in H, whereas
|z´ 2|ą 1 for all xPBU except at z“ 3, at which point |gpzq|“ e´3ă 1. Therefore, by Rouche’s theorem,
f and f`g“z´ 2´e´z have the same number of zeros in U; since f clearly has one zero in U, it follows
that
z´ 2´e´z“ 0
has exactly one solution in H.
Problem 9. Suppose that f is a holomorphic function in the punctured open unit disc D˚ :“ Dzt0u
such that ż
D˚
|fpzq|2dApzq ă 8
where integration is with respect to two dimensional Lebesgue measure. Show that f has a holomorphic
extension to the unit disc D.
Solution. Let gpzq “zfpzq. It’s clear that g is also holomorphic on D˚. By the mean value property,
for zP D˚ ﬁxed we have
|gpzq| “ 1
πp1{2|z|q2
⏐⏐⏐⏐⏐
ż
Bpz,1{2|z|q
wfpwqdApwq
⏐⏐⏐⏐⏐ À |z|´2
˜ż
Bpz,1{2|z|q
|w|2dApwq
¸1{2˜ż
Bpz,1{2|z|q
|fpwq|2dApwq
¸1{2
À |z|´2
˜ż
Bp0,3{2|z|q
|w|2dApwq
¸1{2
À |z|´2
˜ż 3{2|z|
0
ż 2π
0
r2rdθdr
¸1{2
À|z|´2
˜ż 3{2|z|
0
r3dr
¸1{2
À|z|´2
ˆ
p3
2|z|q4
˙1{2
À 1.
Thusg is bounded and holomorphic in the punctured disc D˚, which means that the singularity at 0 must
be removable. So zfpzq has a removable singularity at 0, which implies that the singularity of f at 0 is
31

either removable or a simple pole. But if f has a simple pole at zero, then there is a constant Cą 0 and a
neighborhood of 0 on which |fpzq|ě C|z|´1, which contradicts the fact that
ş
D˚|fpzq|2dApzq ă 8. So f
has a removable singularity at 0 and therefore can be extended to a holomorphic function on D.
Problem 10. Let Ω Ĺ C be a simply connected domain and f : Ω Ñ Ω be a holomorphic mapping.
Suppose there are points z1‰z2 with fpz1q“ z1 and fpz2q“ z2. Show that f is the identity on Ω.
Solution. We need to assume f is conformal, otherwise it isn’t true (as a counterexample take Ω “Bp0, 2q
and fpzq“ z2, then 0 and 1 are both ﬁxed points). By the Riemann mapping theorem, let T : ΩÑ D be a
conformal map. Then φ“TfT ´1 : DÑ D is a conformal map with φpα1q“ α1, φpα2q“ α2 and α1‰α2
(take αj “ Tpzjq). Let ψ be an automorphism of D that sends α1 to 0. Then we have ψpφpψ´1p0qqq“ 0,
so the Schwartz lemma applies to ψφψ´1. But note also that ψpφpψ´1pψpα2qqqq“ ψpα2q. So equality holds
in the Schwartz lemma (actual equality, not just equality in absolute value), so ψφψ´1 is the identity, which
implies φ is the identity, which implies f is the identity.
Problem 11. Let f : C Ñ C be a holomorphic function with fpzq ‰ 0 for all z P C. Deﬁne U “
tzP C :|fpzq|ă 1u. Show that all connected components of U are unbounded.
Solution. Since f is nonvanishing, 1{f is also entire. First note that U is clearly an open set because
it’s the preimage of p0, 1q under the continuous function |fpzq|. Suppose that Ω were a bounded connected
component of U. Note that Ω is also open: let z P Ω and let B be an open ball centered at z contained
in U. If B were not contained in Ω, then there would be wP B where w belongs to a diﬀerent connected
component of U. But z and w can be joined by a path lying in U, so they must be in the same connected
component. Thus Ω is a bounded connected open set, i.e. a region on which the maximum principle can be
applied. First note that by continuity and by the fact that BΩ is disjoint from Ω, we must have |f|“ 1 on
BΩ. Thus |1{f|“ 1 on BΩ also. So by the maximum principle, we have |1{f|ď 1 throughout Ω, implying
|f|ě 1 throughout Ω. But |f|ă 1 in Ω by deﬁnition, which is a contradiction.
Problem 12. A holomorphic function f : CÑ C is said to be of exponential type if there are constants
c1,c 2ą 0 such that
|fpzq| ď c1ec2|z| for all zP C.
Show that f is of exponential type if and only if f1 is of exponential type.
Solution. First suppose f is of exponential type. For any z, the Cauchy estimates give
|f1pzq| ď 1
R sup
|w´z|“R
|fpwq| ď 1
Rc1ec2p|z|`Rq
for any Rą 0. Pick R“ 1, we get
|f1pzq| ď c1ec2p|z|`1q “ c1ec2ec2|z|,
so f is of exponential type.
Now suppose f1 is of exponential type. For any z we can write
fpzq “ fp0q`
ż
γ
fpwqdw
where γ is a straight line from 0 to z. So we have
|fpzq| ď |fp0q|`| z| sup
wPγ
|f1pwq| ď |fp0q|`| z|c1ec2|z| ď p|fp0q|` c1qepc2`1q|z|,
so f is of exponential type.
32

7 Spring 2012
Problem 1. fnPL3pr0, 1sq. True or false:
(a) If fnÑf almost everywhere then a subsequence converges to f in L3.
(b) If fnÑf in L3 then a subsequence converges almost everywhere.
(c) If fnÑf in measure then the sequence converges to f in L3.
(d) If fnÑf in L3 then the sequence converges to f in measure.
Solution.
(a) False. Let fn“n¨χr0,1{ns. Then fnÑ 0 almost everywhere but
ş1
0|fn|3“
ş1{n
0 n3“n2, so fn doesn’t
converge to 0 in L3.
(b) True. By part (d) we know that fnÑf in measure. So for each k, we have
lim
nÑ8
tx :|fnpxq´ fpxq|ą 1{ku“ 0.
For each k, pick nk large enough so that λtx :|fnpxq´ fpxq|ą 1{kuă 2´k. Let Ek “t x :|fnpxq´
fpxq| ą1{ku. We claim that fnk Ñ f almost everywhere. Note that since ř8
k“1λpEkq ă 8, the
Borel-Cantelli lemma implies that the set of x that lie in inﬁnitely many Ek has measure zero. Fix
ϵą 0 and let x be one of the almost everywhere points lying in only ﬁnitely many Ek. Then, as long
as k is big enough so that 1 {kă ϵ and xR Ek, we have |fnkpxq´ fpxq|ď 1{kă ϵ. This shows that
fnkpxqÑ fpxq for a.e. x.
(c) False. The same counterexample from part (a) works again.
(d) True. Fix αą 0. Then we have
ż
|fn´f|3 ě
ż
tx:|fnpxq´fpxq|ąαu
|fn´f|3 ě α3¨λtx :|fnpxq´ fpxq|ą αu.
The left side goes to 0 as nÑ8 , so the right side does as well.
Problem 2. LetX andY be topological spaces andXˆY the Cartesian product endowed with the product
topology. BpXq denotes the Borel sets in X and similarly, BpYq and BpXˆYq.
(a) Suppose f :XÑY is continuous. Prove that EP BpYq implies f´1pEqP BpXq.
(b) Suppose AP BpXq and EP BpYq. Show that AˆEP BpXˆYq.
Solution.
(a) Let F“tEĎY :f´1pEqP BpXqu. We want to show that BpYqĎ F. It’s enough to show that F is a
σ-algebra containing all open sets of Y . It’s clear that F contains all open sets in Y by the deﬁnition
of continuous functions. Thus H and Y are in F because they are open. Suppose AP F. Then we
have f´1pAcq “f´1pAqc P BpXq, so F is closed under complementation. Finally, suppose An P F.
Then we have f´1pŤAnq“ Ťf´1pAnqP BpXq, so F is closed under countable unions. Thus F is a
σ-algebra, so we’re done.
(b) Fix an open set U Ď X. We ﬁrst show that UˆE P BpXˆYq for any E P BpYq. Let FU “t E Ď
Y :UˆEP BpXˆYqu. To verify that claim, we just need to show FU is a σ-algebra containing all
open sets of Y . It’s clear that FU contains all open sets because the product of open sets is open. So
FU containsH and Y . If E P FU, then UˆEc “ pUˆYqzpUˆEq PBpXˆYq, so FU is closed
33

under complementation. If EnP FU, then UˆŤEn“ ŤpUˆEnqP BpXˆYq, so FU is closed under
countable unions, so it’s a σ-algebra. This shows that UˆEP BpXˆYq for any open UĎX and any
Borel EĎY .
Now ﬁx a Borel set E Ď Y and let FE “ tA Ď X : AˆE P BpXˆYqu. We want to show FE
contains all Borel sets in X, so it’s enough to show FE is a σ-algebra containing all open sets of
X. We know it contains all open sets of X by the above work. The exact same argument as above
shows that it’s aσ-algebra. Thus we conclude thatAˆEP BpXˆYq for anyAP BpXq,EP BpYq.
Alternate solution. (b) Let πX (resp. πY ) be the projection maps XˆY ÑX (resp. Y ). They are
both continuous. Then by part (a),
AˆE “ π´1
X pAqX π´1
Y pEq P BpXˆYq.
Problem 3. Givenf :r0, 1sÑ R belonging to L1 and nP N, deﬁne
fnpxq “ n
żpk`1q{n
k{n
fpyqdy for xPrk{n,pk` 1q{nq and 0ďkďn´ 1.
ProvefnÑf in L1.
Solution. First suppose f is the characteristic function of an interval f “ χra,bs. Then note that for n
large enough, fn is constant and equal to f on each subinterval except for possibly the two subintervals
containinga and b. On these two subintervals, we still have 0 ďfnď 1. Thus we have
ż 1
0
|fn´f| ď 2¨ 1
n¨ max|fn´f| ď 2
n,
which shows that fnÑf in L1. Next note that the map f ÞÑfn is linear, so we also know that fnÑf in
L1 for any f which is a linear combination of characteristic functions of intervals. This class of functions is
dense in L1. So for a general fPL1, let gk be a sequence of functions of the above form with gkÑf inL1.
Then for any n large enough we have
||fn´f||L1 ď ||f´gk||L1`||gk´pgkqn||L1`||pgkqn´fn||L1.
We estimate
||pgkqn´fn||L1 “
n´1ÿ
k“0
żpk`1q{n
k{n
|gkpxq´ fpxq|dx “
n´1ÿ
k“0
żpk`1q{n
k{n
n
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
pgkpyq´ fpyqqdy
⏐⏐⏐⏐⏐ dx
ď
n´1ÿ
k“0
n
żpk`1q{n
k{n
|fpyq´ gkpyq|
żpk`1q{n
k{n
dxdy by Tonelli
“
n´1ÿ
k“0
żpk`1q{n
k{n
|fpyq´ gkpyq|dy “ ||f´gk||L1.
Thus we have
||fn´f||L1 ď 2||f´gk||L1`||gk´pgkqn||L1.
This holds for any n, so taking nÑ8 we get
lim sup
nÑ8
||fn´f||L1 ď 2||f´gk||L1
since we already veriﬁed the desired property for each gk. Now the above holds for any k, so we can take
kÑ8 and conclude limnÑ8||fn´f||L1“ 0.
Problem 4. Let S“tfPL1pR3q :
ş
fpxqdx“ 0u.
34

(a) Show that S is closed in the L1 topology.
(b) Show that SXL2pR3q is a dense subset of L2pR3q.
Solution.
(a) Let fnPS and fPL1 with fnÑf in L1. Then for each n we have
⏐⏐⏐⏐
ż
f
⏐⏐⏐⏐ “
⏐⏐⏐⏐
ż
f´
ż
fn
⏐⏐⏐⏐ ď
ż
|f´fn| Ñ 0,
so
ş
f“ 0.
(b) We know that the set of L2 functions with compact support is dense in L2, so it suﬃces to show that
for any f P L2 with compact support and any ϵą 0, there is some g P SXL2 with||g´f||L2 ă ϵ.
Fix f PL2 with compact support and ϵą 0. Say supppfqĎ Bp0,Mq and let I“
ş
fpxqdx. We know
that I ă 8because L2 functions with compact support are also L1 (by Cauchy-Schwarz). We may
assume Ią 0 because if I“ 0 then we’re done, and if Iă 0 then we can do the same argument with
a negative sign on everything. The idea is to let g“f on the support of f, and then let g be equal to
a small negative value outside the support of f so that
ş
gpxqdx“ 0.
Let C ą M be a solution to 4 π{3pC3´M3q“ I2{ϵ. Let gpxq“ fpxq for|x|ď M, gpxq“´ ϵ{I for
Mă|x|ď C, and gpxq“ 0 otherwise. It’s clear that gPL2. We have
ż
gpxqdx “
ż
|x|ďM
fpxqdx`
ż
Mă|x|ďC
´ϵ{I “ I´ϵ{I¨λ3pMă|x|ď Cq “I´ϵ{I¨ 4
3πpC3´M3q “ 0,
so gPSXL2. Also we have
||g´f||L2 “
ż
Mă|x|ďC
ϵ2{I2 “ ϵ2{I2¨λ3pMă|x|ď Cq “ ϵ.
Problem 5. State and prove the Riesz representation theorem for linear functionals on a Hilbert space.
Solution. Statement: let H be a Hilbert space and let f be a bounded linear functional on H. Then
there exists zPH such that fpxq“x x,zy for all xPH.
Proof: Let f P H˚. Since f is a continuous map into a 1-dimensional space, we know that ker pfq is
a closed, co-dimension 1 subspace of H. Fix a nonzero u P kerpfqK. Then we have the decomposition
H “ kerpfq‘ spanpuq. Let α“fpuq{||u||2. Then we claim that fpxq“x x,αuy for all xPH. Since every
xP H decomposes uniquely as the sum of something in ker pfq and something in spanpuq, we just need to
show that xÞÑfpxq and xÞÑxx,αuy agree on kerpfq and spanpuq. For yP kerpfq, we clearly have fpyq“ 0
and xy,αuy “0 because u was chosen to be in ker pfqK. For z P spanpuq, we have z “ cu for some c, so
we have fpzq“ fpcuq“ cfpuq andxz,αuy“ cα||u||2 “ cfpuq by choice of α. Thus fpxq“x x,αuy for all
xPH.
Problem 6. Suppose f P L2pRq and that the Fourier transform obeys pfpξq ą 0 for almost every ξ.
Show that the set of ﬁnite linear combinations of translates of f is dense in the Hilbert space L2pRq.
Solution. Let M “ spantxÞÑfpx`aquaPR where the closure is with respect to the L2 norm. Suppose for
contradiction thatM‰L2. Then there is some nonzerogPMK. In particular we have
ş
Rfpx`aqgpxqdx“ 0
for all aP R. By Plancherel, this implies that
ż
R
FpxÞÑfpx`aqpξqqFpgqpξqdξ “
ż
R
e´2πiaξ FpfqpξqFpgqpξqdξ “ FpFpfqFpgqqpaq “ 0
35

for all a P R, where F denotes the Fourier-Plancherel transform L2 Ñ L2. This formula is valid because
since f,g P L2, FpfqFpgq PL1, and thus the Fourier-Plancherel transform agrees with the standard L1
Fourier transform. But since F is a bijection this implies that FpfqpξqFpgqpξq“ 0 for almost every ξ. And
since Fpfqpξqą 0 almost everywhere, this implies Fpgq“ 0 almost everywhere, so g“ 0 almost everywhere,
which is a contradiction.
Problem 7. Lettunpzqu be a sequence of real-valued harmonic functions on D that obey
u1pzq ě u2pzq ě ¨¨¨ ě0 for all zP D.
Prove that zÞÑ infnunpzq is a harmonic function on D.
Solution. Let upzq “ infnunpzq “ limnÑ8unpzq (the limit exists and equals the inf because the se-
quence is monotonically decreasing and bounded for each z). First we show that un Ñ u uniformly on
compact subsets of D. Fix a compact subset Bp0,rqĎ D. For any nąm, um´un is a positive harmonic
function on D, so we can apply Harnack’s inequality on the disc Bp0,p1`rq{2q to get, for any |z|ď r,
|umpzq´ unpzq| ď p1`rq{2`|z|
p1`rq{2´|z| |ump0q´ unp0q| ď p1`rq{2`r
p1`rq{2´r |ump0q´ unp0q| Ñ 0
as n,m Ñ8 uniformly in |z|ď r becausetunp0qu is a convergent sequence.
Since each un is continuous, the local uniform convergence implies that u is continuous. Also, for any
Bpz0,rqĎ D, we have
1
2π
ż 2π
0
upz0`reiθqdθ “ 1
2π
ż 2π
0
lim
nÑ8
unpz0`reiθqdθ “ lim
nÑ8
1
2π
ż 2π
0
unpz0`reiθqdθ “ lim
nÑ8
unp0q “up0q
where switching the limit and the integral is justiﬁed by uniform convergence on the compact set BBpz0,rq.
Thusu is continuous and satisﬁes the mean value property on every disc, so it’s harmonic.
Problem 8. Let Ω “ tx`iy : x ą 0,y ą 0,xy ă 1u. Give an example of an unbounded harmonic
function on Ω that extends continuously to BΩ and vanishes there.
Solution. We want to conformally map Ω to a region where it will be easier to ﬁnd such a function.
Motivated by the fact that px`iyq2 “ px2´y2q` ip2xyq, we see that the map z ÞÑ πz2 is a conformal
map from Ω to the strip S :“ tz : 0 ă Impzq ă2πu. Now note that z ÞÑ Impezq is an unbounded har-
monic function in S which vanishes on the boundary of S: we have Impexppx` 0iqq“ Impexppxqq“ 0 and
Impexppx` 2πiqq“ Impexppxqq“ 0, and Impexppx`iπ{2qq“ Impi exppxqq“ exppxq, which is unbounded
in S. Therefore the function upzq“ Impexppπz2qq is a function that works.
Problem 9. Prove Jordan’s lemma: If fpzq : CÑ C is meromorphic, Rą 0, and ką 0, then
⏐⏐⏐⏐
ż
Γ
fpzqeikzdz
⏐⏐⏐⏐ ď 100
k sup
zPΓ
|fpzq|
where Γ is the quarter circle z“Reiθ with 0ďθďπ{2.
Solution. We have
⏐⏐⏐⏐
ż
Γ
fpzqeikzdz
⏐⏐⏐⏐ “
⏐⏐⏐⏐⏐
żπ{2
0
fpReiθqeikReiθ
iReiθdθ
⏐⏐⏐⏐⏐ ď R¨ sup
zPΓ
|fpzq|¨
żπ{2
0
⏐⏐⏐eikRpcosθ`i sinθq
⏐⏐⏐ dθ
“ R¨ sup
zPΓ
|fpzq|¨
żπ{2
0
e´kR sinθdθ.
So we just need to show that
şπ{2
0 e´kR sinθdθď 100
kR . We break the integral in two:
żπ{2
0
e´kR sinθdθ “
żπ{4
0
e´kR sinθdθ`
żπ{2
π{4
e´kR sinθdθ “: A`B.
36

Now we estimate
A “
żπ{4
0
e´kR sinθdθ “
ż?
2{2
0
e´u du
kR cosθ ď 1
kR
?
2{2
ż?
2{2
0
e´udu ď
?
2
kR
B “
żπ{2
π{4
e´kR sinθdθ ď
żπ{2
π{4
e´kR
?
2{2dθ “ π
4e´kR
?
2{2 ď π
?
2
4 ¨ 1
kR because e´xď 1{x for xą 0.
Thus we conclude żπ{2
0
e´kR sinθdθ ď
ˆ?
2` π
?
2
4
˙ 1
kR ď 100
kR.
Alternate solution. Same up to the bound
⏐⏐⏐⏐
ż
Γ
fpzqdz
⏐⏐⏐⏐ ď R¨ sup
zPΓ
|fpzq|¨
żπ{2
0
e´kR sinpθqdθ.
Now note that on r0,π{2s, sinpθqěp 2{πqθ, so we have
⏐⏐⏐⏐
ż
Γ
fpzqdz
⏐⏐⏐⏐ ď R¨sup
zPΓ
|fpzq|¨
żπ{2
0
e´kRp2{πqθdθ “ π{2
k sup
zPΓ
|fpzq|¨
żπ{2
0
e´θdθ ď π{2
k sup
zPΓ
|fpzq|¨
ż8
0
e´θdθ ď π{2
k sup
zPΓ
|fpzq|,
and I think this is the optimal constant.
Problem 10. Let us deﬁne the Gamma function via
Γpzq “
ż8
0
tz´1e´tdt
when the integral is absolutely convergent. Show that this function extends to a meromorphic function in
the whole complex plane.
Solution. Note that for Repzqą 0, we have
ż8
0
⏐⏐tz´1⏐⏐e´tdt “
ż8
0
tRepzq´1e´tdt ă 8.
So the integral is absolutely convergent for all Repzqą 0. First we show that it deﬁnes an analytic function
for Repzqą 1. We have
Γpz`hq´ Γpzq
h “
ż8
0
e´ttz´1
ˆth´ 1
h
˙
.
We estimate
⏐⏐⏐⏐e´ttz´1
ˆth´ 1
h
˙⏐⏐⏐⏐ “ e´ttRepzq´1
⏐⏐⏐⏐
eh logt´ 1
h
⏐⏐⏐⏐ ď e´ttRepzq´1
8ÿ
n“1
|h|n´1| logt|n
n!
ď e´ttRepzq´1
8ÿ
n“1
| logt|n
n! for|h|ď 1
ď e´ttRepzq´1e| logt|.
If Repzqą 1, then e´ttRepzq´1e| logt| is integrable on r0,8q, so by the Dominated Convergence theorem we
see that the above diﬀerence quotient converges as hÑ 0, so Γ is analytic. So far we have that Γ is analytic
in Repzqą 1. By integrating by parts we get, for any Re pzqą 0,
Γpz` 1q “
ż8
0
tze´tdt “ z
ż8
0
tz´1e´tdt “ zΓpzq.
37

So we can extend the deﬁnition of Γ by setting Γ pzq :“ 1
z Γpz` 1q“ 1
zpz`1qΓpz` 2q for all ´1ă Repzqď 0
except for z“ 0. This deﬁnition makes Γ analytic in ´1ă Repzqď 0 except at 0 because for any nonzero
point in that strip, we can take a neighborhood around that point on which zÞÑ 1
zpz`1q andzÞÑ Γpz`2q are
both analytic. There is no problem even when taking neighborhoods around points with Re pzq“ 0 because
in 0ă Repzqď 1, the two deﬁnitions of Γ agree because of the functional equation.
We can extend this deﬁnition to all of C. In general, for non-negative integers n, deﬁne Γ on the strip
´n´ 1ă Repzqď´ n (except not at z“´n) by
Γpzq“ 1
zpz` 1q¨¨¨p z`n` 1qΓpz`n` 2q.
By the same reasoning, this deﬁnition makes Γ analytic everywhere except for at all of the non-positive
integers. To show that Γ is meromorphic, we just need to show that it has poles at each non-positive integer.
Fix a non-positive integer ´n. In any neighborhood of z“´n, the representation
Γpzq“ 1
zpz` 1q¨¨¨p z`n` 1qΓpz`n` 2q.
is valid regardless of whether Repzqď´ n or Repzqą´ n, because of the functional equation which is valid
in the right half plane. Since Γp2q‰ 0, it’s clear that ΓpzqÑ8 aszÑ´n, and thus Γ has a pole at´n.
Problem 11. Let Ppzq be a polynomial. Show that there is an integer n and a second polynomial Qpzq so
that
PpzqQpzq “ zn|Ppzq|2 whenever|z|“ 1.
Solution. Write Ppzq “ pz´a1q¨¨¨p z´amq. Deﬁne Qpzq “ p1´a1zq¨¨¨p 1´amzq. It’s clear Q is a
polynomial. On |z|“ 1, we have
|Ppzq|2 “ PpzqPpzq “ pz´a1q¨¨¨p z´amqpz´a1q¨¨¨p z´amq
“ pz´a1q¨¨¨p z´amqp1{z´a1q¨¨¨p 1{z´amq
“ pz´a1q¨¨¨p z´amqp1{zqmp1´a1zq¨¨¨p 1´amzq “ 1
zmPpzqQpzq.
So PpzqQpzq“ zm|Ppzq|2 on|z|“ 1.
Problem 12. Show that the only entire function fpzq obeying both
|f1pzq| ď e|z| and f
˜
na
1`|n|
¸
“ 0 for all nP Z
is the zero function.
Solution. Suppose f is not identically zero. Then since its zeros are discrete, it has countable many. Enu-
merate themtaku. By hypothesis f vanishes at everyn{
a
1`|n| fornP Z, so we know that ř
k|ak|´2“8 .
This implies that the genus of f is at least 2 (proof below). By Hadamard’s theorem, this also implies the
order of f is at least 2. But by hypothesis, we have fp0q“ 0, and so for any z we can write
|fpzq| “
⏐⏐⏐⏐
ż
γz
f1pwqdx
⏐⏐⏐⏐ ď |z| sup
wPγz
|f1pwq| ď |z|e|z| ď e2|z|
where γz is a straight line from 0 to z. But this shows that the order of f isď 1, a contradiction.
Here is a proof that ř
k|ak|´2 “ 8implies the genus of f is at least 2. It follows from the more gen-
eral claim: If genuspfqď h andtaku are the zeros of f, then ř
k|ak|´ph`1qă8 . If the genus is ďh, then
we know that the product
8ź
k“1
ˆ
1´ z
ak
˙
exp
˜
z
ak
` 1
2
ˆ z
ak
˙2
`... ` 1
h
ˆ z
ak
˙h¸
38

converges uniformly on compact sets. In particular, ﬁx some z which is not a zero of f, then we know the
series
8ÿ
k“1
log
ˆ
1´ z
ak
˙
` z
ak
` 1
2
ˆ z
ak
˙2
`... ` 1
h
ˆ z
ak
˙h
convergs absolutely. For all |ak|ą 3|z|, we have the estimate
⏐⏐⏐⏐⏐log
ˆ
1´ z
ak
˙
` z
ak
` 1
2
ˆ z
ak
˙2
`... ` 1
h
ˆ z
ak
˙h⏐⏐⏐⏐⏐ “
⏐⏐⏐⏐⏐
8ÿ
j“h`1
1
j
ˆ z
ak
˙j⏐⏐⏐⏐⏐
“ 1
h` 1
⏐⏐⏐⏐
z
ak
⏐⏐⏐⏐
h`1 ⏐⏐⏐⏐⏐
8ÿ
j“h`1
h` 1
j
ˆ z
ak
˙j´ph`1q⏐⏐⏐⏐⏐
ě 1
h` 1
⏐⏐⏐⏐
z
ak
⏐⏐⏐⏐
h`1˜
1´
8ÿ
j“h`2
h` 1
j
⏐⏐⏐⏐
z
ak
⏐⏐⏐⏐
j´ph`1q¸
ě 1
h` 1
⏐⏐⏐⏐
z
ak
⏐⏐⏐⏐
h`1˜
1´
8ÿ
j“h`2
p1{3qj´ph`1q
¸
ě |z|h`1
2ph` 1q|ak|´ph`1q.
Thus
ÿ
|ak|ą3|z|
|ak|´ph`1q ď 2ph` 1q
|z|h`1
ÿ
|ak|ą3|z|
⏐⏐⏐⏐⏐log
ˆ
1´ z
ak
˙
` z
ak
` 1
2
ˆ z
ak
˙2
`... ` 1
h
ˆ z
ak
˙h⏐⏐⏐⏐⏐ ă 8.
This establishes the desired claim because there are only ﬁnitely many ak with|ak|ď 3|z|.
Alternate solution. By the same argument as in the other solution we have |fpzq| ďe2|z|. We want
to use Jensen’s formula. First multiply f by a power of z so that fp0q‰ 0. This preserves an inequality of
the form|fpzq|ď ec|z|. For anyR (assumingf has no zeros on|z|“ R), Jensen’s formula gives (enumerating
the zeros of f as an)
log|fp0q| “ 1
2π
ż 2π
0
log|fpReiθq|dθ`
ÿ
|an|ăR
log
⏐⏐⏐an
R
⏐⏐⏐
À logecR`
ÿ
|n|{
?
1`|n|ăR
log
⏐⏐⏐⏐⏐
n
R
a
1`|n|
⏐⏐⏐⏐⏐
À R`
ÿ
nďR2
log
⏐⏐⏐⏐
?n
R
⏐⏐⏐⏐
À R´
ÿ
nďR2
logR`
ÿ
nďR2
log?n
À R´R2 logR` 1
2
żR2
0
logxdx
À R´R2 logR`R2 logR´ 1
2R2
which goes to ´8 as RÑ8 , a contradiction.
39

8 Fall 2012
Problem 1. Let 1ăpă8 and let fn : R3Ñ R be a sequence of functions such that lim sup ||fn||Lpă8 .
Show that if fn converges almost everywhere, then fn converges weakly in Lp.
Solution. Let λ denote Lebesgue measure on R3. Say that fn Ñ f pointwise almost everywhere and
also that||fn||LpďM for all n. To show that fnÑf weakly in Lp, we need to show that φpfnqÑ φpfq for
every bounded linear functional φPpLpq˚. By Lp-Lq duality, we know that every φPpLpq˚ is of the form
φpfq“
ş
fgdλ for some gPLq. So let g be any Lq function; it suﬃces to show that
ż
fng Ñ
ż
fg.
SincefnÑf almost everywhere, we also know thatfngÑfg almost everywhere. By the Vitali Convergence
Theorem, to show
ş
fngdλ Ñ
ş
fgdλ it suﬃces to show that the sequence tfngu is uniformly integrable
and tight.
For uniform integrability, let ϵ ą 0. Since |g|q is integrable, let δ ą 0 be such that whenever λpAq ăδ,
we have
ş
A|g|qdλăϵ. Then for any n and any λpAqă δ, we have by H¨ older’s inequality
ż
A
|fng|dλ ď
ˆż
A
|fn|pdλ
˙1{pˆż
A
|g|qdλ
˙1{q
ă Mϵ1{q,
which shows that tfngu is a uniformly integrable family.
For tightness, let ϵą 0 and let E be a subset of R3 such that
ş
Ec|g|qdλă ϵ. Then for any n, we have by
the same argument
ż
Ec
|fng|dλ ď
ˆż
Ec
|fn|pdλ
˙1{pˆż
Ec
|g|qdλ
˙1{q
ă Mϵ1{q,
sotfngu is a tight family, so we are done.
Problem 2. Suppose dµ is a Borel probability measure on the unit circle in the complex plane such
that
lim
nÑ8
ż
|z|“1
zndµpzq “ 0.
ForfPL1pdµq show that
lim
nÑ8
ż
|z|“1
znfpzqdµpzq “ 0.
Solution. By linearity, it is clear that the desired result holds for any trigonometric polynomial on the
unit circle, i.e. any function of the form Ppzq“ řN
n“´Nanzn. Since µ is a Borel measure and the unit circle
is compact, we know that the set of continuous functions on S1 is dense in L1pµq with respect to the norm
||¨||L1pµq. We also know by the Stone-Weierstrass theorem that the set of trigonometric polynomials on S1
is dense in the set of continuous functions on S1 with respect to the norm ||¨||L8pµq.
So letfPL1pµq and ﬁxϵą 0. Let g be a continuous function onS1 such that||f´g||L1pµqăϵ and letP
be a trigonometric polynomial such that||g´P||L8pµq. Since the result holds for trigonometric polynomials,
we can pick n large enough so that ⏐⏐⏐⏐⏐
ż
|z|“1
znPpzqdµpzq
⏐⏐⏐⏐⏐ ă ϵ.
40

Then for such n, we have
⏐⏐⏐⏐⏐
ż
|z|“1
znfpzqdµpzq
⏐⏐⏐⏐⏐ ď
ż
|z|“1
|znpfpzq´ gpzqq| dµpzq`
ż
|z|“1
|znpgpzq´ Ppzqq| dµpzq`
⏐⏐⏐⏐⏐
ż
|z|“1
znPpzqdµpzq
⏐⏐⏐⏐⏐
ď
ż
|z|“1
|fpzq´ gpzq| dµpzq`
ż
|z|“1
|gpzq´ Ppzq| dµpzq` ϵ
ď ||f´g||L1pµq`||g´P||L8pµqµpS1q` ϵ ă 3ϵ,
which shows that
ş
|z|“1znfpzqdµpzqÑ 0 as nÑ8 .
Problem 3. Let H be a Hilbert space and let E be a closed convex subset of H. Prove that there
exists a unique element xPE such that
||x|| “ inf
yPE
||y||.
Solution. First note that if 0 PE, then the statement is obviously true by taking x“ 0, so assume 0 RE.
Let infyPE||y||“ δą 0. First we prove that such an x must be unique. Suppose that ||x||“|| x1||“ δ. Then
since E is convex, we havep1{2qx`p 1{2qx1PE and
δ “ 1
2||x||` 1
2
ˇˇˇˇx1ˇˇˇˇ “
ˇˇˇˇ
ˇˇˇˇ
1
2x
ˇˇˇˇ
ˇˇˇˇ`
ˇˇˇˇ
ˇˇˇˇ
1
2x1
ˇˇˇˇ
ˇˇˇˇ ě
ˇˇˇˇ
ˇˇˇˇ
1
2x` 1
2x1
ˇˇˇˇ
ˇˇˇˇ ěδ.
But we know that equality in the triangle inequality occurs if and only if x and x1 are scalar multiples of
each other. Thus the above inequality yields the contradiction δąδ unless x and x1 are scalar multiples of
each other. So we can write x“cx1 where|c|“ 1. Then since E is convex,p1{2qpx`x1q“ c`1
2 x1PE also,
so
ˇˇˇˇc`1
2 x1ˇˇˇˇ“ |pc` 1q{2|δ ěδ, which implies c“ 1, so x“x1.
Now we show existence. Let tynu be a sequence in E such that ||yn|| Ñδ as n Ñ 8. Then for any n
and m, by the parallelogram law we can write
ˇˇˇˇ
ˇˇˇˇ
1
2yn` 1
2ym
ˇˇˇˇ
ˇˇˇˇ
2
`
ˇˇˇˇ
ˇˇˇˇ
1
2yn´ 1
2ym
ˇˇˇˇ
ˇˇˇˇ
2
“ 2
ˇˇˇˇ
ˇˇˇˇ
1
2yn
ˇˇˇˇ
ˇˇˇˇ
2
` 2
ˇˇˇˇ
ˇˇˇˇ
1
2ym
ˇˇˇˇ
ˇˇˇˇ
2
.
Since E is convex,p1{2qyn`p 1{2qymPE, so we have
1
4||yn´ym||2 “ 1
2||yn||2` 1
2||ym||2´
ˇˇˇˇ
ˇˇˇˇ
1
2yn` 1
2ym
ˇˇˇˇ
ˇˇˇˇ
2
ď 1
2||yn||2` 1
2||ym||2´δ2.
As n,m Ñ8 , the right side of the above inequality tends to 0 by deﬁnition of the yn, so we conclude that
||yn´ym||2Ñ 0 as n,m Ñ8 , sotynu is a Cauchy sequence. Since H is complete, there is some xPH such
that ynÑx as nÑ8 , and since E is closed, we must have xPE. Finally, since the norm is a continuous
function on H, we must have ||x||“ limnÑ8||yn||“ δ.
Problem 4. Fix f P CpTq where T “ R{2πZ. Let sn denote the nth partial sum of the Fourier series
of f. Prove that
lim
nÑ8
||sn||L8pTq
logpnq “ 0.
Solution. Recall that we have snpfqpxq“p f˚Dnqpxq, where Dn is the Dirichlet kernel
Dnptq “
nÿ
k“´n
eikt “ sinppn` 1{2qtq
sinpt{2q .
41

Therefore we immediately see that ||snpfq||L8ď||f||L8||Dn||L1. We estimate
||Dn||L1 À
żπ
´π
⏐⏐⏐⏐
sinppn` 1{2qtq
sinpt{2q
⏐⏐⏐⏐ dt À
żπ
0
⏐⏐⏐⏐
sinppn` 1{2qtq
t
⏐⏐⏐⏐ dt
where the second inequality is valid because Dn is even and sinpt{2qě t{100 on r0,πs. Continuing,
||Dn||L1 À
żpn`1{2qπ
0
| sinpuq|
u du À
nÿ
k“0
żpk`1qπ
kπ
| sinpuq|
u du
À
nÿ
k“0
żpk`1qπ
kπ
| sinpuq|
pk` 1qπdu À
nÿ
k“0
1
k` 1 À logpnq.
So we have established ||snpfq||L8 À ||f||L8 logpnq for all f PCpTq. Note that if P is a polynomial, then
snpPq ÑP uniformly on T (this is proven by integrating by parts twice on the deﬁnition of the Fourier
coeﬃcients to get |pPpkq|À k´2, and then applying the Weierstrass M-test combined with the general fact
that snpPqÑ P in L2). In particular, ||snpPq||L8 is bounded, so we clearly have ||snpPq||L8{ logpnqÑ 0.
Fix ϵą 0 and any fPCpTq. We can ﬁnd a polynomial P with||f´P||L8ăϵ. Then we have
lim sup
nÑ8
||snpfq||L8
logpnq ď lim sup
nÑ8
||snpf´Pq||L8
logpnq `||snpPq||L8
logpnq À ||f´P||L8 ă ϵ.
TakeϵÑ 0 and we’re done.
Problem 5. Let fn : R3 Ñ R be a sequence of functions such that sup n||fn||L2 ă 8. Show that if
fn converges almost everywhere to a function f : R3Ñ R, then
ż
R3
⏐⏐|fn|2´|fn´f|2´|f|2⏐⏐ dx Ñ 0.
Solution. Let M be such that ||fn||L2 ď M for all n. Since fn Ñ f almost everywhere, we also have
|fn|2Ñ|f|2 almost everywhere, so by Fatou’s lemma,
ż
|f|2 “
ż
lim inf
nÑ8
|fn|2 ď lim inf
nÑ8
ż
|fn|2 ď M2,
which shows that fPL2 and||f||L2ďM. Notice that we have the identity
||fn|2´|fn´f|2´|f|2| “ ||fn´f`f|2´|fn´f|2´|f|2| “ 2|fn´f||f|.
Fix ϵą 0. Since |f|2 is integrable, there is a δą 0 such that λpEqă δ implies
ş
E|f|2ăϵ. We can also pick
anR which is big enough so that
ş
|x|ąR|f|2ăϵ. Then on the set |x|ď R, we can apply Egorov’s theorem to
get a set EĎt|x|ď Ru such thatfnÑf uniformly ont|x|ď RuzE andλpEqă δ. So we have the estimate
ż
|fn´f||f| “
ż
t|x|ďRuzE
|fn´f||f|`
ż
E
|fn´f||f|`
ż
t|x|ąRu
|fn´f||f| “: A`B`C.
Since fn Ñ f uniformly on t|x| ďRuzE, let n be big enough so that
ş
t|x|ďRuzE|fn´f|2 ă ϵ. Now we
estimate each of A, B, C separately using Cauchy-Schwarz. We have
A ď
˜ż
t|x|ďRuzE
|fn´f|2
¸1{2˜ż
t|x|ďRuzE
|f|2
¸1{2
ď M?ϵ
B ď
ˆż
E
|fn´f|2
˙1{2ˆż
E
|f|2
˙1{2
ď
?
2M2?ϵ
C ď
˜ż
t|x|ąRu
|fn´f|2
¸1{2˜ż
t|x|ąRu
|f|2
¸1{2
ď
?
2M2?ϵ.
42

This shows that
ş
|fn´f||f|Ñ 0 as nÑ8 , which is enough to conclude the desired result.
Problem 6. Let fPL1pRq and let Mf denote its maximal function, that is,
pMfqpxq “ sup
0ără8
1
2r
żr
´r
|fpx´yq|dy.
By the Hardy-Littlewood maximal function theorem,
|txP R :pMfqpxqą λu| ď 3λ´1||f||L1 for all λą 0.
Using this show that
lim sup
rÑ0
1
2r
żr
´r
|fpyq´ fpxq|dy “ 0 for almost every xP R.
Solution. This is actually false as stated. As a counterexample, take f “χr´1,1s. For any xRr´ 1, 1s, we
havefpxq“ 0 but
lim sup
rÑ0
1
2r
żr
´r
|fpyq´ fpxq|dy “ lim sup
rÑ0
1
2r
żr
´r
|fpyq|dy “ 1.
Presumably, what the question meant to say is to prove that
lim sup
rÑ0
1
2r
żx`r
x´r
|fpyq´ fpxq|dy “ 0 for almost every xP R,
which is the Lebesgue diﬀerentiation theorem. Here is a proof of this:
Deﬁne
pTrfqpxq :“ 1
2r
żx`r
x´r
|fpyq´ fpxq|dy
pTfqpxq :“ lim sup
rÑ0`
pTrfqpxq.
We want to prove that Tf “ 0 almost everywhere. Fix some ϵą 0. Since the set of continuous functions
with compact support is dense in L1pRq, let g be a continuous function with compact support such that
||f´g||L1ăϵ. Deﬁne h“f´g so that f“g`h. Note that for any rą 0 we have
Trf “ Trpg`hq ď Trg`Trh.
By the deﬁnition of continuity, it is clear that the desired result holds for continuous functions, so we have
that Tg is identically zero, and thus we obtain Tf ďTh .
To show that Tf “ 0 almost everywhere, it suﬃces to show that mtx P R : pTfqpxq ąδu “0 for any
ﬁxed δą 0, where m is Lebesgue measure on R. So ﬁx δą 0 and deﬁne F :“t xP R :pTfqpxqą δu and
E :“txP R :pThqpxqą δu. Since Tf ďTh , F ĎE, so we analyze the measure of E. Note that for any x
and any rą 0, we have
pTrhqpxq “ 1
2r
żx`r
x´r
|hpyq´ hpxq|dy ď 1
2r
żx`r
x´r
|hpyq|dy` 1
2r
żx`r
x´r
|hpxq|dy ď pMhqpxq`| hpxq|.
Therefore we have
E Ď txP R :pMhqpxqą δ{2uYt xP R :|hpxq|ą δ{2u,
43

so by the Hardy-Littlewood theorem, Chebyshev’s inequality, and the deﬁnition of h,
mpEq ď 6
δ||h||L1` 2
δ||h||L1 ă 8
δϵ.
Thus we have mpFqăp 8{δqϵ. Since the set F does not depend on ϵ, this holds for any ϵą 0 and thus we
conclude mpFq“ 0, which is enough to conclude that Tf “ 0 almost everywhere.
Problem 7. Let f be a function holomorphic in C and suppose that fp0q“ 0, fp1q“ 1, and fpDqĎ D.
Show that (a) f1p1qP R and (b) f1p1qě 1.
Solution. (a) Suppose that f1p1qR R. Then there exists vP C with Repvqă 0 such that Repf1p1qvqą 0.
The limit deﬁnition of the derivative, together with the fact that fp1q“ 1 implies that
f1p1qv“ lim
tÑ0`
fp1`tvq´ 1
t .
For suﬃciently small t, we have 1 `tv P D. Since fpDq ĎD, But then Re fp1`tvq´1
t ă 0 small t. After
passing to the limit, we have Repf1p1qvqď 0 which is a contradiction.
(b) Fix tPp 0, 1q. By the Schwarz lemma, |fp1´tq|ď 1´t. Therefore
|fp1´tq´ 1|
t ě 1´|fp1´tq|
t ě 1.
Taking the limit as tÑ 0`, we see that |f1p1q|ě 1.
Problem 8. Let f : C Ñ C be a nonconstant holomorphic function such that every zero of f has even
multiplicity. Show that f has a holomorphic square root, i.e. there exists a holomorphic function g : CÑ C
such that fpzq“ gpzq2 for all zP C.
Solution. If the set of zeros of f had a limit point, then f would have to be identically zero. But f
is nonconstant by hypothesis, so the zeros of f are isolated. Since all of the multiplicities are even and the
zeros are isolated, by Weierstrass’s theorem there exists an entire function h such that h has the same zeros
asf, but with each one half the multiplicity. Then h2 is an entire function with exactly the same zeros as f
with all the same multiplicities. Therefore the function f{h2 is analytic at all points which are not zeros of
f, and it has removable singularities at the zeros of f. So it can be extended to a function which is analytic
everywhere, so we can assume without loss of generality that f{h2 is a nonvanishing entire function. Since
it is nonvanishing, it has a well-deﬁned analytic logarithm, i.e. there is some entire function g such that
f{h2 “ exppgq. Then f “ h2 exppgq “ ph exppg{2qq2, and h exppg{2q is an entire function, so this is the
desired result.
Problem 9. Suppose f is a holomorphic function in the unit disk D andtxnu is a sequence of real numbers
satisfying 0 ă xn`1ă xnă 1 for all nP N and limnÑ8xn“ 0. Show that if fpx2n`1q“ fpx2nq for all n,
then f is a constant function.
Solution. By translating by a constant, we may assume that fp0q “0. Deﬁne gpzq “fpzqfpzq. Since
fpzq is also holomorphic, we see that g is also holomorphic and gpzqP R wheneverzP R. So we can consider
the restriction of g to the positive real axis as a diﬀerential function on R. Then since gpx2n`1q“ gpx2nq for
all n, by the mean value theorem there is a number ynPpx2n`1,x 2nq such that g1pynq“ 0. Since xnÑ 0,
also ynÑ 0. Thus g1 is zero on a set with a limit point, so g1 is identically zero. Therefore g is a constant,
and since fp0q“ 0, we also have gp0q“ 0, so g is identically zero. Therefore we have fpzqfpzq“ 0 for all
zP D, which implies that f is identically zero because either fpzq orfpzq is zero on a set with a limit point.
Problem 10. Lettfnu be a sequence of holomorphic functions on D satisfying|fnpzq|ď 1 for all z and all
n Let AĎ D be the set of all zP D for which the limit lim nÑ8fnpzq exists. Show that if A has an accu-
mulation point in D, then there exists a holomorphic functionf on D such thatfnÑf locally uniformly on D.
44

Solution. Since the sequence fn is uniformly bounded, by Montel’s theorem we know it is a normal
family, so there is a subsequence fnk which converges locally uniformly on D to some function f. Since local
uniform limits of holomorphic functions are holomorphic, we know thatf is holomorphic. Now, to show that
the whole sequence fn converges locally uniformly to f, it suﬃces to prove that every subsequence has a
further subsequence which converges locally uniformly to f. Since the whole sequence is uniformly bounded,
clearly any subsequence is also uniformly bounded, so by applying Montel’s theorem to the subsequence, we
obtain a further subsequence which converges locally uniformly to some holomorphic function g on D. But
note that for everyzPA, since the limit of the whole sequence limnÑ8fnpzq exists, any subsequences which
converge pointwise atz must have the same limit. This implies in particular, since local uniform convergence
implies pointwise convergence, thatfpzq“ gpzq for allzPA. Since A has a limit point in D andf andg are
both holomorphic, this implies that f“g on D. Thus we conclude that any subsequence of fn has a further
subsequence converging locally uniformly to f, which implies that fn converges locally uniformly to f.
Problem 11. Find all holomorphic functions f : CÑ C satisfying fpz` 1q“ fpzq and fpz`iq“ e2πfpzq
for all zP C.
Solution. Note that expp´2πizq is one such function. Let f : C Ñ C be any entire function satisfy-
ing fpz` 1q“ fpzq and fpz`iq“ e2πfpzq for all zP C. Deﬁne gpzq“ fpzq expp2πizq. Then g is also an
entire function and it satisﬁes
gpz` 1q “ fpz` 1q expp2πipz` 1qq “ fpzq expp2πizq expp2πiq “ gpzq
gpz`iq “ fpz`iq expp2πipz`iqq “ e2πfpzq expp2πizq expp´2πq “ gpzq.
Thusg is a doubly periodic entire function, so it must be bounded and hence must be constant by Liouville’s
theorem. Thus we conclude that fpzq“ C expp´2πizq for some CP C, and these are all of the functions f
which satisfy the desired property.
Problem 12a. Let M P R, Ω Ď C be a bounded open set, and u : Ω Ñ R be a harmonic function.
Show that if
lim sup
zÑz0
upzq ď M
for all z0PB Ω, then upzqď M for all zP Ω.
Solution. Fix ϵ ą 0. By the limsup condition, for each z0 P BΩ, there is a radius rpz0q such that
|z´z0|ă rpz0q implies that upzqď M`ϵ. Then the set
ď
z0PBΩ
Bpz0,rpz0qq
is an open cover ofBΩ, which is a compact set because Ω is bounded. Therefore BΩ is covered by only ﬁnitely
many of these balls. Call them B1,...,B N. Now the set
A “ ΩzpB1Y... YBNq
is an open set on which u is harmonic, extends continuously to the boundary, and satisﬁes upwqď M`ϵ for
all wPBA. Thus by the maximum principle, we conclude that upzqď M`ϵ for all zPA. By construction
of A, we also know that upzqď M`ϵ for all z P ΩzA, so we have upzqď M`ϵ for all z P Ω. Since this
argument holds for any ϵą 0 we conclude that upzqď M for all zP Ω.
Problem 12b. Show that if u is bounded from above and the above condition holds for all but ﬁnitely
manyz0PB Ω, then it still follows that upzqď M for all zP Ω.
Solution. Since Ω is bounded, let d “ diampΩq “supz,wPΩ|z´w| ă 8. Let p1,...,p N be the points
inBΩ for which the limsup condition above does not hold. Deﬁne the function
vpzq :“ ´log
⏐⏐⏐⏐
z´p1
d
⏐⏐⏐⏐´... ´ log
⏐⏐⏐⏐
z´pN
d
⏐⏐⏐⏐.
45

Note that v is a nonnegative harmonic function in Ω because the function
z ÞÑ
ˆz´p1
d
˙
¨¨¨
ˆz´pN
d
˙
is a nonvanishing analytic function in Ω.
Fix ϵ ą 0 and deﬁne fpzq “upzq´ ϵvpzq. For any z0 P BΩztp1,...,p Nu, the limsup condition holds,
and so as in the previous problem we have a radius rpz0q such that |z´z0|ă rpz0q implies upzqď M`ϵ,
and since vě 0 we also have fpzqď M`ϵ for all such z. However, for any pj, since u is bounded above
and vpzqÑ8 as zÑ pj, there is also a radius rpjq such that |z´pj|ă rpjq implies fpzqď M`ϵ. Now
we proceed as in the previous problem. Since BΩ is compact, it can be covered by ﬁnitely many of the balls
Bpz0,rpz0qq andBppj,rpjqq. So we obtain a smaller set AĎ Ω on whichf is harmonic, extends continuously
to the boundary, and satisﬁes fpwqď M`ϵ on the boundary of A. So by the maximum principle and by
construction of A we have fpzqď M`ϵ for all z P Ω, i.e. upzqď M`ϵ`ϵvpzq for all z P Ω. And this
argument holds for any ϵą 0, so we conclude that upzqď M for all zP Ω.
46

9 Spring 2013
Problem 1. Suppose f : RÑ R is bounded, Lebesgue measurable, and
lim
hÑ0
ż 1
0
|fpx`hq´ fpxq|
h dx “ 0.
Show that f is a.e. constant on r0, 1s.
Solution. Let Fpxq “
şx
0fptqdt. By the Lebesgue diﬀerentiation theorem, there is a set E of measure
zero such that
lim
hÑ0
Fpx`hq´ Fpxq
h “ fpxq
for all x R E. Then for any a,b R E, pick h small enough so that without loss of generality we have
a,a `hăb,b `h, then we have
|fpaq´ fpbq| “ lim
hÑ0
⏐⏐⏐⏐
Fpa`hq´ Fpaq
h ´ Fpb`hq´ Fpbq
h
⏐⏐⏐⏐ “ lim
hÑ0
1
h
⏐⏐⏐⏐⏐
żb
a
fptqdt´
żb`h
a`h
fptqdt
⏐⏐⏐⏐⏐
ď lim
hÑ0
1
h
żb`h
a`h
|fpt`hq´ fptq|dt ď lim
hÑ0
1
h
ż 1
0
|fpt`hq´ fptq|dt “ 0,
so f is constant a.e.
Problem 2. Consider the Hilbert space 𝓁2pZq. Show that the Borel σ-algebra N on 𝓁2pZq associated
to the norm topology agrees with the Borel σ-algebra W on 𝓁2pZq associated to the weak topology.
Solution. Note: I’m pretty sure this argument still works if 𝓁2pZq is replaced by any separable Hilbert
space.
It’s known that the weak topology is coarser than the norm topology, so we automatically have W Ď N .
We just need to show that any norm-open set in 𝓁2pZq is in W. Since 𝓁2pZq with the norm topology is
separable, any norm-open set is a countable union of open balls, so it suﬃces to show that every norm-open
ball is in W. Fix Bpx,rq“t yP𝓁2pZq :||y´x||2
𝓁2ăr2u. We can view this as a preimage f´1pr0,r 2qq where
f :𝓁2pZqÑ R is given by
fpyq :“ ||y´x||2 “ ||y||2`||x||2´ 2 Rexy,xy “
8ÿ
n“1
|xy,eny|2`||x||2´ 2 Rexy,xy
where tenu is an orthonormal basis for 𝓁2pZq and we have used Parseval’s theorem. We claim that this
function is W-measurable. This is because by deﬁnition of the weak topology, the function y ÞÑ xy,zy is
weak-continuous for anyzP𝓁2pZq and therefore W-measurable. So the ﬁrst term in f is a countable sum of
non-negative measurable functions, which is measurable (combination of the facts that g measurable implies
|g|2 measurable, sum of measurable functions is measurable, and pointwise limit of measurable functions
is measurable). The second term in f is a constant, which is measurable, and the third term in f is the
real part of a measurable function, again measurable. So f is a W-measurable function, and therefore
Bpx,rq“ f´1pr0,r 2qqP W.
Problem 3. Givenf : R2Ñ R continuous, we deﬁne
rArfspx,yq :“ 1
2π
żπ
´π
fpx`r cospθq,y `r sinpθqqdθ
and
rMfspx,yq :“ sup
0ără1
rArfspx,yq.
47

By a theorem of Borgain, there is an absolute constant C so that
||Mf||L3pR2qďC||f||L3pR2q
for all f PCcpR2q. Use this to show the following: If K Ă R2 is compact, then rArχKspx,yqÑ 1 as rÑ 0
at almost every point px,yq in K (with respect to Lebesgue measure).
Solution. We would like to mimic the proof of the Lebesgue diﬀerentiation theorem. This doesn’t work
directly since we are only given Borgain’s result for continuous functions, so we start by expanding this result
slightly. In what follows C will always denote an absolute constant which may change from line to line.
Claim. Let S be a bounded open subset of R2 with λpSqă8 . Then for tą 0 we have
λptpx,yqP R2 :rMχSspx,yqą tuqď CλpSq3
t3 .
Proof. First note that the restriction of χS to a circle is Borel measurable with respect to the uniform
measure on the circle, since the restriction of an open set to a subset of R2 is open in the subspace topology.
SorMχSs is deﬁned.
Note that χS is the characteristic function of an open set and is therefore lower semi-continuous. Thust
we may ﬁnd an increasing sequence of functions fkPCcpR2q converging monotonically to χS. By replacing
fk with maxpfk, 0q, we may assume that each fk is non-negative. From the weak-type L3 estimate which
follows from Borgain’s result, we have
λptpx,yq :rMfkspx,yqą tuqď Ct´3||fk||3
3ďCt´3||χS||3
3“Ct´3λpSq.
IfrMχSspx,yqą t, then there exists rPp 0, 1q such thatrArχSspx,yqą t, and by monotone convergence,
we haverArfkspx,yqą t for suﬃciently large k. Since Mfk is an increasing sequence of functions, we can
write
tpx,yq :rMχSspx,yqą tu“
8ď
k“1
tpx,yq :rMfkspx,yqą tu.
Then applying continuity from below along with the earlier weak-type estimate gives
λptpx,yq :rMχSspx,yqą tuqď Ct´3||f||3
3,
which proves the claim.
To prove the main result, we deﬁne
Sn“tpx,yqP K : lim sup
rÑ0
|ArχKpx,yq´ 1|ą 1
nu.
Next we ﬁx ϵą 0 and approximate K by a bounded open set U Ě K where λpUzKq ăϵ. Note that the
stated theorem is true if we replaced K with U. For ﬁxed rPp 0, 1q andpx,yqP K we have
|ArχKpx,yq´ 1|ď |ArχKpx,yq´ ArχUpx,yq|` |ArχUpx,yq´ 1s|
“rArχUzKspx,yq` |ArχUpx,yq´ 1s|
ďrMχUzKspx,yq` |ArχUpx,yq´ 1s|.
As rÑ 0 the last term tends to 0, so ifpx,yq lies in Sn thenrMχUzKspx,yqą 1{n. Note that UzK is open,
so the claim applies and gives
λ˚pSnqď Cp1{nq´3λpUzKq3ďCn3ϵ3.
But ϵ was arbitrary, so λ˚pSnq“ λpSnq“ 0. Finally we have λpŤ8
n“1Snq“ 0, so
lim sup
rÑ0
|ArχKpx,yq´ 1|“ 0
48

for a.e. px,yq in K, and the main result follows.
Problem 4. Let K be a non-empty compact subset of R3. For any Borel probability measure µ on
K, deﬁne the Newtonian energy IpµqPp 0,`8s by
Ipµq :“
ż
K
ż
K
1
|x´y|dµpxqdµpyq
and let RK be the inﬁmum of Ipµq over all Borel probability measures µ on K. Show that there exists a
Borel probability measure µ such that Ipµq“ RK.
Solution. Let M be the set of all Borel probability measures on K. By the Riesz representation theo-
rem,M is a subset of the unit ball in the dual space CpKq˚. Let µn be a sequence in M withIpµnqÑ RK.
By the Banach-Alaoglu theorem, the unit ball in CpKq˚ is weak-˚ compact, and since CpKq is separable, it
is also sequentially compact. So by passing to a subsequence if necessary, we have a measure µ in the unit
ball of CpKq˚ with µnÑµ in weak-˚. By applying weak-˚ convergence to the constant function 1, we see
that µ is also a probability measure on K.
Now we claim that Ipµq“ RK. We ﬁrst need to show that µnbµnÑµbµ in weak-˚, i.e. that
ĳ
fpx,yqdµnpxqdµnpyq Ñ
ĳ
fpx,yqdµpxqdµpyq
for all f PCpKˆKq. This is clear for all functions of the form px,yqÞÑ gpxqhpyq with g,h PCpKq by the
weak-˚ convergence of µn to µ. Let F be the span of all functions of the above form. Then it’s easy to
check that F is dense in CpKˆKq by the Stone-Weierstrass theorem. Thus the desired result holds for all
of CpKˆKq. This establishes that µnbµnÑµbµ in weak-˚.
We want to conclude that
Ipµq “ lim
nÑ8
Ipµnq “ RK.
We would be done by the weak-˚ convergence ofµnbµn toµbµ, exceptpx,yqÞÑ 1
|x´y| isn’t continuous on
KˆK. However, it is lower semicontinuous, so by the portmanteau theorem, we have
lim inf
nÑ8
Ipµnq ě Ipµq.
But lim infnÑ8Ipµnq“ RK andRK is the inf of all values of Ipµq, so also RKďIpµq and thus Ipµq“ RK,
so I achieves its minimum.
Problem 5. Deﬁne a Hilbert space
H :“
"
u : DÑ R : u is harmonic and
ż
D
|upx,yq|2dxdy ă8
*
with inner product xf,gy“
ş
Dfgdxdy .
(a) Show that fÞÑfxp0, 0q is a bounded linear functional on H.
(b) Compute the norm of this linear functional.
Solution (bad). We show that the norm is 2{?π. Since u is harmonic, ux also is. So we apply the mean
value property on a disc of radius rPp 0, 1q to get
|uxp0q| “ 1
πr2
⏐⏐⏐⏐⏐
ż
Bp0,rq
uxdA
⏐⏐⏐⏐⏐ “ 1
πr2
⏐⏐⏐⏐⏐
ż
BBp0,rq
udy
⏐⏐⏐⏐⏐
49

by Green’s theorem. So
|uxp0q| “ 1
πr2
⏐⏐⏐⏐
ż 2π
0
upr cosθ,r sinθqr cospθqdθ
⏐⏐⏐⏐
|uxp0q|2 ď 1
π2r2
ˆż 2π
0
upr cosθ,r sinθq2dθ
˙ˆż 2π
0
cos2θ
˙
by Cauchy-Schwarz
πr2 |uxp0q|2 ď
ż 2π
0
upr cosθ,r sinθq2dθ.
Multiplying both sides by r and integrating over rPr 0, 1s we get
π
4 |uxp0q|2 ď
ż
D
u2dA,
so |uxp0q| ď 2?π||u||H. Finally, it’s easy to check that upx,yq “x achieves this bound, so 2 {?π is the
operator norm.
Alternate solution (way better). Since D is simply connected, u is the real part of an analytic function
f “ u`iv on D. Write fpzq “ř8
n“0anzn. We know this power series converges uniformly on compact
subsets of D. We have
upreiθq “
8ÿ
n“0
Repanrneinθq “
8ÿ
n“0
rnpRepanq cospnθq´ Impanq sinpnθqq.
We also know that ux“ Repf1q, so we have uxp0q“ Repa1q. We have
ż
D
u2dA “
ż 1
0
ż 2π
0
˜ 8ÿ
n“0
rnpRepanq cospnθq´ Impanq sinpnθqq
¸2
rdθdr
“
ż 1
0
r
ż 2π
0
8ÿ
n,k“0
rnrkpRepanq cospnθq´ Impanq sinpnθqqpRepakq cospkθq´ Impakq sinpkθqqdθdr.
Using the orthonormality properties of sin and cos and the fact that the power series converges uniformly
on compact sets, this is equal to
“
ż 1
0
8ÿ
n“0
r2n`1
ż 2π
0
`
Repanq2 cos2pnθq` Impanq2 sin2pnθq
˘
dθdr
“
ż 1
0
8ÿ
n“0
r2n`1πpRepanq2` Impanq2qdr
ě
ż 1
0
r3π Repa1q2 “ π
4 Repa1q2.
Thus we see that
Repa1q2 ď 4
π
ż
D
u2dA,
so
uxp0q “ Repa1q ď 2?π||u||H.
This shows that the operator norm is at most 2{?π. And by inspecting the above proof, we see that equality
holds if Repanq“ Impanq“ 0 for n‰ 1 and Impa1q“ 0. This is achieved when fpzq“ z, i.e. upx,yq“ x, so
the operator norm is exactly 2{?π. Alternatively one could compute directly that upx,yq“ x achieves this
bound.
50

Problem 6. Let
X :“
"
ξÞÑ
ż
R
eiξxfpxqdx :fPL1pRq
*
.
Show that (a) X is a subset of C0pRq, (b) X is a dense subset of C0pRq, and (c) X‰C0pRq.
Solution. Note that ξ ÞÑ
ş
Reiξxfpxq is the function pfp´ξq. For the sake of a having a convenient no-
tation, we will prove each of these results for the Fourier transform. Obviously (a)-(c) will follow.
(a) Continuity follows immediately from the dominated convergence theorem, since
⏐⏐e´iξxfpxq
⏐⏐ď |fpxq|,
which is integrable by hypothesis.
By directly calculating the integral, it is easy to see thatps lies inC0pRq whens is a sum of characteristic
functions of open intervals. The set of such functions is dense in L1pRq, so given fPL1 choose s with
||f´s||1ăϵ. Then
ˇˇˇ
ˇˇˇpf´ps
ˇˇˇ
ˇˇˇ
8
ď||f´s||1ăϵ, and so
lim
|ξ|Ñ8
pfpξqď lim
|ξ|Ñ8
spξq` ϵ“ϵ.
But ϵ was arbitrary, so the limit is 0.
Remark. One could also solve this problem by invoking the density of C8
c (or even C1
c ) in L1pRq and
then applying integration by parts.
(b) We claim that C8
c pRq is dense in CcpRq. To see this, ﬁx f P CcpRq and choose M large enough so
that |fpxq| ă ϵ when |x| ą M. Let g be a smooth function such that |fpxq´ gpxq| ă ϵ for x P
r´pM`1q,M`1s. Also letβ : RÑr 0, 1s be a smooth bump function with supppβqĎr´p M`1q,M`1s
and which takes the value 1 on r´M,Ms. Then βg is smooth, and we have ||f´βg||8ă 2ϵ.
So C8
c pRq is dense in CcpRq, and in particular the space of Schwartz functions is dense in CcpRq.
The Fourier transform is a bijection on the space of Schwartz functions, so X contains all Schwartz
functions which gives a dense subset.
(c) Recall that the Fourier transform F is an injective bounded linear map from L1pRq to C0pRq. If the
Fourier transform was surjective ontoC0pRq then by the open mapping theorem F´1 :C0pRqÑ L1pRq
would be bounded.
Let h “ χr´1,1s and let hi P C8
c pRq be a uniformly bounded sequence of functions which converges
to h in L2 (for instance, bump functions would suﬃce). Also let gi “ F´1phiq. Note that the gi’s
are Schwartz functions and therefore lie in L1. (Alternatively, this must be true by the hypothesis
of surjectivity.) Now h lies in L2 and is therefore the Fourier-Plancherel transform of a function g.
Since the Fourier-Plancherel transform is an L2 isometry, we have that giÑg in L2. By passing to a
subsequence if necessary, we may assume that giÑg pointwise almost everywhere.
On the other handg is not inL1, otherwise its Fourier transform would be continuous. Thus by Fatou’s
lemma, limiÑ8||gi||1“8. However this contradicts the boundedness of F´1, since we assumed that
the hi’s were uniformly bounded.
Remark. It turns out that gpxq“ sinpxq
x . However this wasn’t important to us. In fact we could have
takenh to be any bounded L2 function which doesn’t agree a.e. with a continuous function.
Problem 7. Let f : CÑ C be an entire function such that log |f| is absolutely integrable with respect to
planar Lebesgue measure. Show that f is constant.
Solution. Suppose that f is not constant. By Liouville there exists z0 P C such that log |fpz0q| ą 1.
Recall that log|f| is subharmonic. By the mean value property we have
ż
R2
log|fpzq|dλ“
ż8
r“0
r
ż 2π
0
log|fpz0`reiθq|dθdr ě
ż8
r“0
2πrdr “8.
51

Problem 8a. Let A and B be positive deﬁnite nˆn real symmetric matrices with the property
ˇˇˇˇBA´1x
ˇˇˇˇď||x||
for all xP Rn, where||x|| denotes the usual Euclidean norm. Show that for each pair x,y P Rn,
zÞÑ
@
y,BzA´zx
D
admits an analytic continuation from 0 ăză 1 to the whole complex plane.
Solution. Since A and B are symmetric and positive deﬁnite, we can write A “ SAΛAS´1
A and B “
SBΛBS´1
B where ΛA and ΛB are diagonal matrices with positive diagonal entries. Then for z P p0, 1q,
A´z“SAΛz
AS´1
A andBz“SBΛz
BS´1
B , where Λz
A is simply the matrix gotten by raising each diagonal entry
to the power z. The given function is seen to be a polynomial in the zth powers of the eigenvalues of B
and the inverses of the eigenvalues of B, and therefore extends to a holomorphic function on C. (Note that
λz“elogpλqz, which is holomorphic.)
Problem 8b. Show that
ˇˇˇˇBθA´θx
ˇˇˇˇď||x|| for all 0 ďθď 1.
Solution. Forx,y P Rn, let fx,ypzq be holomorphic function from part (a).
When Repzq“ 0 we note that the eigenvalues ofBz andA´z have norm 1. These matrices are symmetric,
so they each have operator norm 1, which implies that
|fx,ypzq|“
⏐⏐@
y,BzA´zx
D⏐⏐ď||y||
ˇˇˇˇBzA´zx
ˇˇˇˇď||y||||x||.
When Repzq“ 1, write z“ 1`bi. Then
ˇˇˇˇBzA´zˇˇˇˇ
op“
ˇˇˇˇBizBA´1A´izˇˇˇˇ
opď
ˇˇˇˇBizˇˇˇˇ
op
ˇˇˇˇBA´1ˇˇˇˇ
op
ˇˇˇˇA´izˇˇˇˇ
opď 1,
and so
|fx,ypzq|ď||y||
ˇˇˇˇBzA´zx
ˇˇˇˇď||y||||x||.
Also note that fx,y is bounded on the strip S “t z : RepzqPr 0, 1su, since each function λz is bounded
on the strip (recall the solution to part (a)). By the Hadamard three lines theorem, we conclude that fx,y is
bounded by ||x||||y|| everywhere in S. (Alternatively one can mimic the proof of this theorem by applying
the Phragmen-Lindelof method.)
Finally for θPr 0, 1s we have
ˇˇˇˇBθA´θx
ˇˇˇˇ“ sup
||y||“1
|fx,ypθq|ď||x||.
Problem 9. LetPpzq be a non-constant polynomial, all of whose zeros lie in a half planetzP C : Repzqă σu.
Show that all zeros of P1pzq also lie in the same half plane.
Solution. WritePpzq“p z´a1q¨¨¨p z´anq. Then we have
P1pzq
Ppzq “ 1
z´a1
`... ` 1
z´an
.
Suppose that P1pzq“ 0. If Ppzq“ 0 also, then z is obviously in the same half plane, so assume otherwise.
Then in particular we have
0 “ Re
ˆ 1
z´a1
˙
`... ` Re
ˆ 1
z´an
˙
“ Repzq´ Repa1q
|z´a1|2 `... ` Repzq´ Repanq
|z´an|2 .
52

So
Repzq
nÿ
j“1
1
|z´aj|2 “
nÿ
j“1
Repajq
|z´aj|2 ă σ
nÿ
j“1
1
|z´aj|2,
so Repzqă σ.
Problem 10. Let f : C Ñ C be a non-constant entire function. Without using either of the Picard
theorems, show that there exist arbitrarily large complex numbers z for which fpzq is a positive real.
Solution. Fix a closed ball Br centered at 0 of radius r so that fpzq P CzRě0 for |z| ąr. By com-
pactness,|fpzq| attains a maximum value R on Br. Then fpzq´ R is a holomorphic function which avoids
the poitive real axis.
Letφ : CzRě0Ñ D be a conformal equivalence of the complex plane with the positive real axis removed,
and the open unit disc. Such a map exists by the Riemann mapping theorem. For the sake of being concrete
we may take
φpzq“
?z´i?z`i
where
?
eiθ“eiθ{2 for θPr 0, 2πq.
The mapzÞÑφpfpzq´Rq is holomorphic and bounded, and therefore constant by Liouville. So for some
constantC, we have fpzq“ φ´1pCq` R. We conclude that f is constant.
Problem 11. Let fpzq“´ πz cotpπzq be a meromorphic function on C.
(a) Locate all poles of f and determine their residues.
(b) Show that for each ně 1 the coeﬃcient of z2n in the Taylor expansion of fpzq about z“ 0 coincides
with
an “
8ÿ
k“1
2
k2n.
Solution. (a) We have
´πz cotpπzq “ ´πz cospπzq
sinpπzq .
From this representation it is clear that f has simple poles at every nonzero integer. (because sin pπzq has a
simple pole at every integer). So to calculate the residue at z“n we have
Respf,z “nq “ lim
zÑn
´πzpz´nq cospπzq
sinpπzq “ lim
zÑn
´z¨ cospπzq¨ πpz´nq
sinpπpz´nqq “ p´1qn`1n.
(b) Here we use the other standard representation
π cotpπzq “
8ÿ
k“´8
1
z´k “ 1
z`
8ÿ
k“1
2z
z2´k2,
so we have
fpzq “ ´1´
8ÿ
k“1
2z2
z2´k2.
Writefpzq“ gpz2q where gpzq“´ 1´ř8
k“1
2z
z´k2 . Note that g is holomorphic except at the points where
it equals 8 because the series deﬁning it converges uniformly on compact sets. So the coeﬃcient of z2n in
the power series for f is the same as the coeﬃcient of zn in the power series for g. It now suﬃces to show
53

that gpnqp0q“ n!¨ř8
k“1
2
k2n . Write gpzq“´ 1´ 2zhpzq, where hpzq“ ř8
k“1
1
z´k2 . Again, h is holomorphic
except for at the points where it blows up. Therefore we have
gpnqp0q “ ´2
nÿ
j“0
ˆn
j
˙
pzÞÑzqpjqp0qhpn´jqp0q “ ´2hpn´1qp0q.
Since the series deﬁning h converges uniformly on compact sets, it can be diﬀerentiated term-by-term, so
it’s easy to see by induction that
hpnqpzq “
8ÿ
k“1
p´1qnn!
pz´k2qn`1.
Therefore
gpnqp0q “ ´2hpn´1qp0q “ n!
8ÿ
k“1
2
k2n.
Problem 12. Let f : HÑ H be a holomorphic function obeying
lim
yÑ8
yfpiyq “ i and |fpzq| ď 1
Impzq for all zP H.
(a) For ϵą 0, write gϵpxq :“ 1
π Imfpx`iϵq. Show that
fpz`iϵq “
ż
R
gϵpxq
x´z dx.
(b) Show that there exists a Borel probability measure µ on R such that
fpzq “
ż
R
dµpxq
x´z dx.
Solution.
54

10 Fall 2013
Problem 1. Let U and V be open and connected sets in the complex plane C, and f : U Ñ C be a
holomorphic function with fpUqĎ V. Suppose that f is a proper map from U into V , i.e., f´1pKqĎ U is
compact, whenver KĎV is compact. Then f is surjective.
Solution. We use a connectedness argument. First note that f can’t be constant on U, otherwise f
isn’t proper. Then by the open mapping theorem, fpUq is open.
We claim that VzfpUq is also open. Fix vPVzfpUq, and let B1ĎB2Ď... ĎV be a seqence of nested
closed balls around v such that Ş
iPNBi“v. We have
H“ f´1ptvuq“ f´1
˜č
iPN
Bi
¸
“
č
iPN
f´1pBiq.
By properness, each f´1pBiq is compact. In general, a nested sequence of nonempty compact sets has
nontrivial intersection1 It follows that one of the sets f´1pBiq must be empty. The interior of Bi is an open
neighborhood of v lying in VzfpUq. But vPVzfpUq was arbitrary, so VzfpUq is open.
Since fpUq is nonempty, and V is connected we must have V “fpUq.
Problem 2. Show that there is no function f that is holomorphic near 0 P C and satisﬁes
fp1{n2q “ n2´ 1
n5
for all large nP N.
Solution. Since f is holomorphic near 0, there is an rą 0 such that f has a power series expansion
fpzq “
8ÿ
j“0
ajzj
valid in Bp0,rq. If f is identically zero then it obviously does not satisfy the condition, so assume it isn’t.
Then let k be the smallest j for which aj‰ 0, so we can write
fpzq “ xk
8ÿ
j“k
ajzj´k.
When n is big enough so that 1{n2ăr, we have
fp1{n2q “ 1
n2k
8ÿ
j“1
aj
n2pj´kq.
We have the inequalities
|fp1{n2q| ď 1
n2k
˜
|ak|` 1
n2
⏐⏐⏐⏐⏐
8ÿ
j“k`1
aj
n2pj´k´1q
⏐⏐⏐⏐⏐
¸
ď p3{2q|ak|
n2k
|fp1{n2q| ě 1
n2k
˜
|ak|´ 1
n2
⏐⏐⏐⏐⏐
8ÿ
j“k`1
aj
n2pj´k´1q
⏐⏐⏐⏐⏐
¸
ě p1{2q|ak|
n2k
for suﬃciently large n. Thus if the condition fp1{n2q“p n2´ 1q{n5 is satisﬁed, we would have
p1{2q|ak|
n2k ď n2´ 1
n5 ď p3{2q|ak|
n2k
1To see this, consider a sequence consisting of a point from each set.
55

for all suﬃciently large n. But since pn2´ 1q{n5 is asymptotic to n´3 asnÑ8 , it can’t be Θpn´2kq for any
integerk, and so there is no integer k for which this is true. So f can’t satisfy the condition.
Alternate Solution. By setting x “ 1{n, we have fpx2q “x3´x5 for all x of the form 1 {n where
nP N is large enough. We also have fp0q “0 by continuity. Thus fpx2q is a holomorphic function on a
neighborhood of 0 which agrees with x3´x5 on a set with a limit point. So fpx2q“ x3´x5 everywhere on
a neighborhood of 0. Then for |z| small enough we must have
z3´z5“fpz2q“ fpp´zq2q“p´ zq3´p´zq5,
which is false for z‰ 0.
Problem 3. Does there exist a holomorphic function f : DÑ C such that
lim
nÑ8
|fpznq| “ `8
for all sequences tznu in D with limnÑ8|zn|“ 1?
Solution. There does not exist such a function. Roughly, we would like to apply the minimum princi-
ple on the disk. Unfortunately f may take on the value 0 so this doesn’t work directly. We can rectify the
situation as follows.
By hypothesis, f cannot have a sequence of zeros approaching the boundary of D. Moreover the zeros of
f cannot have a limit point in the interior of D, otherwisef would be identically 0. Moreover each zero of f
occurs with ﬁnite multiplicity. So by compactness, f has only ﬁnitely many zeros α1,...aα n in D counting
multiplicity. Let ppzq“p z´α1q... pz´αnq. Then ppzq{fpzq has removable singularities at the zeros of f,
and hence may be regarded as an analytic function on D. By hypothesis, ppzq{fpzq extends continuously to
take the value 0 on the boundary of D. But then by the maximum principle, ppzq{fpzq is identically 0, which
is a contradiction.
Problem 4. Letu be a non-negative continuous function on Dzt0u that is subharmonic on Dzt0u. Suppose
that u|BD“ 0 and
lim
rÑ0`
1
r2 logp1{rq
ż
tzPC:0ă|z|ăru
upzqdλpzq “ 0,
where integration is with respect to Lebesgue measure λ on C. Show that then u” 0.
Solution. First we want to show that upzq “oplog |1{z|q as |z| Ñ 0. Fix ϵ ă 0. By the hypothesis,
let|z| be small enough so that
ż
tzPC:0ă|w|ă3|z|{2u
upwqdλpwq ă ϵ|z|2 log|1{z|.
Then by the mean value property for subharmonic functions we have
upzq ď 1
πp|z|{2q2
ż
twPC:|w´z|ăp1{2q|z|u
upwqdλpwq ď 4π
|z|2
ż
twPC:0ă|w|ă3|z|{2u
upwqdλpwq ă 4πϵ|z|2 log|1{z|
|z|2 ,
which shows that upzq“ oplog |1{z|q as|z|Ñ 0.
Now let α ą 0 and note that the function fpzq :“ α log |1{z| is harmonic on Dzt0u. Thus we know that
u´f does not have a maximum value inside Dzt0u. Notice that since upzq “oplog |1{z|q as |z| Ñ 0,
upzq´ fpzq Ñ ´8as |z| Ñ0. Thus there exists an r ą 0 such that upzq´ fpzq ď0 for |z| ďr. Now
on the compact set S :“ tz P C : r ď |z| ď1u, u´f is continuous so it achieves a maximum. But the
maximum must be achieved on the boundary of f because u´f doesn’t have any maxima inside Dzt0u.
Since u´f “ 0 on BD and u´f ď 0 on |z|“ r by choice of r, this implies that u´f ď 0 in all of Dzt0u.
So upzq´ α log |1{z|ď 0 for all zP Dzt0u, and since α is arbitrary this implies upzqď 0 for all zP Dzt0u,
56

which since uě 0 by hypothesis gives that u is identically zero.
Problem 5. Lettfnu be a sequence of holomorphic functions on D and suppose that
ż
D
|fnpzq|dλpzq ď1
for all n P N. Show that then there exists a subsequence tfnku that converges uniformly on all compact
subsets of D.
Solution. We would like to show that the functions fn form a normal family. Since each fn is holo-
morphic, this is equivalent to verifying that the fn’s are uniformly bounded on the closed ball Br“Bp0,rq
for eachrPp 0, 1q. (Note that each compact subset of D is contained in some such ball.) Fix z0PBr and let
U“Bpz0, 1´|z0|q. Applying the mean value property we have
1ě
ż
U
|fnpzq|dλpzqě
ˇˇˇˇ
ż
U
fnpzqdλ
ˇˇˇˇěπp1´|z0|q2|fpz0q|ě πp1´rq2|fpz0q|.
Therefore|fpz0q|ď 1
πp1´rq2 for all z0PBr, and so f is uniformly bounded on compact sets.
Problem 6. Let U Ď C be a bounded open set with 0 P U, and f : U Ñ C be holomorphic with
fpUqĎ U and fp0q“ 0. Show that |f1p0q|ď 1. Hint: Consider the iterates fn“f˝¨¨¨˝ floooomoooon
n times
of f.
Solution. First we prove by induction thatpfnq1p0q“p f1p0qqn. The case n“ 1 is obviously true. Supposing
pfn´1q1p0q“p f1p0qqn´1, since fp0q“ 0 we have
pfnq1p0q “ pfn´1˝fq1p0q “ pfn´1q1pfp0qqf1p0q “ pf1p0qqn,
so the induction is ﬁnished. Note that since U is a bounded set and fpUqĎ U, also fnpUqĎ U for all n
and there is an M such that |fnpzq|ď M for all zPU and all n. Since U is open, let Rą 0 be such that
Bp0,RqĎ U. Then applying the Cauchy estimate to fn, we get
|f1p0q|n “ |pfnq1p0q| ď 1
R sup
|z|“R
|fnpzq| ď M
R
for all n. If |f1p0q| ą 1 this would be impossible because |f1p0q|n would tend to inﬁnity as n Ñ 8, so
|f1p0q|ď 1.
Problem 7. Show that there is a dense set of functions fPL2pr0, 1sq such that xÞÑx´1{2fpxqP L1pr0, 1sq
and
ş1
0x´1{2fpxqdx“ 0.
Solution. Let S :“ tf P L2pr0, 1sq : x ÞÑ x´1{2fpxq PL1pr0, 1sq and
ş1
0x´1{2fpxqdx “ 0u. Since the
set of continuous functions with compact support properly contained inr0, 1s is dense inL2pr0, 1sq, it suﬃces
to show that S is dense in that set. Let g be a function which is continuous on rδ, 1s and identically zero on
r0,δs for some ﬁxed δą 0. Fix ϵą 0. Deﬁne
I :“
ż 1
δ
x´1{2gpxqdx “ă 8
because x´1{2 is bounded on rδ, 1s. Now deﬁne the function fϵ by
fϵpxq :“
$
’&
’%
gpxq xPrδ, 1s
´Iϵ
δϵ x´1{2`ϵ xPp 0,δq
0 x“ 0
.
57

We calculate
ż 1
0
x´1{2fϵpxqdx “ ´Iϵ
δϵ
żδ
0
x´1`ϵdx`I “ 0
and
||fϵ´g||2
2 “
żδ
0
|fϵpxq´ gpxq|2dx ď 4
żδ
0
|fϵpxq|2dx
ă 4I2ϵ2
δ2ϵ
żδ
0
x´1`2ϵdx “ 4I2ϵ2
δ2ϵ ¨ δ2ϵ
2ϵ “ 2I2ϵ,
which can be made as small as desired. So S is dense in L2pr0, 1sq.
Problem 8(a). Compute
lim
kÑ8
żk
0
xn
´
1´ x
k
¯k
dx
where nP N.
Solution. Deﬁne the functions fkpxq :“ xnp1´x{kqk¨χr0,ks. For each x P r0,8q, as soon as k ě x
we havefkpxq“ xnp1´x{kqk, so we see that fkpxqÑ xne´x pointwise onr0,8q. Also note that for each k,
fkpxqě 0 for all xPr 0,8q becausep1´x{kqě 0 for xPr 0,ks and fkpxq“ 0 for xąk. We want to show
that fkpxq ďfk`1pxq for all x so that we can use the Monotone Convergence Theorem. By the AM-GM
inequality, we have
ˆ
1¨
´
1´ x
k
¯k˙1{pk`1q
ď 1`k
`
1´ x
k
˘
k` 1 “ 1`k´x
k` 1 “ 1´ x
k` 1,
sop1´x{kqkďp 1´x{pk` 1qqk`1. This establishes that fkďfk`1. Since xne´x is integrable onr0,8q, the
Monotone Convergence Theorem gives
lim
kÑ8
żk
0
xn
´
1´ x
k
¯k
dx “
ż8
0
fkpxqdx “
ż8
0
xne´xdx “ n!
Problem 8(b). Compute
lim
kÑ8
ż8
0
´
1` x
k
¯´k
cospx{kqdx.
Solution. For eachkě 2 deﬁnefkpxq :“p 1`px{kqq´k cospx{kq. For a ﬁxedxPr 0,8q, we have cospx{kqÑ 1
as kÑ8 andp1`px{kqq´kÑe´x as kÑ8 . Thus fkpxq converges pointwise to e´x onr0,8q. Using the
same AM-GM inequality argument as in the problem above, we see
ˆ
1¨
´
1` x
k
¯k˙1{pk`1q
ď 1`k
`
1` x
k
˘
k` 1 “ k` 1`x
k` 1 “ 1` x
k` 1,
which establishesp1`x{kqkďp 1`x{pk` 1qqk`1. Thus fkpxqě fk`1pxq for all xPr 0,8q. So we have the
estimate
|fkpxq| ď
´
1` x
k
¯´k
ď 1
p1`x{2q2
which is integrable on r0,8q, for all kě 2. Thus by the Dominated Convergence Theorem we have
lim
kÑ8
ż8
0
´
1` x
k
¯´k
cospx{kqdx “
ż8
0
e´x “ 1.
58

Note. Alternate way of showing that Dominated Convergence applies: we just need to show that 0 ď
p1´x{kqk ď e´x for all k and all x P r0,ks. Equivalent, we want k logp1´x{kq ď ´x. Expanding
tÞÑ logp1´tq in a power series around t“ 0 gives this.
Problem 9. Let X be a Banach space, Y be a normed linear space, and B : XˆY Ñ R be a bilin-
ear function. Suppose that for each xP X there exists a constant Cxě 0 such that |Bpx,yq|ď Cx||y|| for
all yPY , and for each yPY there exists Cyě 0 such that |Bpx,yq|ď Cy||x|| for all xPX.
Show that then there exists a constant Cě 0 such that|Bpx,yq|ď C||x||||y|| for all xPX and all yPY .
Solution. For each y P Y , deﬁne the function Ty : X Ñ R by Typxq “Bpx,yq. Since B is bilinear,
Ty is a linear functional on X. By hypothesis, for each y we have |Typxq|“| Bpx,yq| ď Cy||x||, so Ty is
actually a bounded linear functional. Let F“tTy :||y||“ 1u. This is a family of bounded linear functionals
on X, and for each xPX we have by the other hypothesis
sup
||y||“1
|Typxq| “ sup
||y||“1
|Bpx,yq| ď Cx ă 8.
Thus sinceX is a Banach space, we can apply the uniform boundedness principle to conclude that sup||y||“1||Ty||ă
8. This means that there is a C ě 0 such that ||Ty|| ďC for any ||y|| “1, which means that |Typxq| “
|Bpx,yq| ďC||x|| for any x P X and any ||y|| “1. Then by linearity in the second variable we get that
|Bpx,yq|ď C||x||||y|| for any xPX, yPY .
Problem 10a. Let f P L2pRq and deﬁne hpxq “
ş
Rfpx´yqfpyqdy for x P R. Show that then there
exists a function gPL1pRq such that
hpξq “
ż
R
e´iξxgpxqdx
for ξP R, i.e. h is the Fourier transform of a function in L1pRq.
Solution. We are motivated by the fact that if g were such a function, then we would have Fpgq “
f˚f“ FpF´1pfqq˚ FpF´1pfqq“ FpF´1pfq2q, so g“ F´1pfq2.
Let F denote the Fourier-Plancherel transform. Recall it is an isometric isomorphism L2 Ñ L2. Given
f P L2, deﬁne g :“ F´1pfq2. It’s clear that gP L1. Let p¨ denote the regular Fourier transform L1 Ñ L8.
Recall thatp¨ and Fp¨q agree on L1XL2. We verify
pg “ {F´1pfqF´1pfq “ FpF´1pfqq˚ FpF´1pfqq “ f˚f.
In the previous line we used the identity pab“ Fpaq˚ Fpbq fora,b PL2. Here is a proof of it (not sure if this
would be required on the qual or not):
We know the identity holds for Schwartz functions (this follows from basic properties of the Fourier transform
and a lot of Fubini’s theorem). Let an,bn be Schwartz functions with anÑa and bnÑb in L2. We know
that zanbn“ Fpanq˚ Fpbnq for eachn, so it suﬃces to show that zanbnÑ pab and Fpanq˚ FpbnqÑ Fpaq˚ Fpbq
in L8. We have
ˇˇˇ
ˇˇˇzanbn´ pab
ˇˇˇ
ˇˇˇ
L8
“
ˇˇˇ
ˇˇˇ {anbn´ab
ˇˇˇ
ˇˇˇ
L8
ď ||anbn´ab||L1 ď ||pan´aqb||L1`||pbn´bqa||L1
ď ||an´a||L2||b||L2`||bn´b||L2||a||L2 Ñ 0
||Fpanq˚ Fpbnq´ Fpaq˚ Fpbq||L8 ď ||Fpan´aq˚ Fpbq||L8`|| Fpbn´bq˚ Fpaq||L8
ď ||Fpan´aq||L2||Fpbq||L2`|| Fpbn´bq||L2||Fpaq||L2
“ ||an´a||L2||b||L2`||bn´b||L2||a||L2 Ñ 0.
59

Problem 10b. Conversely, show that if g P L1pRq, then there is a function f P L2pRq such that the
Fourier transform of g is given by xÞÑhpxq :“
ş
Rfpx´yqfpyqdy.
Solution. Using a similar motivating argument as in part (a), we see that we want to set f “ F´1p
a
qgq
(recall that qgpxq :“ gp´xq and that for Schwartz functions, F2psq“ qs). This is a little annoying becausea
qg isn’t even necessarily deﬁned. But in general, for measurable functions h : RÑ C, we can deﬁne
a
hpxq
to be the square root deﬁned by removing the positive real axis if hpxq is not a positive real, and deﬁne it
to be the positive real square root if hpxq is a positive real. The representation
?
h “ sqrt1ph¨χtx:hpxqRR`uq` sqrt2ph¨χtx:hpxqPR`uq
where sqrt1 is the branch cut square root and sqrt2 is the positive real square root immediately shows that
the square root deﬁned this way is measurable, and it’s clear that
?
hP L2 if and only if hP L1. So the
deﬁnition f :“ F´1p
a
qgqP L2 makes sense. Again, we just verify
f˚f “ F´1p
a
qgq˚ F´1p
a
qgq “ Fpqqgq “ Fpgq.
Here we have used the identity F´1paq˚ F´1pbq “ Fpqabq for a,b P L2. This is proven using a similar
argument as for the corresponding identity in part (a), recalling that F´1“ F3 for Schwartz functions.
Problem 11. Consider the space Cpr0, 1sq of real-valued continuous functions on the unit interval r0, 1s.
We denote by||f||8 :“ supxPr0,1s|fpxq| the supremum norm and by ||f||2 :“
´ş1
0|fpxq|2
¯1{2
the L2-norm of
a function fPCpr0, 1sq.
Let S be a subspace of Cpr0, 1sq. Show that if there exists a constant Kě 0 such that ||f||8ďK||f||2
for all fPS, then S is ﬁnite-dimensional.
Solution. Let S denote the closure of S with respect to the L2 norm. It obviously suﬃces to show
thatS is ﬁnite-dimensional. First we show that S is still contained inCpr0, 1sq. Suppose fPS, then there is
a sequence fnPS with||fn´f||2Ñ 0 as nÑ8 . For any n,m , we have||fn´fm||8ďK||fn´fm||2, and
sincetfnu converges in L2, it is also Cauchy in L2, so by the above inequality it is also a Cauchy sequence
in Cpr0, 1sq. Since Cpr0, 1sq is complete, there is some gP Cpr0, 1sq with||fn´g||8 Ñ 0 as nÑ8 . Note
that since ||h||2ď||h||8 for any hPCpr0, 1sq, we have
||g´f||2 ď ||g´fn||2`||fn´f||2 ď ||g´fn||8`||fn´f||2Ñ 0
as nÑ8 . Thus ||g´f||2“ 0, so f“g in L2, hence f is continuous. Thus SĎCpr0, 1sq.
For each x P r0, 1s, deﬁne the map between normed vector spaces φx : pS,||¨||2q Ñ R by f ÞÑ fpxq.
This is clearly a linear functional on the space S. For any fPS, we have
|φxpfq| “ |fpxq| ď ||f||8 ď K||f||2,
so in factφx is a bounded linear functional on S. Since S is a closed subspace of the Hilbert space L2pr0, 1sq,
it is also a Hilbert space, and thus by the Riesz representation theorem for each x there exists some gxPS
such that fpxq“ φxpfq“x f,gxy for all fPS. Note also that for each x
||gx||2
2 “ |xgx,gxy| “ |gxpxq| ď ||gx||8 ď K||gx||2,
so||gx||2ďK.
Now let tf1,...,f Nu be any linearly independent set in S. By applying the Gram-Schmidt process if
necessary we may assume that it is an orthonormal set. Then by Bessel’s inequality, we have for each x that
Nÿ
j“1
|fjpxq|2 “
Nÿ
j“1
|xfj,gxy| 2 ď ||gx||2
2 ď K2.
60

Then integrating both sides from 0 to 1 we get
K2 ě
Nÿ
j“1
ż 1
0
|fjpxq|2dx “
Nÿ
j“1
||fj||2
2 “ N.
This shows that a linearly independent set in S can have at most K2 elements and thus dimpSqď K2ă8 .
Problem 12(a). Let f : r0, 1s ÑR be a continuous function that is absolutely continuous on each in-
tervalrϵ, 1s with 0ăϵď 1. Show that f is not necessarily absolutely continuous on r0, 1s.
Solution. Let fpxq“ x sinp1{xq for xą 0 and fp0q“ 0. For any xą 0, f is diﬀerentiable and
f1pxq “ sinp1{xq´ cosp1{xq
x .
So for a ﬁxed ϵą 0 and any xPrϵ, 1s, we have
|f1pxq| ď |sinp1{xq|`
⏐⏐⏐⏐
cosp1{xq
x
⏐⏐⏐⏐ ď 1` 1
ϵ.
Thusf1 is bounded on rϵ, 1s, so f is Lipschitz and thus f is absolutely continuous on rϵ, 1s.
Let xn“ 1{2πn and yn“ 1{pπ` 2πnq. Note that we have
|xn´yn| “
⏐⏐⏐⏐
π
4π2n2` 2π2n
⏐⏐⏐⏐ ă 1
n2
|fpxnq´ fpynq| “ |xn`yn| “
⏐⏐⏐⏐
π` 4πn
4π2n2` 2π2n
⏐⏐⏐⏐.
In particular, ř8
n“1|xn´yn| ă 8and ř8
n“1|fpxnq´ fpynq| “ 8. Suppose that f were absolutely con-
tinuous on r0, 1s. Then pick ϵ “ 1 and let δ be such that for any N,M , řM
n“N|xn´yn| ăδ impliesřM
n“N|fpxnq´ fpynq|ă 1. But by the convergence and divergence of the above series, we can pick an N
such that ř8
n“N|xn´yn|ă δ and then we can pick an M such that řM
n“N|fpxnq´ fpynq|ą 1, which is a
contradiction. Thus f is not absolutely continuous on r0, 1s.
Problem 12(b). Show that if f is of bounded variation on r0, 1s, then f is absolutely continuous on
r0, 1s.
Solution. Let TVra,bs denote the total variation of f on the interval ra,bs. Since f is continuous and
of bounded variation on r0, 1s, we can show that TVr0,xs is a continuous function of x. Fix ϵą 0. Since f is
of bounded variation, pick a partition t0“t0ăt1ă¨¨¨ă tn“ 1u such that
nÿ
j“1
|fptjq´ fptj´1q| ą TVr0,1s´ϵ.
Since f is continuous, we can pick an hPp 0,t 1q such that |fphq´ fp0q|ă ϵ. By adding h into the original
partition, the variation can only increase. Furthermore, th,t 1,...,t nu is a partition of rh, 1s, so we get
ϵ`TVrh,1s ą |fphq´ fp0q|`| fpt1q´ fphq|`
nÿ
j“2
|fptjq´ fptj´1q| ą TVr0,1s´ϵ,
which implies TVr0,hs“TVr0,1s´TVrh,1să 2ϵ. Since TVr0,xs is an increasing function, this shows that it
is continuous at 0.
61

Now we want to show that f is absolutely continuous on r0, 1s. Fix ϵ ą 0 and let h ą 0 be such that
TVr0,hs ă ϵ. By hypothesis, f is absolutely continuous on rh, 1s, so let δ ą 0 be as in the deﬁnition of
absolute continuity onrh, 1s. Let a1ăb1ďa2ă¨¨¨ď anăbn be such that řn
k“1bk´akăδ. By dividing
one of the intervals into two subintervals, the variation can only increase, so without loss of generality we
may assume that hRpak,bkq for anyk. Let 𝓁 be the index such that b𝓁ďhďa𝓁`1. Since ta1,b 1,...,a 𝓁,b𝓁u
is a partition of r0,hs, by the choice of h we have
𝓁ÿ
j“1
|fpbjq´ fpajq| ď TVr0,hs ă ϵ.
By absolute continuity on rh, 1s, we have
nÿ
j“𝓁`1
|fpbjq´ fpajq| ă ϵ
and hence nÿ
j“1
|fpbjq´ fpajq| ă 2ϵ,
which establishes that f is absolutely continuous on r0, 1s.
62

11 Spring 2014
Problem 1. Let pX, A,µq be a σ-ﬁnite measure space. For each t P R let et be the characteristic
function of the interval pt,8q. Prove that if f,g : X Ñ R are A-measurable, then ||f´g||L1pXq “ş
R||et˝f´et˝g||L1pXq dt.
Solution. We have
ż
R
||et˝f´et˝g||L1dt“
ż
R
ˆż
R
|et˝fpxq´ et˝gpxq|dx
˙
dt
“
ż
R
ˆż
R
|et˝fpxq´ et˝gpxq|dt
˙
dx,
where we are justiﬁed in switching the order of integration by Tonelli’s theorem since µ is σ-ﬁnite. Now
observe that|et˝fpxq´ et˝gpxq| is equal to 1 if either fpxqă tďgpxq orgpxqă tďfpxq and 0 otherwise.
Thus the inner integral evaluates to |fpxq´ gpxq|, which gives the desired result.
Problem 2. Let fPL1pR,dxq and βPp 0, 1q. Prove that
ż
R
|fpxq|
|x´a|βdxă8
for (Lebesgue) a.e. aP R.
Solution. Write Fpaq “
ş
R
|fpxq|
|x´a|βdx. We would be done if we could show that
ş
RFpaqda ă 8. Unfor-
tunately this isn’t true. However it is enough to show that
ş
RupaqFpaqda ă 8for some strictly positive
u.
We takeupaq“ minpa´2, 1q, with the convention that up0q“ 1. By Tonelli’s theorem, we write
ż
R
upaqFpaqda“
ż
R
upaq
ˆż
R
|fpxq|
|x´a|βdx
˙
da
“
ż
R
|fpxq|
ˆż
R
upaq
|a´x|βda
˙
dx.
Let I be the interval rx´ 1,x ` 1s. We bound the inner integral as follows:
ż
R
upaq
|a´x|βda“
ż
I
upaq
|a´x|βda`
ż
RzI
upaq
|a´x|βda
ď
ż
I
1
|a´x|βda`
ż
RzI
upaqda
ď
ż
I
1
|a´x|βda`
ż
R
upaqda
“
ż
r´1,1s
1
|a|βda`
ż
R
upaqda,
where we applied a linear change of variables in the last step. But β Pp 0, 1q so the ﬁrst integral is ﬁnite,
and it’s clear the second integral integral is ﬁnite. So there is a constant C, independent of x such thatş
R
upaq
|a´x|β ăC. Returning to the original integral, we have
ż
R
upaqFpaqdaď
ż
R
C|fpxq|dx“C||f||L1,
which is ﬁnite by hypothesis. It follows that Fpaqă8 for a.e. aP R.
63

Problem 3.1. Letra,bs be a ﬁnite interval and let f :ra,bsÑ R be a bounded Borel measurable function.
Prove thattxPra,bs :f is continuous at xu is Borel measurable.
Solution. Let
En :“ txPra,bs : there exists a δą 0 such that |fpaq´ fpbq|ă 1{n for any a,b Ppx´δ,x`δqu.
Note that f is continuous at x if and only if xP Ş8
n“1En. So to show the set of continuities of f is Borel
it suﬃces to show that each En is an open set. Let x P En and let δ be as in the deﬁnition of En. We
show that px´δ{2,x `δ{2qĎ En. Indeed, if |y´x|ă δ{2, then for any a,b Pp y´δ{2,y `δ{2q we have
|a´x|,|b´x|ă δ, so |fpaq´ fpbq|ă 1{n. Thus yPEn with the choice δ{2, so En is open.
Problem 3.2. Prove that f is Riemann integrable if and only if it is continuous almost everywhere.
Solution. Let I be the upper Riemann integral of f and I be the lower Riemann integral of f. We
know that we can ﬁnd a sequence of nested partitions P1 Ď P2 Ď ... of ra,bs such that the mesh size of
Pn tends to 0 as n Ñ 8and limnÑ8Upf,Pnq “I and limnÑ8Lpf,Pnq “I. Denote by Ek,n the kth
subinterval of the partition Pn and let mk,n and Mk,n be the inﬁmum and supremum respectively of f on
Ek,n. Deﬁne the functions Un and Ln by
Ln :“
ÿ
k
mk,nχEk,n
Un :“
ÿ
k
Mk,nχEk,n.
By construction we have
şb
aUn “ Upf,Pnq and
şb
aLn “ Lpf,Pnq. Also, since the partitions are nested, we
have
L1 ď L2 ď ... ď f ď ... ď U2 ď U1.
Since tUnu andtLnu are both monotone, they converge pointwise to functions U and L respectively such
that L ď f ď U. By applying the Dominated Convergence Theorem to both Ln and Un with U1 as the
dominating function, we see that
şb
aL “ I and
şb
aU “ I. Now we have that f is Riemann intergrable if
and only if I “ I, which happens if and only if
şb
aL “
şb
aU, which since L ď U happens if and only if
L“ U almost everywhere, and since Lď f ď U this happens if and only if Lpxq “fpxq “Upxq almost
everywhere. Note that the set of x which appear as a partition point of some Pn is at most countable, and
thus has measure zero and can be ignored. For other x, the statement that Lpxq“ fpxq“ Upxq is exactly
the statement thatf is continuous atx (because the mesh size of the partition tends to 0). Thus we conclude
that f is Riemann integrable if and only if f is continuous almost everywhere.
Problem 4a. Consider a sequence tanuĎr 0, 1s. For fPCpr0, 1sq, let us denote
φpfq “
8ÿ
n“1
2´nfpanq.
Prove that there is no gPL1pr0, 1sq such that φpfq“
ş
fpxqgpxqdx is true for all fPCpr0, 1sq.
Solution. Suppose there was such a g. Let fk be the function which is zero outside ra1´ 1{k,a 1` 1{ks,
equal to 1 at a1, and linear in between (the graph is a triangle of height 1 and width 2 {k centered at a1).
Then for each k we have φpfkqě 1{2. But we also have fkÑ 0 pointwise almost everywhere and |fk|ď 1,
so by the dominated convergence theorem,
ş1
0fkgÑ 0, which is a contradiction.
Problem 4b. EachgPL1pr0, 1sq deﬁnes a continuous functional Tg on L8pr0, 1sq by
Tgpfq “
ż
fpxqgpxqdx.
64

Prove that there are continuous functionals on L8pr0, 1sq that are not of this form.
Solution. Suppose not, i.e. that every element of pL8q˚ is of the form Tg for some g P L1. Then the
map g ÞÑ Tg is a normed vector space isomorphism L1 Ñ pL8q˚. Indeed, it is surjective by assumption,
injective because Tg“ 0 implies
ş1
0fg “ 0 for all fPCpr0, 1sq, which implies g“ 0, and bounded because
||Tg||op “ sup
||f||L8“1
⏐⏐⏐⏐
ż 1
0
fg
⏐⏐⏐⏐ ď
⏐⏐⏐⏐
ż 1
0
g
⏐⏐⏐⏐ ď ||g||L1.
Thus by the open mapping theorem, it’s inverse is also bounded and therefore it’s an isomorphism. Thus
L1»pL8q˚. Since L1 is separable, this implies pL8q˚ is separable, which implies L8 is separable. But this
is a contradiction: tχr0,rsu0ără1 is an uncountable discrete set in L8.
Alternate Solution (using part a). Note that φ is a bounded linear functional on the space Cpr0, 1sq, so
by Hahn-Banach φ extends to a bounded linear functional rφ on L8pr0, 1sq. If rφ was of the form Tg then its
restriction φ would also be of this form, which contradicts part (a).
Problem 5a. Prove that 𝓁1pNq and 𝓁2pNq are separable Banach spaces but 𝓁8pNq is not.
Solution. Let X be either 𝓁1pNq or 𝓁2pNq (the proof that follows works for both). Deﬁne the set
Sn :“ tfPX :fpkqP Q`iQ for all k and fpkq“ 0 for kąnu
and let S “ Ť8
n“1Sn. Note that each Sn can be identiﬁed with pQ`iQqn, which is countable, so S is
countable as well. We now show that S is dense in X. Let f P X and ﬁx ϵ ą 0. Let e be either 1 or 2
depending on if X is 𝓁1pNq or 𝓁2pNq. Since ř8
k“1|fpkq|eă8 , there is an N such that ř8
k“N`1|fpkq|eăϵ.
For eachkďN, since Q`iQ is dense in C, pick qkP Q`iQ such that|qk´fpkq|ăp ϵ{Nq1{e. Now deﬁne
g bygpkq“ qk for kďN and gpkq“ 0 for kąN. Then we see that gPSN ĎS and
||f´g||X “
8ÿ
k“1
|fpkq´ gpkq|e “
Nÿ
k“1
|fpkq´ qk|e`
8ÿ
k“N`1
|fpkq|e ă ϵ`ϵ “ 2ϵ.
ThusS is dense in X, so X is separable.
For 𝓁8pNq, for any subset A Ď N, deﬁne fA P 𝓁8pNq by fApkq “ 1 if k P A and 0 otherwise. Note
that for any two subsets A and B, if A‰B then||fA´fB||𝓁8 “ 1. But since there are uncountably many
subsets of N, the collection tfAuAĎN is an uncountable discrete subset of 𝓁8pNq, which means 𝓁8pNq can’t
be separable.
Problem 5b. Prove that there exists no bounded linear surjective map T :𝓁2pNqÑ 𝓁1pNq.
Solution. If such a map existed then it would induce a bounded injective map T˚ :l8pNqÑ l2pNq between
the dual spaces. Taking duals again, we obtain a surjective bounded linear map T˚˚ : l2pNqÑp l8pNqq˚.
But the image of a separable space under a bounded linear map is separable, so pl8pNqq˚ must be separable.
But then l8pNq is separable, which is a contradiction.
Problem 6a. Given a Hilbert space H, let tanu be a sequence with ||an|| “ 1 for all n. Recall that
the closed convex hull of tanu is the closure of the set of all convex combinations of elements in tanu. Show
that if tanu spans H linearly, then H is ﬁnite dimensional.
Solution. Suppose tanu linearly spans H and suppose that H is inﬁnite-dimensional. By inductively
removing any elements an which are in the span of ta1,...,a n´1u, we may assume that tanu is a linearly
independent set in H. Deﬁne SN :“ spanpa1,...,a Nq. We know that SN is a ﬁnite-dimensional subspace of
H and is therefore closed. We also know that SN does not contain any open sets because if SN contained the
65

open ball Bpx,rq, then since S is a subspace it would also contain the set Bpx,rq´ x“Bp0,rq, and then it
would also have to contain the set n¨Bp0,rq“ Bp0,nrq for all integers n, implying that SN would be equal
to all of H. But since H is inﬁnite dimensional this is not the case. Hence SN has empty interior and since
SN is closed, SN is nowhere dense. By the assumption that tanu spans H, we see that H“ Ť8
N“1SN. But
this is a countable union of nowhere dense sets, and since Hilbert spaces are complete, this contradicts the
Baire category theorem. Thus H must be ﬁnite dimensional.
Problem 6b. Show that if xan,ξyÑ 0 for all ξP H, then 0 is in the closed convex hull of tanu.
Solution. Fix ϵ ą 0. It suﬃces to show the existence of a convex combination of the an with norm
less than ϵ. Set aN1 “ a1. Since xan,aN1y Ñ0 as nÑ 8, pick aN2 so that |xaN2,aN1y|ă ϵ. Now since
xan,aN1y and xan,aN2y both tend to 0 as nÑ 8, we can pick aN3 so that |xaN3,aN1y|, |xaN3,aN2y|ă ϵ.
Continuing this construction inductively we get a subsequence aNk with the property that every pairwise
inner product in the subsequence has absolute value less than ϵ. Now let r be big enough so that 1 {ră ϵ
and consider the convex combination p1{rqaN1`... `p 1{rqaNr. We have
ˇˇˇˇ
ˇˇˇˇ
1
raN1`... ` 1
raNr
ˇˇˇˇ
ˇˇˇˇ
2
“ 1
r2xaN1`...a Nr,aN1`...a Nry
“ 1
r2
˜ rÿ
j“1
ˇˇˇˇaNj
ˇˇˇˇ2
`
ÿ
i‰j
@
aNi,aNj
D
¸
ă 1
r2
`
r`r2ϵ
˘
ă 3
2ϵ.
Problem 7. Characterize all entire functions f with|fpzq|ą 0 for z large and
lim sup
zÑ8
|log |fpzq||
|z| ă 8.
Solution. The condition that |fpzq|ą 0 for |z| large implies that all of the zeros of f lie in some bounded
set, and since the zeros have to be discrete, f has only ﬁnitely many zeros. Let ppzq be the polynomial with
the same zeros as f, counting multiplicity. Then fpzq{ppzq is a nonvanishing entire function, so we can write
fpzq{ppzq“ ehpzq for some entire function h. So we have the representation fpzq“ ppzqehpzq where p is a
polynomial and h is entire. We have
lim sup
zÑ8
|log |fpzq||
|z| “ lim sup
zÑ8
|log|ppzq||
|z| `| log| Rephpzqq||
|z| “ lim sup
zÑ8
| log| Rephpzqq||
|z| ă 8.
Thus we have | Rephpzqq|ď C|z| for some constant C and all z. We claim this implies that h is a degree 1
polynomial. It would be obvious if the bound had |hpzq| instead of| Rephpzqq|, but it doesn’t, so we have to
do more work. Write h“u`iv and also write
hpzq“ hpreiθq“
8ÿ
n“0
anrneinθ.
Then we haveupreiθq“ ř8
n“0rnpRepanq cospnθq´ Impanq sinpnθqq. Using various orthonormality properties
and the fact the the power series converges uniformly on compact sets, one can compute
ż 2π
0
upreiθqe´ikθdθ “ πrkak
for each ﬁxed k. Thus
|ak|rk ď 1
π
ż 2π
0
|upreiθq|dθ.
66

Combining this with the mean value property for u, we have
|ak|rk` 2up0q ď 1
π
ż 2π
0
p|upreiθq|` upreiθqqdθ ď 1
π¨ 2π¨ 2Cr “ 4Cr
by the estimate on | Rephq| from above. Thus we have |ak|ď 4Cr1´k´ 2up0qr´k. This holds for any r, so
we can take rÑ8 to conclude that ak“ 0 for any ką 1. This implies that h is a degree 1 polynomial.
So we conclude that if f satisﬁes the given conditions, then fpzq“ ppzqeaz`b for some polynomial p and
a,b P C. It’s clear that every function of this form satisﬁes the conditions, so this is a complete characteri-
zation.
Problem 8. Construct a non-constant entire function fpzq such that the zeros of f are simple and co-
incide with the set of all (positive) natural numbers.
Solution. Use the canonical product representation. Let
fpzq “
8ź
n“1
´
1´ z
n
¯
ez{n.
This clearly has the right zeros. We just need to show f is entire. It’s enough to show that the product
converges uniformly and absolutely on compact sets. Equivalently, we need to show that
8ÿ
n“1
|logp1´z{nq` z{n|
converges uniformly on compact sets. Examining the power series expansion of log p1´xq around 0, we see
that there exists δą 0 such that |x|ă δ implies| logp1´xq` x|ď| x|2. Fix a compact set Bp0,Rq. Pick n
big enough so that R{năδ and also so that nąR. Then for any |z|ď R, we have|z|{năδ, so
|logp1´z{nq` z{n| ď |z|2
n2 ď R2
n2.
Thus the series in question is eventually majorized by the convergent series ř8
n“1R2{n2 for all |z| ďR,
which shows that it converges uniformly and absolutely on Bp0,Rq.
Problem 9. Prove Hurwitz’ Theorem: Let Ω Ď C be a connected open set and fn,f : Ω Ñ C holo-
morphic functions. Assume that fnpzq converges uniformly to fpzq on compact subsets of Ω. Prove that if
fnpzq‰ 0 for all zP Ω and all n, then either f is identically zero or fpzq‰ 0 for all zP Ω.
Solution. Since fn Ñ f uniformly on compact sets, we also know that f1
n Ñ f1 uniformly on compact
sets. Suppose that f is not identically zero. Then the zeros of f are isolated. Fix any z0 P Ω. Choose
an rą 0 small enough so that f has no zeros in Bpz0,rq except for possibly at z0 and|fpzq|ě δ ą 0 for
|z´z0|“ r. Because BBpz0,rq is compact and each fn is nonvanishing, eachfn is bounded away from 0 on
BBpz0,rq, and since f is also bounded away from zero on it, we have 1 {fn Ñ 1{f uniformly on BBpz0,rq.
Therefore by the argument principle, we have
0 “ lim
nÑ8
p# zeros of fn inside Bpz0,rqq “ lim
nÑ8
ż
BBpz0,rq
f1
npzq
fnpzqdz “
ż
BBpz0,rq
f1pzq
fpzq dz “ p# zeros of f inside Bpz0,rqq.
Therefore fpz0q‰ 0, and since this argument can be applied at any point z0, we conclude that f is nonvan-
ishing in Ω.
Problem 10. Let αPr 0, 1szQ and let tanuP 𝓁1pNq with an‰ 0 for all n. Show that
fpzq “
ÿ
ně1
an
z´eiαn
67

converges and deﬁnes a function that is analytic in D which does not admit an analytic continuation to any
domain larger than D.
Solution. Each of the summands is analytic in D, so to show that f is analytic in D it suﬃces to show that
the sum converges uniformly on compact sets. Note that it is enough to show that sum converges uniformly
on Dr“tz :|z|ă ru ForzPDr we have
⏐⏐⏐⏐⏐
8ÿ
n“k
an
z´eiαn
⏐⏐⏐⏐⏐ď
8ÿ
n“k
|an|
|z´eiαn| ă 1
1´r
8ÿ
n“k
|an|,
which converges to 0 as kÑ8 . Thus the sequence of partial sums for f is uniformly Cauchy on Dr. This
establishes that the, sum converges everywhere in D, and deﬁnes an analytic function in D.
Let Ω be any region containingD. Then Ω contains an open arc of the unit circle. Sinceα is irrational, the
pointsteiαnu are dense in the unit circle, so there is someeiαkP Ω. The intuition is that this is a contradiction
because f will blow up near eiαk, but it’s hard to show this directly. Instead let gpzq“p z´eiαkqfpzq. Since
f is analytic in Ω by assumption, gpeiαkq“ 0. Consider for 0 ără 1
gpreiαkq “ ak`
ÿ
n‰k
anpr´ 1qeiαk
reiαk´eiαn
where changing the order of summation is allowed because the series converges absolutely on each circle
|z|“ r for ră 1. Now note that we have
⏐⏐⏐⏐
anpr´ 1qeiαk
reiαk´eiαn
⏐⏐⏐⏐ ď |an|1´r
1´r ď |an|
for all ră 1, so by the Dominated Convergence theorem we have
gpeiαkq “ lim
rÑ1´
gpreiαkq “ ak`
ÿ
n‰k
lim
rÑ1´
anpr´ 1qeiαk
reiαk´eiαn “ ak ‰ 0,
which is a contradiction.
Problem 11. For eachpPp´ 1, 1q, compute the improper Riemann integral
ż8
0
xp
x2` 1dx.
Solution. Deﬁne logpzq to be the branch with the negative imaginary axis removed, i.e. Im plogpreiθqq“
θPp´π{2, 3π{2q. Then deﬁne
fpzq :“ zp
z2` 1 “ exppp logzq
z2` 1 .
Integratef over the contour which consists of a half circle in the upper half plane from ´R toR, then along
the negative real axis from ´R to´ϵ, then a half circle in the upper half plane from ´ϵ toϵ, then along the
positive real axis from ϵ toR. The contributions from the two half circles go to 0 as ϵÑ 0,RÑ8 and you
are left with
p1` expppπiqq
ż8
0
xp
x2` 1dx “ 2πi¨ Resz“ifpzq “ π¨ expppπi{2q
(I left out the computation of the residue). After rearranging you get that the answer is π
2 cosppπ{2q.
Problem 12. Compute the number of zeros, including multiplicity, of fpzq “z6`iz4` 1 in the up-
per half plane.
Solution. Since the polynomial is even,z is a root of multiplicitym if and only if´z is a root of multiplicity
m. Therefore the roots in the open upper half plane are in bijection with the roots in the open lower half
plane. If r‰ 0 is real, then Impfprqq“ r4 which is nonzero. Since fp0q‰ 0 we see that f has no real roots.
Since z has 6 total roots (counting multiplicity), exactly 3 of them must lie in the upper half plane.
68

12 Fall 2014
Problem 1. Show that
A :“ tfPL3pRq :
ż
R
|fpxq|2dxă8u
is a Borel subset of L3pRq.
Solution. Deﬁne the functional φn on L3pRq by
φnpfq “
żn
´n
|f|2.
Note that we have
A “
8ď
m“1
8č
n“1
tfPL3pRq :φnpfqď mu.
So to show A is Borel it suﬃces to prove that φn is a continuous function from L3pRqÑ R. For f,g PL3,
we have
|φnpfq´ φnpgq| ď
żn
´n
⏐⏐f2´g2⏐⏐ ď
żn
´n
|f´g|p|f |` |g|q
ď
żn
´n
|f´g||f|`
żn
´n
|f´g||g|
ď
ˆżn
´n
|f´g|3
˙1{3ˆżn
´n
|f |3
˙1{3ˆżn
´n
13
˙1{3
`
ˆżn
´n
|f´g|3
˙1{3ˆżn
´n
|g|3
˙1{3ˆżn
´n
13
˙1{3
ďp 2nq1{3||f´g||L3p||f||L3`||g||L3q.
Fix ϵą 0. If ||f´g||L3ăϵ¨p 3p2nq1{3||f||L3q´1 and||f´g||L3ă||f||L3, then
|φnpfq´ φnpgq| ă p2nq1{3p3||f||L3q||f´g||L3 ă ϵ.
Thusφnpfq is continuous at f for every fPL3pRq, so we’re done.
Problem 2. Construct an f P L1pRq so that fpx`yq does not converge almost everywhere to fpxq as
yÑ 0. Prove that your f has this property.
Solution. Let K be a fat Cantor set contained in r0, 1s. Recall that K is closed, has positive measure,
and that each point in K is a boundary point. Take f “χK. Since K is closed, f is measurable, and since
K has ﬁnite measure, f lies in L1. But for each xPK every neighborhood U of x contains a point u which
lies outside K and hence has fpuq “0. Therefore for each xP K, fpx`yq does not converge to fpxq as
yÑ 0. This is enough, since K has positive measure.
Problem 3. Let pfnq be a bounded sequence in L2pRq and suppose that fn Ñ 0 Lebesgue almost ev-
erywhere. Show that fnÑ 0 in the weak topology on L2pRq.
Solution. To show that fn Ñ 0 in the weak topology on L2pRq, we need to show that φpfnq Ñ0 for
every bounded linear functional φ on L2pRq. Since L2pRq is a Hilbert space, by the Riesz representation
theorem we know that every bounded linear functional φ is of the form φpfq “
ş
fpxqgpxqdx for some
g P L2pRq. So it suﬃces to show that for any g P L2pRq, we have
ş
fnpxqgpxqdx Ñ 0 as n Ñ 8. Since
fn Ñ 0 pointwise almost everywhere, we also have that fng Ñ 0 pointwise almost everywhere. By the
Vitali Convergence Theorem, to conclude that
ş
fngÑ 0, it suﬃces to show that the sequence tfngu is both
uniformly integrable and tight.
As a reminder, uniformly integrable means that for every ϵą 0 there exists a δ ą 0 such that for any n,
mpAqă δ implies
ş
A|fng|ă ϵ. Tight means that for any ϵą 0, there exists a subset EĎ R such that for
69

anyn,
ş
Ec|fng|ă ϵ.
We know that tfnu is a bounded sequence in L2pRq, so let ||fn||L2 ď M for all n. First we show uni-
form integrability. Fix ϵą 0. Since |g|2 is integrable, there is a δ so that mpAqă δ implies
ş
A|g|2ăϵ{M.
Now for any n, we have by Cauchy-Schwarz that if mpAqă δ,
ż
A
|fng| ď
ˆż
A
|fn|2
˙1{2ˆż
A
|g|2
˙1{2
ď ||fn||L2
ϵ
M ď ϵ,
so the family tfngu is uniformly integrable.
For tightness, ﬁx ϵ ą 0. Since |g|2 is integrable, there is a set E such that
ş
Ec|g|2 ă ϵ{M. Then for
anyn, by the same Cauchy-Schwarz argument we have
ż
A
|fng| ď ϵ.
Thustfngu is tight, so we conclude that
ş
fngÑ 0 as nÑ8 .
Problem 4. GivenfPL2pr0,πsq, we say that fP G if f admits a representation of the form
fpxq “
8ÿ
n“0
cn cospnxq with
8ÿ
n“0
p1`n2q|cn|2 ă 8.
Show that if fP G and gP G then fg P G.
Solution. The motivation for this is that the cn are basically the Fourier coeﬃcients of f, so the con-
dition for membership in G translates as p1`n2q1{2pfpnqP 𝓁2. So G is basically a “Fourier series version” of
the Sobolev space H1.
First we want to make a technical modiﬁcation so that we can work directly with the regular Fourier
coeﬃcients (it makes stuﬀ easier later). It’s clear that L2pr0,πsq is in bijection with the space L2
e :“ the
subspace of L2pr´π,πsq consisting of even functions. So we identify each f P G with its even extension to
r´π,πs. For fP G, the given condition implies that
8ÿ
n“0
|cn| “
8ÿ
n“0
|cn|p1`n2q1{2p1`n2q´1{2 ď
˜ 8ÿ
n“0
|cn|2p1`n2q
¸1{2˜ 8ÿ
n“0
p1`n2q´1
¸1{2
ă 8.
Thus by the Weierstrass M-test, we know that the given series representation for f converges absolutely and
uniformly onr´π,πs. Recall that tcospnxqu8
n“0 is an orthonormal basis for the Hilbert space L2
e. For a ﬁxed
n, we calculate in two diﬀerent ways the inner product
xf, cospnxqy “
B
f, 1
2peinx`e´inxq
F
“ 1
2ppfpnq` pfp´nqq “ pfpnq because f is even
xf, cospnxqy “ 1
2π
żπ
´π
fpxq cospnxqdx “ 1
2π
żπ
´π
8ÿ
m“1
cm cospmxq cospnxqdx
“
8ÿ
m“1
cm
1
2π
żπ
´π
cospmxq cospnxqdx “
#
1
2cn n‰ 0
c0 n“ 0
where switching the order is justiﬁed because of the uniform convergence. Thus we conclude that for fP G,
the coeﬃcients cn are exactly equal to 2 pfpnq for n‰ 0 and pfp0q for n“ 0. So the problem is equivalent to
showing that for f,g P G, we havep1`n2q1{2xfgpnqP 𝓁2.
70

Let f,g P G. The same argument from above that showed the uniform convergence of the series repre-
sentations also shows that the representations f or gpxq“ ř8
n“´8
{f or gpnqeinx converge uniformly, so we
can compute the Fourier coeﬃcients
xfgpnq “ 1
2π
żπ
´π
fpxqgpxqe´inxdx “ 1
2π
żπ
´π
8ÿ
k“´8
pfpkqeikx
8ÿ
𝓁“´8
pgp𝓁qei𝓁xe´inxdx
“
8ÿ
k,𝓁“´8
pfpkqpgp𝓁q 1
2π
żπ
´π
eipk`𝓁´nqxdx “
8ÿ
k“´8
pfpkqpgpn´kq “ ppf˚pgqpnq.
Also note the elementary estimate
p1`n2q1{2 “ p1`pn´k`kq2q1{2 “ p1`pn´kq2`k2` 2pn´kqkq1{2 ď p1` 2pn´kq2` 2k2q1{2
ď p2` 2pn´kq2` 2` 2k2q1{2 À p1`pn´kq2q1{2`p 1`k2q1{2,
valid for any kP R. So we estimate
p1`n2q1{2xfgpnq À
8ÿ
k“´8
p1`k2q1{2pfpkqpgpn´kq`
8ÿ
k“´8
p1`pn´kq2q1{2pgpn´kqpfpkq
“ pp1`k2q1{2pfpkq˚ pgqpnq`pp 1`k2q1{2pgpkq˚ pfqpnq.
Thus we have
ˇˇˇ
ˇˇˇp1`n2q1{2xfgpnq
ˇˇˇ
ˇˇˇ
𝓁2
À
ˇˇˇ
ˇˇˇp1`k2q1{2pfpkq˚ pg
ˇˇˇ
ˇˇˇ
𝓁2
`
ˇˇˇ
ˇˇˇp1`k2q1{2pgpkq˚ pf
ˇˇˇ
ˇˇˇ
𝓁2
ď
ˇˇˇ
ˇˇˇp1`k2q1{2pfpkq
ˇˇˇ
ˇˇˇ
𝓁2
||pg||𝓁1`
ˇˇˇ
ˇˇˇp1`k2q1{2pgpkq
ˇˇˇ
ˇˇˇ
𝓁2
ˇˇˇ
ˇˇˇpf
ˇˇˇ
ˇˇˇ
𝓁1
by Young’s convolution inequality
ă 8
because we showed at the very beginning that f P G implies pf P 𝓁1. Thus p1`n2q1{2xfgpnq P𝓁2 so we’re
done.
Problem 5. Let φ : r0, 1s Ñ r0, 1s be continuous and let dµ be a Borel probability measure on r0, 1s.
Suppose µpφ´1pEqq“ 0 for every Borel set EĎr 0, 1s withµpEq“ 0. Show that there is a Borel measurable
function w :r0, 1sÑr 0,8q so that
ż
f˝φpxqdµpxq “
ż
fpyqwpyqdµpyq
for all continuous f :r0, 1sÑ R.
Solution. Since φ is continuous, it is Borel measurable. The condition that µpφ´1pEqq “ 0 whenever
µpEq“ 0 says that the measure φ˚µ is absolutely continuous with respect to µ. Both µ and φ˚µ are ﬁnite
measures on r0, 1s, so by the Radon-Nikodym theorem there is a Borel measurable function w such that
pφ˚µqpAq “
ż
A
wpxqdµpxq
for all Borel sets A. Since φ˚µ is a positive measure, we know that w is a nonnegative function. Also, if f
is any continuous function on r0, 1s, then it is also integrable on r0, 1s, so by a well-known property of the
Radon-Nikodym derivative,
ż 1
0
fpφpxqqdµpxq “
ż 1
0
fpxqdpφ˚µqpxq “
ż 1
0
fpxqwpxqdµpxq.
71

Problem 6. Let X be a Banach space and let X˚ be its dual space. Suppose X˚ is separable; show
that X is separable (you should assume the Axiom of Choice).
Solution. Let tfnu8
n“1 be a countable dense subset of X˚. By deﬁnition of operator norm, for each n
pickxnPX with||xn||“ 1 such that|fnpxnq|ąp 1{2q||fn||. Let M“ spantxnu. We ﬁrst want to show that
M is dense in X, i.e. M “ X. Suppose that yR M. Then by the Hahn-Banach theorem, there is a linear
functional f P X˚ such that f “ 0 on M and fpyq‰ 0. By the separability of X˚, there is a subsequence
tfnku that converges to f in the operator norm topology. We have
||fnk´f|| ě |fnkpxnkq´ fpxnkq| “ |fnkpxnkq| ą 1
2||fnk||,
and since ||fnk´f|| Ñ0 as k Ñ 8, this implies that ||fnk|| Ñ0 as k Ñ 8as well, which implies that
fnkÑ 0. But fnkÑf, and f is not identically zero, so this is a contradiction. Thus M“X, so M is dense
in X.
Now to show X is separable, it suﬃces to ﬁnd a countable set which is dense in M. Let S be the sub-
set of M which consists only of linear combinations with coeﬃcients in Q`iQ. S is a countable set because
it can be put in bijection with Ť8
n“1pQ`iQqn, which is countable. Since Q`iQ is dense in C, it follows
that S is dense in M, so S is dense in X and hence X is separable.
Problem 7. Find an explicit conformal mapping from the upper half plane slit along the vertical seg-
ment
tzP C : Impzqą 0uzp0, 0`ihs, h ą 0
to the unit disk.
Solution. Start with Ω 1 “t z P C : Impzqą 0uzp0, 0`ihs. Let f1pzq“ iph{zq. This is a conformal map
ΩÑ Ω2 :“tz : Repzqą 0uzr1,8q. Let f2pzq“ z2. This is a conformal map Ω 1Ñ Ω2 :“ Czr1,8qzp´8, 0s.
Let f3pzq “1{z´ 1. This is a conformal map Ω 2 Ñ Ω3 :“ Czp´8, 0s. Let f4pzq be the branch of ?z
that you get by removing the negative real axis. Then this is a conformal map Ω 3 Ñ H. Finally let
f5pzq“p z´iq{pz`iq; this is a conformal map HÑ D. Thus f :“f5˝f4˝f3˝f2˝f1 is a conformal map
ΩÑ D.
Problem 8. Let f : CÑ C be an entire function. Show that
|fpzq| ď Cea|z|
for some constants C and a if and only if we have
|fpnqp0q| ď Mn`1
for some constant M.
Solution. First suppose that |fpzq| ďCea|z| for all z P C. Then by applying the Cauchy estimates to
a disk of radius R centered at 0, we get
|fpnqp0q| ď n!
RnCeaR.
Since f is entire, the above inequality is valid for any Rą 0, so we choose R“n{a to get
|fpnqp0q| ď n!an
nn Cen ď C¨peaqn ď Mn`1
for some constant M.
Conversely, suppose that|fpnqp0q|ď Mn`1 for alln. Then, since f is entire, we can writef as a power series
fpzq “
8ÿ
n“0
anzn
72

and it is valid for all zP C. We know that the power series coeﬃcients are given by
an “ fpnqp0q
n! ,
so we have
|fpzq| ď
8ÿ
n“0
|an||z|n ď
8ÿ
n“0
Mn`1
n! |z|n “ MeM|z|
for all zP C.
Problem 9. Let Ω Ď C be open and connected. Suppose pfnq is a sequence of injective holomorphic
functions deﬁned on Ω such that fnÑ f locally uniformly in Ω. Show that if f is not constant, then f is
also injective in Ω.
Solution. Since fn Ñ f locally uniformly, we know that f is also holomorphic. We ﬁrst prove the fol-
lowing variation of Hurwitz’s theorem: If each fn has at most one zero in Ω, then either f is identically zero
or f has at most one zero in Ω.
Suppose that f is not identically zero. Then the zeros of f are isolated. Suppose that fpz0q “0. Pick
r ą 0 small enough so that f has no other zeros in Bpz0,rq. Since f is nonzero on BBpz0,rq, which is
compact, we have |fpzq|ě δą 0 for |z´z0|“ r. This shows that 1 {fnÑ 1{f uniformly on BBpz0,rq. We
also know that f1
nÑf1 uniformly on compact sets. Thus we conclude that
lim
nÑ8
ż
BBpz0,rq
f1
npzq
fnpzqdz “
ż
BBpz0,rq
f1pzq
fpzq dz.
By the argument principle, the right side of this equation is equal to the number of zeros of f insideBpz0,rq,
which is one. Similarly, the left side is equal to the number of zeros of fn inside Bpz0,rq. Thus the above
equation implies that for suﬃciently large n,fn has exactly one zero inside Bpz0,rq. So we have shown that
given a zero of f and a suﬃciently small ball around that zero, then n can be made suﬃciently large so that
fn has zero inside that ball. Thus, if f had two zeros, we could put two disjoint balls around them, then the
previous statement would imply that fn would eventually have to have two zeros, which is a contradiction.
Thus we conclude that f has only one zero.
Now, for any w P C, we have that fn´w converges locally uniformly to f ´w. Since each fn is injec-
tive,fn´w has at most one zero in Ω. Thus f´w is either identically zero or has at most one zero. Since
this is true for every wP C, it implies that f is either constant or injective.
Problem 10. Let us introduce a vector space B as follows.
B “
$
&
%u : CÑ C :u is holomorphic and
ĳ
C
|upx`iyq|2e´px2`y2qdxdy ă8
,
.
-.
Show that B becomes a complete vector space when equipped with the norm
||u||2 “
ĳ
C
|upx`iyq|2e´px2`y2qdxdy.
Solution. Deﬁne a measure µ on C bydµ“e´px2`y2qdxdy , i.e.
µpAq :“
ż
A
e´px2`y2qdxdy.
73

Note thatµ is a ﬁnite measure on C, andL2pµq is a complete vector space. Thus B is simply the subspace of
L2pµq consisting of holomorphic functions, so to show that B is complete it suﬃces to show that B is closed
with respect to the L2pµq norm.
Let tfnu be a sequence in B converging to f P L2pµq. We need to show that f is holomorphic. To do
that, it suﬃces to show that fn Ñ f uniformly on compact subsets of C. Let K Ď C be compact. Then
K1 :“ tz P C : distpz,Kq ď1u is also compact, so in particular, we have e´px2`y2q ě c ą 0 on K1 and
λpK1q ă 8where λ denotes Lebesgue measure on C. For any z P K, we use the mean value property of
holomorphic functions to write
fnpzq´ fmpzq “ 1
π
ż
Bpz,1q
pfnpwq´ fmpwqqdλpwq,
thus we have by Cauchy-Schwarz
|fnpzq´ fmpzq| ď 1
π
ż
Bpz,1q
|fnpwq´ fmpwq|dλpwq
ď 1
πλpBpz, 1qq1{2
˜ż
Bpz,1q
|fnpwq´ fmpwq|2dλpwq
¸1{2
ď 1
πλpK1q1{2
˜
1
c
ż
Bpz,1q
|fnpwq´ fmpwq|2cdλpwq
¸1{2
ď MK
˜ż
Bpz,1q
|fnpwq´ fmpwq|2e´px2`y2qdλpwq
¸
ď MK||fn´fm||L2pµq.
Sincetfnu converges in theL2pµq norm, the above inequality implies that||fn´fm||L8pKqÑ 0 asn,m Ñ8 ,
meaning thattfnu is uniformly Cauchy onK. Since L8 is complete, this means that fn converges uniformly
on K to some function g. In particular, fn converges pointwise to g on K. But we know that fn converges
to f in L2pµq, and thus (by passing to a subsequence if necessary) we also know that fn converges to f
pointwise. Thus we must have f“g, so we conclude that fn converges uniformly to f onK. This holds for
any compact set KĎ C and thus we know that f must be holomorphic, so B is a closed subspace of L2pµq
and therefore complete.
Problem 11. Let Ω Ď C be open, bounded, and simply connected. Let u be harmonic in Ω and as-
sume that uě 0. Show the following: for each compact set K Ď Ω, there exists a constant CK ą 0 such
that
sup
xPK
upxq ď CK inf
xPK
upxq.
Solution. Since Ω is open, simply connected and not all of C, by the Riemann mapping theorem there
is a conformal map φ : D Ñ Ω. Then the function vpzq “upφpzqq is a harmonic function on D. Let K
be any compact subset of Ω. Then φ´1pKq is a compact subset of D, so there is some rPp 0, 1q such that
φ´1pKqĎ Bp0,rqĎ Bp0,rqĎ D. Since u is nonnegative, so is v, and thus by Harnack’s inequality, for any
zPφ´1pKq we have
1´r
1`rvp0q ď 1´|z|
1`|z|vp0q ď vpzq ď 1`|z|
1´|z|vp0q ď 1`r
1´rvp0q.
The left inequality shows that inf zPφ´1pKqvpzqě 1´r
1`rvp0q, which implies vp0qď 1`r
1´r infzPφ´1pKqvpzq. Then
by putting this into the right inequality we get
vpzq ď
ˆ1`r
1´r
˙2
inf
zPφ´1pKq
vpzq
74

for any zP φ´1pKq, so supzPφ´1pKqvpzqď
´
1`r
1´r
¯2
infzPφ´1pKqvpzq. The constant
´
1`r
1´r
¯2
depends only on
the set K, so we conclude
sup
zPφ´1pKq
upφpzqq ď CK inf
zPφ´1pKq
upφpzqq,
and since φ is a bijection this is the same as saying sup wPKupwq ď CK infwPKupwq.
Problem 12. Let Ω “ tz P C : |z| ą 1u. Suppose u : Ω Ñ R is bounded and continuous on Ω and
subharmonic on Ω. Prove the following: if upzqď 0 for all |z|“ 1 then upzqď 0 for all zP Ω.
Solution. Let vpzq “up1{zq. Then v is subharmonic on A :“ Dzt0u and bounded and continuous on
Azt0u because zÞÑ 1{z is a conformal map from AÑ Ω. Fix ϵą 0 and let fpzq“ vpzq´ ϵ log|1{z|. Since
log|z| is harmonic on A, we know that f does not have a local maximum in A. Also, since u is bounded,
v also is, and thus fpzqÑ´8 as|z|Ñ 0. So there exists an rą 0 such that fpzqď 0 for |z|ď r. Now
f is continuous on the compact set tzP C :rď| z|ď 1u, so it achieves a maximum somewhere. But since
fpzqď 0 for all |z|“ r and all |z|“ 1, if that maximum were positive then it would have to be achieved on
the interior ofA, which contradicts the maximum principle. Thus the maximum is at most zero, so fpzqď 0
for all rď|z|ď 1, and by choice of r this implies that f ď 0 on A. Thus we have vpzqď ϵ log|1{z| for all
zP A. Since ϵ is arbitrary, this means vpzq“ up1{zqď 0 for all zP A, which means that upwqď 0 for all
wP Ω.
75

13 Spring 2015
Problem 1. Let fPL1pRq. Show that
lim
nÑ8
n2
ÿ
k“´n2
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
fpxqdx
⏐⏐⏐⏐⏐ “
ż
|fpxq|dx.
Solution. Let V be the set of functions which are ﬁnite linear combinations of characteristic functions
of closed intervals. First we show that the result holds for elements of V . Let gPV and write
g “
Mÿ
j“1
αj¨χraj,bjs.
Let n be suﬃciently large so that for each ´n2 ď k ď n2, the interval rk{n,pk` 1q{ns does not intersect
more than one of the intervals raj,bjs. Then in particular, on each subinterval rk{n,pk` 1q{ns, f is either
non-negative or non-positive, depending on the sign of αj. Thus we have, for such suﬃciently large n,
n2
ÿ
k“´n2
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
fpxqdx
⏐⏐⏐⏐⏐ “
n2
ÿ
k“´n2
żpk`1q{n
k{n
|fpxq| dx “
żn
´n
|fpxq| dx,
so
lim
nÑ8
n2
ÿ
k“´n2
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
fpxqdx
⏐⏐⏐⏐⏐ “
ż
|fpxq|dx.
Thus the result holds for functions in V .
We know that V is dense in L1pRq. Let f P L1pRq and ﬁx ϵ ą 0. We need to show that when n is
suﬃciently large, we have ⏐⏐⏐⏐⏐⏐
n2
ÿ
k“´n2
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
fpxqdx
⏐⏐⏐⏐⏐´
ż
|fpxq|dx
⏐⏐⏐⏐⏐⏐
ă ϵ.
Let g be an element of V such that||f´g||L1ăϵ{3. We have the estimate
⏐⏐⏐⏐⏐⏐
n2
ÿ
k“´n2
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
fpxqdx
⏐⏐⏐⏐⏐´
ż
|fpxq|dx
⏐⏐⏐⏐⏐⏐
ď
⏐⏐⏐⏐
ż
|fpxq|dx´
ż
|gpxq|dx
⏐⏐⏐⏐`
⏐⏐⏐⏐⏐⏐
n2
ÿ
k“´n2
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
gpxqdx
⏐⏐⏐⏐⏐´
ż
|gpxq|dx
⏐⏐⏐⏐⏐⏐
`
⏐⏐⏐⏐⏐⏐
n2
ÿ
k“´n2
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
fpxqdx
⏐⏐⏐⏐⏐´
n2
ÿ
k“´n2
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
gpxqdx
⏐⏐⏐⏐⏐
⏐⏐⏐⏐⏐⏐
“: I`II`III.
By choice of g, we have I ă ϵ{3. Since we have already proved the result for elements of V , let n be large
enough so that II ăϵ{3. Finally, by taking absolute values inside multiple times we have
III ď
n2
ÿ
k“´n2
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
fpxqdx´
żpk`1q{n
k{n
gpxqdx
⏐⏐⏐⏐⏐ ď
n2
ÿ
k“´n2
żpk`1q{n
k{n
|fpxq´ gpxq| dx “
żn
´n
|fpxq´ gpxq|dx
ď ||f´g||L1 ă ϵ{3.
Thus we conclude that ⏐⏐⏐⏐⏐⏐
n2
ÿ
k“´n2
⏐⏐⏐⏐⏐
żpk`1q{n
k{n
fpxqdx
⏐⏐⏐⏐⏐´
ż
|fpxq|dx
⏐⏐⏐⏐⏐⏐
ă ϵ
76

for all suﬃciently large n and thus the result holds for all fPL1pRq.
Problem 2. Let fPL2
locpRnq, gPL3
locpRnq. Assume that for all real rě 1, we have
ż
rď|x|ď2r
|fpxq|2dx ď ra,
ż
rď|x|ď2r
|gpxq|3dx ď rb.
Here a and b are such that 3a` 2b`nă 0. Show that fg PL1pRnq.
Solution. Let E0 “ tx P Rn : |x| ď 1u and for k ě 1 let Ek “ tx P Rn : 2k´1 ď |x| ď 2ku. Since
each Ek is compact for kě 0, |f|2 and|g|3 are integrable on each Ek, which also implies by compactness
that|f| and|g| are integrable on each Ek. To show that fg PL1pRnq it suﬃces to show that
8ÿ
k“1
ż
Ek
|fpxqgpxq|dx ă 8.
For eachkě 1, by H¨ older’s inequality using 1{6` 1{2` 1{3“ 1, we have
ż
Ek
|fpxqgpxq|dx ď
ˆż
Ek
16dx
˙1{6ˆż
Ek
|fpxq|2dx
˙1{2ˆż
Ek
|gpxq|3dx
˙1{3
ď pλnpEkqq1{6pp2k´1qaq1{2pp2k´1qbq1{3.
Since EkĎr´ 2k, 2ks, we have λnpEkqďp 2k`1qn. Thus we have
ż
Ek
|fpxqgpxq|dx ď p2k`1qn{6p2k´1qa{2p2k´1qb{3 “ 4n{6¨p 2k´1qn{6`a{2`b{3.
By hypothesis, n{6`a{2`b{3ă 0, so let ´δPpn{6`a{2`b{3, 0q. Then we have
8ÿ
k“1
ż
Ek
|fpxqgpxq|dx ď 4n{6
8ÿ
k“1
p2k´1q´δ “ 4n{6
8ÿ
k“1
ˆ 1
2δ
˙k´1
ă 8
because 2δą 1. Thus fg PL1pRnq.
Problem 3a. Let fPL1
locpRnq and let
Mfpxq “ sup
rą0
1
mpBpr,xqq
ż
Bpr,xq
|fpyq|dy
be the Hardy-Littlewood maximal function. Show that
mptx :Mfpxqą suq ď Cn
s
ż
|fpxq|ąs{2
|fpxq|dx, s ą 0,
where the constant Cn depends on n only. The Hardy-Littlewood maximal theorem may be used.
Solution. Suppose that BĎ Rn is a ball and that 1
mpBq
ş
B|fpyq|dyąs. Then we have
s¨mpBqă
ż
BXtx:|fpxq|ďs{2u
|fpyq|dy`
ż
BXtx:|fpxq|ąs{2u
|fpyq|dy
ď s
2¨mpBq`
ż
BXtx:|fpxq|ąs{2u
|fpyq|dy.
Deﬁne ˜fpxq to be fpxq if|fpxq|ą s{2 and 0 otherwise. It follows from the work above that
ż
B
| ˜fpyq|dyą s
2.
77

Thus if Mfpxqą s, then M ˜fpxqą s{2. Applying the Hardy-Littlewood maximal inequality to ˜f gives
mptx :Mfpxqą suqď mptx :M ˜fpxqą s{2uq
ď Cn
s
ż
| ˜fpyq|dy
“ Cn
s
ż
|fpxq|ąs{2
|fpyq|dy,
for some constant Cn.
Problem 3b. Prove that if φPC1pRq,φp0q“ 0, and φ1ą 0, then
ż
φpMfpxqqdx ď Cn
ż
|fpxq|
˜ż
0ătă2|fpxq|
φ1ptq
t dt
¸
dx.
Solution. Using part (a), we estimate the integral on the right by
Cn
ż
|fpxq|
˜ż
0ătă2|fpxq|
φ1ptq
t dt
¸
dx “ Cn
ĳ
tpx,tq:0ătă2|fpxq|u
|fpxq|φ1ptq
t dxdt by Tonelli because φ1ą 0
“ Cn
ż8
0
φ1ptq
t
ż
|fpxq|ąt{2
|fpxq|dxdt
ě
ż8
0
φ1ptq
t t¨mtx :Mfpxqą tudt “
ż8
0
φ1ptq¨ mtx :Mfpxqą tudt
“
ż8
0
φ1ptq
ż
Mfpxqąt
dxdt
“
ĳ
tpx,tq:0ătăMfpxqu
φ1ptqdxdt again by Tonelli because φ1ą 0
“
ż
xPR
żMfpxq
0
φ1ptqdtdx “
ż
pφpMfpxqq´ φp0qqdx “
ż
φpMfpxqqdx.
Problem 4. LetfPL1
locpRq be 2π-periodic. Show that the linear combinations of the translatesfpx´aq, aP
R, are dense in L1pp0, 2πqq if and only if each Fourier coeﬃcient of f is‰ 0.
Solution. For a function u P L1pr0, 2πsq, denote by ˆupnq the nth Fourier coeﬃcient of u. First sup-
pose that ˆfpnq “ 0 for some n. Then note that for any linear combination of translates of f, hpxq “
α1fpx´a1q` ... `αmfpx´amq, we have ˆhpnq“ α1e´ina1 ˆfpnq` ... `αme´inam ˆfpnq“ 0. But then the
span of the linear translates of f can’t possibly be dense in L1, because if we let gpxq“ einx, then ˆgpnq“ 1,
and since the mapuÞÑ ˆu is a continuous mappingL1Ñ𝓁8, there can’t be a sequence of linear combinations
of translates of f converging to g in L1.
Conversely, suppose that ˆfpnq ‰0 for every n. Let M be the closure (with respect to the L1 norm) of
spantfpx´aq : aP Ru and suppose that M ‰ L1. Then by the Hahn-Banach theorem, there is a nonzero
bounded linear functional φ P pL1q˚ which is zero on M. Since pL1q˚ » L8, we get that there exists a
nonzero gPL8 such that ż 2π
0
gpxqfpx´aqdx “ 0
for every a P R. If we consider the above integral as a function of a, call it hpaq, then h is identically
zero, so in particular it is 2 π-periodic, so we can look at its Fourier coeﬃcients. A standard computation
78

shows that ˆhpnq “ˆgpnq ˆfpnq for all n, and since h is identically zero, ˆhpnq “0 for all n. Since ˆfpnq ‰0
for alln, this implies that ˆgpnq“ 0 for alln, but this contradicts the fact thatg is nonzero, so we’re done.
Problem 5. Let uPL2pRq and let us set
Upx,ξq “
ż
e´px`iξ´yq2{2upyqdy, x,ξ P R.
Show that Upx,ξq is well-deﬁned on R2 and that there exists a constant Cą 0 such that for all uPL2pRq,
we have ĳ
|Upx,ξq|2e´ξ2
dxdξ “ C
ż
|upyq|2dy.
Determine C explicitly.
Solution. To show that Upx,ξq is well-deﬁned, note that by Cauchy-Schwarz
ż ⏐⏐⏐e´px`iξ´yq2{2upyq
⏐⏐⏐ dy ď
ˆż
e´px`iξ´yq2
dy
˙1{2ˆż
|upyq|2dy
˙1{2
ă 8.
Now we expand
Upx,ξq “ e´x2{2eξ2{2e´ixξ
ż
exy´y2{2upyqeiξydy.
For a ﬁxed x, let
fxpyq “ upyqexy´y2{2.
Then we see that
ˆfxpξq “
ż
exy´y2{2upyqe´2πiξydy,
so
Upx,ξq “ e´x2{2eξ2{2e´ixξ ˆfxp´ξ{p2πqq.
Therefore, by Plancherel and Tonelli since everything is non-negative, we have
ĳ
|Upxξq|2e´ξ2
dxdξ “
ĳ
e´x2
| ˆfxp´ξ{p2πqq|2dxdξ “ 2π
ż
e´x2
ż ⏐⏐⏐ ˆfxpξq
⏐⏐⏐
2
dξdx
“ 2π
ż
e´x2
ż
|fxpyq|2dydx “ 2π
ĳ
e´x2`2xy´y2
|upyq|2dydx
“ 2π
ż
|upyq|2
ˆż
e´px´yq2
dx
˙
dy “ 2π3{2
ż
|upyq|2dy.
Problem 6. When B1 and B2 are Banach spaces, we say a linear operator T : B1 Ñ B2 is compact
if for any bounded sequence pxnq in B1, the sequence pTxnq has a convergent subsequence. Show that if T
is compact then ImpTq has a dense countable subset.
Solution. Since T is a compact operator, we know that for any bounded set A Ď B1, TpAq is a rela-
tively compact subset of B2. Let An “t xP B1 :||x||B1 ď nu. Then we can write B1 “ Ť8
n“1An, so we
have ImpTq“ Ť8
n“1TpAnq. Since each An is a bounded set, each TpAnq is relatively compact. This means
thatTpAnq is compact. Since compact sets are separable (this follows from the totally bounded deﬁnition of
compactness), it follows that TpAnq has a countable dense subset. We need to upgrade this to a countable
dense subset of TpAnq. Let E be a countable dense subset of TpAnq. Start with rE :“EXTpAnq. For any
xP EzTpAnq, there is a sequence txkuP TpAnq converging to x. Add the sequence txku to rE. Repeating
this process for every xPEzTpAnq, we see that rE is at most a countable union of countable sequences and
is thus countable, and it’s clear that it is dense in TpAnq. Thus TpAnq also has a countable dense subset for
eachn. Thus by taking the (countable) union of these dense subsets, we see that Im pTq“ Ť8
n“1TpAnq has
79

a countable dense subset.
Problem 7. Suppose fn : D Ñ H is a sequence of holomorphic functions and fnp0q Ñ 0 as n Ñ 8.
Show that fnpzqÑ 0 uniformly on compact subsets of D.
Solution. Any compact subset of D is contained in Bp0,rq for some 0 ă r ă 1, so it suﬃces to show
that fnÑ 0 uniformly on Bp0,rq for each 0 ă ră 1. Fix such an r. Note that since each fn takes values
only in H, we can deﬁne a single-valued analytic branch of gnpzq :“
a
fnpzq on D. Each gn is a holomorphic
function from D to Ω :“ tz P C : Repzq, Impzq ą1u and it is still true that gnp0q Ñ0 as n Ñ 8. Let
un“ Repgnq andvn“ Impgnq. We also have unp0q,vnp0qÑ 0 as nÑ8 . Since gn is holomorphic and takes
values in Ω, un and vn are both positive harmonic functions on D. Thus for any zPBp0,rq, we can apply
Harnack’s inequality to get
|unpzq| ď 1`|z|
1´|z||unp0q| ď 1`r
1´r|unp0q|,
which shows that un Ñ 0 uniformly on Bp0,rq. The same argument holds for vn. Thus since Re pgnq and
Impgnq both converge uniformly to 0 on Bp0,rq, gn also does. Finally, since |fnpzq| “ |gnpzq|2, this also
shows that fnÑ 0 uniformly on Bp0,rq, so we are done.
Alternate solution. Let gn “ fn´i
fn`i. The relation fn “ p´iqpgn`1q
gn´1 shows that it suﬃces to show that
the gn converge locally uniformly to ´1. Note the gn are holomorphic maps DÑ D. Let ψ´1
n be an au-
tomorphism of D which takes gnp0q to 0 and let hn “ ψ´1
n ˝gn. Then hn is holomorphic with hnp0q“ 0.
Write gn “ ψn˝hn. We want to show that gn converges locally uniformly to ´1. Fix a compact set
K :“Bp0,rqĎ D. By the Schwarz lemma, hnpKqĎ K. So to show gnÑ´ 1 uniformly on K, it’s enough
to show ψnÑ´ 1 uniformly on K. This is just a calculation: for any |z|ď r, we have
|ψnpzq´ gnp0q| “
⏐⏐⏐⏐⏐
z`gnp0q
1`gnp0qz
´gnp0q
⏐⏐⏐⏐⏐ “ |z|⏐⏐⏐1`gnp0qz
⏐⏐⏐
p1´|gnp0q|2q ď 2r
1´rp1´|gnp0q|2q
for suﬃciently large n (where “suﬃciently large” here only depends on the convergence of gnp0q to´1, so
this is uniform in |z| ďr). Since gnp0q Ñ ´1 by hypothesis (because fnp0q Ñ0), this shows ψn Ñ ´1
uniformly on K, so we’re done.
Problem 8. Let f : CÑ C be holomorphic and suppose
sup
xPR
t|fpxq|2`|fpixq|2uă8 and|fpzq|ď e|z| for all zP C.
Deduce that f is constant.
Solution. By Liouville’s theorem, to show f is constant it is enough to show that f is bounded. The
ﬁrst given condition implies that there is some Mă8 such that|fpzq|ď M for all z with either Repzq“ 0
or Impzq“ 0. First we show that f is bounded in the ﬁrst quadrant A :“tz : Repzqą 0, Impzqą 0u.
We use the Phragmen-Lindel¨ of method. Fixϵą 0, and deﬁne
gpzq “ fpzq¨ expp´ϵpe´iπ{4zq3{2q
where w ÞÑ w3{2 is deﬁned by removing the branch cut along the negative real axis, so that preiθq3{2 “
r3{2ei3θ{2. We wish to show that |gpzq|Ñ 0 as |z|Ñ8 in A. Writing z“reiθ, we have
|gpzq| “ |fpzq| exppRep´ϵpe´iπ{4zq3{2qq ď expprq expp´ϵr3{2 Repe´i3π{8ei3θ{2qq
ď expprq expp´ϵr3{2 cosp3θ{2´ 3π{8qq.
OnA, sinceθPp 0,π{2q, we have 3θ{2´3π{8Pp´ 3π{8, 3π{8q, and thus cosp3θ{2´3π{8qą cosp3π{8q“ :δą 0.
So we have
|gpzq| ď exppr´ϵδr3{2q
80

and this tends to 0 as |z|“ rÑ8 .
So pick R big enough so that |gpzq| ďM for all z P A with |z| ěR. Now AXBp0,Rq is a bounded
domain such that|gpzq|ď M everywhere on the boundary. Thus, since g is holomorphic, it follows from the
maximum principle that|g|ď M everywhere inAXBp0,Rq. Thus by choice of R,|g|ď M on all of A. This
means that for any zPA,
|fpzq| ď M¨
⏐⏐⏐exppϵpe´iπ{4zq3{2q
⏐⏐⏐.
Since ϵ is arbitrary, we can take ϵÑ 0 and thus conclude that |fpzq|ď M for all zPA.
Since M is a bound for |fpzq| on the entirety of the real and imaginary axes, we can repeat this argu-
ment in each of the other three quadrants and hence obtain that |fpzq|ď M for all zP C, implying that f
is a bounded entire function and thus f must be constant.
Problem 9. Let Ω “ tz P C : |z| ą1 and Repzq ą ´2u. Suppose u : Ω Ñ R is bounded, continuous,
and harmonic on Ω and also that upzq“ 1 when |z|“ 1 and that upzq“ 0 when Repzq“´ 2. Determine
up2q.
Solution. Note that Ω is a region on which the Dirichlet problem can be solved, so the function u is
uniquely determined by its boundary values. We want to conformally map Ω to an annulus, on which we can
determineu easily. Note that the mapzÞÑ 1{z is a conformal map from Ω to Ω1“ DztzP C :|z`1{4|ď 1{4u.
We now want to conformally map Ω 1 to the annulus tz P C : ră| z|ă 1u. It suﬃces to ﬁnd a conformal
map which ﬁxes the unit circle and maps 0 to r and´1{2 to ´r. We know that the map
φ :zÑ z´α
1´αz
ﬁxes the unit circle, so we just need to pick an α such that φp0q“ r andφp´1{2q“´ r. Solving the system
of equations, we ﬁnd that ´α“r“ 2´
?
3 is the right choice.
So we know that z ÞÑ φp1{zq is a conformal map from Ω to the annulus A “ tz P C : r ă |z| ă 1u,
with the line Repzq“´ 2 mapping onto the inner circle |z|“ r and the unit circle mapping to itself. So we
ﬁnd a harmonic function v on A with vpzq“ 0 for |z|“ r and vpzq“ 1 for |z|“ 1. The function
vpzq “ log |z{r|
logp1{rq
accomplishes this. Thus the original function u is given by
upzq “ vpφp1{zqq “ 1
logp1{rq log
⏐⏐⏐⏐
1`rz
rz`r2
⏐⏐⏐⏐.
So up2q“ 1
logp1{rq log
⏐⏐⏐ 1`2r
2r`r2
⏐⏐⏐.
Problem 10. Determine ż8
´8
dy
p1`y2qp1`px´yq2q
for all xP R.
Solution. For a ﬁxed xP R, integrate the function
fpzq “ 1
p1`z2qp1`px´zq2q
around a half circle in the upper half plane from R to´R and then along the real axis from ´R toR. After
computing the residues and taking the limit (the contribution from the half circle goes to 0) you get that
81

the answer is 2π
x2`4.
Problem 11. Let Ω “ Dzt0u. Prove that for every bounded harmonic function u : Ω Ñ R there is a
harmonic function v : ΩÑ R obeying
Bu
Bx “ Bv
By, Bu
By “ ´Bv
Bx.
Solution. Let ˚du“´ uydx`uxdy be the conjugate diﬀerential of u. We know that for any 0 ă ră 1,
the function u satisﬁes ż
|z|“r
upreiθqdθ “ α logprq` β
for some constants α and β, and α is given by the quantity
ż
|z|“r
˚du,
which is constant with respect to r. Since u is bounded on Ω, write |u|ď M, then we have
⏐⏐⏐⏐⏐
ż
|z|“r
upreiθqdθ
⏐⏐⏐⏐⏐ ď
ż
|z|“r
|upreiθq|dθ ď 2πrM,
which tends to 0 as r Ñ 0`. This implies that we must have α“ 0. Thus in particular
ş
|z|“1{2
˚du“ 0.
Since the circle |z|“ 1{2 forms a homology basis for Ω, this implies that
ş
γ
˚du“ 0 for any curve γ Ď Ω,
so ˚du is an exact diﬀerential on Ω. This implies that there is a function v on Ω satisfying dv“ ˚du, i.e.
vx“´uy andvy“ux. The only thing left to verify is that v is harmonic. Note that we can deﬁne f“u`iv
on Ω and since f satisﬁes the Cauchy-Riemann equations, it is holomorphic on Ω, and therefore its real and
imaginary parts are harmonic, so v is harmonic on Ω.
Alternate solution. It is a standard fact that a harmonic function on a simply connected domain has
a harmonic conjugate. So to show the existence of v it suﬃces to show that u can be extended to be har-
monic on all of D. We know that u is continuous on the circle |z|“ 1{2, so let h be the function which is
harmonic in|z|ă 1{2 and solves the Dirichlet problem with boundary values upwq for|w|“ 1{2. If we show
thatu“h everywhere where they are both deﬁned, then this shows that u can be extended to be harmonic
at 0. Let f “ u´h. Then f is a function which is harmonic in |z| ă1{2 and is equal to 0 everywhere
on|z|“ 1{2. Also, since u and h are both bounded, f is bounded. We now proceed with the standard ϵ
argument. Fix ϵą 0 and consider the function zÞÑfpzq` ϵ log|2z|. This function is harmonic in |z|ă 1{2
and is equal to 0 on the boundary |z|“ 1{2. Furthermore, since f is bounded, this function tends to ´8
as z Ñ 0. Therefore, we may pick 0 ă r ą 1{2 such that fpzq` ϵ log|2z| ď0 for |z| ďr. Now since
fpzq` ϵ log|2z| is harmonic on ră|z|ă 1{2 and vanishes on the boundary, by the maximum principle we
conclude that fpzqď´ ϵ log|2z| for all ră|z|ă 1{2, and by choice of r we also have that fpzqď´ ϵ log|2z|
for all zP Ω. Now taking ϵÑ 0 we conclude that fpzqď 0 for all zP Ω, so upzqď hpzq in Ω. Now we can
repeat the entire argument again with ˜f :“h´u in place of f, and conclude that hpzqď upzq in Ω, so h“u
and we are done.
Problem 12. Find all entire functions f : CÑ C that obey
f1pzq2`fpzq2 “ 1.
Prove your list is exhaustive.
Solution. By taking the derivative of the above equation, we see that a necessary condition is
2f1pzqf2pzq` 2fpzqf1pzq “ 2f1pzqpf2pzq` fpzqq “ 0
82

for all zP C. This means we have tzP C : f1pzq“ 0uYt zP C : f2pzq` fpzq“ 0u“ C, so at least one of
those sets must have a limit point, and since f is holomorphic, both f1 and f2`f also are, and thus we
either have f1“ 0 or f2`f“ 0 on all of C.
If f1 “ 0, then f is a constant, and the only constants which satisfy the original equation are fpzq“˘ 1.
Now focus on the case f2`f “ 0. We show that the most general function that satisﬁes this is given by
fpzq“ a cospzq` b sinpzq. We can write f as a power series fpzq“ ř8
n“0anzn, and since f2pzq“´ fpzq
and power series can be diﬀerentiated term by term, we conclude that an“´p n` 2qpn` 1qan`2 for each
n. This shows that a solution f is uniquely determined by its ﬁrst two coeﬃcients a0 and a1, which means
the set of solutions is a 2-dimensional subspace of the vector space of entire functions. Since we know that
cospzq and sinpzq are two linearly independent solutions, it follows that fpzq“ a cospzq`b sinpzq is the most
general solution. Plugging this into the original condition, we get
p´a sinpzq` b cospzqq2`pa cospzq` b sinpzqq2 “ a2`b2 “ 1.
Thus we conclude that all of the solutions of the original equation are fpzq“˘ 1 orfpzq“ a cospzq`b sinpzq
where a2`b2“ 1.
83

14 Fall 2015
Problem 1. Letgn be a sequence of measurable functions on Rd, such that|gnpxq|ď 1 for allx, and assume
that gnÑ 0 almost everywhere. Let fPL1pRdq. Show that the sequence
f˚gnpxq“
ż
fpx´yqgnpyqÑ 0
uniformly on each compact subset of Rd, as nÑ8.
Solution. Fix rą 0 and let Br denote the closed ball of radius r centered at the origin. We will show that
f˚gn converges uniformly on Br.
For an arbitrary aą 0, we and xPBr have
|f˚gnpxq|ď
ż
|fpx´yqgnpyq|dy
“
ż
Ba
|fpx´yq|¨| gnpyq|dy`
ż
RzBa
|fpx´yq|¨| gnpyq|dy
ď
ż
Ba
|fpx´yq|¨| gnpyq|dy`
ż
RzBa
|fpx´yq|dy
We analyze each of these last two integrals separately.
For the second integral, we recall that xPBr, so we have
ż
RzBa
|fpx´yq|ď
ż
RzBa´r
|fpyq|dy,
after a linear change of variables. Then for ﬁxed ϵą 0 we may choose an a“ apϵq so that this integral is
bounded by ϵ2.
For the ﬁrst integral, recall that the integral of an L1 function over a set of small measure is small. So by
Egarov we may ﬁnd a measurable set EĎBa so that fnÑf uniformly on BazE, and
ş
Efpx´yqdyăϵ1.
Then for large enough n we have
ż
Ba
|fpx´yq|¨| gnpyq|dy“
ż
E
|fpx´yq|¨| gnpyq|dy`
ż
BazE
|fpx´yq|¨| gnpyq|dy
ď
ż
E
|fpx´yq|dy`ϵ1
ż
BazE
|gnpyq|dy
ďϵ1p1`λdpBaqq.
Combining the two pieces, we have
|f˚gnpxq|ď ϵ1¨p 1`λdpBapϵqqq` ϵ.
By choosing ϵ1 “ ϵ{p1`λdpBapϵqqq, we see that |f˚gnpxq| ă2ϵ for large enough n. Since this bound is
independent of x, we conclude that f˚gnÑ 0 uniformly on Br.
Remark. One can also solve this problem by ﬁrst solving it when f has compact support and then ap-
plying an approximation argument. This is equivalent, but perhaps conceptually simpler since some of the
details get abstracted into the compact support case.
Problem 2. Let f P LppRq, 1 ă p ă 8, and let a P R be such that a ą 1´ 1{p. Show that the
series
8ÿ
n“1
żn`n´a
n
|fpx`yq|dy
2This follows by “continuity from below” for general measures.
84

converges for almost all xP R.
Solution. Let q be the conjugate exponent so that 1{p` 1{q“ 1. Deﬁne
gpxq “
8ÿ
n“1
żn`n´a
n
|fpx`yq|dy.
With a change of variables we can write
gpxq “
8ÿ
n“1
n´a
ż 1
0
|fpx`n`n´azq|dz.
Applying H¨ older’s inequality for sums we have
|gpxq| ď
˜ 8ÿ
n“1
n´aq
¸1{q˜ 8ÿ
n“1
ˆż 1
0
|fpx`n`n´azq|dz
˙p¸1{p
.
Sinceaqą 1 by hypothesis, the ﬁrst term on the right side is just a constant C, and applying H¨ older to the
integral in the second term we get
|gpxq| ďC
˜ 8ÿ
n“1
˜ˆż 1
0
1q
˙1{qˆż 1
0
|fpx`n`n´az|pdz
˙1{p¸p¸1{p
“ C
˜ 8ÿ
n“1
ż 1
0
|fpx`n`n´azq|pdz
¸1{p
.
To showg is ﬁnite almost everywhere it is suﬃcient to show that
şN`1
N |gpxq|pdxă8 for each N P Z. We
have
żN`1
N
|gpxq|pdx ď Cp
żN`1
N
8ÿ
n“1
ż 1
0
|fpx`n`n´azq|pdzdx
“ Cp
ż 1
0
8ÿ
n“1
żN`1
N
|fpx`n`n´azq|pdxdz
by two applications of the Monotone Convergence Theorem and one application of Tonelli’s Theorem. Chang-
ing variables again we get
żN`1
N
|gpxq|pdx ď Cp
ż 1
0
8ÿ
n“1
żN`1`n`n´az
N`n`n´az
|fpuq|pdudz
ď Cp
ż 1
0
8ÿ
n“1
żN`n`2
N`n
|fpuq|pdudz
ď Cp
ż 1
0
2||f||p
Lp dz “ 2Cp||f||p
Lp ă 8.
Thus
şN`1
N |g|p is ﬁnite for any integer N, so we conclude that gpxq is ﬁnite almost everywhere.
Problem 3. Let fPL1
locpRdq be such that for some 0 ăpă 1, we have
⏐⏐⏐⏐
ż
fpxqgpxqdx
⏐⏐⏐⏐ ď
ˆż
|gpxq|p
˙1{p
,
for all gPC0pRdq (continuous functions with compact support). Show that fpxq“ 0 a.e.
Solution.
85

We would like to apply the condition of the problem when g is a characteristic function. Unfortunately
characteristic functions aren’t continuous, but we’re able to recover the same information via a suitable
approximation.
Lemma. Let K be a compact set. Then |
ş
Kfpxqdx|ď λdpKq1{p.
Proof: Fixϵą 0 and letU be an open set with compact closure containingK such that
ş
UzK|fpxq|dxăϵ.
(This is possible by continuity from above together with the fact that the integral of f over a set of small
measure is small.) By replacing U with a set of smaller measure if necessary, we may suppose in addition
thatλdpUzKqă ϵ. LetgK be a continuous function RdÑr 0, 1s which takes the value 1 on K and 0 outside
of U (such a function exists by Urysohn). We have
ˇˇˇˇ
ż
fpxqgKpxqdx´
ż
K
fpxqdx
ˇˇˇˇ“
ˇˇˇˇ
ż
fpxqpgKpxq´ χKpxqqdx
ˇˇˇˇ
ď
ż
UzK
|fpxq|
ăϵ.
Then we have
ˇˇˇˇ
ż
K
fpxqdx
ˇˇˇˇďϵ`
ˇˇˇˇ
ż
fpxqgKpxqdx
ˇˇˇˇ
ďϵ`
ˆż
|gKpxq|p
˙1{p
ďϵ`λdpUq1{p
ďϵ`pλdpKq` ϵq1{p.
But ϵ was arbitrary, so we the lemma follows by taking the limit as ϵÑ 0`.
Now ﬁx a cube C Ď Rd of side length s. For any positive integer N we may dissect C into Nd cubes
tCiuiPrNds of side lengths s{N. By the lemma,
ż
Ci
fpxqdxďλdpCiq1{p“
´ s
N
¯d{p
.
Summing over all Ci we ﬁnd that
ż
C
fpxqdxďNd¨
´ s
N
¯d{p
“sd{p¨Ndp1´1{pq.
But 1´ 1
p ă 0, so the right-hand side tends to 0 as N Ñ8. Thus we conclude that
ş
Cfpxqdx for all cubes
C.
Every open set is a union of countably many cubes with disjoint interiors. Therefore
ş
Ufpxqdx“ 0 for
any open setU. Then by continuity from above,
ş
Mfpxq must be zero for any measurable set M, from which
it follows that f is 0 a.e.
Alternate solution. Same idea as the ﬁrst solution but the technical details are diﬀerent.
Fix a large closed ball S“Bp0,Rq, it’s enough to show f“ 0 a.e. on S. Suppose not. Then
Claim: There exists a δą 0 and a set EĎS with λpEqą 0 with the property that for any subset F ĎE,⏐⏐ş
Ffpxqdx
⏐⏐ąδλpFq.
Assume the claim for now. A corollary of the claim is that there exist sets E of arbitrarily small positive
measure satisfying the inequality in the claim. Fix such a set E with measure small enough to satisfy
δλpEqą λpEq1{p (possible because 1{pą 1).
Fix ϵą 0 (assume w.l.o.g that ϵă λpEq{10). Since f is integrable on S, let αą 0 be small enough so
that λpAqă 2α and AĎS implies
ş
A|f|ă ϵ. We may also pick αăϵ. Take a compact set K and an open
86

setU withKĎEĎUĎS andλpEzKq,λpUzEqă ϵ. Let g be a continuous function with 0 ďgď 1,g“ 1
on K, and g“ 0 outside U. Then g also has compact support. We have the estimates
ˆż
|gpxq|pdx
˙1{p
“
˜ż
K
|gpxq|p`
ż
UzK
|gpxq|pdx
¸1{p
ď pλpKq` 2ϵq1{p ď pλpEq` 2ϵq1{p
⏐⏐⏐⏐
ż
fpxqgpxqdx
⏐⏐⏐⏐ “
⏐⏐⏐⏐⏐
ż
K
fpxqgpxqdx`
ż
UzK
fpxqgpxqdx
⏐⏐⏐⏐⏐ ě
⏐⏐⏐⏐
ż
K
fpxqdx
⏐⏐⏐⏐´
ż
UzK
|fpxq|dx
ě δλpKq´ ϵ ě δpλpEq` ϵq´ ϵ “ δλpEq´p δ` 1qϵ.
By the hypothesis of the problem, this implies
δλpEq´p δ` 1qϵ ď pλpEq` 2ϵq1{p.
Sinceϵ was arbitrary, takingϵÑ 0 givesδλpEqď λpEq1{p, a contradiction by the choice ofE at the beginning.
We need to prove the claim. Suppose f is not a.e. 0. Then by continuity from below, there is some
δą 0 such that λtxPS :|fpxq|ą 2δuą 0. For any k, we have the decomposition
txPS :|fpxq|ą 2δu “
txPS :|fpxq|ą 2δ, argpfqPr´ 2π{k, 2π{kquY ... YtxPS :|fpxq|ą 2δ, argpfqPr´ 2πpk´ 3q{k, 2πpk´ 1q{kq,u
so one of those sets has positive measure. By multiplying f by a rotation, without loss of generality we can
assume
λpEq :“ λtxPS :|fpxq|ą 2δ, argpfqPr´ 2π{k, 2π{kqu ą 0.
Letk be big enough so that |fpxq|ą 2δ and argpfqPr´ 2π{k, 2π{kq implies Repfqą δ. Then for any subset
F ĎE, we have ⏐⏐⏐⏐
ż
F
f
⏐⏐⏐⏐ ě
⏐⏐⏐⏐
ż
F
Repfq
⏐⏐⏐⏐ ą δλpFq.
This proves the claim, so we’re done.
Problem 4a. Let H be a separable inﬁnite-dimensional Hilbert space and assume that penq is an or-
thonormal system in H. Let pfnq be another orthonormal system which is complete, i.e. the closure of the
span ofpfnq is all of H. Show that if ř8
n“1||fn´en||2ă 1 then the orthonormal systempenq is also complete.
Solution. Let v be a vector which is orthogonal to each of the ei. It suﬃces to show that v “ 0. Since
pfiq is an orthonormal system, we can write v “ ř8
n“1xv,fnyfn. Using this expression as motivation, we
deﬁne w “ ř8
n“1xv,fnyen. Note that v and w are orthogonal, while the original condition suggests that
they should be close in some suitable sense. More precisely, by applying Cauchy-Schwarz we have
||v´w||2“
ˇˇˇˇˇ
ˇˇˇˇˇ
8ÿ
n“1
xv,fnypfn´enq
ˇˇˇˇˇ
ˇˇˇˇˇ
2
ď
˜ 8ÿ
n“1
|xvn,fny|||fi´ei||
¸2
ď
˜ 8ÿ
n“1
|xv,fiy|2
¸
¨
˜ 8ÿ
n“1
||fn´en||2
¸
ď||v||2.
On the other hand,v andw are orthogonal, so||v´w||2“||v||2`||w||2. Thus||w||2“ 0, and by our original
deﬁnition of w we must havexv,fny“ 0 for all n. Sincepfnq is a complete system, this means that v“ 0 as
desired.
Problem 4b. Assume we only have ř8
n“1||fn´en||2ă8 . Prove that it is still true that penq is complete.
Solution. LetEN “ spanpeN,eN`1,... q andFN “ spanpfN,fN`1,... q. The condition thatř8
n“1||fn´en||2ă
87

8 tells us that for big n, en and fn are very close together, so the subspaces EN and FN should also be
“close together” when N is big enough. For a closed subspace M Ď H, let πM : HÑM be the orthogonal
projection onto M. We show that ||πEN´πFN||opÑ 0 as N Ñ8 (this is one way of saying the subspaces
are close to each other). For any xP H we have
||pπEN´πFNqpxq|| “
ˇˇˇˇˇ
ˇˇˇˇˇ
8ÿ
n“N`1
xx,enyen´xx,fnyfn
ˇˇˇˇˇ
ˇˇˇˇˇ “
ˇˇˇˇˇ
ˇˇˇˇˇ
8ÿ
n“N`1
xx,enypen´fnq`
8ÿ
n“N`1
xx,en´fnyfn
ˇˇˇˇˇ
ˇˇˇˇˇ
ď
8ÿ
n“N`1
|xx,eny|||en´fn||`
¨
˝
ˇˇˇˇˇ
ˇˇˇˇˇ
8ÿ
n“N`1
xx,en´fnyfn
ˇˇˇˇˇ
ˇˇˇˇˇ
2˛
‚
1{2
ď
˜ 8ÿ
n“N`1
|xx,eny|2
¸1{2˜ 8ÿ
n“N`1
||en´fn||2
¸1{2
`
˜ 8ÿ
n“N`1
⏐⏐⏐xx,en´fny2
⏐⏐⏐
¸1{2
ď ||x||
˜ 8ÿ
n“N`1
||en´fn||2
¸1{2
`
˜ 8ÿ
n“N`1
||x||2||en´fn||2
¸1{2
ď ||x||¨ 2
˜ 8ÿ
n“N`1
||en´fn||2
¸1{2
where we have used Cauchy-Schwarz for sums, the Pythagorean theorem, and Cauchy-Schwarz in H. This
shows that||πEN´πFN||2
opď 4ř8
n“N`1||en´fn||2, which goes to 0 as NÑ8 by hypothesis.
We know that H “ EN ‘EK
N for any N because EN is closed. So to show that spanptenuq “ H,
it’s enough to ﬁnd an N such that te1,...,e Nu spans EK
N. Since the en are orthonormal, we at least
know that span pe1,...,e Nq Ď EK
N for each N. The ej are also independent, so it suﬃces to ﬁnd an
N such that dim pEK
Nq ď N. By the assumption that tfnu is a complete system, we also know that
spanpf1,...,f Nq“ FK
N, so dimpFK
Nq“ N. Finally, since πSK “id´πS for any closed subspace S, we haveˇˇˇ
ˇˇˇπEK
N
´πFK
N
ˇˇˇ
ˇˇˇ
op
“||πEN´πFN||opÑ 0 asNÑ8 . Pick N to be large enough so that
ˇˇˇ
ˇˇˇπEK
N
´πFK
N
ˇˇˇ
ˇˇˇ
op
ď 1{2.
Now the desired result follows from the following lemma.
Claim: Let S and T be two closed subspaces of H with ||πS´πT||op ď 1{2 and dim pTq “N ă 8.
Then dimpSqď N.
Proof: Let x1,...,x N`1 be any N` 1 vectors in S. Then πTpx1q,...,π TpxN`1q are N` 1 vectors in an
N-dimensional space, so we have
0 “ α1πTpx1q` ... `αN`1πTpxN`1q “ πTpα1x1`... `αN`1xN`1q
But also since each xjPS, we have πSpα1x1`... `αN`1xN`1q“ α1x1`... `αN`1xN`1, so
||α1x1`... `αN`1xN`1|| “ ||πSpα1x1`... `αN`1xN`1q´ πTpα1x1`... `αN`1xN`1q||
ď 1
2||α1x1`... `αN`1xN`1||,
which implies α1x1`... `αN`1xN`1“ 0, so the xj are a dependent set. So any set of N` 1 vectors in S
is dependent, so dimpSqď N.
Problem 5. A function f P Cpr0, 1sq is called H¨ older continuous of order δ ą 0 if there is a constant
C such that|fpxq´ fpyq|ď C|x´y|δ for all x,y Pr 0, 1s. Show that the H¨ older continuous functions form a
meager set in Cpr0, 1sq.
Solution. Deﬁne Λδ to be the set of all H¨ older continuous functions of order δ on r0, 1s and let Λ be
the set of all H¨ older continuous functions of any order onr0, 1s. First note that δąη implies that ΛδĎ Λη,
so we can write
Λ “
8ď
n“1
Λ1{n.
88

Since a countable union of meager sets is meager, it suﬃces to show that Λ δ is a meager subset of Cpr0, 1sq
for any ﬁxed δ. We can write
Λδ “
8ď
m“1
tfP Λδ :||f||Λδ ďmu “:
8ď
m“1
Em
where the norm ||f||Λδ is deﬁned by
|fp0q|` sup
x,yPr0,1s
|fpxq´ fpyq|
|x´y|δ
(this is one of the standard norms on the space of H¨ older continuous functions). So it suﬃces to show that
eachEm is closed and nowhere dense with respect to the L8 norm.
To show Em is closed, suppose that fn P Em and fn converges uniformly to f P Cpr0, 1sq. Fix ϵ ą 0,
and for any x,y Pr 0, 1s, let n be big enough so that |f´fn|ă ϵ|x´y|δďϵ onr0, 1s. Then we have
|fp0q|` |fpxq´ fpyq|
|x´y|δ ď |fp0q´ fnp0q|`| fnp0q|` |fpxq´ fnpxq|
|x´y|δ `|fnpxq´ fnpyq|
|x´y|δ `|fnpyq´ fpyq|
|x´y|δ
ď ||fn||Λδ` 3ϵ ď M` 3ϵ,
and since the left side does not depend on ϵ, we conclude that
|fp0q|` |fpxq´ fpyq|
|x´y|δ ď m
for all x,y , so ||f||Λδ ďm. Therefore Em is closed.
For nowhere dense, let f P Em and ﬁx ϵ ą 0. We just need to show the existence of some h R Em
with ||h´f||L8 ď ϵ. Fix any g R Λδ (for example, gpxq “xδ{2 works) and by scaling, we may assume
||g||L8 “ 1. Then let h “ f`ϵg. Then we clearly have ||h´f||L8 “ϵ. Since gR Λδ, we can ﬁnd points
xn,yn such that
|gpxnq´ gpynq|
|xn´yn|δ ě n
ϵ.
Then we have
|hpxnq´ hpynq|
|xn´yn|δ “ |fpxnq` ϵgpxnq´ fpynq´ ϵgpynq|
|xn´yn|δ
ě ϵ|gpxnq´ gpynq|
|xn´yn|δ ´|fpxnq´ fpynq|
|xn´yn|δ ě n´m,
which goes to 8 as nÑ8 , so hR Λδ. Therefore Em is closed and nowhere dense, so we’re done.
Problem 6. Let uPL2pRdq and say that uPH1{2pRdq (a Sobolev space) if
´
1`|ξ|1{2
¯
ˆupξqP L2pRdq.
Here ˆu is the Fourier transform of u. Show that uPH1{2pRdq if and only if
ĳ |upx`yq´ upxq|2
|y|d`1 dxdy ă 8.
89

Solution. Since u P L2pRdq, we know immediately that ˆu P L2pRdq also, so we just need to show that`
1`|ξ|1{2˘
ˆupξqP L2pRdq if and only if the above double integral is ﬁnite. It suﬃces to prove that
ż
|ξ| |ˆupξq|2 dξ À
ĳ |upx`yq´ upxq|2
|y|d`1 dxdy À
ż
|ξ| |ˆupξq|2 dξ,
where throughout this problem À denotes an implied constant which depends only on d. First note that by
Plancherel, we have
ĳ |upx`yq´ upxq|2
|y|d`1 dxdy “
ż 1
|y|d`1
ż ⏐⏐1´e2πiy¨ξ⏐⏐2
|ˆupξq|2 dξdy “
ż
|ˆupξq|2
ż ⏐⏐1´e2πiy¨ξ⏐⏐2
|y|d`1 dydξ,
so it now suﬃces just to prove the estimates
|ξ| À
ż ⏐⏐1´e2πiy¨ξ⏐⏐2
|y|d`1 dy À |ξ|.
For the upper bound, we have the estimate
ż ⏐⏐1´e2πiy¨ξ⏐⏐2
|y|d`1 dy “
ż
|y|ď1{p2|ξ|q
⏐⏐1´e2πiy¨ξ⏐⏐2
|y|d`1 dy`
ż
|y|ą1{p2|ξ|q
⏐⏐1´e2πiy¨ξ⏐⏐2
|y|d`1 dy
ď
ż
|y|ď1{p2|ξ|q
|4πy¨ξ|2
|y|d`1 dy`
ż
|y|ą1{p2|ξ|q
4
|y|d`1dy because |1´ez|ď 2|z| for|z|ď 1{2
À |ξ|2
ż
|y|ď1{p2|ξ|q
|y|2
|y|d`1 dy`
ż
|y|ą1{p2|ξ|q
1
|y|d`1 dy
À |ξ|`| ξ| À |ξ|.
Now we do the lower bound. For ξ ﬁxed, deﬁne E“tyP Rd : |y¨ξ|ěp 1{2q|y||ξ|u. We estimate
ż ⏐⏐1´e2πiy¨ξ⏐⏐2
|y|d`1 dy ě
ż
|y|ď1{p3|ξ|q,yPE
⏐⏐1´e2πiy¨ξ⏐⏐2
|y|d`1 dy
ě
ż
|y|ď1{p3|ξ|q,yPE
|πy¨ξ|2
|y|d`1 dy because|ez´ 1|ěp 1{2q|z| for|z|ď 1{3
Á
ż
|y|ď1{p3|ξ|q,yPE
p1{2q|y|2|ξ|2
|y|d`1 dy Á |ξ|2
ż
|y|ď1{p3|ξ|q,yPE
1
|y|d´1 dy.
Now note that membership inE is determined only by the direction ofy and is independent of the magnitude
of y. So since the above integrand is a function only of |y|, and E takes up a “positive proportion” of all of
Rd (this can be made precise), it follows that the above integral is
Á |ξ|2
ż
|y|ď1{p3|ξ|q
1
|y|d´1 dy Á |ξ|,
which concludes the proof of the lower bound, so we are done.
Problem 7. Assume that fpzq is analytic in D and continuous on D. If fpzq “fp1{zq when |z| “ 1,
prove that fpzq is constant.
Solution. Deﬁne the function g by
gpzq :“
#
fpzq | z|ď 1
fp1{zq |z|ě 1.
90

Because of the condition that fpzq“ fp1{zq for|z|“ 1, we see that g is continuous on all of C. We now
mimic the proof of the Schwarz reﬂection principle to show that g is analytic on all of C. By Morera’s
theorem, it is enough to show that ż
BR
gpzqdz “ 0
for any rectangleR. It is clear from the deﬁnition that g is analytic inside D and so we don’t need to consider
rectangles R that are contained in D. Also, since zÞÑ 1{z is a conformal map from CzD into Dzt0u, we also
see that g is analytic on the exterior of D, so we also don’t need to consider rectangles that are contained
in the exterior of D. Thus we only need to consider rectangles which intersect the unit circle. For such a
rectangle, split the contour along the arc of the unit circle into a band of width δ (this is hard to explain
without a picture). Since g is analytic on both the inside and the outside of D, the integral over this split
contour is necessarily 0. Then, since g is continuous everywhere, as we let δÑ 0, the integral over the split
contour approaches the integral over the original rectangle, and so we conclude that
ş
BRgpzqdz“ 0 for all
rectangles R and thus g is analytic on all of C.
Now note that since f is continuous on D, which is compact, f must be bounded, and thus g must also
be bounded. But g is entire, so g must be a constant, which means f must also be a constant.
Problem 8. Assume that fpzq is an entire function that is 2π-periodic in the sense that fpz` 2πq“ fpzq,
and
|fpx`iyq| ď Ceα|y|
for some Cą 0, where 0 ăαă 1. Prove that f is constant.
Solution. Since fpzq is 2π periodic, we can express f as the pullback of a holomorphic function on the
cylinder. More formally, we can write
fpzq“ gpeizq
where we deﬁne g on Czt0u bygpzq“ fp 1
i logpzqq. Sincef is 2π-periodic, the branch of log is irrelevant, and
g is well-deﬁned.
The given bound implies that |gpey¨eixq|ď Ceα|y|. Thus we have
|gpzq|ď C exppα| log|z||q.
As|z|Ñ 0, we have|gpzq|ď Cz´α, but αă 1, so g has a removable singularity at 0, and we can extend g
to an analytic function on C. Similarly as |z|Ñ 0, we have|gpzq|ď Czα, and so g must be constant. This
immediately implies that f is constant.
Problem 9. Letpfjq be a sequence of entire functions such that, writing z“x`iy, we have
ĳ
C
|fjpzq|2e´|z|2
dxdy ď C, j “ 1, 2,...
for some constant Cą 0. Show that there exists a subsequence pfjkq and an entire function f such that we
have ĳ
C
|fjkpzq´ fpzq|2e´2|z|2
dxdy Ñ 0, k Ñ8.
Solution. By the mean value property and Cauchy-Schwarz, for any z P C with |z| ě2 and any j we
can write
|fjpzq| À
ż
Bpz,1q
|fjpwq| dxdy À
˜ż
Bpz,1q
|fjpwq|2 dxdy
¸1{2
ď e
1
2p|z|`1q2
˜ż
Bpz,1q
|fjpwq|2e´|w|2
dxdy
¸1{2
ď Ce
1
2p|z|`1q2
.
91

In particular, this implies that the sequence tfju is uniformly bounded on every compact subset of C, so it
is a normal family. Thus it has a subsequence tfjku which converges uniformly on every compact subset of
C. Since each fj is entire, we also know that the limit function f is entire and also satisﬁes the estimate
|fpzq|À e
1
2p|z|`1q2
.
for|z|ě 2.
To show the desired conclusion, ﬁx ϵą 0. Let R be big enough so that
ż
|z|ąR
e´|z|2`|z|`1dxdy ă ϵ.
Since fjkÑf uniformly on every compact subset of C, we may choose k to be big enough so that
ż
|z|ďR
|fjkpzq´ fpzq|2e´2|z|2
dxdy ă ϵ.
Thus we have the estimate
ż
C
|fjkpzq´ fpzq|2e´2|z|2
dxdy “
ż
|z|ďR
|fjkpzq´ fpzq|2e´2|z|2
dxdy `
ż
|z|ąR
|fjkpzq´ fpzq|2e´2|z|2
dxdy
ă ϵ`
ż
|z|ąR
pC1¨ 2e
1
2p|z|`1q2
q2e´2|z|2
dxdy
ď ϵ`C2
ż
|z|ąR
e´|z|2`|z|`1dxdy ă p1`C2qϵ,
which establishes the desired conclusion.
Problem 10. Use the Residue Theorem to prove that
ż8
0
ecosx sinpsinxqdx
x “ π
2pe´ 1q
Use a large semicircle as part of the contour.
Solution. For realx, the integrand can be written as 1
x Impeeix
q. We can rewrite our integral as
ż8
0
Impeeix
qdx
x “ Im
ż8
´8
eeixdx
x ,
where the equality holds provided the second integral exists (which it will).
Set fpzq“ 1
zeeiz
and let ΓR denote a large semicircular contour of radius R with endpoints at ´R and
R. Also let γr denote a small clockwise contour of radius r with endpoints at ´r and r.
Note that f is holomorphic everywhere except z“ 0, where it has a simple pole with residue e. Thus by
(a variant of) the residue theorem for “indented contours”, we have
lim
rÑ0
ż
γr
fpzqdz“´ 1
2¨ 2πi¨e“´iπe.
On the outer contour we have ż
ΓR
fpzqdz“i
żπ
0
eeiR exppiθq
dθ.
Note that for θPr 0,πs, ⏐⏐⏐eiR exppiθq
⏐⏐⏐“e´R sinpθqď 1.
92

Thus by the bound |ez|ďe|z|, our integrand is dominated by e. Also as RÑ8, the same bound shows that
the integrand tends pointwise to e0“ 1 (except at θ“ 0 and θ“π), so by dominated convergence,
ż
ΓR
fpzqdzÑiπ as RÑ8.
By Cauchy’s applying Cauchy’s theorem to a contour joining the two semicircles, we have
0“ 2
żR
´r
fpzqdz`
ż
γr
fpzqdz`
ż
ΓR
fpzqdz,
and taking the limit as rÑ 0 and RÑ8 gives
ż8
0
fpxqdx“iπ
2pe´ 1q.
Finally, the imaginary part of this is the desired value.
Problem 11. Let Ω “ tpx,yq P R2 : x ą 0,y ą 0u and let u be subharmonic in Ω, continuous in Ω,
such that
upx,yq ď |x`iy|,
for large px,yqP Ω. Assume that
upx, 0q ď ax, u p0,yq ď by, x,y ě 0,
for some a,b ą 0. Show that
upx,yq ď ax`by, px,yqP Ω.
Solution. We use the Phregman-Linedl¨ of method. Fixϵą 0 and, writing px,yq“ reiθ, deﬁne
φpx,yq “ ax`by`ϵr3{2 cos
ˆ´3π
8 ` 3θ
2
˙
.
Note that ϵr3{2 cos
`´3π
8 ` 3θ
2
˘
is the real part of the function fpzq“´ ϵpe´iπ{4zq3{2, which is single-valued
and analytic in Ω, so φ is harmonic in Ω (because ax`by is clearly harmonic). Thus, since u is subharmonic
in Ω, we know that v :“u´φ does not have any local maximum in Ω.
We want to show that vpx,yqÑ´8 as rÑ8 in Ω. Note that since for px,yqP Ω we have θPp 0,π{2q, we
have´3π{8` 3θ{2Pp´ 3π{8, 3π{8q and thus cosp´3π{8` 3θ{2qą cosp3π{8q“ :δą 0. So as rÑ8 , by the
hypothesis that upx,yqă r for r suﬃciently large, we have
vpx,yq “ upx,yq´ ax´by´ϵr3{2 cos
ˆ´3π
8 ` 3θ
2
˙
ď r´ϵδr3{2Ñ´8
as rÑ8 . Thus we can pick an R large enough so that vpx,yqď 0 for all rě R. We also know from the
other hypotheses that on the x-axis,
vpx, 0q“ upx,yq´ ax´ϵr3{2 cos
ˆ´3π
8 ` 3θ
2
˙
ď 0
and similarly on the y-axisvp0,yqď 0. Thus we can now apply the maximum principle to v on the bounded
regiontpx,yqP Ω :rďRu, and since vď 0 on the boundary, we conclude that vď 0 throughout the entire
region, and thus by choice of R, vpx,yqď 0 for all px,yqP Ω. This means that
upx,yq ď ax`by`ϵr3{2 cos
ˆ´3π
8 ` 3θ
2
˙
93

for eachpx,yqP Ω, and since ϵ is arbitrary, we conclude that upx,yqď ax`by for all px,yqP Ω.
Problem 12. Find a function upx,yq harmonic in the region between the circles |z|“ 2 and |z´ 1|“ 1
which equals 1 on the outer circle and 0 on the inner circle (except at the point where the circles are tangent
to each other).
Solution. Let Ω “ tz P C : |z| ă2,|z´ 1| ą1u be the original region. We want to conformally map
Ω to a region on which such a function can easily be found and then pull it back. The map zÞÑ 1{pz´ 2q
sends Ω to the strip tzP C :´1{2ă Repzqă´ 1{4u, with the circle |z|“ 2 going to the line Repzq“´ 1{4
and the circle|z´1|“ 1 going to the circle Repzq“´ 1{2. So we are looking for a harmonic function v which
satisﬁes vpzq“ 0 when Repzq“´ 1{2 and vpzq“ 1 when Repzq“´ 1{4. The function vpzq“ Rep4z` 2q
clearly satisﬁes this and is harmonic because it is the real part of an analytic function. Therefore the function
upzq “ v
ˆ 1
z´ 2
˙
“ Re
ˆ 4
z´ 2` 2
˙
“ Re
ˆ 2z
z´ 2
˙
is a harmonic function on Ω with the desired properties.
94

15 Spring 2016
Problem 1a. Let
Ktpxq “ p4πtq´3{2e´|x|2{4t, x P R2, tą 0,
where|x| is the Euclidean norm of R3. Show that the linear map
f ÞÑ t1{2pKt˚fq, L 3pR3qÑ L8pR3q
is bounded uniformly in tą 0.
Solution. Throughout this problem, we use the symbol À to denote an implied constant which does
not depend on f, x or t. For any xP R3, we calculate
⏐⏐⏐t1{2pKt˚fqpxq
⏐⏐⏐ À t´1
ż
R3
exp
ˆ´1
4t|x´y|2
˙
|fpyq|dy ď t´1
ˆż
R3
|fpyq|3dy
˙1{3ˆż
R3
exp
ˆ´3
8t|x´y|2dy
˙˙2{3
by H¨ older’s inequality. Making the change of variablesz“
?
3?
8px´yq in the last integral, we get
⏐⏐⏐t1{2pKt˚fqpxq
⏐⏐⏐ À t´1||f||L3
˜ż
R3
exp
˜
´
⏐⏐⏐⏐
z?
t
⏐⏐⏐⏐
2¸
dz
¸2{3
“ t´1||f||L3
˜ˆż
R
expp´pu{
?
tq2qdu
˙3¸2{3
by Tonelli’s theorem
À t´1||f||L3p
?
πtq2 À||f||L3.
Thus
ˇˇˇˇt1{2pKt˚fq
ˇˇˇˇ
L8À||f||L3, so we see thatfÞÑt1{2pKt˚fq is a bounded linear operator whose operator
norm is bounded uniformly in tą 0.
Problem 1b. Prove that t1{2||Kt˚f||L8Ñ 0 as tÑ 0, for fPL3pR3q.
Solution. We know that CcpR3q, the set of continuous functions with compact support, is dense in L3pRq.
If gPCcpR3q, then we have
|pKt˚gqpxq| ď
ż
R3
|Ktpx´yqgpyq|dy ď ||g||L8
ż
R3
|Ktpx´yq|dy À ||g||L8
where again the implied constant here does not depend on t. Thus we have t1{2||Kt˚g||L8 Ñ 0 as tÑ 0
for all gPCcpR3q.
Now let f be any function in L3pR3q. Let the linear operator φt :L3pR3qÑ L8pR3q be deﬁned by
φtpfq “ t1{2pKt˚fq.
Recall that in part (a) we showed that there is a constantC, independent oft, such that||φtpfq||L8ďC||f||L3
for all f P L3. Fix ϵą 0. By density, we can pick gP CcpR3q such that ||f´g||L3 ă ϵ{2C. Since we have
proved the result for functions in CcpR3q, we can now pick a δą 0 such that for all tăδ,||φtpgq||L8ăϵ{2.
Then we conclude that for any tăδ we have
t1{2||Kt˚f||L8 “ ||φtpfq||L8 ď ||φtpgq||L8`||φtpf´gq||L8 ă ϵ
2`C||f´g||L3 ă ϵ.
This shows that limtÑ0t1{2||Kt˚f||L8“ 0 for any fPL3pR3q.
Problem 2. Let fPL1pRq. Show that the series
8ÿ
n“1
1?nfpx´?nq
95

converges absolutely for almost all xP R.
Solution. Let
gpxq “
8ÿ
n“1
1?n
⏐⏐fpx´?nq
⏐⏐.
We show that
şM`1
M gpxqdx is ﬁnite for every integer M, which is enough to conclude that gpxq ă 8for
almost every xPr M,M ` 1s, which in turn implies that gpxq is ﬁnite almost everywhere, which is exactly
what we need to prove.
For a ﬁxed integer M, we have
żM`1
M
gpxqdx “
żM`1
M
8ÿ
n“1
1?n
⏐⏐fpx´?nq
⏐⏐ “
8ÿ
n“1
1?n
żM`1
M
|fpx´?nq|dx
by the Monotone Convergence Theorem, and after changing variables we get
żM`1
M
gpxqdx “
8ÿ
n“1
1?n
żM`1´?n
M´?n
|fpyq|dy.
For each integer k, there are 2k` 1 integers n such that kă?nďk` 1. For each of these integers n, we
haverM´?n,M ` 1´?nsĎr M´k´ 1,M ` 1´ks. Thus the above sum is bounded by
8ÿ
k“1
p2k` 1q¨ 1
k
żM`1´k
M´k´1
|fpyq|dy ď 3
8ÿ
k“1
«żM´k
M´k´1
|fpyq|dy`
żM`1´k
M´k
|fpyq|dy
ﬀ
ď 6||f||L1.
Thus we conclude that
şM`1
M gpxqă8 , so gpxq is ﬁnite almost everywhere.
Problem 3. Let fPL1
locpRq be real-valued and assume that for each integer ną 0, we have
f
ˆ
x` 1
n
˙
ě fpxq,
for almost all xP R. Show that for each real number aě 0 we have
fpx`aq ě fpxq
for almost all xP R.
Solution. Let E be the (measure zero) set of x P Rn that do not have the property of the hypothesis.
Deﬁne F “ Ť
pPQpE`pq. This is a countable union of measure zero sets so it also has measure zero. If
a“ 0, the result is obvious, so let aą 0 be ﬁxed. By the Lebesgue diﬀerentiation theorem, we know that
fpx`aq´ fpxq “ lim
rÑ0`
1
2r
żx`r
x´r
pfpy`aq´ fpyqqdy.
for all x outside of some measure zero set G. We show that fpx`aq´ fpxqě 0 for all x outside of G. It is
enough to show that for any interval rb,cs,
żc
b
fpy`aqdy ě
żc
b
fpyqdy,
or equivalently żc`a
b`a
fpyqdy ě
żc
b
fpyqdy.
96

We can write a in binary as
a “ m`
8ÿ
j“1
ϵj
2j “
8ÿ
j“1
1
kj
where tkju is some sequence of integers (not necessarily distinct, because there could by many 1s at the
beginning). Let aN “ řN
j“1 1{kj. For any yR F and any N, we know that y`aN R E by construction of
F . Therefore we have fpy`aNq “fpy`aN´1` 1{kNq ěfpy`aN´1q. By induction and the fact that
y`aN RE for each N, we see that fpy`aNqě fpyq for all N. Therefore, since F has measure zero, this
means żc`aN
b`aN
fpyqdy “
żc
b
fpy`aNqdy ě
żc
b
fpyqdy.
Deﬁning fNpyq“ fpyqχrb`aN,c`aNspyq, we see that
ż
R
fNpyqdy ě
żc
b
fpyqdy.
Since fN Ñfχrb`a,c`as pointwise as N Ñ8 and|fN|ď| f|χrb,c`as for all N, and |f|χrb,c`as is integrable,
by the Dominated Convergence Theorem we conclude that
żc`a
b`a
fpyqdy “
ż
R
fχrb`a,c`as ě
żc
b
fpyqdy.
Thus we conclude that fpx`aq´ fpxqě 0 for all x for which the Lebesgue diﬀerentiation theorem applies
to the function xÞÑfpx`aq´ fpxq, which is almost all xP R.
Problem 4. Let V1 be a ﬁnite-dimensional subspace of the Banach space V . Show that there exists a
continuous projectionP :V ÑV1, i.e., a continuous linear mapP :V ÑV1 such thatP 2“P and the range
of P is equal to V1.
Solution. Let te1,...,e nu be a basis for V1. Without loss of generality we may assume that ||ej|| “1
for eachj. For a ﬁxed j, we know that spanteiui‰j is a closed subspace ofV . Thus by the Hahn-Banach the-
orem, there is a linear functional fjPV˚ such that fjpejq“ ||ej||“ 1 and fjpxq“ 0 for all xP spanteiui‰j.
Now deﬁne the map P :V ÑV1 by
Ppxq :“
nÿ
j“1
fjpxqej.
It is clear that ImpPqĎ V1 by construction, and since each fj is linear, P is also linear. We see that P is
continuous because
||Px´Py|| “
ˇˇˇˇˇ
ˇˇˇˇˇ
nÿ
j“1
fjpx´yqej
ˇˇˇˇˇ
ˇˇˇˇˇ ď
nÿ
j“1
|fjpx´yq|||ej|| ď
˜ nÿ
j“1
||fj||
¸
||x´y||.
Finally, for any vPV1, we write v“v1e1`... `vnen and note that
Pv “
nÿ
j“1
fjpv1e1`... `vnenqej “
nÿ
j“1
vjej “ v.
This implies both that P 2“P and that V1Ď ImpPq, so ImpPq“ V1. Thus P is the desired map.
Problem 5. ForfPC8
0 pR2q deﬁne upx,tq by
upx,tq “
ż
R2
eix¨ξ sinpt|ξ|q
|ξ| fpξqdξ, x P R2, t ą 0.
97

Show that limtÑ8||up¨,tq||L2“8 for a set of f that is dense in L2pRq.
Solution. We claim the desired result holds for all f in the set
S :“ tfPL2 : lim
xÑ0
|fpxq|“8u .
Deﬁne
gtpξq “ sinpt|ξ|q
|ξ| fpξq,
then we see that
upx,tq “
ż
R2
eix¨ξgtpξqdξ “ ˆgtpxq.
Therefore by Plancherel we have
||up¨,tq||2
L2 “ ||ˆgt||2
L2 “ ||gt||2
L2 “
ż ˆsinpt|ξ|q
|ξ|
˙2
|fpξq|2dξ ě
ż
Bp0,π{p2tqq
ˆsinpt|ξ|q
|ξ|
˙2
|fpξq|2dξ
Á
ż
Bp0,π{p2tqq
ˆt|ξ|
|ξ|
˙2
|fpξq|2dξ “ t2
ż
Bp0,π{p2tqq
|fpξq|2dξ
ě t2¨λ2pBp0,π{p2tqqq¨ min
|ξ|“π{p2tq
|fpξq|2 Á min
|ξ|“π{p2tq
|fpξq|2,
which goes to 8 as tÑ8 for fPS.
Now we need to show S is dense in L2. Fix f P L2, ϵ ą 0. Let gpxq “ |x|´1{2¨χBp0,1qpxq PL2pR2q.
Pick a continuous function φ with||f´φ||L2ăϵ and let h“φ`ϵg. It’s clear that hPS and we have
||f´h||L2 ď ||f´φ||L2`||ϵg||L2 ď ϵp1`||g||L2q.
So S is dense in L2.
Problem 6. Suppose that tφnu is an orthonormal system of continuous functions in L2pr0, 1sq and let
S be the closure of the span of tφnu. If supfPSzt0u
||f||L8
||f||L2
is ﬁnite, prove that S is ﬁnite dimensional.
Solution. We considerS as a subspace ofL2pr0, 1sq equipped with the L2 norm onr0, 1s. The sup condition
on S tells us that there exists a constant M such that for any f P S, ||f||L8 ď M||f||L2. For a ﬁxed
xPr 0, 1s, note that the map fÞÑfpxq is a linear functional on S and that
|fpxq| ď ||f||L8 ď M||f||L2,
which shows that this is in fact a bounded linear functional on S. Since S is a closed subspace of the Hilbert
space L2pr0, 1sq, S is also a Hilbert space by itself, and thus by the Riesz representation theorem we know
that there exists a function gxPS such that fpxq“x f,gxy for all fPS. Moreover, notice that
||gx||2
L2 “ xgx,gxy “ |gxpxq| ď ||gx||L8 ď M||gx||L2,
which implies that ||gx||L2ďM for each xPr 0, 1s.
Now lettf1,...,f Nu be any orthonormal set in S. By Bessel’s inequality, for each xPr 0, 1s we have
M2 ě ||gx||2
L2 ě
Nÿ
n“1
|xfn,gxy|2 “
Nÿ
n“1
|fnpxq|2.
Integrating both sides from 0 to 1 we obtain
M2 ě
Nÿ
n“1
ż 1
0
|fnpxq|2dx “
Nÿ
n“1
||fn||2
L2 “ N.
98

This shows that any orthonormal set in S can contain no more than M2 elements, which implies that
dimpSqď M2.
Problem 7. Determine ż8
0
xa´1
x`z dx
for 0ăaă 1 and Repzqą 0.
Solution. Pick the branch of log with the positive real axis cut out and integrate
fpwq :“ wa´1
w`z “ expppa´ 1q logpwqq
w`z
along a “Pac-Man” contour with a circle of radius ϵ around 0, a large semicircle of radius R, and an angle of
α away from the positive real axis. The integrals over the circles go to 0 in the limit and the two integrals
along the straight paths combine in the limit as αÑ 0 to give
p1´ expp2πiaqq
ż8
0
ta´1
t`z dt.
Then calculate the residue at w“´ z, it’s equal to p´zqa´1 (this is well-deﬁned because since Re pzqą 0,
´z does not lie on the positive real axis). So we conclude that the answer is
ż8
0
ta´1
t`z dt “ 2πip´zqa´1
1´ expp2πiaq.
Problem 8. Let fn : H Ñ H be a sequence of holomorphic functions. Show that unless |fn| Ñ 8
uniformly on compact subsets of H, there exists a subsequence converging uniformly on compact subsets of
H.
Solution. By Marty’s Theorem, we know that the family tfnu is either a normal family or tends uni-
formly to 8 on every compact set if and only if the spherical derivatives
ρnpzq “ |f1
npzq|
1`|fnpzq|2
are uniformly bounded on every compact set. So suppose that fn does not tend uniformly to 8 on every
compact set. Then if we show that tfnu is a normal family, it implies that tfnu has a subsequence that
converges uniformly on all compact sets. So it suﬃces to show that the quantites ρnpzq above are uniformly
bounded on compact sets.
Deﬁne
gnpzq “ fnpzq´ i
fnpzq` i.
Then each gn is a holomorphic function HÑ D. In particular, the family tgnu is uniformly bounded on all
of H, so tgnu is a normal family. Thus we know that the quantities
|g1
npzq|
1`|gnpzq|2
are uniformly bounded on compact subsets of H. Now we have the calculation
|g1
npzq|
1`|gnpzq|2 “
4 |f1
npzq|2
|fnpzq`i|2
1` |fnpzq´i|2
|fnpzq`i|2
“ 4|f1
npzq|2
|fnpzq` i|2`|fnpzq´ i|2 “ 2¨ |f1
npzq|
1`|fnpzq|2 “ 2ρnpzq.
99

This shows that ρnpzq must also be uniformly bounded on compact subsets of H and thustfnu is a normal
family, so we are done.
Alternate solution. Without using Marty’s theorem (it’s not such a standard result).
Letgn be deﬁned as in the ﬁrst solution, so that gn : HÑ D is holomorphic. Fix a compact set KĎ H. The
gn are uniformly bounded, so there is a subsequence gnk converging uniformly to another function g on K.
Let vk“gnk. First suppose that g‰ 1 anywhere on K. Then, since gpKq is compact (g is continuous as a
local uniform limit of continuous functions), |gpzq´ 1| is bounded away from 0 for zPK. Therefore, letting
f “ ´ipg` 1q
pg´ 1q ,
we have for any zPK
|fnkpzq´ fpzq| “
⏐⏐⏐⏐
vkpzq` 1
vkpzq´ 1´ gpzq` 1
gpzq´ 1
⏐⏐⏐⏐ “ 2
⏐⏐⏐⏐
vkpzq´ gpzq
pvkpzq´ 1qpgpzq´ 1q
⏐⏐⏐⏐ À 2 |vkpzq´ gpzq|,
which shows that fnk Ñ f uniformly on K. This is the “subsequence converging uniformly on compact
subsets of H” part of the problem.
On the other hand, now assume that gpz0q “1 for some z0 P K. We want to show that in fact g is
identically 1 andvkÑ 1 uniformly onK. Fix a conformal mapT : DÑ H withTp0q“ z0 and lethk“vk˝T .
Let
ψkpzq “ z`hkp0q
1`hkp0q
be an automorphism of D taking 0 to hkp0q. Let uk “ ψ´1
k ˝hk so that we have hk “ ψk˝uk where
uk : DÑ D is holomorphic and satisﬁes ukp0q“ 0. Since T is conformal, to show vkÑ 1 locally uniformly
it is enough to show hk Ñ 1 locally uniformly. It’s enough to show hk Ñ 1 uniformly on the closed ball
Bp0,rq for 0ără 1. By the Schwarz lemma, we have unpBp0,rqqĎ Bp0,rq, so to show hkÑ 1 uniformly
onBp0,rq it’s enough to showψkÑ 1 uniformly on Bp0,rq. This is true because for any zPBp0,rq we have
|ψkpzq´ hkp0q| “ |z|
|1`hkp0qz|
p1´|hnp0q|2q ď 2r
1´rp1´|hnp0q|2q
which tends to 0 uniformly for zPBp0,rq. So we have shown hkÑ 1 locally uniformly on D, which shows
vkÑ 1 locally uniformly. It then follows that
fnk “ p´iqpvk` 1q
vk´ 1
tends locally uniformly to 8.
So far we’ve only shown that a subsequence of the fn tends locally uniformly to 8. But the argument
above can be applied to any subsequence of the fn to conclude that any subsequence of the fn has a further
subsequence converging locally uniformly to 8, which implies that fnÑ8 locally uniformly.
Problem 9. Let f : CÑ C be entire and assume that |fpzq|“ 1 when |z|“ 1. Show that fpzq“ Czm for
some integer mą 0 and CP C with|C|“ 1.
Solution. We know that f is not identically zero, so the zeros of f are isolated and thus f has only
ﬁnitely many zeros inside D. Denote them by a1,...,a n, where each root is listed as many times as its
multiplicity. Deﬁne
Bpzq :“
nź
j“1
z´aj
1´ajz.
Notice that B is a function which is analytic in D, has exactly the same zeros as f in D, and satisﬁes
|Bpzq|“ 1 for all|z|“ 1. Thus f{B andB{f are two nonvanishing analytic functions in D which have mod-
ulus 1 on BD. By the maximum modulus principle, we conclude that |B{f|ď 1 and |f{B|ď 1 throughout
100

D, which implies that |f{B|“ 1 throughout D, which by the open mapping theorem implies that f{B must
be equal to a constant C with|C|“ 1 on all of D.
So we can write
fpzq “ CBpzq “ C
nź
j“1
z´aj
1´ajz
for all z P D. Since f is entire, by the uniqueness of analytic continuations we know that B must also be
entire. But notice that if any aj is nonzero, then B has a pole at aj, which would be a contradiction. So we
must have all aj “ 0 and thus Bpzq“ zm for some integer m. Since we know fpzq“ CBpzq“ Czm for all
zP D, since both sides are entire functions this implies that fpzq“ Czm for all zP C.
Alternate solution. This solution is basically just a worse version of the ﬁrst one, but it uses the re-
ﬂection principle so it’s cool.
The fact that |f|“ 1 on the unit circle essentially allows us to use the reﬂection principle. But we need to
get rid of the roots at 0 ﬁrst. More concretely:
Letm be the order of vanishing of f at 0 and let gpzq“ z´mfpzq. Then g is entire,gp0q‰ 0, and we still
have|gpzq|“ 1 for all |z|“ 1. We can write this as 1 “ gpzqgpzq “ gpzqgp1{zq for|z|“ 1. The function
zÞÑ 1
gp1{zq is analytic in a neighborhood of the unit circle (because gp1{zq does not vanish on the unit circle)
and agrees with g on the unit circle. Therefore since the unit circle has a limit point, by uniqueness of
analytic continuation we have
gpzq“ 1
gp1{zq
for all z‰ 0.
TakingzÑ8 , we see that lim zÑ8gpzq “ 1{gp0qă8 because g does not vanish at 0. So g is bounded,
but it’s not necessarily entire because zeros of g inside D reﬂect to poles outside of D. Let a1,...,a m be the
zeros of g inside D, counted with multiplicity. Then
zÞÑgpzqpz´ 1{a1q¨¨¨p z´ 1{anq
pz´a1q¨¨¨p z´anq
is bounded and entire, so it must be a constant. Therefore we conclude
fpzq“ Czm pz´a1q¨¨¨p z´anq
pz´ 1{a1q¨¨¨p z´ 1{anq,
but since f is entire, it can’t have any of those poles, so it also can’t have any of the corresponding zeros, so
fpzq“ Czm.
Problem 10. Does there exist a functionfpzq holomorphic in the disk|z|ă 1 such that lim|z|Ñ1|fpzq|“8 ?
Either ﬁnd one or prove that none exist.
Solution. No such function exists. Suppose f had that property. Then in particular f is not identi-
cally zero, so f has only ﬁnitely many zeros r1,...,r n P D (where roots are listed as many times as their
multiplicity). Let gpzq“ fpzq{pz´r1q¨¨¨p z´rnq. Then g is a function which is holomorphic and nonva-
nishing in D, and since pz´r1q¨¨¨p z´rnq does not tend to 8 as |z| Ñ1, we still have that |gpzq| Ñ 8
as|z|Ñ 1. Since g is nonvanishing, 1{g is also holomorphic in D and |1{gpzq|Ñ 0 as |z|Ñ 1. But apply-
ing the maximum principle to 1 {g, we see that |1{g| can’t have any local maximum inside D, and since it
extends continuously to be identically zero on BD, this implies that 1 {g must be identically zero on all of
D, which is a contradiction becauseg is a holomorphic function on D. Thus no such functionf can exist.
Problem 11. Assume that fpzq is holomorphic on |z|ă 2. Show that
max
|z|“1
⏐⏐⏐⏐fpzq´ 1
z
⏐⏐⏐⏐ ě 1.
101

Solution. Let M be the max in question, and let γ be the counterclockwise contour around the unit
circle. By the ML inequality ˇˇˇˇ
ż
γ
fpzq´ 1
z dz
ˇˇˇˇď 2πM.
On the other hand, ż
γ
fpzq´ 1
z dz“ 0´ 2πi“´ 2πi.
Therefore 2πď 2πM, hence the result.
Alternate solution. I think these two solutions are essentially equivalent but this one feels less like a
trick.
Suppose instead that |fpzq´ 1{z| ă 1 for all |z| “ 1. Let C be the unit circle. The idea is that the
image of C under 1{z has winding number´1 around the origin, and if fpzq is always less than 1 away from
1{z, then f should also wind C around the origin ´1 times, which is bad.
By assumption we have |zfpzq´ 1|ă| z|“ 1 for all zPC. So the image of C under zfpzq is contained
in Bp1, 1q, which implies it has winding number 0 around the origin. Therefore by the argument principle,
zfpzq has no zeros inside D, which is impossible if f is analytic. Alternatively, one can apply Rouche’s
theorem to the inequality |zfpzq´ 1|ă| z|“ 1 to conclude that zfpzq has the same number of zeros in D as
the constant function 1, which is zero (the ﬁrst argument given here is essentially just a proof of Rouche’s
theorem).
Problem 12a. Find a real-valued harmonic function v deﬁned on the disk |z| ă1 such that vpzq ą0
and limzÑ1vpzq“8 .
Solution. Deﬁne vpzq “log
⏐⏐⏐z`1
z´1´ 1
⏐⏐⏐. It is clear that vpzq Ñ 8as z Ñ 1. To see that v is harmonic
in D, note that the map zÞÑ z`1
z´1´ 1 is nonvanishing on D, so zÞÑ log
´
z`1
z´1´ 1
¯
is a well-deﬁned analytic
function on D, and vpzq“ Re
´
log
´
z`1
z´1´ 1
¯¯
, so v is harmonic in D. To show that vpzqą 0 on D, note
that zÞÑ z´1
z`1´ 1 is a conformal map from D totzP C : Impzqă´ 1u, so
⏐⏐⏐z´1
z`1´ 1
⏐⏐⏐ą 1 for all zP D and
thusvpzqą 0.
“Alternate” Solution Simply deﬁne vpzq“´ log
⏐⏐z´1
2
⏐⏐. On the disc, z´1
2 is nonzero and holomorphic, so
vpzq is harmonic. It is also non-negative since z´1
2 ă 1 for |z|ă 1. The blowup near 1 is clear.
Problem 12b. Let u be a real-valued harmonic function in the disk |z| ă1 such that upzq ďM ă 8
and limrÑ1upreiθqď 0 for almost all θ. Show that upzqď 0.
Solution. For any 0 ă r ă 1, u is harmonic on the closed disk |z| ďr. So for any 0 ă s ă 1, we
can use the Poisson integral formula to write
uprseiθq “ 1
2π
ż 2π
0
r2´prsq2
|reiφ´rseiθ|2upreiφqdφ. (2)
For a ﬁxed s and θ, deﬁne
grpφq “ r2´prsq2
|reiφ´rseiθ|2upreiφq.
We see thatgr is bounded onr0, 2πs because uďM on all of D by hypothesis and|reiφ´rseiθ|2 is bounded
away from 0 because s ă 1. So say that |grpφq| ďA for all φ P r0, 2πs. Therefore we can apply Fatou’s
102

lemma to the functions A´grpφq to get
ż 2π
0
lim inf
rÑ1
pA´grpφqqdφ ď lim inf
rÑ1
ż 2π
0
pA´grpφqqdφ,
which implies that ż 2π
0
lim sup
rÑ1
grpφqdφ ě lim sup
rÑ1
ż 2π
0
grpφqdφ.
So taking the lim sup as rÑ 1 on both sides of equation (1) yields, since u is continuous on D,
upseiθq “ lim sup
rÑ1
uprseiθq “ lim sup
rÑ1
ż 2π
0
grpφqdφ ď
ż 2π
0
lim sup
rÑ1
grpφqdφ “
ż 2π
0
1´s2
|eiφ´seiθ|2 lim sup
rÑ1
upreiφqdφ.
By hypothesis, the integral on the far right is an integral of a function which is ď 0 almost everywhere, so
we haveupseiθqď 0. This argument holds for any 0 ăsă 1 and any θPr 0, 2πs, so we conclude that uď 0
on D.
103

16 Fall 2016
Problem 1. We consider the space L1pµq of integrable functions on a measure space pX, M,µq. For
fPL1pµq let
||g||1“
ż
|gpxq|dµ
be the corresponding L1-norm. Suppose that f and fn for nP N are functions in L1pµq such that
(i) fnpxqÑ fpxq for µ-almost every xPX and
(ii) ||fn||1Ñ||f||1.
Show that then ||fn´f||1Ñ 0.
Solution. Note that the function |f|`| fn|´| f ´fn| is nonnegative for all n (this just follows from
the triangle inequality). Then we apply Fatou’s lemma to get
ż
lim inf
nÑ8
p|f|`| fn|´| f´fn|qdµ ď lim inf
nÑ8
ż
p|f|`| fn|´| f´fn|qdµ.
Since fnÑf pointwise almost everywhere, the left side of the above inequality reduces to
2
ż
|f|dµ.
Since||fn||L1Ñ||f||L1 as nÑ8 , the right side reduces to
2
ż
|f|dµ´ lim sup
nÑ8
ż
|f´fn|dµ.
Together these imply that
lim sup
nÑ8
ż
|f´fn|dµ ď 0,
which implies that ||f´fn||L1Ñ 0 as nÑ8 .
Problem 2. Let µ be a ﬁnite positive Borel measure on R that is singular to the Lebesgue measure.
Show that
lim
rÑ0`
µprx´r,x`rsq
2r “`8
for µ-almost every xP R.
Solution. Let λ be Lebesgue measure on R. It suﬃces to show that
lim
rÑ0`
λprx´r,x`rsq
µprx´r,x`rsq “ 0
for µ-almost every xP R. Since λ and µ are singular, write R“AYAc where λpAq“ 0 and µpAcq“ 0. It
suﬃces to just look at xPA because µpAcq“ 0. Deﬁne
Ek “
"
xPA : lim sup
rÑ0`
λprx´r,x`rsq
µprx´r,x`rsq ą 1
k
*
.
To prove the desired result it suﬃces to show that µpEkq“ 0 for each ﬁxed k. Fix ϵą 0. By the regularity
of Lebesgue measure, let V be an open set with EkĎV andλpVqă ϵ. By deﬁnition of Ek, for each xPEk
there is an open interval Ipxq“p x´rpxq,r `rpxqq such that
λpIpxqq
µpIpxqq ě λprx´rpxq,x `rpxqsq
µprx´rpxq,x `rpxqsq ą 1
k,
104

and rpxq may be chosen small enough so that IpxqĎ V for each x. Then Ť
xPEk
p1{5qIpxq is a covering of
Ek by open intervals, so by the Vitali covering lemma, we can pick a countable subcollection tp1{5qIpxnqu
which is pairwise disjoint and satisﬁes
Ek Ď
ď
xPEk
p1{5qIpxq Ď
8ď
n“1
Ipxnq.
Therefore we have the estimate
µpEkq ď
8ÿ
n“1
µpIpxnqq ď k
8ÿ
n“1
λpIpxnqq “ kλ
˜ 8ď
n“1
Ipxnq
¸
ď kλpVq ă kϵ.
Since µpEkq is independent of ϵ, we may take ϵÑ 0 and conclude that µpEkq“ 0, so we are done.
Problem 3a. If X is a compact metric space, we denote by PpXq the set of all positive Borel mea-
sures µ on X with µpXq“ 1. Let φ : X Ñr 0,8s be lower semicontinuous function on X. Show that if µ
and µn are in PpXq and µnÑµ with respect to the weak-star topology on PpXq, then
ż
φdµ ď lim inf
nÑ8
ż
φdµn.
Solution. Since φ is lower semicontinuous, we can write it as a monotonically increasing limit of con-
tinuous functions, and since φě 0 we may also take these continuous functions to be nonnegative. So say
that 0 ď fk Õ φ as k Ñ 8. Then, by deﬁnition of weak- ˚ convergence of measures and applying the
Monotone Convergence Theorem twice, we have
ż
φdµ “ lim
kÑ8
ż
fkdµ “ lim
kÑ8
lim
nÑ8
ż
fkdµn ď lim inf
nÑ8
lim
kÑ8
ż
fkdµn “ lim inf
nÑ8
ż
φdµn.
The interchange of the limits with the inequality is justiﬁed by the following statement:
Let tan,ku8
n,k“1 be nonnegative numbers such that lim nÑ8an,k and limkÑ8an,k both exist for each ﬁxed
k and n respectively, limkÑ8 limnÑ8an,k exists, and for each ﬁxed n, an,k is increasing in k. Then
limkÑ8 limnÑ8an,kď lim infnÑ8 limkÑ8an,k.
Proof: Deﬁne
bn :“ lim
kÑ8
an,k ck :“ lim
nÑ8
an,k L :“ lim
kÑ8
ck.
Fix ϵą 0. Let K be big enough so that cK ą L´ϵ. By the increasing condition, we have bn ě an,K for
eachn. Therefore
lim inf
nÑ8
bn ě lim inf
nÑ8
an,K “ cK ą L´ϵ.
Since lim infnÑ8bn does not depend on ϵ, we conclude that lim infnÑ8bněL.
Problem 3b. Let KĎ Rd be a compact set. For µP PpKq, deﬁne
Epµq “
ż
K
ż
K
1
|x´y|dµpxqdµpyq.
Show that the function E : PpKqÑr 0,8s attains its minimum on PpKq (which could possibly be inﬁnity).
Solution. See Spring 2013 # 4
Problem 4. Let L1 “ L1pr0, 1sq be the space of integrable functions and L2 “ L2pr0, 1sq be the space
105

of square-integrable functions on r0, 1s. Then L2ĂL1. Show that L2 is a meager subset of L1., i.e., L2 can
be written as a countable union of sets in L1 that are closed and have empty interior in L1.
Solution. Write
L2 “
8ď
N“1
"
fPL1 :
ż 1
0
|f|2ďN
*
“: EN.
To show thatL2 is a meager subset of L1, it suﬃces to show that each EN is closed and nowhere dense with
respect to the L1 norm. To show EN is closed, let fk be a sequence in EN and suppose that fkÑf in the
L1 norm. This implies that a subsequence converges to f almost everywhere, so by relabeling if necessary
we may just assume that fkÑf almost everywhere, so also |fk|2Ñ|f|2 almost everywhere. Therefore by
Fatou’s lemma we have
ż 1
0
|f|2 “
ż 1
0
lim inf
kÑ8
|fk|2 “ lim inf
kÑ8
ż 1
0
|fk|2 ď N,
so fPEN. Thus EN is closed.
To show EN is nowhere dense, ﬁx f P EN and ϵ ą 0. It suﬃces to ﬁnd a function g such that g R EN
and||g´f||L1ăϵ. Deﬁne gpxq“ fpxq` ϵx´1{2. It is clear that gREN because if g were in L2, then x´1{2
would also be, which is a contradiction. It is also clear that
||g´f||L1 “ ϵ
ż 1
0
x´1{2dx “ 2ϵ,
so we are done.
Problem 5. Let X“Cpr0, 1sq be the Banach space of real valued continuous functions on r0, 1s equipped
with the sup norm. Let A be the Borel σ-algebra on X. Show that A is the smallest σ-algebra on X that
contains all sets of the form
Spt,Bq “ tfPX :fptqP Bu
for tPr 0, 1s and B a Borel subset of R.
Solution. First we show that each set of the form Spt,Bq is actually a Borel set in X. Note that for
each t, the evaluation map φt : X Ñ R given by f ÞÑ fptq is a bounded linear functional on X because
|fptq| ď ||f||X. Therefore φt is a continuous function X Ñ R, and since Spt,Bq “φ´1
t pBq where B is a
Borel set in R, we see that Spt,Bq must be a Borel set in X.
Let F denote the σ-algebra generated by the sets of the form Spt,Bq. To show that F “ A, it suﬃces
to show that every closed neighborhood in X is in F. So ﬁx g P X and ϵ ą 0. We need to show that
E :“tf PX :||f´g||X ďϵu is an element of F. For any qP QXr 0, 1s, deﬁne Bq :“ rgpqq´ ϵ,gpqq` ϵs.
It is clear that Bq is a Borel subset of R. Now we claim that
E “
č
qPQXr0,1s
Spq,Bqq.
Proving this is enough to conclude that E is an element of F, so this will ﬁnish the problem.
If f P E, then ||f´g||X ď ϵ, so in particular |fpqq´ gpqq| ďϵ for every q P QXr 0, 1s, which implies
that fpqq PBq for every q, so f is an element of the set on the right side of the above equation. Con-
versely, let f be an element of the right side and suppose that f R E. Then we have |fpxq´ gpxq| ąϵ
for some x P r0, 1s, and since f and g are both continuous, we can ﬁnd a rational number q near x such
that |fpqq´ gpqq| ąϵ, which contradicts the assumption that f P Spq,Bqq. Therefore we conclude that
E “ Ş
qPQXr0,1sSpq,BqqP F, so we are done.
106

Problem 6a. Consider the Banach space 𝓁1 consisting of all sequences u“txiu in R with
||u||𝓁1 “
8ÿ
i“1
|xi| ă 8
and the Banach space 𝓁8 consisting of all sequences v“tyiu in R with
||v||𝓁8 “ sup
iPN
|yi| ă 8.
There is a well-deﬁned dual pairing between 𝓁1 and 𝓁8 given by
xu,vy “
8ÿ
i“1
xiyi
for u“txiuP 𝓁1 and v“tyiuP 𝓁8. With this dual pairing, 𝓁8“p𝓁1q˚ is the dual space of 𝓁1.
Show that there exists no sequence tunu in 𝓁1 such that ||un||𝓁1 ě 1 for all n andxun,vyÑ 0 for each
vP𝓁8.
Solution. Let tunu be a sequence in 𝓁1 satisfying ||un||𝓁1 ě 1 for all n. We can assume by scaling that
||un||𝓁1“ 1 for eachn because scaling the sequences down can only decrease xun,vy for anyvP𝓁8. Suppose
thatxun,vyÑ 0 as nÑ8 for all v P 𝓁8. We will get a contradiction by constructing a sequence v P 𝓁8
such thatxun,vy is bounded away from zero inﬁnitely often.
First note that by letting v be the sequence which has a 1 in the jth spot and 0 everywhere else, we
know that punqj Ñ 0 as nÑ8 for each ﬁxed j. Also note that since ||un||𝓁1 “ 1 for each n, necessarily
||un||𝓁8ď 1 for all n. Now, for any ﬁxed ϵPp 0, 1{2q, we can do the following construction:
PickJ1 to be large enough so that ÿ
jPr1,J1s
|pu1qj| ą 1´ϵ.
Now, since we know that punqj tends to zero in each slot individually, pick N1 to be large enough so that
maxp|puN1q1|,..., |puN1qJ1|q ă ϵ
2J1
.
Then we see that ÿ
jPr1,J1s
|puN1qj| ă ϵ{2,
so we may pick J2 such that ÿ
jPrJ1`1,J2s
|puN1qj| ą 1´ϵ.
Now pick N2 to be large enough so that
maxp|puN2q1|,..., |puN2qJ2|q ă ϵ
2J2
.
We may repeat this process indeﬁnitely, and so we obtain a sequence tNku and a sequence tJku such that
for each k ÿ
jPrJk`1,Jk`1s
|puNkqj| ą 1´ϵ.
Now, letting spxq denote the function which is 1 if xě 0 and ´1 if xă 0, deﬁne the sequence vP𝓁8 by
pvqj “ sppuNkqjq when jPrJk` 1,Jk`1s.
107

Note that each pvqj is an entry of some un, so we have ||v||𝓁8ď 1. By construction, for each k we have
ÿ
jPrJk`1,Jk`1s
puNkqjpvqj “
ÿ
jPrJk`1,Jk`1s
|puNkqj| ą 1´ϵ,
so
xuNk,vy “
ÿ
jPrJk`1,Jk`1s
puNkqjpvqj`
ÿ
jRrJk`1,Jk`1s
puNkqjpvqj ě 1´ϵ´||v||𝓁8
ÿ
jRrJk`1,Jk`1s
|puNkqj| ą 1´2ϵ.
Therefore, picking (for example) ϵ“ 1{3, we see that xuNk,vy is bounded away from zero for every k, which
is our contradiction. (Note: I would really prefer a nicer, non-constructive solution)
Problem 6b. Show that every weakly convergent sequence tunu in 𝓁1 converges in the norm topology
of 𝓁1.
Solution. Suppose that un Ñ u weakly in 𝓁1. This means that φpunq Ñφpuq for every bounded lin-
ear functional φPp 𝓁1q˚, and by the given dual pairing this means that xun,vyÑx u,vy for every v P 𝓁8,
i.e. xun´u,vy Ñ0 for every v P 𝓁8. Suppose that un did not converge to u in the norm topology on
𝓁1. Then there is a subsequence unk and a δ ą 0 such that ||unk´u||𝓁1 ě δ for all k. Replacing unk´u
with p1{δqpunk´uq if necessary, we may assume that ||unk´u||𝓁1 ě 1 for all k. But we still must have
xunk´u,vyÑ 0 for every vP𝓁8, which contradicts part (a). Therefore we must have unÑu in the norm
topology on 𝓁1.
Problem 7a. Let H be the space of holomorphic functions f on D such that
ż
D
|fpzq|2dApzq ă 8.
Here integration is with respect to Lebesgue measure A on D. The vector space H is a Hilbert space if
equipped with the inner product
xf,gy “
ż
D
fpzqgpzqdApzq
for f,g P H. Fix z0P D and deﬁne Lz0pfq“ fpz0q for fP H.
Show that Lz0 : HÑ C is a bounded linear functional on H.
Solution. It’s obvious that Lz0 is a linear functional. For z0 ﬁxed, let δ ą 0 be small enough so that
Bpz0,δqĎ D. Then for any fP H, we have by the mean value formula
|Lz0pfq| “ |fpz0q| “
⏐⏐⏐⏐⏐
1
πδ2
ż
Bpz0,δq
fpzqdApzq
⏐⏐⏐⏐⏐ ď 1
πδ2
ż
Bpz0,δq
|fpzq|dApzq ď 1
πδ2
ż
D
|fpzq|dApzq
ď 1
πδ2
ˆż
D
12dApzq
˙1{2ˆż
D
|fpzq|2dApzq
˙1{2
by Cauchy-Schwarz
ď 1?πδ2||f||H,
so Lz0 is a bounded linear functional.
Problem 7b. Find an explicit function gz0P H such that
Lz0pfq “ fpz0q “ xf,gz0y
for all fP H.
108

Solution. Note that such a gz0 exists for each z0 P D by the Riesz representation theorem. First we
claim that the set #
enpzq :“
c
n` 1
π zn
+
is an orthonormal basis for H. It’s easy to compute directly using polar coordinates that it’s an orthonormal
set. To show it’s a basis, it’s enough to show that xf,eny“ 0 for all n implies f“ 0. We compute
xf,eny “ Cpnq
ż
D
fpzqzndApzq “ Cpnq
ż 1
0
ż 2π
0
fpreiθqrn`1e´inθdθdr.
The Cauchy integral formula gives
fpnqp0q “ Cpnq
ż 2π
0
fpreiθq
rn`1eipn`1qθreiθdθ.
Combining these two we can observe that
xf,eny “ Cpnq
ż 1
0
r2n`1fpnqp0qdr “ Cpnqfpnqp0q.
(Cpnq is a constant in terms of n that is diﬀerent from line to line). This implies that xf,eny“ 0 implies
fpnqp0q “0. Therefore because holomorphic functions have power series expansions, xf,eny “0 for all n
implies f“ 0. This shows that the en form an orthonormal basis for H.
Now we determine gz0. For zP D we have
gz0pzq “ xgz0,gzy “
8ÿ
n“0
xgz0,enyxgz,eny by Parseval
“
8ÿ
n“0
xen,gz0yxen,gzy “
8ÿ
n“0
enpz0qenpzq
“
8ÿ
n“0
n` 1
π pz0zqn “ 1
πp1´z0zq2.
Problem 8a. Letf be a continuous complex-valued function on D which is holomorphic on D andfp0q‰ 0.
Show that if 0 ără 1 and inf|z|“r|fpzq|ą 0, then
1
2π
ż 2π
0
log
⏐⏐fpreiθq
⏐⏐ dθ ě log |fp0q|.
Solution. Let r be such that inf |z|“r|fpzq|ą 0. Since f is not identically zero, it has only ﬁnitely many
zeros inside the disc |z|ă r. Denote them by a1,...,a n. Deﬁne the function
gpzq “
ˆrpz´a1q
r2´a1z
˙
¨¨¨
ˆrpz´anq
r2´anz
˙
.
We know that |gpzq|“ 1 for all |z|“ r and g has the same zeros as f and no poles in |z|ď r. Therefore
the function f{g is a nonvanishing holomorphic function on |z| ăr with |fpzq{gpzq| “ |fpzq| for |z| “r.
Since it is nonvanishing we know that it has a holomorphic single-valued logarithm, so log |fpzq{gpzq| “
Replogpfpzq{gpzqqq is harmonic in |z|ă r. Therefore we can apply the mean value property to log |f{g| to
obtain
log
⏐⏐⏐⏐
fp0q
gp0q
⏐⏐⏐⏐ “ 1
2π
ż 2π
0
log
⏐⏐⏐⏐
fpreiθq
gpreiθq
⏐⏐⏐⏐ dθ “ 1
2π
ż 2π
0
log
⏐⏐fpreiθq
⏐⏐ dθ.
109

We compute
log
⏐⏐⏐⏐
fp0q
gp0q
⏐⏐⏐⏐ “ log|fp0q|´
nÿ
j“1
log
⏐⏐⏐aj
r
⏐⏐⏐.
Since each|aj|ă r, we have log|aj{r|ă 0 and therefore
log|fp0q| ď 1
2π
ż 2π
0
log
⏐⏐fpreiθq
⏐⏐ dθ.
Problem 8b. Show that
⏐⏐tθPr 0, 2πs :fpeiθq“ 0u
⏐⏐“ 0, where |E| denotes the Lebesgue measure of E.
Solution. Let E “ tθ P r0, 2πs : fpeiθq “ 0u. Suppose that |E| ą 0. Since D is compact, we know
that f is uniformly continuous on D. Fix ϵ ą 0. Then we know that there is some rϵ ą 0 such that
|fprϵeiθq|ă ϵ for every θPE. We can also say |f|ď M on D. Now we have the following estimate:
ż 2π
0
log
⏐⏐fprϵeiθq
⏐⏐ dθ “
ż
E
log
⏐⏐fprϵeiθq
⏐⏐ dθ`
ż
Ec
log
⏐⏐fprϵeiθq
⏐⏐ dθ ď |E| logpϵq` 2π logpMq.
But since fp0q‰ 0, we can pick ϵą 0 small enough so that the right side above is smaller than 2 π log|fp0q|,
but part (a) says that we must have
ş2π
0 log
⏐⏐fpreiθq
⏐⏐ dθě 2π log|fp0q| for any rą 0, so this is a contradic-
tion.
Alternate Solution. Since f is continuous on the compact set D, we can say |f| ďM. Thus log |f|
takes values in r´8,Ms. Let grpθq“ M´ log|fpreiθq|. Then each gr for 0 ără 1 takes values in r0,8s,
so we can apply Fatou’s lemma:
ż 2π
0
lim inf
rÑ1
grpθqdθ ď lim inf
rÑ1
ż 2π
0
grpθqdθ
2πM´
ż 2π
0
lim sup
rÑ1
log|fpreiθq|dθ ď 2πM´ lim sup
rÑ1
ż 2π
0
log|fpreiθq|dθ
ż 2π
0
log|fpeiθq|dθ ě lim sup
rÑ1
ż 2π
0
log|fpreiθq|dθ ě 2π log|fp0q| ą ´8
by part (a). But if E had positive measure, then the integral on the left side would be ´8, a contradiction.
Problem 9a. Let µ be a positive Borel measure on r0, 1s with µpr0, 1sq “ 1. Show that the function
f deﬁned as
fpzq“
ż
r0,1s
eiztdµptq
for zP C is holomorphic on C.
Solution. ForhkP C with|hk|Ñ 0 we have
1
hpfpz`hkq´ fpzqq“
ż
r0,1s
eizt¨ eihkt´ 1
hk
dµptq
Notice that
lim
kÑ8
eihkt´ 1
hk
“
ˆ d
dzeitz
˙
p0q“ it.
Thus for ﬁxed z, the magnitude of the integrand is bounded by 2 suptPr0,1s|eizt|ă8 fork large enough. By
dominated convergence, we have
f1pzq“
ż
r0,1s
iteiztdµptq.
110

Note that all functions in question are continuous, and hence Borel measurable, so applying dominated
convergence was justiﬁed.
Alternate solution. We are motivated by the fact that if f is holomorphic it should have f1pzq “ş1
0iteiztdµptq. We estimate, for a ﬁxed z,
⏐⏐⏐⏐
1
hpfpz`hq´ fpzqq´
ż 1
0
iteiztdµptq
⏐⏐⏐⏐ “
⏐⏐⏐⏐
1
h
ż 1
0
peipz`hqt´eizt´ihteiztqdµptq
⏐⏐⏐⏐
ď 1
|h|
ż 1
0
⏐⏐eizt⏐⏐ ⏐⏐eiht´p 1`ihtq
⏐⏐ dµptq.
We can pick|h| to be small enough so that
⏐⏐eiht´p 1`ihtq
⏐⏐ďC |iht|2“Ct2|h|2 for some absolute constant
C. Then we have
⏐⏐⏐⏐
1
hpfpz`hq´ fpzqq´
ż 1
0
iteiztdµptq
⏐⏐⏐⏐ ď 1
|h|C|h|2
ż 1
0
pe|z|qtt2dµptq ď Ce|z||h|
ż 1
0
dµptq “ Ce|z||h|,
which tends to 0 as |h|Ñ 0, so we conclude that f1pzq“
ş1
0iteiztdµptq.
Problem 9b. Suppose that there exists nP N such that
lim sup
|z|Ñ8
|fpzq|{|z|nă8
Show that then µ is equal to the Dirac measure δ0 at 0.
Solution. By the given condition, we have for large |z| that|fpzq|ă C|z|n for some constant C. Since f is
polynomially bounded and holomorphic, f must in fact be a polynomial.
Forz real,
|fpzq|ď
ż
r0,1s
|eizt|dµptqď 1.
But a polynomial which is bounded on the real line must be constant. Since fp0q“ 1, we havefpzq“ 1 for
all z.
For realz, we must therefore have equality in the rightmost inequality above. This occurs only if eizt is
real, outside a subset of r0, 1s with measure 0. However eizt is real only for t an integer multiple of πk{z. It
follows that the set of multiples Mz of πk{z has µ-measure 1 for all z. But Mz and M?
2z intersect only at
0, so we must have µpt0uq“ 1. (Is there a nicer way to ﬁnish oﬀ the problem?)
Alternate solution. Using the same argument from above, we know that f is a polynomial of degree
n and the derivatives of f are given by fpjqpzq“
ş1
0pitqjeiztdµptq. Since it’s a polynomial of degree n, the
pn` 1qst derivative is identically zero, so
ż 1
0
tn`1eiztdµptq “ 0
for all z P C. If µ is not a point mass at 0, then µp0, 1są 0, so by continuity, µrδ, 1są 0 for some δ ą 0.
Then taking z“´i we have
0 “
ż 1
0
tn`1etdµptq ě
ż 1
δ
tn`1etdµptq ě δn`1eδµrδ, 1s ą 0,
a contradiction.
Problem 10 a. Consider the quadratic polynomial fpzq “z2´ 1 on C. We are interested in the iter-
ates fn of f for nP N. Find an explicit constant M ą 0 such that the following dichotomy holds for each
111

point zP C: either (i) |fnpzq|Ñ8 as nÑ8 or (ii) |fnpzq|ď M for all nP N0.
Solution. We takeM“ 2. For|z|ě 2, we have
|fpzq|“| z2´ 1|
“
ˇˇˇˇz´ 1
z
ˇˇˇˇ¨|z|
ě
ˆ
|z|´ 1
|z|
˙
¨|z|
ě 3
2|z|.
Thus if |z| ě2, we have fnpzq ą2¨p 3{2qn. So if |fkpzq| is greater than 2 for some k, then |fnpzq| Ñ 8
as k Ñ 8. In particular if (i) does not hold, then (ii) must hold. It is clear that (i) and (ii) cannot hold
simultaneously.
Problem 10b. Let U be the set of all z P C for which the ﬁrst alternative (i) holds and K be the set
of all zP C for which the second alternative (ii) holds. Show that U is an open set and K is a compact set
without “holes”, i.e., CzK has no bounded connected components.
Solution. For k P N, let Uk be the set of all z P C where |fkpzq| ąM. Then Uk is the preimage of
an open set, and hence open. By part (a) we have that U is the union of the sets Uk, so U is open.
It is immediate that K is closed, since K is the complement of U. Any element z in K must satisfy
|z|ď M, so K is compact.
Suppose that S was a bounded connected component of U. By part (a) we have that fkpxqă M for all
xPK, and hence for all xPB S. But then the maximum principle implies that fkpxq is bounded by M for
all x in S. Thus (i) is not satisﬁed, and so xRU, which is a contradiction.
Problem 11 a. Supposef : CÑ C is a holomorphic function such that the functionzÞÑgpzq“ fpzqfp1{zq
is bounded on Czt0u. Show that if fp0q‰ 0, then f is constant.
Solution. Let|gpzq| be bounded by M. Since fp0q‰ 0, there is a constant mą 0 such that |fpzq|ą m on
a δ-neighborhood of 0. For |z|ă δ, we then have
Měfpzqfp1{zqě mfp1{zq.
So fp1{zq ďM{m for |z| ăδ, and hence fpzq is bounded for |z| ą1{δ. It follows that f is bounded and
therefore constant.
Problem 11 b. Show that if fp0q “ 0, then there exists n P N and a P C such that fpzq “azn for
all zP C.
Solution. Let n be the order of f’s zero at 0. Then we can write fpzq “znhpzq where h is holomor-
phic and hp0q‰ 0. Note that hpzqhp1{zq“ fpzqfp1{zq“ gpzq for z‰ 0. By part (a) hpzq“ a identically for
some constant a, and then we have fpzq“ azn.
Problem 12a. Let U Ď C be an open set and K Ď U be a compact subset of U. Prove that there
exists a bounded open set V with K Ď V Ď V Ď U such that BV consists of ﬁnitely many closed line
segments.
Solution. Since K is compact and Uc is closed, we have dist pK,U cq “δ ą 0. Tile the complex plane
with squares of side length δ{100. Let Q be the family of all squares Q such that distpQ,Kqď δ{10. This
is a ﬁnite family because K is compact and therefore bounded. Then let V be the interior of Ť
QPQQ. This
is clearly a bounded open set such that K Ď V Ď V Ď U, and BV just consists of ﬁnitely many edges of
112

squares.
Problem 12b. Let f be a holomorphic function on U. Show that there exists a sequence tRnu of ra-
tional functions such that RnÑf uniformly on K and none of the functions Rn has a pole in K.
Solution. Let the set V be as in the previous part. For any z P K, by the Cauchy integral formula
we can write
fpzq “ 1
2πi
ż
BV
fpwq
w´z dw “ 1
2πi
Nÿ
j“1
ż
γj
fpwq
w´z dw
where each γj is a straight line and they all have the same length. We parametrize each of these integrals
and write
fpzq “ 1
2πi
Nÿ
j“1
ż 1
0
fpγjptqqγ1
jptq
γjptq´ z dt
and we know that |γ1
jptq|“ c for some constant c and all j.
We want to show that the above integral can be approximated uniformly in z P K by its Riemann sums.
Fix ϵą 0. By construction of the set V , we know that |γjptq´ z| is bounded away from zero uniformly for
zP K and tPr 0, 1s, and therefore, since everything involved is continuous, we know that there is a δą 0
such that|t1´t2|ă δ implies
⏐⏐⏐⏐
fpγjpt1qqγ1
jpt1q
γjpt1q´ z ´ fpγjpt2qqγ1
jpt2q
γjpt2q´ z
⏐⏐⏐⏐ ă ϵ
for every zPK. So for each j, lett0“tj,0ătj,1ă... ătj,Mpjq“ 1u be a partition of r0, 1s with mesh size
less than δ. Then we have, for any zPK,
⏐⏐⏐⏐⏐⏐
fpzq´
Nÿ
j“1
Mpjqÿ
i“1
fpγjptj,iqqγ1
jptj,iq
γjptj,iq´ z ptj,i´tj,i´1q
⏐⏐⏐⏐⏐⏐
“
⏐⏐⏐⏐⏐⏐
Nÿ
j“1
1
2πi
ż 1
0
fpγjptqqγ1
jptq
γjptq´ z dt´
Mpjqÿ
i“1
fpγjptj,iqqγ1
jptj,iq
γjptj,iq´ z ptj,i´tj,i´1q
⏐⏐⏐⏐⏐⏐
“
⏐⏐⏐⏐⏐⏐
Nÿ
j“1
Mpjqÿ
i“1
żtj,i
tj,i´1
ˆfpγjptqqγ1
jptq
γjptq´ z ´ fpγjptj,iqqγ1
jptj,iq
γjptj,iq´ z
˙
dt
⏐⏐⏐⏐⏐⏐
ď
Nÿ
j“1
Mpjqÿ
i“1
żtj,i
tj,i´1
⏐⏐⏐⏐
fpγjptqqγ1
jptq
γjptq´ z ´ fpγjptj,iqqγ1
jptj,iq
γjptj,iq´ z
⏐⏐⏐⏐ dt ă
Nÿ
j“1
Mpjqÿ
i“1
ϵptj,i´tj,i´1q ă Nϵ.
Finally, notice that the big double sum in the ﬁrst term is exactly a rational function in z which only has
poles on the lines γj, which are all outside of K, so this gives us the desired result.
113

17 Spring 2017
Problem 1. Let KĎ R be a compact set of positive measure and let fPL8pRq. Show that the function
Fpxq “ 1
|K|
ż
K
fpx`tqdt
is uniformly continuous on R. Here |K| denotes the Lebesgue measure of K.
Solution. We calculate
|Fpxq´ Fpyq| “ 1
|K|
⏐⏐⏐⏐
ż
K
fpx`tqdt´
ż
K
fpy`tqdt
⏐⏐⏐⏐ “ 1
|K|
⏐⏐⏐⏐
ż
K´x
fptqdt´
ż
K´y
fptqdt
⏐⏐⏐⏐
ď 1
|K|
ż
pK´xq∆pK´yq
|fptq|dt ď ||f||L8
|K| λppK´xq∆pK´yqq “ ||f||L8
|K| λppK´px´yqq∆Kq
where ∆ denotes the symmetric diﬀerence of two sets and λ is Lebesgue measure.
Fixϵą 0. Let h“x´y; we want to estimate the measure ofpK´hq∆K. Since K is compact, there is a set
V which is a ﬁnite union of disjoint open intervals such that KĎV andλpVzKqă ϵ. Say V “I1Y... YIn.
We have
pK´hq∆K “ ppK´hqzKqYp KzpK´hqq
Ď ppV ´hqzVqYp VzKqYp VzpV ´hqqYpp V ´hqzpK´hqq
“ ppV ´hq∆VqYp VzKqYpp V ´hqzpK´hqq.
Since V is a ﬁnite union of disjoint open intervals, it is clear that
λppV ´hq∆Vq ď 2n|h|.
Therefore we have λppK´hq∆Kqď 2ϵ` 2n|h|. So for any x,y P R satisfying|x´y|ă ϵ
2n`2, we have
|Fpxq´ Fpyq| ă ||f||L8
|K| λppK´px´yqq∆Kq ă ||f||L8
|K| ϵ.
Since n is a parameter depending only on ϵ and the set K, this shows that F is uniformly continuous on R.
Problem 2. Let fn : r0, 1s Ñ r0,8q be a sequence of functions, each of which is non-decreasing on
the intervalr0, 1s. Suppose the sequence is uniformly bounded in L2pr0, 1sq. Show that there exists a subse-
quence that converges in L1pr0, 1sq.
Solution. Let M be a uniform upper bound for ||fn||L2. Since each fn is nondecreasing, we get the
bound 0ďfnptqď M?1´t fortPr 0, 1s. In particular note that for ﬁxed t,fnptq is restricted to a compact set.
Therefore the standard diagonalization argument allows us to construct a subsequence fnk which converges
onr0, 1sX Q.
We claim thatfnk converges pointwise a.e. as kÑ8. For a rationalq, letaq be the limit of the sequence
fnkpqq. Note that aq ď aq1 for q ă q1, since each fnk is nondecreasing. For r P R let Lr “ supqăraq and
Ur“ infq1ąraq1. Observe that the intervalspLr,Urq are all disjoint, so at most countably many of them are
nonempty. The interval is empty exactly when Lr“Ur, so this equality holds for almost every r. But when
Lr“Ur, the sequence fnkprq converges to this value. This establishes pointwise a.e. convergence.
Letf be a function on r0, 1s such thatfnkÑf pointwise a.e. We have|fnkptq´ fptq|ď M?1´t for almost
everyt. Since M?1´t lies in L1pr0, 1sq, Dominated Convergence implies that fnÑf in L1.
Note that there are no issues of measurability to worry about; an increasing function is continuous a.e.
(in fact everywhere except possibly on a countable set) and therefore measurable.
114

Problem 3. Let Cpr0, 1sq denote the Banach space of continuous functions on the interval r0, 1s endowed
with the sup-norm. Let F be a σ-algebra on Cpr0, 1sq so that for all xPr 0, 1s, the map deﬁned via
Lxpfq “ fpxq
is F-measurable. Show that F contains all open sets.
Solution. Since Cpr0, 1sq is separable, every open set is a countable union of open balls, so it suﬃces
to show that F contains every open ball. And every open ball is a countable union of closed balls, so it
suﬃces to show F contains every closed ball. Fix gPCpr0, 1sq, ϵą 0, and let
E “ tfPCpr0, 1sq :||f´g||L8ďϵu
be a closed ball. For each qP QXr 0, 1s, let
Eq “ tfPCpr0, 1sq :|fpqq´ gpqq|ď ϵu.
Note that each EqP F because Eq“L´1
q pBpgpqq,ϵqq and Bpgpqq,ϵq is a Borel set in C. Now we claim that
E “
č
qPQ
Eq.
First, if f P E, then |fpxq´ gpxq| ď ||f´g||L8 ď ϵ for all x P r0, 1s, so clearly f P Eq for every q, so
EĎ Ş
qPQEq. Conversely, suppose fPEq for everyq. If we had fRE, then we would have|fpxq´gpxq|ą ϵ
for some xPr 0, 1s, but since|f´g| is continuous and Q is dense, this would imply the existence of qPr 0, 1s
with|fpqq´ gpqq|ą ϵ, a contradiction. So E “ Ş
qPQEq, which expresses E as a countable intersection of
elements of F, so EP F.
Problem 4. For n ě 1, let an : r0, 1q Ñ t0, 1u denote the nth digit in the binary expansion of x, so
that
x “
ÿ
ně1
anpxq2´n for all xPr 0, 1q.
(We remove any ambiguity from this deﬁnition by requiring that lim inf anpxq “0 for all xP r0, 1q.) Let
Mpr0, 1qq denote the Banach space of ﬁnite complex Borel measures on r0, 1q and deﬁne linear functionals
Ln on Mpr0, 1qq via
Lnpµq “
ż 1
0
anpxqdµpxq.
Show that no subsequence of the sequence Ln converges in the weak-˚ topology on Mpr0, 1qq˚.
Solution. Let Lnk be any subsequence of the Ln. To show that Lnk is not weak-˚ convergent, it suf-
ﬁces to ﬁnd some µPMpr0, 1qq such thattLnkpµqu8
k“1 is not a convergent sequence in C. Let
b “
8ÿ
k“1
pk mod 2q¨ 2´nk,
i.e. b is the number inr0, 1q whosenth digit in binary is equal to 1 ifn“nk for some oddk, and 0 otherwise.
Now let µ“δb be the point mass measure at b. Clearly µPMpr0, 1qq, and we have
Lnkpµq “
ż 1
0
ankpxqdµpxq “ ankpbq “ k mod 2.
SotLnkpµqu8
k“1 is not a convergent sequence, so tLnku does not weak-˚ converge.
Problem 5. Let dµ be a ﬁnite complex Borel measure on r0, 1s such that
ˆµpnq “
ż 1
0
e2πinxdµpxq Ñ 0 as nÑ8.
115

Let dν be a ﬁnite complex Borel measure on r0, 1s that is absolutely continuous with respect to dµ. Show
that
ˆνpnq Ñ 0 as nÑ8.
Solution. Since dν is absolutely continuous with respect to dµ, by the Radon-Nikodym theorem there
is a function f“ dν
dµ PL1pdµq such that
ˆνpnq “
ż 1
0
e2πinxdνpxq “
ż 1
0
e2πinxfpxqdµpxq.
Fixϵą 0. Since dµ is a ﬁnite Borel measure on a compact metric space, we know that the set of continuous
functions is dense in L1pdµq with respect to the L1 norm, so let g be a continuous function satisfying
||f´g||L1 ă ϵ. We also know that trigonometric polynomials are dense in the set of continuous functions
with respect to the sup norm, so let P be a trigonometric polynomial such that ||g´P||L8 ă ϵ. Writing
Ppxq“ řN
m“´Nane2πimx, we calculate
lim
nÑ8
ż 1
0
e2πnxPpxqdµpxq “ lim
nÑ8
Nÿ
m“´N
an
ż 1
0
e2πipn`mqxdµpxq “ 0
by hypothesis. Thus, as soon as n is big enough so that
⏐⏐⏐⏐
ż 1
0
e2πnxPpxqdµpxq
⏐⏐⏐⏐ ăϵ,
we have
|ˆνpnq| “
⏐⏐⏐⏐
ż 1
0
e2πinxfpxqdµpxq
⏐⏐⏐⏐
ď
⏐⏐⏐⏐
ż 1
0
e2πinxpfpxq´ gpxqqdµpxq
⏐⏐⏐⏐`
⏐⏐⏐⏐
ż 1
0
e2πinxpgpxq´ Ppxqqdµpxq
⏐⏐⏐⏐`
⏐⏐⏐⏐
ż 1
0
e2πinxPpxqdµpxq
⏐⏐⏐⏐
ď ϵ`
ż 1
0
|fpxq´ gpxq|dµpxq`
ż 1
0
|gpxq´ Ppxq|dµpxq
ď ϵ`ϵ`ϵµr0, 1s,
which shows ˆνpnqÑ 0 as nÑ8 .
Problem 6. Let D be the closed unit disc in the complex plane, let tpnu be distinct points in D and
let rną 0 be such that the discs Dn“tz :|z´pn|ď rnu satisfy
1. DnĎ D;
2. DnXDm“H if n‰m; and
3. řrnă8 .
ProveX“ DzŤ
nDn has positive area.
Solution. Let fpx,yq “ř8
i“1χDipx,yq. Also let upxq “ř8
i“1χπpDiqpxq where π denotes projection onto
the real axis. We have ż 1
´1
upxqdx “
8ÿ
i“1
2ri ă 8
by hypothesis, so we conclude that upxqă8 for a.e. xPp´ 1, 1q. For a ﬁxed x, upxq counts the number
of the Di that intersect the line Re pzq“ x. Since the Di are closed disjoint discs, upxqă8 implies that
116

the portion of the line Re pzq“ x not contained in any of the Di has positive (one-dimensional) Lebesgue
measure. Let mpxq denote the one-dimensional measure of the portion of the line Re pzq“ x not contained
in any of theDi. Then the area of X is given exactly by
ş1
´1mpxqdx, and since m is a non-negative function
which has a positive value for a.e. xPp´ 1, 1q, this implies that
ş1
´1mpxqdxą 0.
Problem 7. Let fpzq be a one-to-one continuous mapping from the closed annulus
t1ď|z|ď Ru
onto the closed annulus
t1ď|z|ď Su
such that f is analytic on the open annulus t1ă|z|ă Ru. Prove S“R.
Solution. Let A “ tz : 1 ă |z| ăRu and B “ tz : 1 ă |z| ăSu. We know that f maps BA to BB,
so by composing f with an inversion if necessary we may assume that f maps the unit circle to itself. Since
f is a nonvanishing analytic function in A, log|f| is harmonic in A and extends continuously to BA, and
satisﬁes log|fpzq|“ 0 on|z|“ 1 and log|fpzq|“ logpSq on|z|“ R. Since A is a region on which the Dirichlet
problem can be solved, log |f| is uniquely determined by its boundary values. Since z ÞÑ log|z|¨ logpSq
logpRq is
another harmonic function on A with the same boundary values, we conclude that
log|fpzq| “ log|z|¨ logpSq
logpRq
for allzPA. Therefore we have|fpzq|“| zα| whereα :“ logpSq{ logpRq. Since fpzq andzα are both analytic
functions in the slit annulus ˜A :“Azr´R,´1s, this implies that fpzq“ Czα for some|C|“ 1 (this is proven
by applying the maximum principle to fpzq{zα andzα{fpzq). But we know that f analytically continues to
all of A, so by uniqueness of analytic continuation, zα must also, which implies that α is a positive integer.
But if α ě 2, then zα is not one-to-one on A, so we must have α “ 1 and therefore log pRq “logpSq, so
R“S.
Problem 8. Let a1,...,a n be n ě 1 points in the disc D (possibly with repetitions), so that the func-
tion
Bpzq “
nź
j“1
z´aj
1´ajz
has n zeros in D. Prove that the derivative B1pzq has n´ 1 zeros in D.
Solution. First assume that Bp0q ‰ 0 ‰ B1p0q and that B has no repeated roots. One can calculate
that
B1pzq
Bpzq “
nÿ
j“1
1´|aj|2
pz´ajqp1´ajzq “
řn
j“1
”
p1´|aj|2qś
i‰jpz´aiqp1´aizq
ı
śn
j“1pz´ajqp1´ajzq .
Since we assume B has no repeated roots, the zeros of B1{B are precisely the zeros of B1. Note that B1{B
is a rational function with a numerator of degree 2 pn´ 1q, so it has 2 pn´ 1q total zeros. With a lot of
calculation, one can verify the identity
B1p1{zq
Bp1{zq
“ z2B1pzq
Bpzq.
This shows that for z‰ 0, B1pzq“ 0 if and only if B1p1{zq“ 0. Since we assumed neither B nor B1 vanish
at 0, this implies that the zeros come in pairs tz, 1{zu. Exactly one member of each pair is inside D and the
other is outside D, so since there are 2pn´ 1q total zeros of B1, it must have n´ 1 zeros inside D.
For the general case, it is a theorem that if B is any function of the given form with n factors, then there
is a sequence Bk of functions of the given form, each with n factors, satisfying (a) BkÑB uniformly on D,
117

(b)Bkp0q‰ 0‰B1
kp0q, and (c) Bk has no repeated roots. To see why this is true, note that z´α
1´αz converges
uniformly on D to z´β
1´βz as αÑ β. Therefore this is also true for products of functions of that form. Also
note that Bkp0q and B1
kp0q are continuous functions of the roots a1,...,a n. Therefore by just taking the
original function B and perturbing its roots by suﬃciently small amounts, we can guarantee that the new
function has all of the desired properties and is still uniformly close to B.
So by the ﬁrst part of this problem, we know that each Bk has exactly n´ 1 roots in D. Since the
convergence is uniform on D, we also know that B1
kÑB1 uniformly on D. Since each Bk has absolute value
1 on BD, we then have that B1
k{Bk converges uniformly to B1{B onBD, so by the argument principle
# zeros of B in D “
ż
BD
B1
B dz “ lim
kÑ8
ż
BD
B1
k
Bk
dz “ lim
kÑ8
p# zeros of Bk in Dq “ n´ 1.
Problem 9a. Let fpzq be an analytic function in the entire complex plane C and assume fp0q ‰ 0.
Lettanu be the zeros of f, repeated according to their multiplicities. Let Rą 0 be such that |fpzq|ą 0 on
|z|“ R. Prove
1
2π
ż 2π
0
log
⏐⏐fpReiθq
⏐⏐ dθ “ log|fp0q|`
ÿ
|an|ăR
log R
|an|.
Solution. Since f is not identically zero, there are only ﬁnitely many an satisfying|an|ă R. Deﬁne
gpzq “
ź
|an|ăR
Rpz´anq
R2´anz .
Note that in the disc |z|ă R, g has the same zeros as f, no poles, and |gpzq|“ 1 for |z|“ R. Therefore
f{g is a nonvanishing holomorphic function in |z|ă R, and |f{g|“| f| on the boundary |z|“ R. Therefore
log|f{g| is a harmonic function in |z|ă R, so we apply the mean value formula to obtain
log
⏐⏐⏐⏐
fp0q
gp0q
⏐⏐⏐⏐ “ 1
2π
ż 2π
0
log
⏐⏐⏐⏐
fpReiθq
gpReiθq
⏐⏐⏐⏐ dθ “ 1
2π
ż 2π
0
log
⏐⏐fpReiθq
⏐⏐ dθ.
We also have
log
⏐⏐⏐⏐
fp0q
gp0q
⏐⏐⏐⏐ “ log|fp0q|´
ÿ
|an|ăR
log
⏐⏐⏐⏐
Rp0´anq
R2´ 0
⏐⏐⏐⏐ “ log|fp0q|`
ÿ
|an|ăR
log
⏐⏐⏐⏐
R
an
⏐⏐⏐⏐,
so combining this with the above equation gives the desired result.
Problem 9b. Prove that if there are constants C and λ such that|fpzq|ď Ce|z|λ
for all z, then
ÿˆ 1
|an|
˙λ`ϵ
ă 8
for all ϵą 0.
Solution. Let NpRq“ #tn :|an|ă Ru. Applying part (a) with 2 R in place of R we get
1
2π
ż 2π
0
log|fp2Reiθq|dθ “ log|fp0q|`
ÿ
|an|ă2R
log
ˆ 2R
|an|
˙
ď log|fp0q|`
ÿ
|an|ăR
log
ˆ 2R
|an|
˙
ď log|fp0q|`NpRq logp2q.
By the hypothesis on the growth rate of f, we also have
1
2π
ż 2π
0
log|fp2Reiθq|dθ ď p2Rqλ` logpCq,
118

so combining the two estimates gives p2Rqλ` logpCqě log|fp0q|` NpRq logp2q, which implies that
NpRq ď p2Rqλ´ logpCq´ log|fp0q|
logp2q ď Kp2Rqλ
for some constantK andR suﬃciently large. Let M be big enough so that the above estimate holds whenever
Rě 2M´1. It suﬃces to show that
ÿ
|an|ě2M´1
ˆ 1
|an|
˙λ`ϵ
ă 8
for any ϵą 0. We estimate
ÿ
|an|ě2M´1
ˆ 1
|an|
˙λ`ϵ
“
8ÿ
r“M
ÿ
2r´1ď|an|ă2r
ˆ 1
|an|
˙λ`ϵ
ď
8ÿ
r“M
pNp2rq´ Np2r´1q
ˆ 1
2r´1
˙λ`ϵ
ď
8ÿ
r“M
Np2rq
p2r´1qλ`ϵ ď K
8ÿ
r“M
p2r`1qλ
p2r´1qλ`ϵ “ K¨ 22λ`ϵ
8ÿ
r“M
p2´ϵqr ă 8.
Problem 10. Let a1,...,a n be n ě 1 distinct points in C and let Ω “ Czta1,...,a nu. Let HpΩq be
the vector space of real-valued harmonic functions on Ω and let RpΩqĎ HpΩq be the space of real parts of
analytic functions on Ω. Prove the quotient space HpΩq
RpΩq has dimension n, ﬁnd a basis for this space, and
prove it is a basis.
Solution. We claim that the functions fi “ log |z´ai| form a basis for this space. We will work with
a homology basis γ1,...,γ n for Ω, consisting of small counterclockwise circles around each point. For a
function uPHpΩq be arbitrary, we let ˚du“´uydx`uxdy denote the conjugate diﬀerential for u. Recall
that the periods of˚du with respect our homology basis are deﬁned to be the real numbers
ş
γi
u. (See section
6.1 in Ahlfors.)
The harmonic function apzq“ log |z| deﬁned on Czt0u has conjugate diﬀerential dθ, and so the period of
˚da on a counterclockwise circle about the origin is 2π. Alternatively one can see this by settingf“ax´iay
(which is analytic) and then writing fdz “ da`i ˚da. The diﬀerential da is exact, and we can compute
thatfpzq“ 1
z. Thus the integral of i˚dv around a counterclockwise circle is 2πi, and we again get a period
of 2π. Note that the period of ˚da around any cycle homologous to 0 is 0, since the integral of fdz around
such a cycle is 0. Therefore by translating, we see that the period of ˚dfi along γj is 2πδij.
If uPRpΩq then u has a harmonic conjugate v and˚du“dv, which is exact. Thus each period of u is
0. If řn
i“1aifiPRpΩq, then it must have period 0 about each cycle. By linearity of periods, this can only
happen if each ai is 0. So our fi’s are independent.
Let gPHpΩq be arbitrary, with ˚dg having periods pi on γi. Set
rg“g´ 1
2π
nÿ
i“1
pifi,
so that˚drg has period 0 on eachγi. We claim thatrg lies inRpΩq, which will imply that thefi’s span. Indeed
we have that˚drg is exact and so we may integrate˚drg to obtain a harmonic conjugate for rg. More precisely,
set fpzq“ rux´iruy. Then fdz “du`i˚du is exact on Ω and so f has an anti-derivative F “U`iV on
Ω. It’s easy to verify that U and u agree up to constants, so V is a harmonic conjugate for u.
Problem 11. Let 1ďpă8 and let Upzq be a harmonic function on the complex plane C such that
ĳ
RˆR
|Upx`iyq|pdxdy ă 8.
Prove that Upzq“ 0 for all z“x`iyP C.
119

Solution. Let q be the conjugate exponent, so 1 {p` 1{q “ 1. Since U is harmonic on all of C, for
anyrą 0 and any zP C we have the mean value property
Upzq “ 1
πr2
ĳ
Bpz,rq
Upx`iyqdxdy.
By H¨ older’s inequality we have
|Upzq| ď 1
πr2
ĳ
Bpz,rq
|Upx`iyq|dxdy “ 1
πr2
ˆĳ
Bpz,rq|Upx`iyq|pdxdy
˙1{p
¨
˚˝
ĳ
Bpz,rq
1dxdy
˛
‹‚
1{q
ď pπr2q1{q
πr2
¨
˝
ĳ
RˆR
|Upx`iyq|pdxdy
˛
‚
1{p
ď Cr2p1{q´1q “ Cr´2{p
for some constant C ă 8. This holds for any r ą 0, so we can take r Ñ 8and conclude that Upzq “0
(because´2{pă 0).
Problem 12. Let 0ăαă 1 and let fpzq be an analytic function on the unit disc D. Prove that if
|fpzq´ fpwq| ď C|z´w|α
for all z,w P D and some constant CP R, then there is a constant A“ApCqă8 such that
|f1pzq| ď Ap1´|z|qα´1.
Solution. Fix zP D. Then for any rą 0 we have
ż
|w´z|“r
1
pw´zq2 dw “ 0,
so by the Cauchy integral formula we can write
f1pzq “
ż
|w´z|“r
fpwq
pw´zq2 dw “
ż
|w´z|“r
fpwq´ fpzq
pw´zq2 dw.
Therefore taking absolute values inside we get
|f1pzq| ď 2πr¨ 1
r2 ¨ sup
|w´z|“r
|fpzq´ fpwq| ď 2π
r Crα “ 2πCr 1´α.
This is true for any r for which Bpz,rqĎ D, so pick r“ 1´|z|
2 , then we get
|f1pzq| ď Ap1´|z|qα´1.
120

18 Fall 2017
Problem 1. Suppose f : RÑ R is non-decreasing. Show that if AĎ R is a Borel set, then so is fpAq.
Solution. Let F “ tA Ď R : fpAq is Borelu. It suﬃces to show that F is a σ-algebra containing all
closed intervals. It’s clear that H P F. Since f is non-decreasing, it is continuous except for at most
countably many jump discontinuities. Thus fpRq is a countable union of intervals, so it’s Borel, so RP F.
Suppose A P F. Note that fpAq and fpAcq have at most countably many elements in common and that
fpRq “fpAqY fpAcq, so we can write fpAcq “fpRqzfpAqY (countable set), so fpAcq is Borel and thus
AcP F. Finally, if A1,A 2,... P F, then we have fpŤAnq“ ŤfpAnq, so it’s Borel, so ŤAnP F. Thus F
is a σ-algebra. If ra,bs is a closed interval, then by the same argument as above, since f is non-decreasing,
fpra,bsq is an at most countable union of intervals, so it’s Borel. Therefore F contains all closed intervals so
we’re done.
Problem 2. Let tfnu denote a bounded sequence in L2pr0, 1sq. Suppose the sequence also converges
almost everywhere. Show that then tfnu converges in the weak topology on L2pr0, 1sq.
Solution. Say that ||fn||L2 ď M for all n and that fn Ñ f almost everywhere. Then also |fn|2 Ñ |f|2
almost everywhere, so by Fatou’s lemma we have
ż
|f|2 “
ż
lim inf
nÑ8
|fn|2 ď lim inf
nÑ8
ż
|fn|2 ď M2,
so also f P L2 and||f||L2 ď M. To show that fn Ñ f weakly in L2, we need to show that φpfnqÑ φpfq
for every φPp L2q˚, and by Lp-Lq duality, this is the same as showing that
ş
fngÑ
ş
fg for every gP L2.
Fix gP L2 and ϵą 0. Since |g|2 is integrable, let δą 0 be such that λpEqă δ implies
ş
E|g|2ă ϵ (here λ
denotes Lebesgue measure). By Egorov’s theorem, we can ﬁnd a set EĎr 0, 1s such that fnÑf uniformly
on Ec and λpEqă δ. Let n be big enough so that |fn´f|ă ϵ{||g||L2 on Ec. Then we have
ż
|fng´fg| “
ż
A
|fng´fg|`
ż
Ac
|fng´fg| “
ż
A
|g||fn´f|`
ż
Ac
|g||fn´f|
ď
ˆż
A
|g|2
˙1{2ˆż
A
|fn´f|2
˙1{2
`
ˆż
Ac
|g|2
˙1{2ˆż
Ac
|fn´f|2
˙1{2
ď ϵ1{2
˜ż
r0,1s
4p|fn|2`|f|2q
¸1{2
`||g||L2
˜ż
r0,1s
ϵ2{||g||2
L2
¸1{2
ď ϵ1{2p8M2q1{2`ϵ.
This shows that
ş
|fng´fg|Ñ 0 as nÑ8 , which implies the desired result.
Problem 3. Let tµnu denote a sequence of Borel probability measures on R. For n P N and x P R
we deﬁne
Fnpxq :“ µnpp´8,xsq.
Suppose the sequencetFnu converges uniformly on R. Show that then for every bounded continuous function
f : RÑ R, the numbers ż
R
fpxqdµnpxq
converge as nÑ8 .
Solution. Let F denote the set of linear combinations of characteristic functions of disjoint intervals of
the formpa,bs, where a may be´8 andb may be8. First we show the result holds for elements of F. Let
121

g“ řN
k“1αkχpak,bks. Then we have (with the convention that Fnp8q“ 1 and Fnp´8q“ 0)
⏐⏐⏐⏐
ż
gdµn´
ż
gdµm
⏐⏐⏐⏐ “
⏐⏐⏐⏐⏐
Nÿ
k“1
αkpFnpbkq´ Fnpakqq´
Nÿ
k“1
αkpFmpbkq´ Fmpakqq
⏐⏐⏐⏐⏐
ď
Nÿ
k“1
|αk|p|Fnpbkq´ Fmpbkq|`| Fnpbkq´ Fnpakq|q.
Fix ϵ ą 0. Since the sequence tFnu converges uniformly, pick n,m big enough so that ||Fn´Fm||L8 ă
ϵ{p2ř|αk|q. Then the above estimate implies that for all such n,m , we have
⏐⏐ş
gdµn´
ş
gdµm
⏐⏐ ă ϵ. So
the numbers t
ş
gdµnu form a Cauchy sequence in R and therefore converge. This establishes the result for
elements of F.
Now let f be any bounded continuous function R Ñ R. On any compact interval, f can be approxi-
mated in the L8 norm by functions in F. So just work on a compact interval that is big enough so that
almost all of the mass of the µn is inside that interval (this can be made precise using the fact that the Fn
converge uniformly on R, but I don’t have time to write it down right now). Fix ϵą 0 and pick gP F such
that||f´g||L8ăϵ. Then for n,m big enough, we have
⏐⏐⏐⏐
ż
fdµ n´
ż
fdµ m
⏐⏐⏐⏐ ď
⏐⏐⏐⏐
ż
fdµ n´
ż
gdµn
⏐⏐⏐⏐`
⏐⏐⏐⏐
ż
gdµn´
ż
gdµm
⏐⏐⏐⏐`
⏐⏐⏐⏐
ż
gdµm´
ż
fdµ m
⏐⏐⏐⏐
ď
ż
|f´g|dµn`
ż
|f´g|dµm`ϵ
ď ϵµnpRq` ϵµmpRq` ϵ “ 3ϵ,
which establishes the desired result.
Problem 4. Consider the Banach space V “ Cpr´1, 1sq of all real-valued continuous functions on r´1, 1s
equipped with the supremum norm. Let B“tf PV :||f||L8 ď 1u be the closed unit ball in V . Show that
there exists a bounded linear functional Λ : V Ñ R such that ΛpBq is an open subset of R.
Solution. Deﬁne Λ : V Ñ R by
Λpfq “ ´
ż 0
´1
fpxqdx`
ż 1
0
fpxqdx.
It is clear that |Λpfq|ď 2||f||L8 for all f P V , so Λ is a bounded linear functional. Since Λ is continuous
andB is a connected set, ΛpBq is a connected subset of R and is therefore an interval. We claim that ΛpBq
is the open interval p´2, 2q.
Let fn be the function which is equal to ´1 for x P r´1,´1{ns, equal to 1 for x P r1{n, 1s, and linear
onr´1{n, 1{ns. Note that each fnPB, and we calculate Λpfnq“ 2´ 1{n. Since ΛpBq is an interval in R,
this implies that p´2, 2qĎ ΛpBq. We now just need to check that Λ never achieves the values ˘2. But note
that we have|Λpfq|ď
ş1
´1|fpxq|dxď 2. But the second inequality is strict for all f which are not identically
˘1. Since Λ p˘1q “0, this shows that in fact the strict inequality |Λpfq| ă2 holds for all f P B, so we
conclude that ΛpBq“p´ 2, 2q.
Problem 5. Suppose f : R Ñ R is a bounded and measurable function satisfying fpx` 1q “fpxq
and fp2xq“ fpxq for almost every xP R. Show that then there exists a constant cP R such that fpxq“ c
for almost every xP R.
Solution. Let Z be the measure zero set of bad points for which the given property doesn’t hold. Let
rZ be the set of all points in R which are reachable from a point in Z by a ﬁnite sequence of the operations
xÞÑx` 1,xÞÑx´ 1,xÞÑ 2x, or xÞÑx{2. Then rZ is just a countable union of translates and dilates of Z,
122

so rZ also has measure zero. We will show that f is constant on the complement of rZ. By construction of
rZ, for any xR rZ we have 2´np2nx` 1` 2nmq“ x`m` 2´nR rZ for all integers n,m . Let Q be the set of
numbers of the form m` 2´n for n,m P Z.
Let x0,y 0 R rZ and ﬁx ϵ ą 0. Since f is bounded, it is locally integrable. Therefore by the Lebesgue
diﬀerentiation theorem we can pick rą 0 such that
⏐⏐⏐⏐fpx0q´ 1
2r
żx0`r
x0´r
fptqdt
⏐⏐⏐⏐ ă ϵ,
⏐⏐⏐⏐fpy0q´ 1
2r
ży0`r
y0´r
fptqdt
⏐⏐⏐⏐ ă ϵ.
Also, since f is bounded we can ﬁnd δą 0 such that for any set AĎ R, λpAqă δ implies
ş
A|fptq|dtăϵr
(here λ denotes Lebesgue measure). We can pick a number q P Q such that |px0`qq´ y0|ă δ{2. Then,
since fpt`qq“ fptq for all tR rZ, which is almost every t, we have the estimate
⏐⏐⏐⏐
1
2r
żx0`r
x0´r
fptqdt´ 1
2r
ży0`r
y0´r
fptqdt
⏐⏐⏐⏐ “ 1
2r
⏐⏐⏐⏐
żx0`q`r
x0`q´r
fptqdt´
ży0`r
y0´r
fptqdt
⏐⏐⏐⏐
“ 1
2r
⏐⏐⏐⏐⏐
ż
rx0`q´r,x0`q`rs∆ry0´r,y0`rs
fptqdt
⏐⏐⏐⏐⏐ ă ϵ{2.
So combining the above three inequalities with the triangle inequality gives |fpx0q´fpy0q|ăp 2` 1{2qϵ, and
taking ϵÑ 0 shows that fpx0q“ fpy0q, so f is constant on the complement of rZ.
Alternative Solution. Let E be the measure zero set on which fpxq ‰fp2xq. Then fpxq “fp2xq
for all x P Ec, and so fp2kxq “fpxq for all x P Ec and k P N. Since we are only trying to show that f
is constant almost everywhere, we can discard E. So, we can suppose fp2kxq“ fpxq for all x. Moreover,
fpx` 1q “fpxq for almost all x means f can be considered as a function on S1 “ R{Z “ r0, 1q. As a
bounded measurable function on S1, f is in L1pS1q, and so has Fourier coeﬃcients ˆfpkq for all kP Z. An
elementary theorem says that L1pS1q functions are determined by their Fourier coeﬃcients. Therefore, to
show f is constant, it is enough to show that every nonzero Fourier coeﬃcient of f vanishes (since then f
will have the same Fourier coeﬃcients as the constant function xÞÑ ˆfp0q).
Now, for any kP N, and any nP Z,
ˆfpnq“
ż 1
0
fpxqe´2πnixdx
“
ż 1
0
fp2kxqe´2πnixdx
“ 2´k
ż 2k
0
fpyqe´2πin2´kydy
“ 2´k
2k´1ÿ
j“0
ż 1
0
fpyqe´2πin2´kpy`jqdy
“ck,n¨ 2´k
ż 1
0
fpyqe´2πin2´kydy,
where ck,n is the constant
ck,n“
2k´1ÿ
j“0
e´2πin2´kj.
But, if n2´k is not an integer, then
ck,n“ pe´2πin2´k
q2k
´ 1
e´2πin2´k
´ 1 “ e´2πin´ 1
e´2πin2´k
´ 1 “ 0,
123

and so ˆfpnq“ 0 in this case. But if n‰ 0, then of course there is some kP N with n2´kR Z. Consequently
ˆfpnq“ 0 if n‰ 0, which completes the proof.
Problem 6. Let fPL2pCq. For zP C we deﬁne
gpzq “
ż
twPC:|w´z|ď1u
|fpwq|
|z´w|dApwq
wheredA denotes integrations with respect to Lebesgue measure on C. Show that then|gpzq|ă8 for almost
everyzP C and that gPL2pCq.
Solution. Let C“
ş
|u|ď1
1
|u|dApuqă8 . We have
|gpzq|2 “
˜ż
|w´z|ď1
|fpwq|
|w´z|dApwq
¸2
ď
˜ż
|w´z|ď1
|fpwq|2
|w´z| dApwq
¸˜ż
|w´z|ď1
1
|w´z|dApwq
¸
by Cauchy-Schwarz
ď C¨
ż
|w´z|ď1
|fpwq|2
|w´z| dApwq.
Therefore we can estimate
ż
C
|gpzq|2dApzq ď C
ż
C
ż
|w´z|ď1
|fpwq|2
|w´z| dApwqdApzq
ď C
ż
C
|fpwq|2
ż
|z´w|ď1
1
|z´w|dApzqdApwq by Tonelli
ď C2||f||2
L2pCq ă 8.
This shows both that |gpzq|ă8 for almost every zP C and gPL2pCq.
Problem 7. Prove that there exists a meromorphic function f on C with the following properties.
1. fpzq“ 0 if and only if zP Z.
2. fpzq“8 if and only if z´ 1{3P Z.
3. |fpx`iyq|ď 1 for all xP R and all yP R with|y|ě 1.
Solution. Letfpzq“ 1
2
sinpπzq
sinpπpz´1{3qq. It’s clear that f is meromorphic with fpzq“ 0 if and only if zP Z and
fpzq“8 if and only if z´ 1{3P Z. Now we just estimate
2|fpx`iyq| “
⏐⏐⏐⏐
exppiπzq´ expp´iπzq
exppiπpz´ 1{3qq´ expp´iπpz´ 1{3qq
⏐⏐⏐⏐ ď | exppiπzq|`| expp´iπzq|
|| exppiπpz´ 1{3qq|´| expp´iπpz´ 1{3qq||
“ expp´πyq` exppπyq
|expp´πyq´ exppπyq| ď 2 when |y|ě 1.
Problem 8. Show that a harmonic function u : DÑ R is uniformly continuous if and only if it admits the
representation
upzq “ 1
2π
ż 2π
0
Re
ˆeiθ`z
eiθ´z
˙
fpeiθqdθ, z P D,
with f :BDÑ R continuous.
124

Solution. It is a standard fact that u is uniformly continuous on D if and only if it admits a continu-
ous extension to BD. First suppose that u admits a continuous extension to BD. Then the Poisson integral
formula is exactly the representation
upzq “ 1
2π
ż 2π
0
Re
ˆeiθ`z
eiθ´z
˙
upeiθqdθ
(To prove the Poisson integral formula, you simply apply the regular mean value formula to u composed
with the conformal map wÞÑ w`z
1`zw and simplify the change of variables. Not sure if proving that would be
required for this problem or not).
Conversely, suppose u has the above representation. We just need to show that the continuous function
f :BDÑ R continuously extends u. Fix eiθ0 PB D. We need to show that upzqÑ fpeiθ0q as zÑeiθ0 in D.
Fix ϵą 0. Pick δ1 such that|θ´θ0|ă δ1 implies|fpeiθq´ fpeiθ0q|ă ϵ (by continuity of f). Also, since BD
is compact, let M“ maxθPr0,2πs|fpeiθq|. Now we can pick δą 0 to be small enough so that
|z´eiθ0|ă δ and |θ´θ0|ě δ1 imply 1´|z|2
|eiθ´z|2 “ Re
ˆeiθ`z
eiθ´z
˙
ă ϵ
2M.
Then for all |z´eiθ0|ă δ, we have the estimate (using the fact that
ş2π
0
1´|z|2
|eiθ´z|2 dθ“ 2π for any zP D)
|upzq´ fpeiθ0q| “ 1
2π
⏐⏐⏐⏐
ż 2π
0
1´|z|2
|eiθ´z|2fpeiθqdθ´
ż 2π
0
1´|z|2
|eiθ´z|2fpeiθ0qdθ
⏐⏐⏐⏐
ď 1
2π
ż 2π
0
1´|z|2
|eiθ´z|2|fpeiθq´ fpeiθ0q|dθ
ď 1
2π
˜ż
|θ´θ0|ăδ1
1´|z|2
|eiθ´z|2ϵdθ `
ż
|θ´θ0|ěδ1
ϵ
2M 2Mdθ
¸
ď ϵ
2πp2π` 2πq “2ϵ.
This shows that upzqÑ fpeiθ0q as zÑeiθ0 so f is a continuous extension of u toBD and we are done.
Problem 9. Consider a map F : Cˆ CÑ C with the following properties.
1. For each ﬁxed zP C the map wÞÑFpz,wq is injective.
2. For each ﬁxed wP C the map zÞÑFpz,wq is holomorphic.
3. Fp0,wq“ w for wP C.
Show that then
Fpz,wq “ apzqw`bpzq
for z,w P C, where a and b are entire functions with ap0q“ 1, bp0q“ 0, and apzq‰ 0 for zP C.
Solution. Deﬁne Gpz,wq “ Fpz,wq´Fpz,0q
Fpz,1q´Fpz,0q . We claim that Gpz,wq “w for all z,w . Then we can just
take apzq “Fpz, 1q´ Fpz, 0q and bpzq “Fpz, 0q and we will be done. By the injectivity condition, the
denominator of Gpz,wq is never 0, so for each ﬁxed w, z ÞÑ Gpz,wq is an entire function. Also note that
Gp0,wq “w and that Gpz, 0q “0 for all z and Gpz, 1q “1 for all z. So the desired condition is veriﬁed
for w “ 0, 1. Fix w ‰ 1. Then by the injectivity condition, if Gpz,wq “1 for any z, then w “ 1, and if
Gpz,wq“ 0 for any z, then w“ 0. So z ÞÑ Gpz,wq is an entire function that misses both 0 and 1, so by
Picard’s little theorem, zÞÑGpz,wq is constant. Then the fact that Gp0,wq“ w implies that Gpz,wq“ w
for all z, so we are done.
Problem 10. Lettfnu be a sequence of holomorphic functions on D with the property that
Fpzq :“
8ÿ
n“1
|fnpzq|2 ď 1
125

for all zP D. Show that the series deﬁning Fpzq converges uniformly on compact subsets of D and that F
is subharmonic.
Solution. Since fn is holomorphic, |fn|2 is subharmonic. Therefore each gN :“ řN
n“1|fn|2 is also sub-
harmonic, and we have that gN increases monotonically to F pointwise. Notice that if subharmonic were
replaced by harmonic, we would be done automatically by Harnack’s Principle. The following argument is
just a modiﬁcation of the proof of Harnack to work for subharmonic functions, where we rely heavily on the
fact that F is bounded and that the gN are partial sums rather than general subharmonic functions (it’s
not true in general that an increasing limit of subharmonic functions converges locally uniformly to another
subharmonic function).
First, suppose we knew that gN ÑF locally uniformly on D. Then since each gN is continuous, F also
is, and for any disc Bpz0,rqĎ D, we have
Fpz0q “ lim
NÑ8
gNpz0q ď lim
NÑ8
1
2π
ż 2π
0
gNpz0`reiθqdθ “ 1
2π
ż 2π
0
Fpz0`reiθqdθ
by the monotone convergence theorem (or by uniform convergence on compact sets). So F is continuous and
satisﬁes the sub mean value property, so it is subharmonic.
Now we show local uniform convergence. Fix a compact set K Ď D and ϵą 0. By compactness, there
is a radius rą 0 such that Bpz,rqĎ D for any zPK. Also by compactness, we can cover K with ﬁnitely
many balls Bpw1,r{2qY ... YBpwk,r{2q. For any zPK,
lim
NÑ8
1
2π
ż 2π
0
´
F
´
z` r
2eiθ
¯
´gN
´
z` r
2eiθ
¯¯
dθ “ 0
again by the monotone convergence theorem (this is where we need the fact that F is bounded). So let N
be large enough so that
max
1ďjďk
1
2π
ż 2π
0
´
F
´
zj` r
2eiθ
¯
´gN
´
zj` r
2eiθ
¯¯
dθ ă ϵ.
Now for any M ą N, gM´gN “ řM
n“N`1|fn|2 is still a positive subharmonic function (this is where we
need the fact that thegN are partial sums). Therefore it satisﬁes the “sub Poisson integral formula” (regular
Poisson integral formula but with a ď instead of “). For any zPK, we have zPBpzj,r{2q for some j, so
we apply the sub Poisson formula on Bpzj,rq to obtain
gMpzq´ gNpzq ď 1
2π
ż 2π
0
r2´|z´zj|2
|pzj`reiθq´ z|2
`
gMpzj`reiθq´ gNpzj`reiθq
˘
dθ
ď r`|z´zj|
r´|z´zj|
1
2π
ż 2π
0
pgM´gNqpzj`reiθqdθ
ď r`r{2
r´r{2¨ 1
2π
ż 2π
0
pF´gNqpzj`reiθqdθ ă 3ϵ.
This shows that the sequence gN is uniformly Cauchy on K and therefore converges uniformly to F on K,
so gN ÑF locally uniformly on D and we are done.
Problem 11. Let f : D Ñ C be an injective and holomorphic function with fp0q “0 and f1p0q “1.
Show that then
inft|w| :wRfpDqu ď 1
with equality if and only if fpzq“ z for all zP D.
Solution. We analyze the situation when inf t|w| : w R fpDqu ě 1. Then D Ď fpDq, and since f is
injective, it has a holomorphic inverse g : D Ñ D on the disk. It’s clear that gp0q “0 and g1p0q “1, so
by the Schwarz lemma (and the fact that g1p0q“ 1) we must have gpzq“ z. Thus fpzq“ z as well. The
126

original statement follows.
Problem 12. Let f,g , and h be complex-valued functions on C with
f “ g˝h.
Show that if h is continuous, and both f and g are holomorphic, then h is holomorphic as well.
Solution. Let B (for bad) be the set of points z for which g1phpzqq “0. For z P CzB, we can ﬁnd an
analytic local inverse g´1
U forg on a neighborhood of U ofhpzq. Thus onU, we can write h“g´1
U ˝f, which
implies that h is analytic at z. So h is analytic on CzB.
Since g is non-constant, we must have g1pzq“ 0 only on a discrete set. Furthermore, h is continuous, so
in fact B is discrete. But h is continuous so by Riemann’s theorem on removable singularities, h must be
analytic.
Remark. It’s not true in general that the preimage of a discrete set under a continuous function is also
discrete (a constant function is a counterexample), so that step takes a bit more work. Let Z denote the
zeros of g1 and suppose that h´1pZq has a limit point. Take a convergent sequence zn withthpznquĎ Z, so
it’s discrete. The set thpznqu can’t be inﬁnite, because its also discrete, so the limit would have to be inﬁnity,
butzn converges to a non-inﬁnite limit z8, which is impossible by the continuity of h. So thpznqu is a ﬁnite
set, meaning that there is some subsequence tznku converging to z8 on which h is constant. But then f is
also constant on tznku, and since f is holomorphic this implies f is a constant, which is a contradiction.
19 Spring 2018
Problem 1. Suppose fPL1pRq satisﬁes
lim sup
hÑ0
ż
R
⏐⏐⏐⏐
fpx`hq´ fpxq
h
⏐⏐⏐⏐dx“ 0.
Show that f“ 0 almost everywhere.
Solution. Let Fpxq“
şx
´8 |fptq|dt. We then consider the diﬀerence quotient
⏐⏐⏐⏐
Fpx`hq´ Fpxq
h
⏐⏐⏐⏐“ 1
|h|
⏐⏐⏐⏐
żx
´8
|fpt`hq|´ |fptq|dt
⏐⏐⏐⏐
ď
żx
´8
⏐⏐⏐⏐
fpt`hq´ fptq
h
⏐⏐⏐⏐
ď
ż
R
⏐⏐⏐⏐
fpt`hq´ fptq
h
⏐⏐⏐⏐dx.
By hypothesis, this last quantity tends to 0 ashÑ 0. SoF is diﬀerentiable with derivative 0, and is therefore
constant. It follows (by continuity from below) that
ş
R |fptq|dt“ 0, and so f“ 0 a.e.
Alternate solution. LetFpxq“
şx
´8fptqdt. Since f is integrable, by the Lebesgue diﬀerentiation theorem
we have that for a.e. xP R,
fpxq “ lim
hÑ0
1
h
żx`h
x
fptqdt “ lim
hÑ0
Fpx`hq´ Fpxq
h .
127

So for any two Lebesgue points xąy, we have
|fpxq´ fpyq| “ lim
hÑ0
⏐⏐⏐⏐
Fpx`hq´ Fpxq
h ´ Fpy`hq´ Fpyq
h
⏐⏐⏐⏐ “ lim
hÑ0
⏐⏐⏐⏐⏐
żx`h
y`h
fptq
h dt´
żx
y
fptq
h dt
⏐⏐⏐⏐⏐
“ lim
hÑ0
⏐⏐⏐⏐
żx
y
fpt`hq´ fptq
h dt
⏐⏐⏐⏐ ď lim sup
hÑ0
ż
R
⏐⏐⏐⏐
fpt`hq´ fptq
h dt
⏐⏐⏐⏐ “ 0.
So f is constant a.e., and since f is also integrable we must have f“ 0 a.e.
Problem 2. GivenfPL2pRq and hą 0 we deﬁne
Qpf,hq “
ż
R
2fpxq´ fpx`hq´ fpx´hq
h2 fpxqdx.
(a) Show that
Qpf,hqě 0 for all fPL2pRq and all hą 0.
(b) Show that the set
E “ tfPL2pRq : lim sup
hÑ0
Qpf,hqď 1u
is closed in L2pRq.
Solution.
(a) It suﬃces to show that
ż
R
2fpxq2dxě
ż
R
fpxqpfpx`hq´ fpx´hqqdx.
Indeed by Cauchy-Schwarz
ż
R
fpxqpfpx`hq´ fpx´hqqdxď||f||2¨||fpx`hq´ fpx´hq||2
ď||f||2¨p||fpx`hq||2`||fpx´hq||2q
“||f||2p||f||2`||f||2q
“ 2||f||2
2,
as desired.
(b) Let gpxq “ 2fpxq´ fpx`hq´ fpx´hq. Note g P L2. Using the form of Plancherel that says
xf,gy“
A
pf, pg
E
, we can rewrite
Qpf,hq “
ż
R
2pfpuq´ eihupfpuq´ e´ihupfpuq
h2
pfpuqdu “
ż
R
2´ 2 cosphuq
h2
⏐⏐⏐pfpuq
⏐⏐⏐
2
du.
Now let fn be a sequence in E with fnÑf in L2. By passing to a subsequence if necessary, we may
also assume thatfnÑf almost everywhere. By Plancherel, we also have xfnÑ pf inL2, and by passing
to a further subsequence if necessary we can also assume xfnÑ pf almost everywhere. Then by Fatou’s
lemma, since 1´ cosphuqě 0 for all h,u , for each n we have
1 ě lim sup
hÑ0
ż
R
2´ 2 cosphuq
h2
⏐⏐⏐xfnpuq
⏐⏐⏐
2
du ě lim inf
hÑ0
ż
R
2´ 2 cosphuq
h2
⏐⏐⏐xfnpuq
⏐⏐⏐
2
du
ě
ż
R
lim inf
hÑ0
2´ 2 cosphuq
h2
⏐⏐⏐xfnpuq
⏐⏐⏐
2
du “
ż
R
u2
⏐⏐⏐xfnpuq
⏐⏐⏐
2
du.
128

Then by applying Fatou’s lemma again, this time in n, we have
ż
R
u2
⏐⏐⏐pfpuq
⏐⏐⏐
2
du “
ż
R
lim inf
nÑ8
u2
⏐⏐⏐xfnpuq
⏐⏐⏐
2
du ď lim inf
nÑ8
ż
R
u2
⏐⏐⏐xfnpuq
⏐⏐⏐
2
du ď 1,
so uÞÑu2
⏐⏐⏐pfpuq
⏐⏐⏐
2
is integrable. Note we have the estimate
2´ 2 cosphuq
h2 “ u2 2´ 2 cosphuq
phuq2 ď 5u2
for all h,u P R because tÞÑ 2´2 cosptq
t2 is bounded by 5 for all real t. Therefore we have
2´ 2 cosphuq
h2
⏐⏐⏐pfpuq
⏐⏐⏐
2
du ď 5u2
⏐⏐⏐pfpuq
⏐⏐⏐
2
du
for allh,u P R, where the function on the right is integrable, so by the dominated convergence theorem
we have
1 ě
ż
R
u2
⏐⏐⏐pfpuq
⏐⏐⏐
2
du “
ż
R
lim
hÑ0
2´ 2 cosphuq
h2
⏐⏐⏐pfpuq
⏐⏐⏐
2
du “ lim
hÑ0
ż
R
2´ 2 cosphuq
h2
⏐⏐⏐pfpuq
⏐⏐⏐
2
du “ lim
hÑ0
Qpf,hq,
so fPE and thus E is closed in L2.
Problem 3. Suppose fPL1pRq satisﬁes
lim sup
ϵÑ0
ż
R
ż
R
|fpxqfpyq|
|x´y|2`ϵ2 dxdy ă 8.
Show that f“ 0 almost everywhere.
Solution. By applying monotone convergence to the limit (after using Tonelli’s theorem to convert the
double integral into an integral over R2), we have
ż
R
ż
R
|fpxqfpyq|
|x´y|2 dxdy ă8.
If f is not zero almost everywhere, then f has a Lebesgue point a with|fpaq|ą 0. We have
ża`r
a´r
ża`r
a´r
|fpxqfpyq|
|x´y|2 dxdy ě
ża`r
a´r
ża`r
a´r
|fpxqfpyq|
p2rq2 dxdy “
ˆ 1
2r
ża`r
a´r
|fpxq| dx
˙2
.
By the Lebesgue diﬀerentiation theorem, the right side tends to fpaq2 as rÑ 0`. On the other hand, the
left-most integral must tend to 0, since the integrand is inL1 (in factL1
loc is enough). This is a contradiction,
so we must have f“ 0 a.e.
Problem 4.
(a) Fix 1 ăpă8 . Show that
fÞÑrMfspx,yq “ sup
rą0,ρą0
1
4rρ
żr
´r
żρ
´ρ
fpx`h,y `𝓁qdhd𝓁
is bounded on LppR2q.
(b) Show that
rArfspx,yq “ 1
4r3
żr
´r
żr2
´r2
fpx`h,y `𝓁qdhd𝓁
converges to f a.e. in the plane as rÑ 0.
129

Solution.
(a) For g : RÑ R, let
Mgpxq :“ sup
rą0
1
2r
żr
´r
|gpx`hq|dh
be the usual maximal operator. For xP R, deﬁne fxpyq :“fpx,yq. Since f PLppR2q, fxPLppRq for
a.e. xP R (this is proved by Tonelli’s theorem). Therefore by the usual Hardy-Littlewood maximal
theorem, we have ż
|Mfxpyq|pdy À
ż
|fxpyq|pdy
for a.e. xP R. Now, for eachyP R, deﬁnegypxq :“Mfxpyq. Tonelli’s theorem and the above inequality
show that gyPLppRq for a.e. yP R:
ż ˆż
|gypxq|pdx
˙
dy “
ĳ
|Mfxpyq|pdydx
À
ĳ
|fxpyq|pdydx “ ||f||p
LppR2q ă 8.
Therefore using Hardy-Littlewood again we have
ż
|Mgypxq|pdx À
ż
|gypxq|pdx
for a.e. yP R. Now note that we have
rMfspx,yq ď sup
rą0
1
2r
żr
´r
sup
ρą0
1
2ρ
żρ
´ρ
|fpx`h,y `𝓁q|d𝓁dh by Tonelli
“ sup
rą0
1
2r
żr
´r
Mfx`hpyqdh
“ Mgypxq.
So by the above work we conclude that
ĳ
|rMfspx,yq|pdxdy ď
ĳ
|Mgypxq|pdxdy À
ĳ
|gypxq|pdxdy À ||f||p
LppR2q.
(b) We mimic the proof of the Lebesgue diﬀerentiation theorem. Deﬁne
Trfpx,yq :“ 1
4r3
żr
´r
żr2
´r2
|fpx,yq´ fpx`h,y `𝓁q| dhd𝓁, Tf px,yq :“ lim sup
rÑ0
Trfpx,yq.
It suﬃces to show that Tf “ 0 a.e., and for that it suﬃces to show that for any ﬁxed α ą 0,
λtpx,yq :Tfpx,yqě αu“ 0 (where λ denotes 2-dimensional Lebesgue measure). Fix αą 0 and ϵą 0.
Note that the desired result is obviously true for continuous functions. Since continuous functions are
dense in Lp, write f“g`u where g is continuous and||u||Lpăϵ. The operator Tr is subadditive, so
TrfďTrg`Tru, and taking rÑ 0 gives that Tf ďTu .
We now estimate the quantity λtpx,yq :Tupx,yqě αu. Notice that
Trupx,yq ď 1
4r3
żr
´r
żr2
´r2
p|upx,yq|`| upx`h,y `𝓁q|q dhd𝓁 ď |upx,yq|`r Muspx,yq.
Sotpx,yq :Tupx,yqě αuĎtp x,yq :|upx,yq|ě α{2uYtp x,yq :Mupx,yqě α{2u, which implies that
λtpx,yq :Tupx,yqě αu ď λtpx,yq :|upx,yq|ě α{2u` λtpx,yq :Mupx,yqě α{2u
ď ||u||p
Lp
pα{2qp `||Mu||p
Lp
pα{2qp by Chebyshev’s inequality
ď ϵp2p
αp ` Cpϵp2p
αp where C is the constant from part (a) on the boundedness of fÞÑrMfs.
130

Since Tf ď Tu , we also have λtpx,yq : Tfpx,yq ěαu ďϵp2p
αp ` Cpϵp2p
αp . Now the left side does not
depend on ϵ, so we can take ϵÑ 0 and conclude that λtpx,yq :Tfpx,yqě αu“ 0.
Problem 5. Let µ be a real-valued Borel measure on r0, 1s such that
ż 1
0
1
x`tdµptq“ 0
for all xą 1. Show that µ“ 0.
Solution. Let S denote the real span of the functions of the form 1
x`t for x ą 1 in Cpr0, 1sq. We ap-
ply Stone-Weirstrass to show that S is dense in Cpr0, 1sq. Forx0‰x1ą 1, we have
1
x0`t¨ 1
x1`t “ 1
x1´x0
ˆ 1
x0`t´ 1
x1`t
˙
,
which lies in S. We also have that 1
x`t¨ 1
x`t`ϵ Ñ 1
px`tq2
uniformly on r0, 1s as ϵÑ 0`. Thus 1
px`tq2 lies in S for tą 1. Therefore the product of any two elements
in S lies in S. This implies that S is closed under multiplication. Indeed if f and g lie in S then we have
sequences fiÑ f and giÑ g uniformly with fi,giP S. Since f and g are bounded on r0, 1s, we have that
figiÑfg uniformly, and so fg PS.
HenceS is an algebra. It’s clear that S separates points, and that there is no pointx0 such every function
in S vanishes at x0. ThusS“Cpr0, 1sq.
So we have that
ş1
0fptqdµptq “0 for all f in S, and by density for all f in Cpr0, 1sq. Note that µ is a
ﬁnite measure, otherwise
ş1
0
1
2`t would be either 8 or´8. By the Riesz representation theorem, we must
haveµ“ 0.
Remark. We used a slighly non-standard (although well-known) version of Stone-Weirstrass here. It’s
easy to avoid this, and instead show that the constant function 1 lies in S. For instance, the functions x
x`t
converge uniformly to 1 on r0, 1s as xÑ8.
Alternate Solution. Let ak“
ş1
0tkdµptq. ForxPp 0, 1q we have
0“
ż 1
0
1
1{x`tdµptq“
ż 1
0
x
1`txdµptq“
ż 1
0
˜ 8ÿ
k“0
p´1qktkxk`1
¸
dµptq“
8ÿ
k“0
p´1qkakxk`1,
where swapping the order of summation and integration can be justiﬁed by Fubini-Tonelli, after noting that
µ is ﬁnite (to prove Fubini-Tonelli for signed measures, one looks at a Jordan decomposition and applies
Fubini separately to each piece). This latter sum is a power a series in x which is identically 0 for xPp 0, 1q,
so each ak must equal 0. By taking linear combinations of the ak, we see that
ş
ppxqdµptq “ 0 for any
polynomial p. But polynomials are dense in Cpr0, 1sq, and so µ“ 0 by the Riesz representation theorem.
Problem 6. Let T denote the unit circle in the complex plane and let PpTq denote the space of Borel
probability measures on T and PpTˆ Tq denote the space of Borel probability measures on Tˆ T. Fix
µ,ν P PpTq and deﬁne
M “
$
&
%γP PpTˆ Tq :
ĳ
TˆT
fpxqgpyqdγpx,yq“
ż
T
fpxqdµpxq¨
ż
T
gpyqdνpyq for all f,g PCpTq
,
.
-.
Show that F : MÑ R deﬁned by
Fpγq “
ĳ
TˆT
sin2
ˆθ´φ
2
˙
dγpeiθ,eiφq
131

achieves its minimum on M.
Solution (trick). Note that sin 2
´
θ´φ
2
¯
“ 1
2p1´ cosθ cosφ` sinθ sinφq, which is just a sum of three
functions of the form fpθqgpφq where each f,g PCpTq. So by deﬁnition of M, Fpγq is actually independent
of γ, so F is constant on M and therefore obviously achieves its minimum.
Alternate solution (idea generalizes to other similar problems). Let I “ infγPMFpγq. Let γn
be a sequence of measures in M such that FpγnqÑ I as nÑ8 . Since Tˆ T is compact, one version of
the Riesz representation theorem says that the space of complex Borel measures on Tˆ T is isomorphic to
CpTˆ Tq˚, and the operator norm of a measure is its total variation. Therefore PpTˆ Tq is a subset of
the unit ball in CpTˆ Tq˚. By the Banach-Alaoglu theorem, this unit ball is weak- ˚ compact, and since
CpTˆ Tq is separable, it is actually sequentially compact. Thus there is a subsequence tγnku that weak-˚
converges to some complex Borel measure γ in the unit ball of CpTˆ Tq˚.
We claim that γ is the minimizer of F . We need to verify that γP M and that Fpγq“ I. Note that γ
is a probability measure because
γpTˆ Tq “
ĳ
TˆT
1dγ “ lim
nÑ8
ĳ
TˆT
1dγn “ 1
by weak-˚ convergence because 1 is continuous. To show that γ P M, let f,g P CpTq be ﬁxed. Then the
functionpx,yqÞÑ fpxqgpyq is in CpTˆ Tq, so by weak-˚ convergence we have
ĳ
TˆT
fpxqgpyqdγpx,yq “ lim
nÑ8
ĳ
TˆT
fpxqgpyqdγnpx,yq “
ż
T
fpxqdµpxq¨
ż
T
gpyqdνpyq.
Thus γ P M. To show that Fpγq “I, just note that sin 2
´
θ´φ
2
¯
is also continuous on Tˆ T, so weak-˚
convergence implies Fpγq“ limnÑ8Fpγnq.
Problem 7. Let F : Cˆ C Ñ C be jointly continuous and holomorphic in each variable separately.
Show that zÞÑFpz,zq is holomorphic.
Solution. Letpa,bqP C2. Since zÞÑFpz,bq is holomorphic, by the Cauchy Integral Formula
Fpa,bq“ 1
2πi
ż
|z´a|“r1
Fpz,bq
z´a dz.
Similarly, for each z, the function wÞÑFpz,wq is holormophic, so
Fpz,bq“ 1
2πi
ż
|w´b|“r2
Fpz,wq
w´b dw.
Therefore,
Fpa,bq“ 1
p2πiq2
ż
|z´a|“r1
1
pz´aq
«ż
|w´b|“r2
Fpz,wq
pw´bq dw
ﬀ
dz.
Now, because F is continuous on C2, Fubini’s theorem allows us to rewrite this iterated integral as a
multiple integral:
Fpa,bq“ 1
p2πiq2
ż
T1ˆT2
Fpz,wq
pz´aqpw´bqdwdz,
where T1“t|z´a|“ r1u, T2“t|w´b|“ r2u. Thus,
fpzq“ Fpz,zq“ 1
p2πiq2
ż
T1ˆT2
Fpζ,ξq
pζ´zqpξ´zqdζdξ,
132

Since F is continuous on the compact set T1ˆT2, we can now simply diﬀerentiate under the integral sign
to see that f is holomorphic. (Note: this proof actually shows that F is holomorphic on C2, i.e. has a
convergent power series in two variables.)
Problem 8. Determine the supremum of ⏐⏐⏐⏐
Bu
Bxp0, 0q
⏐⏐⏐⏐
among all harmonic functions u : DÑr 0, 1s.
Solution. The answer is 2 {π. Since D is simply connected, any such u is the real part of an analytic
function f “u`iv : DÑS :“tzP C : 0ď Repzqď 1u. Adding a pure imaginary constant doesn’t change
anything, so we can assume fp0q is real. We have f1“ux`ivy, so we want to bound Re pf1p0qq. Since we
can pre-compose f with a rotation without changing the absolute value of f1 or changing the codomain of
f, this is the same as bounding |f1p0q|. This shows that the desired supremum is the same as the supremum
of|f1p0q| over all f : DÑ S holomorphic with fp0qP R. Let f be such a function. Let T : S Ñ D be the
conformal map given by
Tpzq “ exppiπzq´ i
exppiπzq` i.
Let α“Tpfp0qq and let ψpzq“ z´α
1´αz be the automorphism of D that sends α to 0. Then g“ψ˝T˝f is a
holomorphic function DÑ D withgp0q“ 0. So by the Schwarz lemma we have|g1p0q|ď 1. Now we compute
|g1p0q| “ |ψ1pαq||T1pfp0qq||f1p0q| “ 1
1´|α|2|T1pfp0qq||f1p0q| ě |T1pfp0qq||f1p0q|
ě 2π
⏐⏐⏐⏐
exppiπfp0qq
pexppiπfp0qq` iq2
⏐⏐⏐⏐ “
⏐⏐⏐⏐
2π
2i` 2i Impexppiπfp0qqq
⏐⏐⏐⏐ ě π
2
because exppiπfp0qq lies on the top half of the unit circle because fp0qPr 0, 1s. Therefore we conclude
1 ě |g1p0q| ě π
2|f1p0q|,
which shows that 2{π is an upper bound for the desired quantity. Now taking
fpzq “ T´1pzq “ 1
iπ log
ˆi`iz
1´z
˙
,
where the log here is well-deﬁned because i`iz
1´z P H for all zP D, it’s easy to calculate that |f1p0q|“ 2{π, so
it must be the supremum and it’s actually attained.
Problem 9. Consider the formal product
8ź
n“1
ˆ
1` 1
n
˙z´
1´ z
n
¯
.
(a) Show that the product converges for any zPp´8, 0q.
(b) Show that the resulting function extends from this interval to an entire function of zP C.
Solution.
(a) For zPp 0,8q we have
1´ z
n “ 1`´z
n ď
ˆ
1` 1
n
˙´z
by Bernoulli’s inequality (or simply by looking at the generalized binomial expansion of the term on
the right). Thus each term in the product lies in p0, 1s. So the partial products form a decreasing
sequence of positive real numbers and therefore the product converges.
133

(b) MISSING
Problem 10. Let C˚ “ CYt8u be the Riemann sphere and let Ω “ C˚zt0, 1u. Let f : Ω Ñ Ω be a
holomorphic function.
(a) Prove that if f is injective then fpΩq“ Ω.
(b) Make a list of all such injective functions f.
Solution. Part (a) follows from part (b) by just examining the list of all possible functions and observing
that each of them is surjective. For part (b) we ﬁrst consider the same problem on a modiﬁed region
rΩ :“ C˚zt0,8u. Let g : rΩÑ rΩ be injective and holomorphic. First we show that the injectivity implies
that when considered as a function on all of C˚, g has at worst simple poles at 0 and 8 (i.e. g has either a
removable singularity or a simple pole at 0 and 8). Essential singularities are impossible by the big Picard
theorem. To show that higher order poles are impossible, suppose g has a pole of order ě 2 at 0 (the
argument for 8 is the same). Then 1 {g has a zero of order ě 2 at 0. Let γ be a small circle around the
origin; then the argument principle says that p1{gqpγq winds twice around 0. Thus there is a neighborhood
U of 0 such thatp1{gqpγq winds at least twice around every point of U, and by the argument principle again,
this means that g achieves every value in U at least twice inside of γ. This contradicts g being injective
unless it happens to be the case that every value in U is achieved byg at one point with multiplicity 2. But
this is impossible because if gpz0q“ w0 with multiplicity 2, then g1 vanishes atz0. So if the above situation
happened, then g1 would be identically zero on pg1q´1pUq, which is an open set, so by uniqueness of analytic
continuation this would imply that g1 is identically zero, which is also a contradiction. Thus we conclude
that g has at worst simple poles at 0 and 8.
Therefore we have the representationgpzq“ a{z`b`cz for somea,b,c P C. But note that by hypothesis,
gpzq is never 0 forzP rΩ. The equation a{z`b`cz“ 0 always has a nonzero, non-inﬁnite solution ifa‰ 0‰c,
so we must have a“ 0 or c“ 0. And in either case, we must then also have b“ 0 to avoid achieving 0. So
the only possible functions g are gpzq“ az and gpzq“ a{z with a‰ 0.
Now let f : Ω Ñ Ω be injective and holomorphic. This induces an injective holomorphic function
g“T´1fT : rΩÑ rΩ whereTpzq“ z{pz` 1q is an automorphism of C˚ sending 0 to 0 and8 to 1. Therefore
by the above we have
gpzq “ fpz{pz` 1qq
fpz{pz` 1qq´ 1 “ az or a
z.
After simplifying everything and changing variables w“ z{pz` 1q we ﬁnd that the only possibilities for f
are
fpwq “ 1` w´ 1
pa´ 1qw` 1, f pwq “ 1` w
pa´ 1qw´a for some a‰ 0.
Since az and a{z are both surjective as maps rΩÑ rΩ, and we got the possibilities for f by composing with
conformal maps, it’s clear that both of these possibilities are surjective as maps from Ω Ñ Ω.
Comment Instead of using the big Picard theorem as above, we can cite the much simpler Casorati-
Weierstrass theorem.
Problem 11. For R ą 1 let AR be the annulus t1 ă |z| ăRu. Assume there is a conformal mapping
F from AR1 ontoAR2. Prove that R1“R2.
Solution. See Spring 2017 #7.
Problem 12. Let fpzq be bounded and holomorphic on the unit disc D. Prove that for any w P D we
have
fpwq “ 1
π
ż
D
fpzq
p1´zwq2 dApzq,
134

where dApzq means integration with respect to Lebesgue measure.
Solution. Considerf as an element of the Bergman spaceA2pDq :“
␣
f : DÑ C holomorphic :
ş
D|fpzq|2dApzqă8
(
.
This is a Hilbert space with inner product
xf,gy “
ż
D
fpzqgpzqdApzq
and orthonormal basis
!
zÞÑ
b
n`1
π zn
)8
n“0
(It’s easy to check that these are actually an inner product and
orthonormal basis). For each ﬁxed wP D, we ﬁrst show the map f ÞÑ fpwq is a bounded linear functional
on A2. We have
|fpwq| “
⏐⏐⏐⏐⏐⏐⏐
1
π
´
1´|w|
2
¯2
ż
Bpw,p1´|w|q{2q
fpzqdApzq
⏐⏐⏐⏐⏐⏐⏐
À
˜ż
Bpw,p1´|w|q{2q
|fpzq|2dApzq
¸1{2
ď ||f||A2
where the equality is by the mean value property of holomorphic functions and the ﬁrst inequality is by
Cauchy-Schwarz. Thus fÞÑfpwq is bounded, and it’s clearly linear.
Thus by the Riesz representation theorem, for each wP D there is a function gwPA2 such that
fpwq “ xf,gwy “
ż
D
fpzqgwpzqdApzq
for all f PA2. So we just need to show that gwpzq“ 1
πp1´wzq2 . By deﬁnition of the functions gw, for any z
we have
gwpzq “ xgw,gzy “
8ÿ
n“0
xgw,enyxgz,eny by Parseval (wheretenu is the orthnormal basis mentioned above)
“
8ÿ
n“0
xen,gwyxen,gzy “
8ÿ
n“0
enpwqenpzq “
8ÿ
n“0
1
πpn` 1qpwzqn “ 1
πp1´wzq2.
Alternative Solution
If w“ 0 this is the mean value property for analytic functions, so assume w‰ 0. Let
dz“dx`idy, dz“dx´idy;
then
dz^dz“ 2idx^dy.
Also let
Bg
Bz “ 1
2
ˆBg
Bx´iBg
By
˙
,
Bg
Bz “ 1
2
ˆBg
Bx`iBg
By
˙
,
for any function g. Then
dg“ Bg
Bxdx`Bg
Bydy“ Bg
Bzdz`Bg
Bzdz.
Now, since f is analytic, we have
B
Bz
" fpzq
1´wz
*
“ wfpzq
p1´wzq2.
135

Thus, the 2-form in the integrand equals
fpzqdx^dy
p1´wzq2 “ 1
2idF,
where F is the 1-form
F “ fpzqdz
wp1´wzq.
Therefore, by Stokes’ theorem,
1
π
ż
D
fpzqdx^dy
p1´wzq2 “ 1
2πi
ż
D
dF “ 1
2πi
ż
BD
F “ 1
2πiw
ż
BD
fpzqdz
1´wz
“ 1
2πiw
ż
BD
zfpzq
z´wdz“ 1
wwfpwq“ fpwq,
by the Cauchy integral formula.
In general, if f : D Ñ C is analytic and bounded, let frpzq “fpzq for 0 ă r ă 1. Then fr is analytic
on the larger disc Dp0, 1{rq and hence by the above
frpwq“ 1
π
ż
D
frpzq
p1´wzq2dApzq.
By continuity,frpwqÑ fpwq as rÑ 1. Moreover, frÑf pointwise on D, and since f,fr are bounded, the
dominated convergence theorem implies
fpwq“ lim
rÑ1
frpwq“ lim
rÑ1
1
π
ż
D
frpzq
p1´wzq2dApzq“ 1
π
ż
D
fpzq
p1´wzq2dApzq.
136

20 Fall 2018
Problem 1. Lettfnu be a sequence of real-valued Lebesgue measurable functions on R, and letf be another
such function. Assume that
(a) fnÑf Lebesgue almost everywhere
(b)
ş
|x||fnpxq|dxď 100 for all n, and
(c)
ş
|fnpxq|2dxď 100 for all n.
Prove that fnPL1 for all n, that fPL1, and that ||fn´f||L1Ñ 0. Also show that neither assumption (b)
nor assumption (c) can be omitted while making these deductions.
Solution. To show that fnPL1, note that
ż
R
|fn| “
ż
|x|ď1
|fn|`
ż
|x|ą1
|fn| ď
˜ż
|x|ď1
|fn|2
¸1{2
21{2`
ż
|x|ą1
|x||fnpxq| ď C ă 8
for some constant C independent of n by hypotheses (b) and (c). Now to show that f P L1, note that by
Fatou’s lemma we have
ż
|f| “
ż
lim inf
nÑ8
|fn| ď lim inf
nÑ8
ż
|fn| ď C ă 8.
Now we show fnÑf in L1. First we need two “uniformity” estimates:
ż
|x|ąR
|fn| ď
ż
|x|ąR
|x|
R|fn| À 1
R
ż
E
|fn| ď mpEq1{2
ˆż
E
|fn|2
˙1{2
À mpEq1{2.
where the implied constant is independent of n in both. By the same Fatou’s lemma argument, the above
estimates also hold for f. Let ϵą 0. Let R be big enough so that
ş
|x|ąR|fn|ă ϵ for all n and
ş
|x|ąR|f|ă ϵ.
By Egorov’s theorem, there is a set EĎt|x|ď Ru on which fnÑf uniformly, and by the second estimate
above we may pick mpEcq to be small enough so that
ş
Ec|fn|,
ş
Ec|fn|ă ϵ. Then we have
ż
|fn´f| “
ż
|x|ąR
|fn´f|`
ż
E
|fn´f|`
ż
Ec
|fn´f|
ď
ż
|x|ąR
|fn|`
ż
|x|ąR
|f|`
ż
E
|fn´f|`
ż
Ec
|fn|`
ż
Ec
|f|
ă 4ϵ`
ż
E
|fn´f|.
TakingnÑ8 , since we have uniform convergence on E, gives
lim sup
nÑ8
|fn´f| ă 4ϵ.
This holds for any ϵą 0, so the result follows.
Problem 2. Let pX,ρq be a compact metric space which has at least two points, and let CpXq be the
space of continuous functions X Ñ R with the uniform norm. Let D be a dense subset of X and for each
yP D deﬁne fy P CpXq by fypxq“ ρpx,yq. Let A be the subalgebra of CpXq generated by the collection
tfy :yPDu.
(a) Prove that A is dense in CpXq under the uniform norm.
(b) Prove that CpXq is separable.
Solution. (a) By one version of the Stone-Weierstrass theorem, it’s enough to check that A separates
137

points (for all x‰yPX there exists fPA withfpxq‰ fpyq) and is nonvanishing (for all xPX there exists
fPA withfpxq‰ 0). Both of these are easily veriﬁed because X has at least two points by hypothesis. For
separating points, given x‰y let f“fy. For nonvanishing, given x let f“fy for any y‰x.
(b)
Problem 3. LetpX,ρq be a compact metric space and let PpXq be the set of all Borel probability measures
on X. Assume µnÑµ in the weak-˚ topology on PpXq. Prove that µnpEqÑ µpEq wheneverE is a Borel
susbet of X such that µpEq“ µpE˝q, where E is the closure and E˝ is the interior.
Solution. Applying the portmanteau theorem twice, since E˝ is open and E is closed, we have
µpE˝q ď lim inf
nÑ8
µnpE˝q ď lim inf
nÑ8
µnpEq ď lim sup
nÑ8
µnpEq ď lim sup
nÑ8
µnpEq ď µpEq
But by hypothesis, µpE˝q“ µpEq, so every inequality in the chain is actually an equality. Since µpEq also
necessarily ﬁts somewhere in between µpE˝q and µpEq, which are equal, we conclude
lim inf
nÑ8
µnpEq “ lim sup
nÑ8
µnpEq “ µpEq.
Problem 4. Let T be the unit circle in the complex plane and for each α P T deﬁne the rotation map
Rα : TÑ T by Rαpzq“ αz. A Borel probability measure µ on T is called α-invariant ifµpRαpEqq“ µpEq
for all Borel sets EĎ T.
(a) Let m be Lebesgue measure on T. Show that for every αP T, m is α-invariant.
(b) Prove that if α is not a root of unity, then the set of powers tαn :nP Zu is dense in T.
(c) Prove that if α is not a root of unity, then m is the only α-invariant Borel probability measure on T.
Solution. Throughout, we identify T with the interval r0, 1q in the natural way, so “ α is not a root of
unity” is replaced by “α is irrational”.
(a) When viewed as a map onr0, 1q,Rαpxq“ x`α pmod 1q. We know that Lebesgue measure is translation
invariant, soRα is measure preserving when considered as a mapr0, 1qÑ R. But in the case whereEĎr 0, 1q
hasRαpEqXr 1,8q‰H ,RαpEq may be reassembled as a subset of r0, 1q by just translating RαpEqXr 1,8q
to the left by 1, which still preserves Lebesgue measure. Thus Rα preservesm.
(b) Method 1. It’s enough to show tnα : n ě 0u is dense in T. Since α is irrational, the orbit con-
tains inﬁnitely many distinct points. Therefore by the pigeonhole principle, for every ϵą 0 there exist some
năm such that ||nα´mα||Tăϵ (||¨||T denotes “mod 1” distance). Therefore the rotation xÞÑpm´nqα
is a rotation by less than ϵ, so tjpm´nqα :jě 0u is a subset of the orbit such that every point of T is at
most ϵ away from some jpm´nqα. Such subsets exist for any ϵą 0, so the orbit is dense.
(b) Method 2. It’s enough to show tnα : n ě 0u is dense in T. In fact we show a stronger result
which is the equidistribution theorem, i.e. for any 0 ďaăbď 1,
lim
NÑ8
#tn :aďnαďbu
N “ b´a.
For anyfPL1pTq, set
ANf :“ 1
N
N´1ÿ
n“0
fpnαq, I pfq :“
ż
T
fdm.
The ﬁrst step is to show that for f P CpTq, ANf Ñ Ipfq as N Ñ8 . It’s easy to see that this property is
linear and behaves well under L8 approximation, so since trig polynomials are dense in CpTq, it’s enough
138

to show that this result holds for fpxq“ expp2πikxq for any kP Z. We calculate directly
ANf “ 1
N
N´1ÿ
n“0
expp2πikαqn “ 1
N
#
N k “ 0
1´expp2πiNkαq
1´expp2πikαq k‰ 0 “
#
1 k“ 0
Okp1{Nq k‰ 0
because expp2πikαq‰ 1 for all k‰ 0 because α is irrational. Thus
lim
NÑ8
ANf “
#
1 k“ 0
0 k‰ 0 “ Ipfq.
To ﬁnish the proof, we want to apply this convergence to the characteristic function χra,bs, but it’s not
continuous, so we have to approximate. Take sequences fk,gk of continuous functions satisfying 0 ď gk ď
χra,bsďfkď 1 with fk and gk both converging Lebesgue almost everywhere to χra,bs. Then we have
ANgk ď ANχra,bs ď ANfk, I pgkq ď Ipχra,bsq ď Ipfkq.
TakingNÑ8 then gives
Ipgkq ď lim inf
NÑ8
ANχra,bs ď lim sup
NÑ8
ANχra,bs ď Ipfkq,
and by the Dominated Convergence Theorem taking kÑ8 gives
Ipχra,bsq ď lim inf
NÑ8
ANχra,bs ď lim sup
NÑ8
ANχra,bs ď Ipχra,bsq,
so they are all equal, as desired. This ﬁnishes the proof because lim NÑ8ANχra,bs is exactly the expression
on the left side and Ipχra,bsq is exactly the expression on the right side of the desired equation.
(c) Method 1. It’s enough to show that
ş
fdµ “
ş
fdm for all fPCpTq. Write
ż
fpxqdµpxq´
ż
fpzqdmpzq “
ż ż
pfpxq´ fpzqqdmpzqdµpxq “
ż ż
pfpxq´ fpx`zqqdmpzqdµpxq
“
ż ż
pfpxq´ fpx`zqqdµpxqdmpzq
where the last equality is by Fubini and the second to last equality is by the translation invariance of m.
So it suﬃces to show that
ş
pfpxq´ fpx`zqqdµpxq “0 for each ﬁxed z P T. By the density from part
(b), there is a subsequence njα Ñ z as j Ñ 8. Thus since f is continuous and T is compact, we have
fpx`njαq Ñfpx`zq uniformly over xP T as j Ñ 8. Therefore, since we are assuming µ is invariant
under rotations by α, we have
ż
pfpxq´ fpx`zqqdµpxq “
ż
fpxqdµpxq´
ż
fpx`zqdµpxq “
ż
fpx`njαqdµpxq´
ż
fpx`zqdµpxq
for every j, and taking jÑ8 makes the right side equal to 0 because the convergence is uniform and f is
continuous.
(c) Method 2 (motivated by ergodic theory). Suppose α is irrational. Then if f is a trig polyno-
mial, the same direct calculation from part (b) shows that
ANfpxq :“ 1
N
N´1ÿ
n“0
fpx`nαqÑ
ż
T
fdm
asNÑ8 for any ﬁxedxP T. Let µ be anyRα-invariant measure. Then since trig polynomials are bounded,
the Dominated Convergence Theorem gives
ż
ANfdµ Ñ
ż ˆż
fdm
˙
dµ “
ż
fdm.
139

But since µ is Rα-invariant, the left side is equal to
ş
fdµ for all N. Thus
ş
fdµ “
ş
fdm for all trig poly-
nomialsf, and by density they are equal for allfPCpTq, so by the Riesz representation theoremµ“m.
Problem 5. Lettfnu be a sequence of continuous real-valued functions on r0, 1s and suppose fnpxq con-
verges to another real valued function fpxq at everyxPr 0, 1s.
(a) Prove that for every ϵą 0 there is a dense subset DϵĎr 0, 1s such that if xPDϵ then there are an open
intervalIQx and a positive integer Nx such that for all nąNx, supyPI|fnpyq´ fpyq|ď ϵ.
(b) Prove that f cannot be the characteristic function χQXr0,1s.
Solution.
Problem 6. Let f P L2pRq and assume the Fourier transform satisﬁes
⏐⏐⏐pfpξq
⏐⏐⏐ ą 0 for Lebesgue almost
everyξP R. Prove the set of ﬁnite linear combinations of the translates fypxq“ fpx´yq is norm dense in
L2pRq.
Solution. See Spring 2012 # 6.
Problem 7. Let fpzq be an analytic function on the entire complex plane C such that the function
Upzq“ log|fpzq| is Lebesgue area integrable. Prove f is constant.
Solution. See Spring 2013 # 7.
Problem 8. Let D be the space of analytic function fpzq on the unit disc D such that fp0q “ 0 andş
D|f1pzq|2dxdy ă8 .
(a) Prove D is complete in the norm
||f|| “
ˆż
D
|f1pzq|2dxdy
˙1{2
.
(b) Give a necessary and suﬃcient condition on the coeﬃcients an for the function fpzq “ř
ně1anzn to
belong to D.
Solution. (a) Let fn be a Cauchy sequence in D. Then by deﬁnition, f1
k is a Cauchy sequence in L2pDq.
Since L2 is known to be complete, there is some g with f1
k Ñ g in L2pDq. We need to show that g is
holomorphic, and for this we use the standard trick. Fix 0 ără 1, then for any |z|ď r and any f P D we
have
|f1pzq| “
⏐⏐⏐⏐⏐
ż
Bpz,p1´rq{2q
f1pwqdApwq
⏐⏐⏐⏐⏐ ď
ż
Bpz,p1´rq{2q
|f1pwq|dApwq Àr
˜ż
Bpz,p1´rq{2q
|f1pwq|2dApwq
¸1{2
ď ||f||D,
so||f1||L8pBp0,rqqÀr ||f||D. Thus, since fn is a Cauchy sequence in D, f1
n is a uniformly Cauchy sequence
on Bp0,rq. Since L8
´
Bp0,rq
¯
is complete, we see that f1
n converges uniformly to some limit function on
Bp0,rq. This holds for any r ă 1, so f1
n has a locally uniform limit on D. But since f1
n Ñ g in L2pDq, it
has a subsequence converging pointwise to g, so in fact f1
n Ñ g locally uniformly on D, which implies g is
holomorphic. Let G be the unique primitive of g with Gp0q“ 0. Then ||fn´G||D“||f1
n´g||L2pDqÑ 0, so
D is complete.
(b) We havef1pzq“ ř
ně1nanzn´1. Write this as f1preiθq“ ř
ně1nanrn´1eipn´1qθ and then we have
⏐⏐f1preiθq
⏐⏐2
“
ÿ
n,kě1
nkanakrn`k´2eipn´kqθ,
140

so
ż
D
|f1pzq|2dxdy “
ż 1
0
ż 2π
0
ÿ
n,kě1
nkanakrn`k´2eipn´kqθrdθdr
“
ż 1
0
ÿ
n,kě1
nkanakrn`k´1
ż 2π
0
eipn´kqθ because the series converges uniformly on compact sets
“
ż 1
0
ÿ
ně1
n2 |an|2r2n´1dr by orthonormality
“
ÿ
ně1
n2 |an|2
ż 1
0
r2n´1dr by the Monotone Convergence Theorem
“ 1
2
ÿ
ně1
n |an|2.
Thus a necessary and suﬃcient condition is that ř
ně1n |an|2ă8 .
Problem 9. Consider the meromorphic function gpzq“´ πz cotpπzq on the entire plane C.
(a) Find all poles of g and determine the residue of g at each pole.
(b) In the Taylor series representation ř8
k“0akzk of gpzq about z“ 0, show that for each kě 1
a2k “
ÿ
ně1
2
n2k.
Solution. See Spring 2013 # 11.
Problem 10. For´1ăβă 1 evaluate ż8
0
xβ
1`x2 dx.
Solution. See Spring 2014 # 11.
Problem 11. An analytic Jordan curve is a set of the form Γ “ fpt|z| “ 1uq where f is analytic
and one to one on an annulus tră| z|ă 1{ru, 0 ă ră 1. Let C˚ “ CYt8u be the Riemann sphere, let
N ă8 , and let Ω Ď C˚ be a domain for which BΩ has N connected components, none of which are single
points. Prove there is a conformal mapping from Ω onto a domain bounded by N pairwise disjoint analytic
Jordan curves.
Solution.
Problem 12. If α P C satisﬁes 0 ă |α| ă1 and if n ě 1, show that the equation ezpz´ 1qn “ α has
exactly n simple roots in the half plane tRepzqą 0u.
Solution.
141

