MATHEMATICAL TRIVIUM
Legend:
/ClockLogo: hardworking, i.e. long exercise
/Radioactivity: hard exercise
P : creative exercise
LINEAR ALGEBRA
1. Describe the ﬁgures that can be obtained as intersection of the conez2 = x2+y2
with the planez −ax =1 ,0 <a< ∞,i nR3.
2. Consider the matrixA =
[ 12
54
]
.
(a) Find AT, A2, A3, A−1,T rA,d e tA.
(b) Find the eigenvalues and the eigenvectors ofA.
(c) Write the transformation that reducesA to diagonal form.
3. Find if the vectors
⎡
⎣
1
2
3
⎤
⎦,
⎡
⎣
1
3
5
⎤
⎦,
⎡
⎣
5
13
15
⎤
⎦ are linear independent or not.
4. Let A be a non-degenerate matrix, andB is obtained fromA by interchange two
of its lines. How are detA and detB related?
5. Let A and B be non-degenerate n × n matrices, c ∈ C. Write the relations
between their determinants, if
(a) B = A
T,( b ) B = A−1,( c ) B = c·A.
6. P Let A be a non-degenerate matrix. Show that logdetA =T rl o gA.
7. Let A = E + ϵB,w h e r eE is the identity matrix andϵ≪ 1. Expand detA to
the ﬁrst order inϵ.
8. Let A, B, C, D be non-degenerate matrices of the same dimension. Show that
det
[ AB
CD
]
=d e t
(
AD−BD−1CD
)
. (1)
9. Calculate detA,i f
A =
⎡
⎢⎢
⎢
⎢
⎢⎣
111 ... 1
101 ... 1
110 ... 1
..
. ..
. ..
. ... ..
.
111 ... 0
⎤
⎥⎥
⎥
⎥
⎥⎦
. (2)
1

10. Calculate the eigenvalues and the eigenvectors of the matrix
A =
⎡
⎢⎢
⎢
⎢
⎢⎣
000 ... 01
100 ... 00
010 ... 00
... ... ..
. ... ..
. ..
.
000 ... 10
⎤
⎥⎥
⎥
⎥
⎥⎦
. (3)
11. Consider the Vandermonde matrix
V(x1,...,x n)=
⎡
⎢⎢
⎢
⎢
⎢⎣
111 ... 1
x
1 x2 x3 ... x n
x2
1 x2
2
x2
3
... x 2
n
..
. ..
. ..
. ... ..
.
x
n−1
1 xn−1
2 xn−1
3 ... x n−1
n
⎤
⎥⎥
⎥
⎥
⎥⎦
. (4)
(a) Calculate detV(x
1,...,x n).
(b) Show that detV(x1,...,x n) = 0 if and only ifxi = xj for somei ⁄= j.
12. Consider the Wronskian
Wx(y1,...,y n)=d e t
⎡
⎢⎢
⎢⎢
⎢⎣
y
1 y2 y3 ... y n
y′
1 y′
2 y′
3 ... y ′
n
y′′
1 y′′
2 y′′
3 ... y ′′
n
..
. ..
. ..
. ... ..
.
y
(n−1)
1 y(n−1)
2 y(n−1)
3 ... y (n−1)
n
⎤
⎥⎥
⎥
⎥
⎥⎦
, (5)
where y
1,...,y n are Cn−1 functions ofx.
(a) Let y1 and y2 be two solutions of the diﬀerential equationy′′−ay′−by =0 ,
where a and b are some known functions ofx. Find an expression for the
WronskianWx(y1,y2) depending ona and b. Then, show that if one of the
solutions, say,y1, is known, then another can be found from the ﬁrst order
equation y′
1 − y′
2
y2
y1 + Wx(y1,y2)
y2
=0 .
(b) Show that under change of variablex → t(x) the Wronskian transforms as
follows,
Wx(y1,...,y n)=
( dt
dx
)n(n−1)
2
Wt(y1,...,y n). (6)
(c) Show thatWx(yy1,...,yy n)= ynWx(y1,...,y n), wherey is someCn−1 func-
tion.
13. Consider the matricesA =
[ cosφ −sinφ
sinφ cosφ
]
, B =
[ cosφ sinφ
sinφ −cosφ
]
.
(a) Calculate A−1, B−1.
(b) Give a geometrical interpretation of the action ofA and B on vectors in
R2.
(c) What can one say about the eigenvectors ofA and B?
2

14. LetAbearealmatrixwith(det A)2 = 1.Giveaconclusionaboutorthogonality
of A.
15. Let A be n×n real orthogonal matrix. Calculate the number of independent
elements ofA.
16. Construct the matrix that performs a reﬂection inR3
(a) across the originO,
(b) across the axisOz,
(c) across the planexOy.
17. Consider the reﬂection maps inRn. The reﬂection across the origin transforms
every vector⃗x ∈ Rn to −⃗x. The reﬂection across one of the basis axisOi inverts
all coordinates of⃗x except xi. Similarly, one can deﬁne the reﬂections across the
planes in R3 and higher dimensional hyperplanes inRn, n> 3. Some of these
reﬂections are equivalent to rotations around the originO, others are not.
(a) Observe that inR2 the central reﬂection is equivalent to the rotation by an
angle π around O. Show that no reﬂections across a line crossingO can be
achieved by any rotation.
(b) In R3, ﬁnd if one can achieve by some rotation aroundO 1) the reﬂec-
tion acrossO, 2) the reﬂection across an arbitrary line crossingO,3 )t h e
reﬂection across an arbitrary plane crossingO.
(c) In Rn, formulate and prove a general statement about the existence of
rotations that perform the reﬂection across a givenm-dimensional plane,
m =0 ,1,...,n −1, crossing the origin (wherem = 1 corresponds to the line,
and m = 0 - to the point).
18. /ClockLogoConsider the rotation by an angle θ around a line determined by a unit
radius-vector ⃗n with componentsnx,ny,nz.
(a) Deduce the rotation matrix that performs this rotation.
(b) Relate the trace of this matrix to the angleθ.
19. Consider the Pauli matrices,σ1 =
[01
10
]
, σ2 =
[0 −i
i 0
]
, σ3 =
[10
0 −1
]
.
(a) Calculate σ†
i, i =1 ,2,3.
(b) Decompose a matrixA =
[ ab +ic
b−ic −a
]
, a,b,c ∈ R,i n t oas u mo fσi.
(c) Prove thatσi, i =1 ,2,3, constitute a basis in the space of 2×2h e r m i t i a n
matrices with zero trace.
(d) Prove that {σi,i =1 ,2,3; 1} constitute a basis in the space of 2× 2
hermitian matrices.
(e) Calculate the eigenvalues and the eigenvectors ofσi, i =1 ,2,3.
20. Let σi, i =1 ,2,3 be the Pauli matrices.
(a) Calculate [σi,σj] ≡ σiσj −σjσi, i,j =1 ,2,3.
3

(b) Calculate {σi,σj}≡ σiσj +σjσi, i,j =1 ,2,3.
(c) Calculate [σi,[σj,σk]]+[ σj,[σk,σi]]+[ σk,[σi,σj]].
21. P Consider the linear transformationsA, B of the vector spaceRn. Prove that
[A,B] ⁄= cE,w h e r eE is the identity matrix,c ∈ R.
22. Consider the transformationsA, B of the vector spaceRn sharing the same
eigenvectors. Is this suﬃcient for their commutator to be zero? Is this necessary
for their commutator to be zero?
23. Consider the basis⃗ei, i =1 ,2,3, in the vector spaceR3. In this basis, write the
matrix of the transformation that
(a) stretches all directions by a factor ofλ.
(b) stretches each direction along⃗ei by a factor ofλi, i =1 ,2,3.
(c) stretches the direction determined by a unit vector ⃗n with components
nx,ny,nz by a factor ofλ.
Find the eigenvectors of these transformations.
24. Show that the translation⃗x → ⃗x+⃗a,w h e r e⃗x,⃗a ∈ Rn, is not a linear transfor-
mation inRn.
25. Alineartransformation Awritesinsomebasisin Rn asfollows, A =
⎡
⎣
021
282
120
⎤
⎦.
(a) Write the transition matrix to the basis composed of the eigenvectors ofA.
(b) Write the transformationA in this basis.
(c) Determine the invariant subspaces ofA.
26. P Describe the linear transformations whose invariant subspaces are
(a) 3-dimensional spherex2
1 +x2
2 +x2
3 = R2 in R3,
(b) 4-dimensional conex2
1 −x2
2 −x2
3 −x2
4 =0i n R4,
(c) n-dimensional hyperboloidx2
1 +...+x2
p −x2
p+1 −...−x2
n = R2 in Rn.
27. For the vectorsA =
⎡
⎣
1√
2√
3
⎤
⎦, B =
⎡
⎣
0√
2
2
⎤
⎦ ﬁnd an orthogonal transformation that
maps A to B.
28. Consider the vectors⃗a1 and ⃗a2 in R2 with the lengths|⃗a1| =2 ,|⃗a2| =6a n d
the angle between themφ = π
6. Construct the orthonormal basis⃗e1,⃗e2 such that
⃗e1||⃗a1, and write the components of⃗a1, ⃗a2 in this basis.
29. Consider the inﬁnite dimensional vector space with the orthonormal basis⃗ei,
i =1 ,2,.... Construct the continuous family of linear transformations U(λ),
0 ⩽ λ ⩽ 1,actinginthisspacesuchthat U(1) =E andU(0)⃗ei =⃗ei+1,i =1 ,2,....
4

30. Let U be n×n unitary matrix. Calculate the number of independent elements
of U.
31. Deﬁne the matrix exponential eA of a matrix A as follows: eA =
∞∑
n=0
An
n! .
Consider the following matrices
Mx =
⎡
⎣
00 0
00 −1
01 0
⎤
⎦,M y =
⎡
⎣
00 1
00 0
−100
⎤
⎦,M z =
⎡
⎣
0 −10
100
000
⎤
⎦. (7)
(a) Write TrMi, MT
i , i = x,y,z .
(b) Calculate eθMx, eθMy, eθMz,w h e r eθ ∈ [0,2π).
(c) Give a geometrical interpretation of the transformationseθMi, i = x,y,z ,
acting on the vectors inR3.
32. Consider the matrices A, B such that [A,B] = 0. Show that in this case
eAeB = eBeA = eA+B.
33. Prove thateA =
(
eA/N)N
, N ∈ R.
34. Consider the matricesA, B and letλ ≪ 1 be a small parameter. Expand the
expression e−λBAeλB
(a) to the ﬁrst order inλ.
(b) to any order inλ.
35. A linear transformation is given by the matrixeA in some basis inRn. Consider
the change of the basis determined by the transition matrixU. Find the matrix
of the transformation in the new basis.
36. P ”Trotter product formula”. Considern × n complex matrices A, B.P r o v e
that eA+B = lim
N→∞
(
eA/NeB/N)N
, N ∈ R.
37. Write the following matrixA as a productA = SO of a symmetric matrixS
and an orthogonal matrixO.
(a) A =
[50
43
]
,( b ) A =
[00
4 −3
]
.
In which case is such decomposition unique?
38. Consider the matrixA =
[ab
cd
]
, a,b,c,d ∈ R,d e tA = 1. It transforms the
basis vectors ⃗e1 =
[1
0
]
, ⃗e2 =
[0
1
]
into ⃗g1 =
[a
c
]
, ⃗g2 =
[b
d
]
. One can obtain a
useful decomposition ofA by making an inverse transformation in three steps.
(a) Construct the rotation matrixR−1 that sends⃗g1 to R−1(⃗g1)‖⃗e1.H o wd o e s
it act on⃗g2?
(b) Constructthediagonalmatrix P−1 suchthatdet P−1 =1a n dP−1(R−1(⃗g1)) =
⃗e1. Show that the components ofP−1(R−1(⃗g2)) are
[x
1
]
, x ∈ R.
5

(c) Applyasheartransformation T−1 thatleaves ⃗e1 invariantandsends P−1(R−1(⃗g2))
to ⃗e2. Then, we haveT−1P−1R−1A = E,o rA = RPT .
(d) Show that this decomposition is unique.
39. Solve the system of linear equations
⎧
⎨
⎩
y +3z = −1
2x+3y +5z =3
3x+5y +7z =6
(8)
40. Solve the following systems of linear equations
(a)
⎧
⎨
⎩
x+y +z =0
x+2y +3z =0
2x+3y +4z =0
(b)
{ x1 +x2 +x3 −x4 =0
3x1 +2x2 +x3 −x5 =0
41. Check if the system of linear equations has a solution and solve
⎧
⎨
⎩
x+2y +3z = −4
2x+3y +4z =1
3x+4y +5z =6
(9)
42. Checkifthefollowingpointsbelongtothesameplane:(6 ,1,2),(2,3,1),(3,4,1),
(6,2,2).
43. Consider two lines formed by intersection of the planes,
l1 =
{ 3x+2y +5z −1=0
−x+2y +3z −1=0 ,l 2 =
{ 4x−6y +7z +2=0
5x+3y −8z −3=0 . (10)
Find out if these lines are
(a) parallel to each other,
(b) crossing each other at some point.
44. Consider the quadratic formf(⃗x)=2 x2
1 +4 x1x2 +3 x2
2 +4 x2x3 +5 x2
3,w h e r e
xi, i =1 ,2,3 are components of⃗x in R3.
(a) Reduce f(⃗x) to the canonical form. Calculate its rang and signature.
(b) Write the transition matrix to the basis wheref(⃗x) has the canonical form.
45. Find if the quadratic formf(⃗x)=9 x2
1 +6x1x2 +6x2
2 +8x2x3 +4x2
3 is positive
deﬁnite or not.
46. Reduce the following quadratic forms to the canonical form and determine the
rank and the signature:
(a) x2
1 +2
n∑
i=2
x2
i −2
n−1∑
i=1
xixi+1,( b )
n∑
i=1
x2
i +
∑
1⩽i<j⩽n
xixj,( c )
∑
1⩽i<j⩽n
xixj.
47. Considerthequadraticforms f(⃗x)= x2
1+2x1x2+3x2
2 andg(⃗x)=4 x2
1+16x1x2+
6x2
2 in R2.
(a) Check if at least one of these forms is sign deﬁnite.
6

Figure 1: Pitch, yaw and roll of the ship




















(b) Find the change of coordinates that reducesf(⃗x)a n dg(⃗x) to the diagonal
form.
48. /Radioactivity
You are a spaceship pilot carrying a lonely watch in front of the main dis-
play while the rest of the crew sleep in anabiosis. You can operate the spaceship
by sending commands to the main computer. You can rotate the ship by typing
the commands pitch angle ψ, yaw angle θ and roll angle φ a ss h o w no nF i g . 1 .
Besides, you can type the commandboost time T, which turns the main engine
on and accelerates the ship with the constant accelerationg during the timeT.
On the display, you see three bright stars around the pointO that depicts the
longitudinal axis of the ship, see Fig.2. Give a series of commands that arrange
them into a perfect triangle with the centerO and the sided.
7

Figure 2: Positions of the stars







 
 

REAL ANALYSIS
1. Find f′(x), iff(x)=l o ga
x, cosarcsin x, x2 +1
x3 +1 .
2. Find f′(x), iff(x)= xx.
3. Find f(n)(0), iff(x)= e− 1
x2 , x ∈ R, n> 0.
4. Find f(100)(0), iff(x)=( x100 +x)e100x.
5. /ClockLogoFind sin100 0.1 with 10% accuracy.
6. Find d
dx f(g(x))|x=0,w h e r ef(u)=c o s hu, g(u)=
√
1−u2.
7. Find the minimal value of the functionf(x)= λ
4(x2 −v2)2 −ϵx, λ,ϵ >0, to the
leading order inϵ≪ 1.
8. Find local minima and local maxima of the functionf(x,y)= xylog(x2 +y2),
(x,y) ⁄=( 0,0).
9. Find local minima and local maxima of the functionf(x,y,z )= x2 +y2 +z2 on
a surface deﬁned by equationx2
a2 + y2
b2 + z2
c2 =1 ,0 <a<b<c .
10. Consider the implicit function of three arguments,f(x,y,z ) = 0. Show that
∂z
∂y · ∂y
∂x · ∂x
∂z = −1. Give an analogue of this statement for the implicit function
of n arguments, f(x1,...,x n)=0 .
8

11. P ”Huygens problem”. Consider the ball with massM moving with velocityV
towards another ball with massm that stays at rest. After the central collision,
the second ball acquires the velocity
v = 2M
m+MV. (11)
This expression can be obtained using the momentum and energy conservation
laws for the two-body system. One can observe thatV ⩽ v ⩽ 2V as far as
0 ⩽ m ⩽ M. One may ask under what conditions the limitv ⩽ 2V can be broken
to makev arbitrary large. A possible solution is to insert a chain of balls staying
at rest with intermediate massesm1,...,m n such thatm<m 1 < ... < mn <M
between the two original bodies, and to transfer the kinetic energy of the moving
balltotheballwithmass mthroughasequenceofintermediatecentralcollisions.
(a) Applying Eq.(11) to the sequence of central collisions between the balls,
deduce how one should choose the massesm
1,...,m n to yield the maximal
velocity of the ball with massm.
(b) Assuming m ≪ M, investigate the limitn →∞ .
12. Find lim
x→0
sinx
x .
13. /RadioactivityFind lim
x→0
sintan x−tansin x
arcsinarctan x−arctanarcsin x.
14. P Find lim
(x,y)→(0,0)
f(x,y), wheref(x,y)=
{
x+ysin 1
x,x ⁄=0 ,
0,x =0 .
. Do the limits
lim
x→0
(lim
y→0
f(x,y)) and lim
y→0
(lim
x→0
f(x,y)) exist?
15. Calculate
∫ dx
tanx.
16. Calculate
∫
logxdx.
17. Calculate
∫ x5 +2
x2 −1dx.
18. Calculate
∫
e2x sinxdx.
19. Calculate
∫ dx
sinx.
20. Find
∫ ∞
0
xne−xdx, n ∈ Z, n> 0.
21. Find
∫ ∞
0
e−x2
dx.
22. Find
∫ π2
0
cos√xdx.
9

23. Find
∫ x0
0
√
1− x2
x2
0
dx.
24. Find
∫ ∞
−∞
e−x−4−x4
sin5 xdx.
25. Find
∫ ∞
√
2
dx
x+x
√
2.
26. Show that
∫ 1
0
dx
(ax+b(1−x))2 = 1
ab, a,b ∈ R.
27. For what values ofα the following integrals are convergent?
(a)
∫ 1
0
dx
xα,( b )
∫ ∞
1
dx
xα.
28. For what values ofα and β the following integrals are convergent?
(a)
∫ 1
0
dx
xα logβ x,( b )
∫ ∞
1
dx
xα logβ x.
29. Is the integral
∫ φ
0
dψ√
sin2 φ0
2 −sin2 ψ
2
convergent asφ → φ0?
30. Show that the cosine integral Cix ≡−
∫ ∞
x
cost
t dt for large enoughx can be
approximated as Cix ≈ sinx
x . Find the region ofx for which the relative error
of this approximation is less than 10−4.
31. Calculate J(y)=
∫ ∞
0
e−axsinxy
x dx, a> 0.
32. Ab o d ym o v e si n(xy)-plane along the trajectoryy =l o gc o sx. Find the path
length of the body whenx ∈ [0, π
6].
33. A helix is written in a parametric form as follows,
x = rcosφ, y = rsinφ, z = aφ, (12)
where r,a > 0 are constants andφ varies from 0 to∞. Find the length of the
helix as a function ofφ.
34. A hyperbolic spiral is written in a parametric form as follows:x = α
t cost,
y = α
t sint,w h e r eα> 0i sac o n s t a n ta n dt varies from 0 to∞. Write the
equation of this spiral in a polar coordinate system in the formr = r(θ). Draw
it schematically. Investigate the limit ofx, y and r as θ → 0.
35. Find Jacobi matrix and Jacobian for the change of coordinates inR3 from
Cartesian coordinates to
(a) spherical coordinates,
10

(b) cylindrical coordinates.
In what regions ofR3 are these coordinate changes regular?
36. Find the surface area of
(a) the two-dimensional sphereS2 of radiusR.
(b) the two-dimensional torusT2 formed by rotation of the center of a circle of
radius R1 along a circle of radiusR2, R2 >R 1.
37. Find the surface area of a body formed by rotation of a curvey =s i nx around
x-axis inR3, x ∈ [0,π].
38. Find the volume of the three-dimensional ballB3.
39. Find the volume of a body formed by rotation of the curvey = arcsinx around
x-axis inR3, x ∈ [0,1].
40. P ”20-dimensional watermelon”
(a) Find the surface area of the unitn-dimensional sphereSn.
Indication: Use the notion of Gamma function Γ(a) ≡
∫ ∞
0
e−xxa−1dx.
(b) Find the volumeVn of the unitn-dimensional ballBn.
(c) Denote byVn,a the volume of a layer of deptha adjacent to the surface of
Bn,0 <a< 1. Compute the ratioVn,a
Vn
and investigate the limitn →∞ .
(d) Assuming the watermelon rind has a thickness 0.1 of its radius, ﬁnd what
fraction of the total volume of the 20-dimensional watermelon would be
occupied by its rind.
41. Consider the vector ﬁeld ⃗A = ⃗∇log 1
r,w h e r er =
√
x2 +y2 +z2. Write the
components of this ﬁeld
(a) in Cartesian coordinates (x,y,z ),
(b) in cylindrical coordinates (r,φ,z ),
(c) in spherical coordinates (r,θ,φ ).
42. Consider the vector ﬁeld⃗A = ⃗∇1
r,w h e r er =
√
x2 +y2 +z2.
(a) Find div⃗A, ∆⃗A, curl⃗A.
(b) How do the values of div⃗A and ∆⃗A depend on the choice of coordinate
system?
43. Show that the ﬂux of the vector ﬁeld⃗A = q ⃗r
r3, q = Const, through the sphere
containing the origin equals 4πq.
44. The electric ﬁeld⃗E created by a point chargeq at a certain distance from itr
in vacuum is given by⃗E = keq ⃗r
r3,w h e r eke is a constant.
11

(a) Consider the charged ring of radiusR with the linear charge densitydq
dl ≡ ρ.
Findthetotalmagnitudeoftheelectricﬁeldcreatedbythisringatadistance
d from its center along the axis orthogonal to it.
(b) Consider the charged disk of radiusR with surface charge densitydq
dA ≡ σ.
Findthetotalmagnitudeoftheelectricﬁeldcreatedbythisdiskatadistance
dfromitscenteralongtheaxisorthogonaltoit.Investigatethelimit R →∞ .
45. Calculate the Fourier image˜f(k) of the functionf(x), iff(x)i sg i v e nb y
(a) f(x)=
{ f0,|x| ⩽ x0,
0,|x| >x 0
(b) f(x)=
{ e−ax,x /greaterorequalslant0,a > 0,
0,x < 0
46. Calculate the inverse Fourier imagef(x) of the function˜f(k)= −1
π
k
a2 +k2.
47. Find a functionf(x) such that its Fourier image˜f(p)= cf(p), where c is a
constant.
48. (a) The functions f(x)a n dg(x) are related byf(x)= g(ax). How are their
Fourier images related?
(b) The functionsf(x)a n dg(x) are related byf(x)= g(x−x0). How are their
Fourier images related?
49. Calculate the Fourier image˜f(⃗k) of the functionf(⃗r)= αe−μr
r ,w h e r er = |⃗r|,
⃗r ∈ R3,a n dα and μ are constants.
50. Calculate the Fourier image˜f(⃗k) of the functionf(⃗r)=
{ f0,r ⩽ r0,
0,r > r 0
in R3.
51. Calculate the Fourier image˜f(⃗k) of the functionf(⃗r)= f0
(1
r + 1
a
)
e− 2r
a in
R3.
52. For what values ofα the series
N∑
n=1
1
nα diverges asN →∞ ?
53. Compute the series
∞∑
n=1
(−1)n
n .
54. Compute the sum
∞∑
n=1
xn−1
n(n+1) for all possible values ofx.
55. Consider the functionJ(a)=
∞∑
n=0
ne−an deﬁned for positivea .
(a) Write an explicit expression forJ(a).
12

(b) Expand J(a) around the pointa =0u pt o O(a0).
56. Compute the seriesJ(a)=
∞∑
n=−∞
|2n+1|e−a|2n+1| for a> 0.
57. Compute the following series:
(a)
n∑
k=0
rkeikφ,( b )
n∑
k=0
rk coskφ,( c )
n∑
k=0
rk sinkφ.
58. P Consider the rubber cord with one end attached to a tree and another - to
a car moving away from the tree with the velocityV =1 0m/s.A ts o m ep o i n t
an ant appears on the ﬁxed end of the cord and starts running along it with the
velocity v =1 0cm/s. Will it reach the car? Assume the cord can be stretched
up to arbitrary length.
59. Find all diﬀerentiable solutions of the equationf(x)f(y)= f(x+y). Find all
continuous solutions of the same equation.
60. P /RadioactivityGive an example of theC∞(R) functionf(x) with the following properties:
1) f(n)(0) = 1 for somen /greaterorequalslant0,
2) f(i)(0) = 0,i /greaterorequalslant0,i ⁄= n,
3)
∫ ∞
0
|f(x)|dx <∞.
(13)
61. P Show that
∫ π
0
log(1−2acosx+a2)dx =0f o r|a| < 1.
62. P Consider the integral
In =
∫ ∞
−∞
dx
x sin(x)
n∏
k=1
cos
( x
2k +1
)
.
Show thatIn = π for n =1 ,2,3,4,5,6. ComputeI7.
13

COMPLEX ANALYSIS
1. Write the following complex numbers in polar form:
3i, 1−i, 2+ i, −4, 2−i
√
3, 2−i
1+4 i, |3+ i|.
2. Write the following complex numbers in cartesian form
eiθ, 3eiπ/4, 1
2eiπ, 2e2iπ/3,e −3iπ/4.
3. Find the (possibly complex) roots of these polynomials
z2 +3z +1 2=0 ,z 4 +5z2 +4=0 ,z 6 =1 ,z 3 = −1.
4. Compute the Laurent series off(z)= ez
(z −1)2 around z0 = 1; give the region
of convergence.
5. /ClockLogoCompute the Laurent series off(z)= 1
(z −3)3 around z0 = i; give the region
of convergence.
6. Compute the Laurent series off(z)= z
(z +1)(z −1) around z0 = 1; give the
region of convergence.
7. Compute the Laurent series off(z)=s i n z
1−z around z0 = 1; give the region
of convergence.
8. /ClockLogoFind the Laurent series off(z)= 1
(z+1)(z+2) such that it converges in the regions
(a) |z| < 1;
(b) 1 < |z| < 2;
(c) |z| > 2;
(d) 0 < |z +1| < 1.
9. Find an analytic map that sends the unit disk (|z| < 1) onto the left half plane
(Re(z) < 0)
10. Take a disk of radiusR with a branch cut on the negative real axis; what does
logz map this onto? Where is the origin mapped onto?
11. What is the image of{z|Re(z) > Im(z) > 0} under the mappingez2
?
12. Compute
∫ ∞
0
1
1+ x2dx;
13. Compute
∫ ∞
−∞
1
1+ x6dx;
14

Figure 3: Contour for problem 20
14. Compute
∫ ∞
−∞
eiαx
x2 +m2dx with α,m ∈ R (hint: consider the two cases of posi-
tive or negativeα separately);
15. Compute
∫ ∞
−∞
eiαx
(3−ix)(1+ ix)dx;
16. Compute
∫ ∞
0
sinx
x dx;
17. Compute
∫ ∞
−∞
x2
x4 −2x2 cos2θ+1 dx;
18. Compute
∫ 2π
0
dθ
1+ acosθdx with |a| < 1;
19. Compute
∫ π
0
(cosθ)2ndθ;
20. (a) Compute the integralI1 =
∫
C
dz
(z +i)√z, where the contourC is shown
in ﬁgure 3,C = L+ ∪CR ∪L− ∪γϵ, and we send the radius ofγϵto zero and
the radius ofCR to inﬁnity. Note that, because of the square root,z =0i s
a branch point. We choose to have a branch cut on the positive real axis.
(b) Find a relation between the integralI1 and I2 =
∫ ∞
0
1
(x+i)√xdx,t h e n
use the result from the previous point to ﬁnd the value ofI2.
21. Repeat exercise 20 this time withI1 =
∫
C
zp
z2 +1 dz and I2 =
∫ ∞
0
xp
x2 +1 dx
with 0<p< 1; the contour is the same as before.
22. /RadioactivityCompute
∫ 1
0
1
(x2 −x3)1/3 (hint: use the contour in ﬁgure 4);
15

Figure 4: Integration contour for exercise 22.
23. /ClockLogoCompute
∫ ∞
0
logx
1+ xαdx for α ∈ N, α> 1( hint:solve problem 34 ﬁrst. Now,
as a contour, use a circular wegde of the complex plane that makes a 2π/α angle
with the positive real axis);
24. /ClockLogoCompute
∫ ∞
0
log2 x
1+ x2dx (hint: solve problem 23 ﬁrst. Use the functionlog3 x
1+x2
integrated over some smart choice of contour);
25. (a) Matsubara summation: in statistical mechanics, one often has to carry out
summations over Matsubara frequencies. These frequencies appear when
the system is put at ﬁnite temperature, and the summation can be te-
dious to carry out. We will consider the expectation value of the num-
ber of particles of a bosonic non-interacting gas. Consider the function
h(ω
n)= − T
iωn −ξ.H e r eωn are called Matsubara frequencies. In this case
(the bosonic one) they are given byωn =2 πnT.
What we want to compute isS ≡ ∑
n h(ωn). To do so, we introduce an
auxiliary functiong(z)= β
eβz−1 (setting kB =1 ,β = T−1).
• Where are the poles ofh? Where are those ofg?
• Consider now the functiong(z)h(−iz). Find a contour for which
1
2πi
∮
dzg(z)h(−iz)= S.
This contour encompasses an inﬁnite number of poles.
• Since for largez the function decays fast enough the residue at inﬁnity
vanishes; inﬂate the contour and ﬂip its orientation, so that it includes
only a ﬁnite number of poles, in this case only one.
• Carry out the integration. You should ﬁnd−T
∑
n
1
iωn −ξ = 1
eβξ −1;
as expected, this is the Bose distribution.
(b) Redothepreviousexerciseforfermions:thefrequenciesare ωn =( 2n+1)πT.
16

It’s convenient to pickg(z)= β
eβz+1. You should ﬁnd
T
∑
n
1
iωn −ξ = 1
eβξ +1
26. Use the saddle point method to approximatef(t)=
∫ ∞
−∞
e−t(z2−1/4) costz
1+ z2 dz
for t ≫ 1.
27. The modiﬁed Bessel function of the second kind has the following integral
representation: Kν(x)= 1
2
∫ ∞
0
exp
(
−x
2
(
s+ 1
s
)) ds
s1−ν . Find the asymptotic
expansion forx ≫ 1.
28. /RadioactivityP The Henkel function of the ﬁrst kind has the following integral representa-
tion: H(1)
ν (x)= 1
πi
∫ −∞+iϵ
0+iϵ
exp
[x
2
(
z − 1
z
)] dz
zν+1.T h eiϵfactor is present since
we have a branch cut along the negative real axis. Find the asymptotic behavior
as x ≫ 1.
29. Find Stirling’s approximation: considern!=Γ (n+1)=
∫∞
0 xne−xdx for n ≫ 1.
30. Using Stirling’s approximation, ﬁnd the leading behavior of:
(a)
(2N
N
)
for largeN.
(b) S =l o gZ(N,m)w i t hZ = N!
(N−m)!m! for largeN.
31. Find an analytic continuationg(z) of the functionf(z)=
∫ ∞
0
te−ztdt. f(z)i s
deﬁned only forz> 0. What is the domain ofg(z)?
32. /ClockLogoRiemann’s zeta function is deﬁned asζ(z)= ∑ ∞
n=1 n−z.
• For which values ofz does this converge?
• Show that the zeta function admits the integral representation
ζ(z)= 1
Γ(z)
∫ ∞
0
tz−1
et −1dt
hint: the relation∑ ∞
m=1 e−mt = e−t
1−e−t might prove useful.
• Now we take the contour of ﬁgure 5. Since we want to allow non integer
values of z, there is a branch cut along the positive real axis. What is
1
Γ(z)
∫∞
0
tz−1
et−1dt along this contour?
• For z< 0 we can deform the contour by sending the radius of the circle D
to inﬁnity; the price to pay is that, to computeI, we have to evaluate an
inﬁnite number of poles, but this can be done. By comparing this result to
what you did in the previous step, you should ﬁnd that
ζ(z)= ζ(1−z)e
3πiz/2 −eπiz/2
e2πiz −1
(2π)z
Γ(z) .
17

Figure 5: Contour for problem 32
• Using the formula you just found, show thatζ(−1) =− 1
12. Notice that this
doesn’t mean that 1 + 2 + 3 + 4 +... = − 1
12, since thatζ(z)= ∑ ∞
n=1 n−z
is valid only forz> 1. On a side note, this is the reason why string theory
(without supersymmetry) needs 26 spacetime dimensions.
33. P The Gamma function Γ(z)=
∫∞
0 xz−1e−xdx is originally deﬁned only for
t> 0; it can however be analytically continued to negative values ofz. Show
that, as z →− n,w h e r en ∈ N0,Γ (z) has poles; compute the order and the
residue of these poles.
34. Solve the integral
∫ ∞
0
1
1+ xαdx for α ∈ N,α> 1 by integrating the function
logz
1+ zα along the contour of ﬁgure 3.
18

V ARIATIONAL PRINCIPLE
1. /Radioactivity”Fubiniinstanton”Considerthefunctional S[f]=2 π2
∫ ∞
0
dxx3
(1
2f′2 +V(f)
)
,
where V(f)= −λ
4f4,a n df ∈ C2[0,∞].
(a) Write the diﬀerential equation onf, whose solution is an extremum ofS[f].
(b) Findallsolutionstothisequationsatisfyingtheboundaryconditions f(∞)=
f′(∞)=0 .
(c) Compute the value ofS[f] on these solutions.
2. Find an extremum of the functional J[f]=
∫ π/2
0
dx(f′2 − f2)i nac l a s so f
functions f ∈ C2[0,π/2] satisfying the boundary conditionsf(0) = 0,f(π/2) =
1.
3. ”Brachistochrone curve” On a vertical planexOy consider the two pointsA and
B. Find a curvey = y(x) connecting these points and such that an ideal point-
like body, that starts at rest at the pointA and moves along this curve without
friction under constant gravity, reaches the pointB within the shortest time.
4. /ClockLogoConsider the pointsA and B lying on the planexOy. Find a curvey = y(x)
connecting these points and such that rotation ofy(x) around the axisOx gives
a surface inR3 with a minimal area.
5. Find an extremum of the functionalJ[f]=
∫ 1
0
dx(360x2f − f′′2)i nac l a s so f
functions f ∈ C3[0,1] satisfying the boundary conditionsf(0) = 0,f′(0) = 1,
f(1) = 0,f′(1) = 2.5.
6. Consider the functionalS[x,y,z ]=
∫ t2
t1
dtL(x,y,z,x ′,y′,z′), where
L = m
2 (x′2 +y′2 +z′2)−U(x,y,z ), (14)
and U is aC1 function ofx,y,z . Write the system of equations onx(t),y(t),z(t)
whose solution is an extremum ofS[x,y,z ]i nac l a s so fC2([t1,t2]) functions with
ﬁxed boundary conditions.
7. Consider the functionalJ[f]=
/dispiint
D
dxdy
[(∂f
∂x
)2
+
(∂f
∂y
)2]
,w h e r eD is a do-
main in (xy)-plane with the boundary ∂D. Write the equation for f,w h o s e
solution in a class of functionsf ∈ C2(¯D), satisfying the boundary condition
f(x,y)|∂D = f0(x,y), is an extremum ofJ[f].
8. Consider the functionalJ[f]=
/dispiint
D
dxdy
[(∂f
∂x
)2
+
(∂f
∂y
)2
+2fg
]
,w h e r eD is
a domain in (xy)-plane with the boundary∂D,a n dg = g(x,y) is a continuous
function in¯D. Write the equation onf, whose solution In a class of functionsf ∈
C2(¯D), satisfying the boundary conditionf(x,y)|∂D = f0(x,y), is an extremum
of J[f].
19

9. Consider the biharmonic equation
∂4f
∂x4 +2 ∂4f
∂x2∂y2 + ∂4f
∂y4 =0 . (15)
Find a functionalJ[f] whose extrema in a class ofC4(¯D) functionsf = f(x,y)
with ﬁxed boundary conditions,f(x,y)|∂D = f0(x,y), satisfy this equation.
10. Consider the following problem
⎧
⎨
⎩
Ff − ∂
∂xFfx − ∂
∂yFfy =0 , (x,y) ∈ D
Ffxnx +Ffyny+= g(s),x ∈ ∂D,
(16)
where f = f(x,y) ∈ C2(¯D), F = F[f,fx,fy](x,y) ∈ C2(R3 × ¯D), g ∈ C1(∂D),
∂/∂n denotes a normal derivative on∂D, fx ≡ ∂f
∂x and Ff ≡ ∂F
∂f .
(a) Show that the solutions to this equation are given by extrema of the func-
tional
J[f]=
/dispiint
D
dxdyF −
∫
∂D
dsfg. (17)
(b) How must the functional above be modiﬁed to give the mixed boundary
conditions on the functionf:
Ffxnx +Ffyny +h(s)f = g(s),h ∈ C1(∂D) (18)
11. Let f ∈ C2(¯D) be an extremum of the functionalS[f]=
∫
D
dxL(f,f ′)i na
class of functions satisfying the boundary conditionf|∂D = f0. What additional
condition must be imposed onf to make it an extremum ofS[f]i nac l a s so f
C2(¯D) functions withall possible boundary conditions?
12. Construct the functionalS[ψ,ψ†] whose variation with respect toψ = ψ(⃗r,t)
and ψ† = ψ†(⃗r,t)g i v e s
(a) the Schrodinger equationiℏ∂ψ
∂t = ˆHψ and its conjugated,
(b) the stationary Schrodinger equationˆHψ = Eψ and its conjugated.
Here ˆH is some hermitian operator.
13. Consider the functionalS[ψ,ψ†]=
∫ ∞
−∞
dxψ†(E − ˆH)ψ,w h e r e
ˆH = − ℏ2
2m
∂2
∂x2 + mω2x2
2 . (19)
(a) Find an extremum ofS[ψ,ψ†]i nac l a s so fC1(R) functions of the form
ψ(x)=
√
πσ2e− x2
2σ2 .
(b) Find an eigenvalue ofˆH corresponding to this extremum.
20

14. Consider the functionalS[φ,φ∗]=4 π
∫ ∞
−∞
dt
∫ ∞
0
drr2(˙φ˙φ∗ −φ′φ′∗−U(φφ∗)),
where U ∈ C1(R)a n dφ is aC2(R×[0,∞)) complex-valued function oft and x.
(a) Varying with respect toφ and φ∗, obtain the Euler-Lagrange equation and
its conjugated. Substituting theansatz φ(r,t)= f(r)eiωt, rewrite them as
an equation on a functionf of a single variabler.
(b) Substitute the ansatz φ(r,t)= f(r)eiωt into the functional S[φ,φ∗] ﬁrst,
and, varying with respect tof, obtain the Euler-Lagrange equation onf.
Compare with the result of the previous point.
15. ”Derrick’s theorem” Consider the functional
E[φ]=
∫
ddx
(
1
2Kab(φ)
d∑
i=1
∂iφa∂iφb +V(φ)
)
, (20)
where φ = φ(x1,...,x d) ∈ C2(Rd), Kab(φ) is a positive-deﬁnite matrix for anyφ,
i.e.,
Kab(φ)∂iφa∂jφb /greaterorequalslant0, (21)
where the equality impliesφ =0 ,a n dV(φ) /greaterorequalslant0, V(φ)=0 ⇒ φ =0 .
Suppose φ0(x) is a non-zero extremum ofE[φ]. Consider the conﬁgurations of
the formφλ(x)= φ0(λx), obtaining fromφ0(x) by stretching the coordinates by
af a c t o ro fλ.
(a) Show thatE(λ) ≡ E[φλ] must satisfy
dE
dλ
⏐⏐
⏐
⏐
λ=1
=0 . (22)
(b) Using the notations
Γ=
∫
ddx1
2Kab(φ0)
d∑
i=1
∂iφa
0∂iφb
0
, Π=
∫
ddxV(φ0), (23)
show that the above relation implies
(2−d)Γ−dΠ=0 . (24)
(c) Give a conclusion about the existence ofφ0,i f
(a) d> 2( b ) d =2 ( c ) d =1
21

DIFFERENTIAL EQUATIONS
1. Solve y′(x)= xex2−2log y(x)
2. Solve
{
x′(t)= −x(t)+6 y(t)
y′(t)=2 x(t)+3 y(t)
3. Solve (x+1) dy
dx =2 y +(x+1)5/2 with y(0) = 3
4. P Solve y′(x)= f(x)y(x)+ g(x)yn(x)
5. Solve y′′−y′−2y =0
6. Solve y′′−6y′+9y =0w i t hy(1) = 1 andy′(3) = 0
7. Solve y′′′−3y′+2y =0
8. Solve y′′−3y′+2y =s i nx
9. Solve y′′+3y′+2y =t a n hx
10. Find C(t)w h e n
C′(t)= α(a−C(t))(b−C(t))
if
(a) a ⁄= b
(b) a = b
and withC(0) = 0.
11. Solve
(xy2 −y)dx+xdy =0
12. Solve y′−y = e3t with y(0) = 2.
13. Solve y′′−3y′+2y = e3t with y(0) = 1,y′(0) = 0
14. /ClockLogoSolve y′′−6y′+15y =2s i n3t with y(0) =−1a n dy′(0) = 4
15. Solve y′+2 y = e−tθ(t), where θ is the Heaviside function,θ(x)=0i f x< 0
and θ(x)=1i f x> 0.
16. Solve y′′+16y = θ(π −t)w i t hy(0) =y′(0) = 0 and whereθ is the Heaviside
function, θ(x)=0i f x< 0a n dθ(x)=1i f x> 0.
17. Consider a forced damped harmonic oscillator:
¨y(t)+2 k˙y(t)+Ω 2y(t)= f(t) (25)
the Green functionG(t) is deﬁned such that
y(t)=
∫
dt′G(t−t′)f(t′). (26)
Find G(t)w h e n
22

(a) Ω >k> 0 (oscillating system)
(b) Ω =k (critical damping)
(c) k> Ω > 0 (overdamped system)
18. Find the charge distribution that gives the electrostatic potential
ϕ(x,y,z )= Z
4πε0
e−ar
r (27)
19. /ClockLogoFind the general solution of the equation :
x(2−x)d2y
dx2 +3(1 −x)dy
dx −y = 0 (28)
as a power series aboutx =1 .
20. Given the diﬀerential equation
d
dξ
(
ξdu
dξ
)
+
(1
2Eξ +α− m2
4ξ − 1
4Fξ2
)
u = 0 (29)
Find the ﬁrst three terms of a series solution aroundξ = 0 by using the largest
solution of the indicial equation.
21. /ClockLogoConsider Schrodinger equation for a quantum harmonic oscillator with small
quartic perturbation
(
−1
2
d2
dx2 + x2
2 + gx4
4
)
ψ(x)= E0(g)ψ(x) (30)
and make the ansatz
ψ(x)= e−x2/2
∞∑
n=0
(g
4
)n
Bn(x)w i t h B0(x) = 1 (31)
E0(g)=
∞∑
k=0
ak
(g
4
)k
. (32)
We already know thata0 = 1
2 from the unperturbed oscillator. We want to ﬁnd
the ﬁrst two correctionsa1 and a2.
(a) Find a recurrence relation forBk(x)a n dak
(b) Solve the relation by assumingBi(x)=
2i∑
j=1
x2j(−1)iBi,j.
(c) Considering diﬀerent powers ofx, ﬁnd the following relations
an =( −1)n+1Bn,1 (33)
2jBn,j =( j +1)(2j +1)Bn,j+1 +Bn−1,j−2 −
n−1∑
k=1
Bn−k,1Bk,j (34)
23

(d) Find a1 and a2. You can check that your result agrees with the usual per-
turbation theory.
22. Consider the equation
y′′(x)+ P(x)y′(x)+ Q(x)y(x) = 0 (35)
and show that ify1 is a solution to this equation, then alsoy2 = y1
∫x
dse−
∫s dtP (t)
[y1(s)]2
is.
23. Verifythat
∫ ∞
1
dt e−xt
√
t2 −1 isasolutiontothediﬀerentialequation y′′+1
xy′−y =
0.
24. Bessel equation of orderp is
x2y′′+xy′+(x2 −p2)y = 0 (36)
Assuming y = ∑
m=0 amxr+m, ﬁnd the two roots of the indicial equation (the two
possible values ofr). For both of them, solve the recurrence relation for theai.
You should ﬁnd, for the largest root,Jp(x)=
∞∑
k=0
(−1)k
k!Γ(k +p+1)
(x
2
)2k+p
,a n d
for the smallest J−p(x)=
∞∑
k=0
(−1)k
k!Γ(k −p+1)
(x
2
)2k−p
(for the normalization,
assume thata0 = 1
2nn!). These are Bessel function of the ﬁrst kind.
25. Prove the following properties of the Bessel functions of the ﬁrst kind:
(a) d
dx (xνJν(x)) =xνJν−1(x)
(b) d
dx
(
x−νJν(x)
)
= −x−νJν+1(x)
(c) d
dxJν(x)= 1
2 (Jν−1(x)−Jν+1(x))
(d) Jν−1(x)+ Jν+1(x)= 2ν
x Jν(x)
26. P The functionKν(x) is the solution of the equationx2y′′+xy′−(x2+ν2)y =0
that diverges whenx → 0. Find the asymptotic behavior for smallx for ν ⁄=0 .
What happens forν = 0? For the sake of completeness,Kν(x) is called modiﬁed
Bessel function of the second kind.
27. Given the eigenvalue problemL(x)ψ(x)= λψ(x)w i t hL(x)= p0(x) d2
dx2 +
p1(x) d
dx +p2(x), L is self-adjoint ifp′
0 = p1. Find a functionf(x) such that, by
multiplying the following ODE, it makes them self adjoint:
(a) Laguerre’s ODE:xy′′+(1 −x)y′+ay =0
(b) Hermite’s ODE:y′′−2xy′+2αy =0
(c) Chabyshev’s ODE: (1−x2)y′′−xy′+n2y =0
24

28. /ClockLogoDevelop a series solution for Laguerre’s ODE (given in problem 27).
29. Find the solutions of:
y′′+λy = 0 (37)
with y′(0) =y′(π)=0 ;
30. Find the solutions of
x2y′′+3xy′+λy = 0 (38)
with x ∈ [1,e]s u c ht h a ty(1) =y(e)=0 .
31. Find the non-zero solutions of
(xu′(x))′= −λu(x)
x (39)
such thatu(1) = 0 andu′(e) = 0. What values ofλ are allowed?
32. Show thatδ(x) = lim
ϵ→0
Im 1
π
1
x−iϵ
33. Show thatδ(αx)= 1
αδ(x), and more generally,δ(f(x)) =
∑
i
δ(x−xi)
|f′(xi)| where
xi are the root off, i.e.f(xi)=0 .
34. Compute
∫ ∞
−∞
δ′′(x−2) 1
1+ x2dx
35. Find the coeﬃcientsa,b,c so that
δ′′(x−x0) 1
(1+ x−x0) = aδ′′(x−x0)+ bδ′(x−x0)+ cδ(x−x0).
36. Solve y′′(x)−3y′(x)+2 y(x)= δ(x−1) withy(0) = 0 andy(1) = 1.
37. Solve
(
− d2
dx2 +m2
)
G(x)= δ(x)
38. /RadioactivityShow that d
dx logx = 1
x −iπδ(x)
39. Find the most general solution of∂f
∂x +a∂f
∂y +(x−2y)f =0
40. Find the most general solution ofx∂f
∂x −y∂f
∂y =0
41. Find the most general solution of
( ∂
∂x + ∂
∂y + ∂
∂z
)
f(x,y,z )= x−y
42. Solve ∂2
xu+2∂x∂yu+∂2
yu = 0 with the boundary conditionsu(x,0) = sinx and
u(0,y)= y2.
43. Solve
(∇2 +k2)u(x,y,z ) = 0 (40)
25

so thatu = 0 whenever any of the coordinates is equal to 0 orL. What are the
allowed values ofk2?
44. A two dimensional rectangular slab (with the two sides of lengtha and b)h a s
its edges ﬁxed; at timet = 0 it has the proﬁle
u(x,y, 0) = sin2xπ
a sin 3yπ
b ; (41)
ﬁnd u(x,y,t ) knowing that it satisﬁes the wave equation with a velocityv.
45. /ClockLogoThe surface of a sphere of radiusR is kept at a constant temperatureTU
for the upper hemisphere (0 ≤ θ<π / 2) and TL for the lower hempisphere
(π/2 ≤ θ ≤ π). Find the stationary temperature distribution inside the sphere,
at a distancer from the center, in an expansion in terms ofr
R. Compute terms
up to third order.
46. Consider an semi-inﬁnite (x ≥ 0) metal rod with conductivityκ. Find the heat
distribution u(x,t)i fu(x,0) =u0δ(x)
47. /ClockLogoConsider a metal rod of lengthL. One end is kept at temperature 0, and the
otherattemperature T0.Findthetemperature T(x,t),knowingthat T(x,0) = 0.
48. P A string has endpoints which are ﬁxed atx =0a n dx = L.A tt =0 ,t h e
string is hit atx = a so it starts vibrating:
y(x,0) = 0 ∂ty(x,0) =Lv0δ(x−a) (42)
where y is the amplitude of the oscillations (assume the amplitude to be small
and the wave velocity to bev). Findy(x,t).
49. /ClockLogo/RadioactivityComputethestationarytemperaturedistribution u(ρ,θ,z )ofasemi-inﬁnite
cylinder of radius 1 when the curved surface is kept at temperature 0 if
(a) the ﬂat surface is kept at a temperatureu0
(b) the ﬂat surface is kept at a temperatureu0ρsinθ
50. Consider a spherically symmetric potential satisfying the Laplace equation in
d dimensions (d ≥ 3) and vanishing at inﬁnity. Show that this potential can be
written asu(r)= a
rb ,w h e r ea is a constant, and ﬁnd the value ofb.
51. P Aconductingsphereofradius awithzerototalchargeisexposedtoauniform
electric ﬁeld ⃗E in the z direction. Find the electrostatic potential outside the
sphere if we set the surface of the sphere to have potential zero.
26

PROBABILITY
1. A collection of stories in 5 volumes is placed on a bookshelf in a random order.
What is the probability that the order is correct (direct or inverse)?
2. Find the least number of students in a group such that the probability that at
least two students have the same birthday is not less than1
2.
3. What is more probable - to get at least one 1 in throwing four dice, or to get at
least two 1 in 24 throws of two dice?
4. Among N tickets forN students there aren happy tickets. The students take
the tickets one by one, each takes one random ticket. What is the probability
that j’s student gets a happy ticket, 1⩽ j ⩽ N?
5. 5 people decide to have a party with presents. Everyone prepares one present
and brings it to the party, where the presents are mixed. Then everyone takes
one random present. What is the probability that nobody gets his own present?
6. Three faces of a tetrahedron are painted red (R), green (G) and blue (B), while
the forth face is painted in all three colors (see the ﬁgure). Denote byP(A)t h e
probability that it falls on a face containing the colorA, A = R,G,B .
RGB R G B
Figure 6: The faces of the tetrahedron
(a) Check ifP(A∩B)= P(A)P(B) for allA,B = R,G,B .
(b) Check ifP(R∩G∩B)= P(R)P(G)P(B). Are the eventsR, G, B pairwise
independent? Are they mutually independent?
7. Let a, b, c be three independent random variables distributed uniformly between
0 and 1. Find the probability that the roots of the equationax2 +bx+c =0a r e
real.
8. Consider the circuit shown in ﬁgure. Each of its ﬁve relays is closed with the
probability p independently of other relays.
-  
@@
rA
rC
  
@@
@@
  
rB
rD
@@
  
-  rE
Figure 7: The circuit
27

(a) Find the probability that a signal will pass through the circuit.
(b) Find the probability that the relayE is open if it is known that the signal
has passed through the circuit.
9. Two persons agreed to meet at some place between 2 and 3 o’clock. Whoever
arrives ﬁrst, he waits 10 minutes, then leaves. What is the probability to fail the
meeting? Assume that anyone can arrive at any time within the given interval.
10. ”Buﬀon’s needle” A needle of lengthl is thrown randomly on a plane lined
with parallel lines with distanced between them, l<d . Find the probability
that the needle will cross some line.
11. Consider the particle moving in a gas of other particles. Given that the last
collision of the particle occurred att = 0, the probability that the next collision
will occur betweent and t +Δ t equals λΔt + o(Δt), when Δt → 0. Find the
probability P(t) that the time between the nearest collisions will exceedt.
12. /ClockLogo/RadioactivityP In nuclear physics, the intensity of a particle source is measured with
Geiger-Muller counters. A particle entering the counter generates a discharge
in it that lasts timeτ, during which the counter does not record any particles
entering the counter. Find the probability that the counter will count all particles
entering it during timet if the following conditions are fulﬁlled:
(a) the particles enter the counter independently;
(b) the probability that during the time interval fromt to t+Δ t, k particles
entered the counter is given by
p
k(t,t +Δt)= (aΔt)ke−aΔt
k! , (43)
where a is the rate.
13. /RadioactivityP ”Random walk” LetA, B, x be integers,A ⩽ x ⩽ B. Consider the particle
that starts moving from the pointx at time t =0 .A te a c hs t e pΔt =1t h e
particle can move left or right from its recent position with the probabilitiesp
and q =1 −p correspondingly. If at some step it reaches the pointsA or B,i t
stays there forever (see example ﬁgure below).
-6 -5 -4 -3 -2 -1 1 2 3 4 5 6
Distance
1
2
3
4
5
6
7
8
Time
AB x
Figure 8: One possible particle’s trajectory. HereA = −B =5 , x =2 ,a n dt h e
particle reaches the pointB after 7 steps.
28

(a) Assuming that the total number of steps approaches inﬁnity, compute the
probabilities α(x), β(x) to ﬁnd the particle at the pointsA and B corre-
spondingly, as functions of the initial positionx of the particle.
(b) Find the mean timem(x) of a random walk of the particle before it hitsA
or B. Assume thatm(x) < ∞. Check that ifp = q = 1
2 and A = −B,t h e n
m(0) =B2. Hence the mean time of random walk is given by a square of
distance traveled.
14. P Prove that the equation
∫ ∞
−∞
x(t)dt
(y −t)2 +1 = e−y2
(44)
has no nonnegative solutionsx(t).
15. P Prove that if for some discrete random variableξ, Eξ2 = Eξ3 = Eξ4,t h e nξ
can only take values 0 or 1.
16. /ClockLogoConsider two independent random variablesξ1 and ξ2 that are distributed
according to the normal distribution with mean valuesa1, a2 and variancesσ2
1,
σ2
2 correspondingly. Find the distribution of a random variableξ1 +ξ2. Repeat
the exercise in case ifξ1,2 are distributed according to the Poisson distribution
with parametersλ1 and λ2.
17. Let ξ be a continuous random variable.
(a) Prove that ifEeλξ is ﬁnite then
P(ξ /greaterorequalslantx) ⩽ e−λxEeλξ,λ > 0. (45)
(b) Prove that ifE|ξ|m is ﬁnite then
P(|ξ| /greaterorequalslantx) ⩽ x−mE|ξ|m,x > 0,m > 0. (46)
18. Consider the seriesω of n experiments whose results are given by independent
variablesξi, i =1 ,...,n , taking the values 1 (success) with the probabilityp,a n d
0 (fail) with the probabilityq =1 −p.C o m po s et h es u mSn(ω)= ξ1+...+ξn.I ti s
clear that for anytypical series ω and for largen, Sn(ω)/n must be close enough
to p. But what is the total amount of the typical series and how it behaves asn
grows? Denote byC(n,ϵ) all typical series, or, more precisely,
C(n,ϵ)=
{
ω|
⏐⏐
⏐
⏐
S
n(ω)
n −p
⏐⏐
⏐
⏐⩽ ϵ
}
, (47)
with some smallϵ.
(a) Show that ifω ∈ C(n,ϵ), then the probabilityp(ω) of such series to realize
is enclosed withing the region
e
−n(H+˜ϵ) ⩽ p(ω) ⩽ e−n(H−˜ϵ), (48)
where
˜ϵ=m a x{ϵ, ϵ(−2log(pq))}, (49)
29

and the quantity
H = −plogp−qlogq (50)
is called entropy.
(b) Show that the total amount of the typical series lies in the region
en(H−˜ϵ) ⩽ N(C(n,ϵ)) ⩽ en(H+˜ϵ). (51)
Hence the number of the typical series is exponentially large, while the
probability of each of them is exponentially small.
19. Let ξ and η be two independent random variables taking values 1 and 0 with
the probabilitiesp and q =1 −p correspondingly. Find
(a) E(ξ +η|η), (b) E(ξ|ξ +η).
20. Let ξ1,...,ξ n,τ be independent random variables,ξ1,...,ξ n have the same dis-
tribution, τ takes the values 1,...,n . Consider the sum of a random number of
the random variablesSτ = ξ1 +...+ξτ. Show that
(a) ESτ = Eτ · Eξ1,
(b) E(Sτ|τ)= τ Eξ1,
(c) DSτ = Eτ · Dξ1 + Dτ ·(Eξ1)2,
(d) D(Sτ|τ)= τ Dξ1.
21. /ClockLogoP Find the expectation value of the area of the projection of a 3-dimensional
randomly oriented cube with edge of length 1 onto a given plane.
22. P A reasonable way to estimate the number of birds in a large ﬂock is to mark
some of them. SupposeM birds were selected, marked and then released. Long
time after, in a sample ofn randomly selected birdsX had the marker. What
is the most probable total amount of birds in the population? Assume the ﬂock
was not mixed with other groups of birds.
23. Consider the suma of 10N real numbersak, a =
10N
∑
k=1
ak.L e t˜ak be an approxi-
mation ofak with precision 10−m. Assume that the round-oﬀ errorsδk = ak −˜ak
are distributed uniformly within the interval (−0.5·10−m, 0.5·10−m). Compose
the sum ˜a =
10N
∑
k=1
˜ak and letδ = a − ˜a be the total error of the approximation.
For the given values ofN and m ﬁnd ϵsuch that
P(|δ| <ϵ) > 0.99. (52)
24. The dice is thrown 12000 times. Find the probability that the total number of
6’s lies between 1800 and 2100.
25. ”Monte-Carlo method” Consider the function f(x1,...,x n) deﬁned in V =
{−1 ⩽ xi ⩽ 1,i =1 ,...,n } and bounded from below and above,|f(x1,...,x n)| ⩽
C. Deﬁne a random variableη = f(ξ1,...,ξ n), whereξi are distributed uniformly
between −1a n d1 .
30

(a) Show that Eη = I,w h e r eI =
∫
V
f(x1,...,x n)dnx. Hence the random vari-
ables can be used to compute the high-dimensional integrals with a given
precision.
(b) Consider the series ofN random variables ηi = f(ξi1,...ξin), i =1 ,...,N
where all ξij are distributed uniformly in [−1,1]. Then the quantity˜I =
1
N(η1 + ... + ηN)f o rl a r g eN approaches I with high enough probability.
Estimate how largeN should be to ensure that
P(|˜I −I| < Δ) /greaterorequalslant1−α, (53)
where Δ andα are given small numbers.
26. From a collection of 500 goods 70 were investigated, and in 14 of them various
defects were revealed. Find the interval in which the fraction of the defected
goods in the whole group lies with the probability 96%.
27. Here is the data about wheat yield from 8 identical wheat ﬁelds in conventional
units:
26.52 6 .23 5 .93 0 .13 2 .32 9 .32 6 .12 5 .0
There is a suspicion that the data about the third ﬁeld is incorrect. Check if it
should be dropped with 5% signiﬁcance level.
28. In an experiment on the detection of cosmic rays a detector counts particles
with diﬀerent energies coming from diﬀerent directions. The observed spectrum
of the particles is shown in table below.
Energy, MeV 0-10 10-20 20-30 30-40 40-50 50-60 60-70 70-80 80-90
#o fp . 15 71 75 68 39 17 10 4 1
At the signiﬁcance level 0.05, test the hypothesis that the particle spectrum
is distributed according to the Poisson distribution with parameterλ. Find the
eﬀective estimate forλ.
29. P A dice is turned randomly from one face to one of four adjoined faces. Sup-
pose it fell 6 att = 0. Find the probabilityPn, n /greaterorequalslant1, that aftern such turns it
will show 6 again. Find the limit lim
n→∞
Pn.
30. An electron can occupy one of a countable number of energy levels in atom.
The transition probabilities fromi’s toj’s level per second are given by
Pij(t =1 )= cie−α|i−j|, (54)
where α> 0a n dci are some constants. Find
(a) Pij(t =2 ) ,
(b) ci.
31. One may naively argue that in one toss of two coins the probability to have
two heads or tails equals 2/3. Indeed, if we use the scheme with three elementary
events (it fell two heads, or two tails, or one head and one tail), the probability
31

thatthecoinsfallequallymayseemtobe2 /3.Thecorrectscheme,however,must
contain four diﬀerent events (head-head, tail-tail, head-tail, tail-head) with the
probabilitiesequallydistributedamongthem,anditgivesthecorrectanswer1 /2.
An experiment can be conducted to overcome the doubts about which scheme
is more reasonable. Let the ﬁrst hypothesis claim that the correct value is 2/3,
and the second - that it is 1/2. Find how many coins tosses one should make
to eliminate the ﬁrst hypothesis with type I error 0.05 (probability to reject the
second hypothesis when it is true) and type II error 0.05 (probability to accept
the ﬁrst hypothesis when it is false).
32. P It is known that the series
∞∑
n=1
1
n diverges while the series
∞∑
n=1
(−1)n
n con-
verges. One may ask about the convergence or divergence of the series
∞∑
n=1
ξn
n ,
where ξn are independent random variables taking the values +1 or−1 with the
probabilities p and q =1 −p correspondingly.
(a) Show that ifp = q = 1
2, the series converges with the unit probability.
(b) Show that otherwise the series diverges with the unit probability.
33. /ClockLogoNormal numbers
Let x ∈ [0,1). Consider the inﬁnite decimal notation forx:
x =0 .a1a2..., a i =0 ,1,..., 9,i ∈ N, (55)
where for the numbers with ﬁnite amount of decimal places we complete the
records with inﬁnite series of 0s. Now selectrandomly one x.W h a tc a no n es a y
about the typical distribution of digits 0,..., 9i n x? To answer the question,
consider the following sequence of approximations:
x0 =0
x1 =0 .a1
...
xn =0 .a1...an
...
(56)
(a) Show that
P
(
lim
n→∞
1
nIn(i)= 1
10
)
=1 , ∀i, (57)
where In(i) gives the number ofi digit in xn. The result implies that al-
most all numbers contain equal (and inﬁnite) amount of all 10 digits. Such
numbers are callednormal.
(b) Check if the rational numbers are normal.
(c) Check if the following number is normal:
x =0 ,12345678910111213... (58)
(all integers are written in ascending order).
32

