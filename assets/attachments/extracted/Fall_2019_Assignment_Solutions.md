



































































































Problem Set 5
D. Zack Garza
October 23, 2019
Contents
1 Problem 1 1
2 Problem 2 3
3 Problem 3 4
4 Problem 4 4
4.1 Part (a) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
4.2 Part (b) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
5 Problem 5 6
6 Problem 6 7
6.1 Part (a) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
6.2 Part (b) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1 Problem 1
We first make the following claim:
S :=
∞∑
j=1
∞∑
k=1
ajk = sup



∑
(j,k)∈B
ajk ϶ B ⊂ N2, |B|< ∞



T :=
∞∑
k=1
∞∑
j=1
akj = sup



∑
(j,k)∈C
akj ϶ C ⊂ N2, |B|< ∞


.
It suﬀices to show the first equality holds, as the other case will follow similarly. Let S =∑∞
j=1
∑∞
k=1 ajk and S′= sup
{∑
(j,k)∈B ajk ϶ B ⊂ N2, |B|< ∞
}
.
Then consider any bounded set B ⊂ N2; so B ⊂ {1, · · ·, n1} × {1, · · ·, n2} for some n1, n2 ∈ N. We
then have
1

∑
B
ajk ≤
n1∑
j=1
n2∑
k=1
ajk ≤
∞∑
j=1
∞∑
k=1
ajk .
where the first equality holds a + jk ≥ 0 for all j, k, so the sum can only increase if we add more
terms. But this holds for every B and thus holds if we take the supremum over all of them, so
S′≤ S.
To see that S ≤ S′, we can just note that
S = lim
J→∞
J∑
j=1
(
lim
K→∞
K∑
k=1
ajk
)
= lim
J→∞
lim
K→∞
J∑
j=1
K∑
k=1
ajk
≤ lim
J→∞
lim
K→∞
S′
= S′,
where the limits commute with finite sums, and we the sum can be replaced with S′because the
set {1, · · ·, K} × {1, · · ·J} is one of the finite sets over which the supremum is taken. Moreover, S′
is a number that doesn’t depend on J, K, yielding the final equality.
We will show that S = T by showing that S ≤ T and T ≤ S.
Let B ⊂ N2 be finite, so B ⊆ [0, I] × [0, J] ⊂ N2.
Now letting R > max(I, J ), we can define C = [0, R]2, which satisfies B ⊆ C ⊂ N2 and |C|< ∞ .
Moreover, since ajk ≥ 0 for all pairs (j, k), we have the following inequality:
∑
(j,k)∈B
ajk <
∑
(k,j)∈C
ajk ≤
∑
(k,j)∈C
ajk ≤ T,
since T is a supremum over all such sets C, and the terms of any finite sum can be rearranged.
But since this holds for every B, we this inequality also holds for the supremum of the smaller term
by order-limit laws, and so
S := sup
B
∑
(k,j)∈B
ajk ≤ T.
(Use epsilon-delta argument)
An identical argument shows that T ≤ S, yielding the desired equality.

2 Problem 2
We want to show the following equality:
∫1
0
g(x) dx =
∫1
0
f (x) dx.
To that end, we can rewrite this using the integral definition of g(x):
∫1
0
∫1
x
f (t)
t dt dx =
∫1
0
f (x) dx
Note that if we can switch the order of integration, we would have
∫1
0
∫1
x
f (t)
t dt dx =?
∫1
0
∫t
0
f (t)
t dx dt
=
∫1
0
f (t)
t
∫t
0
dx dt
=
∫1
0
f (t)
t (t − 0) dt
=
∫1
0
f (t) dt,
which is what we wanted to show, and so we are simply left with the task of showing that this is
switch of integrals is justified.
To this end, define
F : R2 → R
(x, t) ↦→χA(x, t) ˆf (x, t)
t .
where A =
{
(x, t) ⊂ R2 ϶ 0 ≤ x ≤ t ≤ 1
}
and ˆf (x, t) := f (t) is the cylinder on f .
This defines a measurable function on R2, since characteristic functions are measurable, the cylinder
over a measurable function is measurable, and products/quotients of measurable functions are
measurable.
In particular, |F |is measurable and non-negative, and so we can apply Tonelli to |F |. This allows
us to write
∫
R2
|F |=
∫1
0
∫t
0
⏐⏐⏐⏐
f (t)
t
⏐⏐⏐⏐dx dt
=
∫1
0
∫t
0
|f (t)|
t dx dt since t > 0
=
∫1
0
|f (t)|
t
∫t
0
dx dt
=
∫1
0
|f (t)|< ∞ ,

where the switch is justified by Tonelli and the last inequality holds because f was assumed to be
measurable.
Since this shows that F ∈ L1(R2), and we can thus apply Fubini to F to justify the initial switch.
3 Problem 3
Let A = {0 ≤ x ≤ y} ⊂ R2, and define
f (x, y) = x1/3
(1 + xy)3/2
F (x, y) = χA(x, y)f (x, y).
Note that F Then, if all iterated integrals exist and a switch of integration order is justified, we
would have
∫
R2
F =?
∫∞
0
∫∞
y
f (x, y) dx dy
=?
∫∞
0
∫∞
x
x1/3
(1 + xy)3/2 dy dx
= 2
∫
R
1
x2/3√
1 + x2 dx
= 2
∫1
0
1
x2/3√
1 + x2 dx + 2
∫∞
1
1
x2/3√
1 + x2 dx
≤
∫1
0
x−2/3 dx +
∫∞
0
x−5/3
= 2(3) + 2
( 3
2
)
< ∞ ,
where the first term in the split integral is bounded by using the fact that
√
1 + x2 ≥
√
x2 = x,
and the second term from x > 1 = ⇒ x > 0 = ⇒
√
1 + x2 ≥
√
1.
Since F is non-negative, we have |F |= F , and so the above computation would imply that F ∈
L1(R2). It thus remains to show that
∫
F is equal to its iterated integrals, and that the switch of
integration order is justified
Since F is non-negative, Tonelli can be applied directly if F is measurable in R2. But f is measurable
on A, since it is continuous at almost every point in A, and χA is measurable, so F is a product of
measurable functions and thus measurable.
4 Problem 4
4.1 Part (a)
For any x ∈ Rn, let Ax := A⋂(x − B).

We can then write At := A⋂(t − B) and As := A⋂(s − B), and thus
g(t) − g(s) = m(At) − m(As)
=
∫
Rn
χAt(x) dx −
∫
Rn
χAs(x) dx
=
∫
Rn
χAt(x) − χAs(x) dx
=
∫
Rn
χAt(x) − χAt(t − s + x) dx
(since x ∈ s − B ⇐ ⇒ s − x ∈ B ⇐ ⇒ t − (s − x) ∈ t − B),
and thus by continuity in L1, we have
|g(t) − g(s)| ≤
∫
Rn
|χAt(x) − χAt(t − s + x)|dx → 0 as t → s
which means g is continuous.
To see that
∫
g = m(A)m(B), if an interchange of integrals is justified, we can write
∫
Rn
g(t) dt =
∫
Rn
∫
Rn
χAt(x) dx dt
=
∫
Rn
∫
Rn
χA(x)χt−B(x, t) dx dt
=
∫
Rn
∫
Rn
χA(x)χt−B(x, t) dx dt
=
∫
Rn
∫
Rn
χA(x) χB(t − x) dx dt
(since x ∈ t − B ⇐ ⇒ t − x ∈ B)
=?
∫
Rn
∫
Rn
χA(x) χB(t − x) dt dx
=
∫
Rn
χA(x)
∫
Rn
χB(t − x) dt dx
=
∫
Rn
χA(x) m(B) dt
(by translation invariance of Lebesgue integral )
= m(B)
∫
Rn
χA dt
= m(B)m(A).
To see that this is justified, we note that that the map F (x, t) = χA(x) χB(x − t) is non-negative,
and we claim is measurable in R2n.
• The first component is χA(x), which is measurable on Rn, and thus the cylinder over it will
be measurable on R2n.

• The second component involves χB(t − x), which is χB(x) composed with a reflection (which
is still measurable) followed by a translation (which is again still measurable).
• Thus, as a product of two measurable functions, the integrand is measurable.
So Tonelli applies to |F |, and thus
∫
|F |= m(A)m(B) < ∞ since A, B were assumed to be bounded.
But then F is integrable by Fubini, and the claimed equality holds.
4.2 Part (b)
Supposing that m(A), m(B) > 0, we have
∫
g(t) dt > 0, using the fact that
∫
g = 0 a.e. ⇐ ⇒ g = 0
a.e., we can conclude that if T = {t ϶ g(t) ⁄= 0}, then m(T ) > 0. So there is some t ∈ Rn such
that g(t) ⁄= 0 , and since g is continuous, there is in fact some open ball Bt containing t such that
t′∈ Bt =⇒ g(t′) ⁄= 0. So we have
• ∀t′∈ Bt, A ⋂t′− B ⁄= ∅ ⇐ ⇒
• ∀t′∈ Bt, ∃x ∈ A⋂t′− B ⇐ ⇒
• ∀t′∈ Bt, ∃x such that x ∈ A and x ∈ t′− B ⇐ ⇒
• ∀t′∈ Bt, ∃x such that x ∈ A and x = t′− B for some b ∈ B ⇐ ⇒
• ∀t′∈ Bt, ∃x such that x ∈ A and t′= x + B for some b ∈ B ⇐ ⇒
• ∀t′∈ Bt, ∃t′such that t′∈ A + B
And thus Bt ⊆ A + B.
5 Problem 5
If the iterated integrals exist and are equal (so an interchange of integration order is justified), we
have
∫1
0
F (x)g(x) :=
∫1
0
( ∫x
0
f (y) dy
)
g(x) dx
=
∫1
0
∫x
0
f (y)g(x) dy dx
=?
∫1
0
∫1
y
f (y)g(x) dx dy
=
∫1
0
f (y)
( ∫1
y
g(x) dx
)
dy
=
∫1
0
f (y)(G(1) − G(y)) dy
= G(1)
∫1
0
f (y) dy −
∫1
0
f (y)G(y) dy
= G(1)(F (1) − F (0)) −
∫1
0
f (y)G(y) dy
= G(1)F (1) −
∫1
0
f (y)G(y) dy since F (0) = 0 ,
which is what we want to show.

To see that this is justified, let I = [0 , 1] and note that the integrand can be written as H(x, y) =
ˆf (x, y)ˆg(x, y) where ˆf (x, y) = χI f (y) and ˆg(x, y) = χI g(x) are cylinders over f and g respectively.
Since f, g are in L1(I), their cylinders are measurable over R× I, and thus ˆf , ˆg are measurable on R2
as products of measurable functions. Then H is a measurable function as a product of measurable
functions as well.
But then |H|is non-negative and measurable, so by Tonelli all iterated integrals will be equal. We
want to show that H ∈ L1(R2) in order to apply Fubini, so we will show that
∫
|H|< ∞ .
To that end, noting that f, g ∈ L1, we have
∫1
0 f := Cf < ∞ and
∫1
0 g := Cg < ∞ . Then,
∫
R2
|H|=
∫1
0
∫1
0
|f (x)g(y)|dx dy
=
∫1
0
∫1
0
|f (x)| |g(y)|dx dy
=
∫1
0
|g(y)|
( ∫1
0
|f (x)|dx
)
dy
=
∫1
0
|g(y)|Cf dy
= Cf
∫1
0
|g(y)|dy
= Cf Cg < ∞ ,
and thus by Fubini, the original interchange of integrals was justified.
6 Problem 6
6.1 Part (a)
We have

∫
R
|Ah(f )(x)|dx =
∫
R
⏐⏐⏐⏐⏐
1
2h
∫x+h
x−h
f (y) dy
⏐⏐⏐⏐⏐dx
= 1
2h
∫
R
⏐⏐⏐⏐⏐
∫x+h
x−h
f (y) dy
⏐⏐⏐⏐⏐dx
≤ 1
2h
∫
R
( ∫x+h
x−h
|f (y)|dy
)
dx
= 1
2h
∫
R
∫x+h
x−h
|f (y)|dy dx
=?
1
2h
∫
R
∫y+h
y−h
|f (y)|dx dy
= 1
2h
∫
R
|f (y)|
∫y+h
y−h
dx dy
= 1
2h
∫
R
|f (y)|((y + h) − (y − h)) dy
= 1
2h
∫
R
2h|f (y)|dy
=
∫
R
|f (y)|dy < ∞
.
since f was assumed to be in L1(R), where the changed bounds of integration are determined by
considering the following diagram:
To justify the change in the order of integration, consider the function H(x, y) = 1
2h χA(x, y)f (y)
where A =
{
(x, y) ∈ R2 ϶ − ∞ < x − h ≤ x, y ≤ x + h
}
. Since f is measurable, the constant func-
tion (x, y) ↦→ 1
2h is measurable, and characteristic functions are measurable, H is a product of
measurable functions and thus measurable.
Thus it makes sense to write
∫
|H|as an iterated integral by Tonelli, and since
∫
R2 |H|=
∫
R |Ah(f )|<
∞ by the above calculation, we have H ∈ L1(R2), and Fubini applies.
6.2 Part (b)
Let ε > 0; we then have

Figure 1: Changing the bounds of integration
∫
R
|Ah(f )(x) − f (x)|dx =
∫
R
⏐⏐⏐⏐⏐
(
1
2h
∫
B(h,x)
f (y) dy
)
− f (x)
⏐⏐⏐⏐⏐dx
=
∫
R
⏐⏐⏐⏐⏐
(
1
2h
∫
B(h,x)
f (y) dy
)
− 1
2h
∫
B(h,x)
f (x) dy
⏐⏐⏐⏐⏐dx
since 1
2h
∫x+h
x−h
f (x) dy = 1
2h f (x)((x + h) − (x − h)) = 1
2h f (x)2h = f (x)
=
∫
R
⏐⏐⏐⏐⏐
1
2h
∫
B(h,x)
f (y) − f (x) dy
⏐⏐⏐⏐⏐dx
≤
∫
R
1
2h
∫x+h
x−h
|f (y) − f (x)|dy dx
≤
∫
R
1
2h
∫h
−h
|f (y − x) − f (x)|dy dx
.
but since h → 0 will force y → x in the integral, for a fixed x we can let τx(y) = f (y − x) and we
have ‖τx − f ‖1 → 0 by continuity in L1. Thus
∫h
−h |f (y − x) − f (x)| → 0, forcing ‖Ah(f ) − f ‖1 → 0
as h → 0.

Assignment 6: The Fourier Transform
D. Zack Garza
November 5, 2019
Contents
1 Problem 1 1
2 Problem 2 2
2.1 Part (a) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 Part (b) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2.1 (i) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2.2 (ii) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
3 Problem 3 4
3.1 (a) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1.1 (i) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1.2 (ii) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2 (b) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
4 Problem 4 5
4.1 (a) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
4.1.1 (i) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
4.1.2 (ii) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
4.2 (b) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
5 Problem 5 7
5.1 (a) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
5.2 (b) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
5.2.1 (i) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
5.2.2 (ii) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
5.3 (c) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
6 Problem 6 9
1 Problem 1
Assuming the hint, we have
1

lim
|ξ|→∞
ˆf (ξ) = lim
|ξ′|→ 0
1
2
∫
Rn
[
f (x)) − f (x − ξ′)
]
e− 2πix·ξ dx
.
The fact that the limit as ξ → ∞ is equivalent to the limit ξ′ → 0 is a direct consequence of
computing
lim
|ξ|→∞
ξ
2|ξ|2 = lim
|ξ|→∞
1
2|ξ|
ξ
|ξ|= 0,
since ξ
|ξ| is a unit vector, and the term 1
2|ξ| is a scalar that goes to zero.
But as an immediate consequence, this yields
⏐⏐⏐ˆf (ξ)
⏐⏐⏐= 1
2
⏐⏐⏐⏐
∫
Rn
[
f (x) − f (x − ξ′)
]
e− 2πix·ξ dx
⏐⏐⏐⏐
≤
∫
Rn
⏐⏐f (x) − f (x − ξ′)
⏐⏐
⏐⏐⏐e− 2πix·ξ
⏐⏐⏐dx
≤
∫
Rn
⏐⏐f (x) − f (x − ξ′)
⏐⏐dx
→ 0,
which follows from continuity in L1 since f (x − ξ′) → f (x) as ξ′→ 0.
It thus only remains to show that the hint holds.
Note: Sorry, I couldn’t figure out how to prove the hint!!
2 Problem 2
2.1 Part (a)
Assuming an interchange of integrals is justified, we have

[f ∗g(ξ) :=
∫ ∫
f (x − y)g(y) e− 2πix·ξ dy dx
=?
∫ ∫
f (x − y)g(y) e− 2πix·ξ dx dy
=
∫ ∫
f (t)e− 2πi(x− y)·ξ g(y) e− 2πiy·ξ dx dy
(t = x − y, dt = dx)
=
∫ ∫
f (t)e− 2πit·ξg(y)e− 2πiy·ξ dt dy
=
∫
f (t)e− 2πit·ξ
( ∫
g(y) e− 2πiy·ξ dy
)
dt
=
∫
f (t)e− 2πit·ξ ˆg(ξ) dt
= ˆg(ξ)
∫
f (t)e− 2πit·ξ dt
= ˆg(ξ) ˆf (ξ).
To see that this swap is justified, we’ll apply Fubini-Tonelli. Note that if f, g ∈ L1(Rn), then
the map (x, y) ↦→f (x − y) is measurable on Rn × Rn. Since g is measurable as well, taking
the cylinder on g is also measurable on Rn × Rn. The exponential is continuous, and thus
measurable on Rn. Thus the integrand F (x, y) is a product of measurable functions and thus
measurable. In particular, |F |= |f g|is measurable, and ths computation shows that one
iterated integral is finite. From a previous homework question, we know that f ∈ L1 =⇒ ˆf
is bounded, and thus ˆf ˆg is bounded. Since |F |is measurable and one iterated integrable was
finite, Fubini-Tonelli applies.
2.2 Part (b)
We’ll use the following lemma: if ˆf = ˆg, then f = g almost everywhere.
2.2.1 (i)
By part 1, we have
[f ∗g = ˆf ˆg = ˆg ˆf = [g ∗f ,
and so by the lemma, f ∗g = g ∗f .
Similarly, we have
\(f ∗g) ∗h = [f ∗g ˆh = ˆf ˆg ˆh = ˆf [g ∗h = f ∗(g ∗h).
2.2.2 (ii)
Suppose that there exists some I ∈ L1 such that f ∗ I = f . Then [f ∗I = ˆf by the lemma, so
ˆf ˆI = ˆf by the above result.

But this says that ˆf (ξ) ˆI(ξ) = ˆf (ξ) almost everywhere, and thus ˆI(ξ) = 1 almost everywhere. Then
lim
|ξ|→∞
ˆI(ξ) ⁄= 0,
which by Problem 1 shows that I can not be in L1, a contradiction.
3 Problem 3
3.1 (a)
3.1.1 (i)
Let g(x) = f (x − y). We then have
ˆg(ξ) :=
∫
g(x)e− 2πix·ξ dx
=
∫
f (x − y)e− 2πix·ξ dx
=
∫
f (x − y)e− 2πi(x− y)·ξe− 2πiy·ξ dx
= e− 2πiy·ξ
∫
f (x − y)e− 2πi(x− y)·ξ dx
(t = x − y, dt = dx)
= e− 2πiy·ξ
∫
f (t)e− 2πit·ξ dt
= e− 2πiy·ξ ˆf (ξ).
3.1.2 (ii)
Let h(x) = e2πix·yf (x). We then have
ˆh(ξ) :=
∫
e2πix·yf (x)e− 2πix·ξ dx
=
∫
e2πix·y− 2πix·ξ)f (x dx
=
∫
f (ξ − y)e− 2πix·(ξ− y) dx
= ˆf (ξ − y).
3.2 (b)
We’ll use the fact that if ⟨ ·, · ⟩is an inner product on a vector space V and A is an invertible
linear transformation, then for all x, y ∈ V we have
⟨Ax, y⟩=
⟨
x, A T y
⟩

where A− T denotes the transpose of the inverse of A (or (A− 1)∗ if V is complex).
We then have
1
|det T |
ˆf (T − T ξ) = 1
|det T |
∫
f (x)e− 2πix·T − T ξ dx
x ↦→T x, dx ↦→ |det T |dx
= 1
|det T |
∫
f (T x)e− 2πiT x·T − T ξ|det T |dx
=
∫
f (T x)e− 2πix·ξ dx
since T x ·T − T ξ = T − 1T x ·ξ = x ·ξ
= \(f ◦T )(ξ).
4 Problem 4
4.1 (a)
4.1.1 (i)
Let g(x) = xf (x). Then if an interchange of the derivative and the integral is justified, we have
∂
∂ξ
ˆf (ξ) := ∂
∂ξ
∫
f (x)e− 2πix·ξ dx
=?
∫
f (x) ∂
∂ξ e− 2πix·ξ dx
=
∫
f (x)2πixe− 2πix·ξ dx
= 2πi
∫
xf (x)e− 2πix·ξ dx
:= 2πiˆg(ξ).
To see that the interchange is justified, we just note that we can apply the dominated conver-
gence theorem, since
∫⏐⏐f (x)e− 2πix·ξ⏐⏐≤
∫
|f |< ∞ , where we assumed f ∈ L1.
4.1.2 (ii)
We have

ˆh(ξ) :=
∫∂f
∂x (x)e− 2πix·ξ dx
= f (x)e− 2πix·ξ
⏐⏐⏐
x=∞
x=−∞
−
∫
f (x)(2πiξ)e− 2πix·ξ dx
(integrating by parts)
= −
∫
f (x)(− 2πiξ)e− 2πix·ξ dx
(since f (∞ ) = f (−∞ ) = 0)
= 2πiξ
∫
f (x)e− 2πix·ξ dx
:= 2πiξ ˆf (ξ).
4.2 (b)
Let G(x) = e− πx2
and ∂ξ be the operator that differentiates with respect to ξ.
Then
∂ξ
( ˆG(ξ)
G(ξ)
)
= G(ξ)∂ξ ˆG(ξ) − ˆG(ξ)∂ξG(ξ)
G(ξ)2 ,
and the claim is that this is zero. This happens precisely when the numerator is zero, so we’d like
to show that
G(ξ)∂ξ ˆG(ξ) − ˆG(ξ)∂ξG(ξ) = 0 .
A direct computation shows that
∂ξG(ξ) = − 2πξG(ξ), (1)
and we claim that ∂ξ ˆG(ξ) = − 2πξ ˆG(ξ) as well, which follows from the following computation:

∂ξ ˆG(ξ) := ∂ξ
∫
G(x)e− 2πix·ξ dx
=
∫
G(x)∂ξe− 2πix·ξ dx
=
∫
G(x)(− 2πix)e− 2πix·ξ dx
=
∫
G(x)(− 2πix)e− 2πix·ξ dx
= i
∫
2πxG(x)e− 2πix·ξ dx
= i
∫
∂xG(x)e− 2πix·ξ dx by (1)
:= i \∂xG(x)(ξ)
= i (2πiξ ˆG(ξ)) by part (i)
= − 2πξ ˆG(ξ).
We can thus write
G(ξ)∂ξ ˆG(ξ) − ˆG(ξ)∂ξG(ξ) = G(ξ)(− 2πξ ˆG(ξ)) − ˆG(ξ)(− 2πξG(ξ)),
which is patently zero.
It follows that
ˆG(ξ)
G(ξ) = c0 for some constant c0, from which it follows that ˆG(ξ) = c0G(ξ).
Using the fact that G(0) = 1 by direct evaluation and ˆG(0) =
∫
G(x) dx = 1, we can conclude that
c0 = 1 and thus ˆG(ξ) = G(ξ).
5 Problem 5
5.1 (a)
By a direct computation. we have

ˆD(ξ) :=
∫1
2
− 1
2
1e− 2πixξ dx
=
∫1
2
− 1
2
cos(− 2πxξ) + i sin(− 2πxξ) dx
=
∫1
2
− 1
2
cos(− 2πxξ) dx
(since sin is odd and the domain is symmetric about 0)
= 2
∫1
2
0
cos(− 2πxξ) dx
(since cos is even and the domain is symmetric about 0)
= 2
(
1
2πξ sin(− 2πxξ)
⏐⏐⏐
x= 1
2
x=0
)
= sin(πξ)
πξ .
5.2 (b)
5.2.1 (i)
Since F (x) = D(x) ∗D(x), we have ˆF (ξ) = ( ˆD(ξ))2 by question 2a, and so ˆF (ξ) =
( sin(πξ)
πξ
) 2
.
5.2.2 (ii)
Letting F denote the Fourier transform operator, we have F 2(h)(ξ) = h(− ξ) for any h ∈ L1. In
particular, if f is an even function, then f (ξ) = − f (ξ) and F 2(f ) = f .
In this case, letting F be the box function, F can be seen to be even from its definition. Since
f := F (F ) by part (i), we have
ˆf := F (f ) = F (F (F )) = F 2(F ) = F,
which says that ˆf (x) = F (x), the original box function.
5.3 (c)
By a direct computation of the integral in question, we have

I(x) :=
∫
e− 2π|ξ|e2πixξ dξ
=
∫0
−∞
e− 2π(− ξ)e− 2πixξ dξ +
∫∞
0
e2πξ e2πixξ dξ
=
∫∞
0
e− 2πξ e− 2πixξ dξ +
∫∞
0
e2πξ e2πixξ dξ
by the change of variables ξ ↦→ −ξ, dξ ↦→ −dξ and swapping integration bounds
=
∫∞
0
e− 2πξ e− 2πixξ + e2πξ e2πixξ dξ
= 1
2π
∫∞
0
e− ue− ixu + e− ueixu du
= 1
2π
∫∞
0
e− u(1+ix) + e− u(1− ix) du
= 1
2π
(
− e− u(1+ix)
1 + ix
⏐⏐⏐
u=∞
u=0
+ − e− u(1− ix)
1 + ix
⏐⏐⏐
u=∞
u=0
)
= 1
2π
( 1
1 + ix + 1
1 − ix
)
= 1
2π
2
1 + x2
= 1
π
1
1 + x2 ,
so P (x) = I(x).
Then, by the Fourier inversion formula, we have
I(x) = P (x) =
∫
ˆP (ξ)e− 2πixξ dx
=⇒
∫
e− 2π|ξ|e2πixξ =
∫
ˆP (ξ)e− 2πixξ dx
=⇒
∫
e− 2π|ξ|e2πixξ − ˆP (ξ)e− 2πixξ dx = 0
=⇒
∫(
e− 2π|ξ|− ˆP (ξ)
)
e− 2πixξ dx = 0
=⇒
(
e− 2π|ξ|− ˆP (ξ)
)
e− 2πixξ =a.e. 0
=⇒ e− 2π|ξ|=a.e ˆP (ξ),
where equality is almost everywhere and follows from the fact that if
∫
f = 0 then f = 0 almost
everywhere.
6 Problem 6
We first note that if Gt(x) := t− ne− π|x|2/t2
, then ˆGt(ξ) = e− πt2|ξ|2
.

Moreover, if an interchange of integrals is justified, we have have
‖f ‖1 :=
∫
Rn
⏐⏐⏐⏐
∫∞
0
Gt(x)e− πt2
t2ε− 1 dt
⏐⏐⏐⏐dx
=
∫
Rn
∫∞
0
Gt(x)e− πt2
t2ε− 1 dt dx
since the integrand and thus integral is positive.
=?
∫∞
0
∫
Rn
Gt(x)e− πt2
t2ε− 1 dx dt
=
∫∞
0
e− πt2
t2ε− 1
( ∫
Rn
Gt(x) dx
)
dt
=
∫∞
0
e− πt2
t2ε− 1 (1) dt
=
∫∞
0
e− πt2
t2ε− 1 dt,
which we claim is finite, so f ∈ L1.
To see that the norm is finite, we note that
t ∈ [0, 1] = ⇒ e− πt2
< 1
and if we take ε < 1
2 , we have 2ε − 1 < 0 and thus
t ∈ [1, ∞ ) = ⇒ t2ε− 1 ≤ 1.
Thus
∫∞
0
e− πt2
t2ε− 1 dt =
∫1
0
e− πt2
t2ε− 1 dt +
∫∞
1
e− πt2
t2ε− 1 dt
≤
∫1
0
t2ε− 1 dt +
∫∞
1
e− πt2
dt
≤
∫1
0
t2ε− 1 dt +
∫∞
0
e− πt2
dt
= 1
2ε + 1
2 < ∞ ,
where the first term is obtained by directly evaluating the integral, and the second is derived from
the fact that its integral over the real line is 1 and it is an even function.
Justifying the interchange: we note that the integrand Gt(x)e− πt2
t2ε− 1 is non-negative, and
we’ve just showed that one of the iterated integrals is absolutely convergent, so Tonelli will
apply if the integrand is measurable. But Gt(x) is a continuous function on Rn and the
remaining terms are continuous on R, so they are all measurable on Rn and R respectively
But then taking cylinders on everything in sight yields measurable functions, and the product
of measurable functions is measurable.
If another interchange of integrals is justified, we can compute

ˆf (ξ) :=
∫
Rn
( ∫∞
0
Gt(x)e− πt2
t2ε− 1 dt
)
e− 2πix·ξ dx
=
∫
Rn
∫∞
0
Gt(x)e− πt2
t2ε− 1e− 2πix·ξ dt dx
=?
∫∞
0
∫
Rn
Gt(x)e− πt2
t2ε− 1e− 2πix·ξ dx dt
=
∫∞
0
e− πt2
t2ε− 1
( ∫
Rn
Gt(x)e− 2πix·ξ dx
)
dt
=
∫∞
0
e− πt2
t2ε− 1 ˆGt(ξ) dt
=
∫∞
0
e− πt2
t2ε− 1e− πt2|ξ|2
dt
=
∫∞
0
e− πt2(1+|ξ|2)t2ε− 1 dt
=
∫∞
0
e− π(t
√
1+|ξ|2)2
t2ε− 1 dt
s = t
√
1 + |ξ|2, ds =
√
1 + |ξ|2dt
=
∫∞
0
e− πs2

 s√
1 − |ξ|2


2ε− 1
1√
1 + |ξ|2
ds
= (1 + |ξ|2)− 2ε− 1
2 (1 + |ξ|2)− 1
2
∫∞
0
e− πs2
s2ε− 1 ds
= (1 + |ξ|2)− ε
∫
e− πt2
t2ε− 1 dt
:= F (ξ)‖f ‖1.
To see that the interchange is justified, note that
∫
Rn
∫∞
0
⏐⏐⏐Gt(x)e− πt2
t2ε− 1e− 2πix·ξ
⏐⏐⏐dt dx =
∫
Rn
∫∞
0
⏐⏐⏐Gt(x)e− πt2
t2ε− 1
⏐⏐⏐dt dx,
since
⏐⏐e2πix·ξ⏐⏐= 1 . The integrand appearing is precisely what we showed was measurable
when computed ‖f ‖1 above, so Tonelli applies.
Thus F (ξ) is the Fourier transform of the function g(x) := f (x)/‖f ‖1.

Problem Set 7
D. Zack Garza
November 14, 2019
Contents
1 Problem 1 1
1.1 Part a . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Part b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2 Problem 2 3
2.1 Part a: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2 Part b: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3 Problem 3 5
3.1 Part a . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.2 Part b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
4 Problem 4 6
4.1 Part a . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4.1.1 i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4.1.2 ii . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.2 Part b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.2.1 i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.2.2 ii . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
5 Problem 5 9
5.1 Part 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
5.2 Part b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
5.3 Part c . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
6 Problem 6 11
6.1 Part a . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
6.2 Part b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1 Problem 1
1.1 Part a
We want to show that ℓ2(N) is complete, so let {xn} ⊆ ℓ2(N) be a Cauchy sequence. We then have
‖xj − xk‖ℓ2 → 0, and we want to produce some x := limn→∞ xn such that x ∈ ℓ2.
1

To this end, for each fixed index i, define
xi := limn→∞ xn
i .
This is well-defined since ‖xj − xk‖ℓ2 =∑
i
⏐⏐⏐xj
i − xk
i
⏐⏐⏐
2
→ 0, and since this is a sum of positive real
numbers that approaches zero, each term must approach zero. But then for a fixed i, the sequence⏐⏐⏐xj
i − xk
i
⏐⏐⏐
2
is a Cauchy sequence of real numbers which necessarily converges by thethe completeness
of R.
We also have ‖x − xj‖ℓ2 → 0 since
‖x − xj‖ℓ2 = ‖ lim
k→∞
xk − xj‖
ℓ2
= lim
k→∞
‖xk − xj‖ℓ2 → 0
where the limit can be passed through the norm because the map t ↦→ ‖t‖ℓ2 is continuous. So
xj → x in ℓ2 as well.
It remains to show that x ∈ ℓ2(N), i.e. that ∑
i |xi|2 < ∞ . To this end, we write
‖x‖ℓ2 = ‖x − xj + xj‖ℓ2
≤ ‖x − xj‖ℓ2 + ‖xj‖ℓ2
→ M < ∞ ,
where limj ‖x − xj‖ℓ2 = 0 by the previous argument, and the second term is bounded because
xj ∈ ℓ2 ⇐ ⇒ ‖ xj‖ℓ2 := M < ∞ .
1.2 Part b
Let H be a Hilbert space with inner product ⟨ ·, · ⟩and induced norm ‖ · ‖.
Lemma: For any complex number z, we have
ℑ(z) = ℜ(− iz),
and as a corollary, since the inner product on H takes values in C, we have
ℜ(⟨x, iy ⟩) = ℜ(− i⟨x, y ⟩) = ℑ(⟨x, y ⟩).
2

We can compute the following:
‖x + y‖2 = ‖x‖2 + ‖y‖2 + 2 ℜ (⟨x, y ⟩)
‖x − y‖2 = ‖x‖2 + ‖y‖2 − 2 ℜ (⟨x, y ⟩)
‖x + iy‖2 = ‖x‖2 + ‖y‖2 + 2 ℜ (⟨x, iy ⟩)
= ‖x‖2 + ‖y‖2 + ℑ(⟨x, y ⟩)
‖x − iy‖2 = ‖x‖2 + ‖y‖2 − 2 ℜ (⟨x, iy ⟩)
= ‖x‖2 + ‖y‖2 + ℑ(⟨x, y ⟩)
and summing these all
‖x + y‖2 − ‖x − y‖2 + i‖x + iy‖2 − i‖x + iy‖ = 4 ℜ (⟨x, y ⟩) + 4i ℑ (⟨x, y ⟩)
= 4⟨x, y ⟩.
To conclude that a linear map U is an isometry iff U is unitary, if we assume U is unitary then we
can write
‖x‖2 := ⟨x, x ⟩= ⟨U x, U x ⟩:= ‖U x‖2.
Assuming now that U is an isometry, by the polarization identity we can write
⟨U x, U y ⟩= 1
4
(
‖U x + U y‖2 + ‖U x − U y‖2 + i‖U x + U y‖2 − i‖U x + U y‖2)
= 1
4
(
‖U (x + y)‖2 + ‖U (x − y)‖2 + i‖U (x + y)‖2 − i‖U (x + y)‖2)
= 1
4
(
‖x + y‖2 + ‖x − y‖2 + i‖x + y‖2 − i‖x + y‖2)
= ⟨x, y ⟩.
2 Problem 2
Lemma: The map ⟨ ·, · ⟩: H × H → R is continuous.
Proof:
Let xn → x and yn → y, then
3

|⟨xn, y n⟩ − ⟨x, y ⟩|= |⟨xn, y n⟩ − ⟨x, y n⟩+ ⟨x, y n⟩ − ⟨x, y ⟩|
= |⟨xn − x, y n⟩+ ⟨x, y n − y⟩|
≤ ‖xn − x‖‖yn‖+ ‖x‖‖yn − y‖
→ 0 ·M + C ·0 < ∞ ,
where ‖yn‖ → ‖ y‖ := M < ∞ since y ∈ H implies that ‖y‖ is finite.
2.1 Part a:
We want to show that sequences in E⊥ converge to elements of E⊥. Using the lemma, letting {en}
be a sequence in E⊥, so y ∈ E =⇒ ⟨ en, y ⟩= 0 . Since H is complete, en → e ∈ H; we can show
that e ∈ E⊥ by letting y ∈ E be arbitrary and computing
⟨e, y ⟩=
⟨
limn en, y
⟩
= limn ⟨en, y ⟩= limn 0 = 0 ,
so e ∈ E⊥.
2.2 Part b:
Let S := span H (E); then the smallest closed subspace containing E is S, the closure of S. We will
proceed by showing that E⊥⊥ = S.
S ⊆ E⊥⊥:
Let {xn} be a sequence in S, so xn → x ∈ S.
First, each xn is in E⊥⊥, since if we write xn =∑aiei where ei ∈ E, we have
y ∈ E⊥ =⇒ ⟨ xn, y ⟩=
⟨∑
i
aiei, y
⟩
=
∑
i
ai⟨ei, y ⟩= 0 = ⇒ xn ∈ (E⊥)⊥.
It remains to show that x ∈ E⊥⊥, which follows from
y ∈ E⊥ =⇒ ⟨ x, y ⟩=
⟨
limn xn, y
⟩
= limn ⟨xn, y ⟩= 0 = ⇒ x ∈ (E⊥)⊥,
where we’ve used continuity of the inner product.
E⊥⊥ ⊆ S:
For notational convenience, let Sc denote the closure S. Let x ∈ E⊥⊥. Noting that Sc is closed, we
can define P , the operator projecting elements onto Sc, and write
x = P x + (x − P x) ∈ Sc ⊕ S⊥
c
4

But since ⟨x, x − P x⟩= 0 (because x − P x ∈ E⊥ and x ∈ (E⊥)⊥), we can rewrite the first term
in this inner product to obtain
0 = ⟨x, x − P x⟩= ⟨P x + (x − P x), x − P x⟩= ⟨P x, x − P x⟩+ ⟨x − P x, x − P x⟩,
where we can note that the first term is zero because P x ∈ Sc and x − P x ∈ S⊥
c , and the second
term is ‖x − P x‖2.
But this says ‖x − P x‖2 = 0 , so x − P x = 0 and thus x = P x ∈ Sc, which is what we wanted to
show.
3 Problem 3
3.1 Part a
We compute
‖e0‖2 =
∫1
0
12 dx = 1
‖e1‖2 =
∫1
0
3(2x − 1)2 = 1
2 (2x − 1)2
⏐⏐⏐⏐
1
0
= 1
⟨e0, e 1⟩=
∫1
0
√
3(2x − 1) dx =
√
3
4 (2x − 1)
⏐⏐⏐⏐
1
0
= 0.
which verifies that this is an orthonormal system.
3.2 Part b
We first note that this system spans the degree 1 polynomials in L2([0, 1]), since we have
[
1 0
2
√
3
√
3
]
[1, x]t = [e0, e1]
which exhibits a matrix that changes basis from {1, x} to {e0, e1} which is invertible, so both sets
span the same subspace.
Thus the closest degree 1 polynomial f to x3 is given by the projection onto this subspace, and
since {ei} is orthonormal this is given by
5

f (x) =
∑
i
⟨
x3, e i
⟩
ei
=
⟨
x3, 1
⟩
1 +
⟨
x3,
√
3(2x − 1)
⟩√
3(2x − 1)
=
∫1
0
x2 dx +
√
3(2x − 1)
∫1
0
√
3x2(2x − 1) dx
= 1
3 +
√
3(2x − 1)
√
3
6
= x − 1
6 .
We can also compute
‖f − g‖2
2 =
∫1
0
(x2 − x + 1
6 )2 dx
= 1
180
=⇒ ‖ f − g‖2 = 1√
180 .
4 Problem 4
4.1 Part a
4.1.1 i
We can first note that
⟨
1/
√
2, cos(2πnx)
⟩
=
⟨
1/
√
2, sin(2πmx)
⟩
= 0 for any n or m, since this
involves integrating either sine or cosine over an integer multiple of its period.
Letting m, n ∈ Z, we can then compute
⟨cos(2πnx), sin(2πmx)⟩=
∫1
0
cos(2πnx) sin(2πmx) dx
= 1
2
∫1
0
sin(2π(n + m)x) − sin(2π(n − m)x) dx
= 1
2
∫1
0
sin(2π(n + m)x) − 1
2
∫1
0
sin(2π(n − m)x) dx
= 0,
which again follows from integration of sine over a multiple of its period (where we use the fact
that m + n, m − n ∈ Z).
Similarly,
6

⟨cos(2πnx), cos(2πmx)⟩=
∫1
0
cos(2πnx) cos(2πmx) dx
= 1
2
∫1
0
cos(2π(m + n)x) + cos(2π(m − n)x) dx
=
{1
2
∫1
0 cos(4πnx) + 1 dx = 1 m = n
0 m ⁄= n .
⟨sin(2πnx), sin(2πmx)⟩=
∫1
0
sin(2πnx) sin(2πmx) dx
= 1
2
∫1
0
cos(2π(m − n)x) + cos(2π(m + n)x) dx
=
{1
2
∫1
0 1 + cos(4πnx) dx = 1 m = n
0 m ⁄= n .
Thus each pairwise combination of elements are orthonormal, making the entire set orthonormal.
4.1.2 ii
We have
⟨
e2πkx, e −2πiℓx
⟩
=
∫1
0
e2πikxe2πiℓx dx
=
∫1
0
e2πikxe−2πiℓx dx
=
∫1
0
e2πi(k−ℓ)x dx
(=
∫1
0
1 dx = 1 if k = ℓ, otherwise: )
= e2πi(k−ℓ)x
2πi(k − ℓ)
⏐⏐⏐
1
0
= e2πi(k−ℓ) − 1
2πi(k − ℓ)
= 0,
since e2πik = 1 for every k ∈ Z, and k − ℓ ∈ Z. Thus this set is orthonormal.
4.2 Part b
4.2.1 i
By the Weierstrass approximation theorem for functions on a bounded interval, we can find a
polynomials Pn(x) such that ‖f − Pn‖∞ → 0, i.e. the Pn uniformly approximate f on [0, 1].
7

Letting ε > 0, we can thus choose a P such that ‖f − P ‖∞ < ε , which necessarily implies that
‖f − P ‖L1 < ε since we have
∫1
0
|f (x) − P (x)|dx ≤
∫1
0
ε dx = ε.
Thus we can write
f (x) = P (x) + (f (x) − P (x))
where h(x) := f (x) − P (x) satisfies ‖h‖L1 < ε . It only remains to show that P ∈ L2([0, 1]), but
this follows from the fact that any polynomial on a compact interval is uniformly bounded, say
|P (x)| ≤M < ∞ for all x ∈ [0, 1], and thus
‖P ‖2
L2 =
∫1
0
|P (x)|2 dx ≤
∫1
0
M 2 dx = M 2 < ∞ .
It follows that we can let g = P and h = f − P to obtain the desired result.
4.2.2 ii
By part (i), the claim is that it suﬀices to show this is true for f ∈ L2. In this case, we can identify
∫1
0
f (x) cos(2πkx) dx := ℜ( ˆf (k))
∫1
0
f (x) sin(2πkx) dx := ℑ( ˆf (k)),
the real and imaginary parts of the kth Fourier coeﬀicient of f respectively.
By Bessel’s inequality, we know that
{
ˆf (k)
}
k∈N
∈ ℓ1(N), and so ∑
k
⏐⏐⏐ˆf (k)
⏐⏐⏐< ∞ .
But this is a convergent sequence of real numbers, which necessarily implies that
⏐⏐⏐ˆf (k)
⏐⏐⏐→ 0. In
particular, this also means that its real and imaginary parts tend to zero, which is exactly what we
wanted to show.
If we instead have f ∈ L1, write f = g + h where g ∈ L2 and ‖h‖L1 → 0. Then
⏐⏐⏐⏐
∫1
0
f (x) cos(2πkx) dx
⏐⏐⏐⏐=
⏐⏐⏐⏐
∫1
0
(g(x) + h(x)) cos(2πkx) dx
⏐⏐⏐⏐
≤
⏐⏐⏐⏐
∫1
0
g(x) cos(2πkx) dx
⏐⏐⏐⏐+
⏐⏐⏐⏐
∫1
0
h(x) cos(2πkx) dx
⏐⏐⏐⏐
≤
⏐⏐⏐⏐
∫1
0
g(x) cos(2πkx) dx
⏐⏐⏐⏐+
∫1
0
|h(x)||cos(2πkx)|dx
= |ˆg(k)|+ ε
→ 0,
with a similar computation for
∫
f (x) sin(2πkx).
8

5 Problem 5
5.1 Part 1
We use the following algorithm: given {v}i, we set
• e1 = v1, and then normalize to obtain ˆe1 = e1/‖e1‖
• ei = vi −∑
k≤i−1 ⟨vi, ˆei⟩ˆei
The result set {ˆei} is the orthonormalized basis.
We set e1 = 1, and check that ‖e1‖2 = 2, and thus set ˆe1 = 1√
2 .
We then set
e2 = x − ⟨x, ˆe1⟩ˆe1
= x − ⟨x, 1⟩1
= x −
∫1
−1
1√
2 x dx
= x −
∫
odd function
= x,
and so e2 = x. We can then check that
‖e2‖ =
(∫1
−1
x2 dx
) 1/2
=
√
2
3 ,
and so we set ˆe2 =
√
3
2 x.
We continue to compute
e3 = x2 −
⟨
x2, ˆe1
⟩
ˆe1 −
⟨
x2, ˆe2
⟩
ˆe2
= x2 − 1
2
∫1
−1
x2 dx − 3
2 x
∫1
−1
x3 dx
= x2 −
(1
6 x3
) ⏐⏐1
−1 + 3
2 x
∫1
−1
odd function
= x2 − 1
3 .
We can then check that ‖e3‖2 = 8
45 , so we set
9

ˆe3 =
√
45
8 (x2 − 1
3 )
= 1
2
√
45
2
1
3 (3x2 − 1)
= 1
3
√
45
2
(
3x2 − 1
2
)
.
In summary, this yields
ˆe1 = 1√
2
ˆe2 = x
ˆe3 = 1
3
√
45
2
(
3x2 − 1
2
)
,
which are scalar multiples of the first three Legendre polynomials.
5.2 Part b
Let p(x) = a + bx + cx2, we are then looking for p such that ‖x3 − p(x)‖2
2 is minimized. Noting
that
p(x) ∈ span
{
1, x, x2
}
= span {P0(x), P1(x), P2(x)} := S,
we can conclude that p(x) will be the projection of x3 onto S. Thus p(x) =∑2
i=0
⟨
x3, ˆei
⟩
ˆei.
Proceeding to compute the terms in this expansion, we can note that
⟨
x3, f
⟩
for any f that is even
will result in integrating an odd function over a symmetric interval, yielding zero. So only one term
doesn’t vanish:
⟨
x3, x
⟩
x = x
∫1
−1
x4 dx = 2
5 x
.
And thus p(x) = 2
5 x is the minimizer.
5.3 Part c
The first three conditions necessitate g ∈ S⊥ and ‖g‖ = 1 . Since S is a closed subspace, we can
write x3 = p(x) + (x3 − p(x)) ∈ S ⊕ S⊥, and so x3 − p(x) ∈ S⊥.
The claim is that g(x) := x3 − p(x) is a scalar multiple of the desired maximizer. This follows from
the fact that
⏐⏐⏐
⟨
x3 − p, g
⟩⏐⏐⏐≤ ‖x3 − p‖‖g‖
10

by Cauchy-Schwarz, with equality precisely when g = λ(x3 − p) for some scalar λ. However, the
restriction ‖g‖ = 1 forces λ = ‖x3 − p‖−1.
A computation shows that
‖x3 − p‖
2
=
∫1
0
(x3 − 2
5 x)2 dx = 19
525 ,
and so we can take
g(x) := 25√
19
(
x3 − 2
5 x
)
.
6 Problem 6
6.1 Part a
To see that g ∈ C , we can compute
⟨g, 1⟩=
∫1
0
18x2 − 5 dx = 6 − 5 = 1
⟨g, x ⟩=
∫1
0
18x3 − 5x dx = 18
4 − 5
2 = 2.
To see that C = g + S⊥, let f ∈ C , so ⟨f, 1⟩ = 1 and ⟨f, x ⟩ = 2 . We can then conclude that
f − g ∈ S⊥, since we have
⟨f − g, 1⟩= ⟨f, 1⟩ − ⟨g, 1⟩= 1 − 1 = 0
⟨f − g, x ⟩= ⟨f, x ⟩ − ⟨g, x ⟩= 2 − 2 = 0 .
6.2 Part b
Note that this equivalent to finding an f0 ∈ C such that ‖f0‖ is minimized.
Letting f0 ∈ C , be arbitrary and noting that by part (a) we have f0 = g + s where s ∈ S⊥, we can
compute
‖f0‖2 = ⟨f0, f 0⟩
= ⟨g + s, g + s⟩
= ‖g‖2 + 2ℜ⟨g, s ⟩+ ‖s‖2,
which can be minimized by taking s = 0 , which forces ‖s‖2 = 0 and ⟨g, s ⟩= 0 . But this imposes
the condition f0 = g + 0 = g.
11

Problem Set 8
D. Zack Garza
November 28, 2019
Contents
1 Problem 1 1
1.1 Part a . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Part b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 Part c . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2 Problem 2 3
2.1 Part a . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.1.1 Part i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.1.2 Part ii . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2 Part b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3 Problem 3 5
4 Problem 4 7
4.1 Part a . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.2 Part b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
5 Problem 5 8
5.1 Part a . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
5.2 Part b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
6 Problem 6 10
1 Problem 1
1.1 Part a
It follows from the definition that ‖f ‖∞ = 0 ⇐ ⇒ f = 0 almost everywhere, and if ‖f ‖∞ is the
best upper bound for f almost everywhere, then ‖cf ‖∞ is the best upper bound for cf almost
everywhere.
So it remains to show the triangle inequality. Suppose that |f (x)| ≤ ‖f ‖∞ a.e. and |g(x)| ≤ ‖g‖∞
a.e., then by the triangle inequality for the |·|R we have
1

|(f + g)(x)| ≤ |f (x)|+ |g(x)| a.e.
≤ ‖f ‖∞ + ‖g‖∞ a.e.,
which means that ‖f + g‖∞ ≤ ‖f ‖∞ + ‖g‖∞ as desired.
1.2 Part b
=⇒ : Suppose ‖fn − f ‖∞ → 0, then for every ε, Nε can be chosen large enough such that
|fn(x) − f (x)|< ε a.e., which precisely means that there exist sets Eε such that x ∈ Eε =⇒
|fn(x) − f (x)|and m(Ec
ε) = 0 .
But then taking the sequence εn := 1
n → 0, we have fn ⇒ f uniformly on E :=⋂
n En by definition,
and Ec =⋃
n Ec
n is still a null set.
⇐ = : Suppose fn ⇒ f uniformly on some set E and m(Ec) = 0 . Then for any ε, we can choose N
large enough such that |fn(x) − f (x)|< ε on E; but then ε is an upper bound for fn − f almost
everywhere, so ‖fn − f ‖∞ < ε → 0.
1.3 Part c
To see that simple functions are dense in L∞ (X), we can use the fact that f ∈ L∞ (X) ⇐ ⇒ there
exists a g such that f = g a.e. and g is bounded.
Then there is a sequence sn of simple functions such that ‖sn − g‖∞ → 0, which follows from a
proof in Folland:
2

However, C0
c (X) is dense L∞ (X) ⇐ ⇒ every f ∈ L∞ (X) can be approximated by a sequence
{gk} ⊂ C0
c (X) in the sense that ‖f − gn‖∞ → 0. To see why this can not be the case, let f (x) = 1 ,
so ‖f ‖∞ = 1 and let gn → f be an arbitrary sequence of C0
c functions converging to f pointwise.
Since every gn has compact support, say supp(gn) := En, then gn|Ecn
≡ 0 and m(Ec
n) > 0. In
particular, this means that ‖f − gn‖∞ = 1 for every n, so gn can not converge to f in the infinity
norm.
2 Problem 2
2.1 Part a
2.1.1 Part i
Lemma: ‖1‖p = m(X)1/p
This follows from ‖1‖p
p =
∫
X |1|p =
∫
X 1 = m(X) and taking pth roots.
By Holder with p = q = 2, we can now write
‖f ‖1 = ‖1 ·f ‖1 ≤ ‖1‖2‖f ‖2 = m(X)1/2‖f ‖2
=⇒ ‖ f ‖1 ≤ m(X)1/2‖f ‖2.
Letting M := ‖f ‖∞ , We also have
‖f ‖2
2 =
∫
X
|f |2 ≤
∫
X
|M |2 = M 2
∫
X
1 = M 2m(X)
=⇒ ‖ f ‖2 ≤ m(X)1/2‖f ‖∞
=⇒ m(X)1/2‖f ‖2 ≤ m(X)‖f ‖∞ ,
and combining these yields
‖f ‖1 ≤ m(X)1/2‖f ‖2 ≤ m(X)‖f ‖∞ ,
3

from which it immediately follows
m(X) < ∞ =⇒ L∞ (X) ⊆ L2(X) ⊆ L1(X).
The Inclusions Are Strict:
1. ∃f ∈ L1(X) \ L2(X):
Let X = [0, 1] and consider f (x) = x− 1
2 . Then
‖f ‖1 =
∫1
0
x− 1
2 < ∞ by the p test,
while
‖f ‖2
2 =
∫1
0
x−1 → ∞ by the p test.
2. ∃f ∈ L2(X) \ L∞ (X):
Take X = [0, 1] and f (x) = x− 1
4 . Then
‖f ‖2
2 =
∫1
0
x− 1
4 < ∞ by the p test,
while ‖f ‖∞ > M for any finite M , since f is unbounded in neighborhoods of 0, so ‖f ‖∞ = ∞ .
2.1.2 Part ii
1. ∃f ∈ L2(X) \ L1(X) when m(X) = ∞ :
Take X = [1, ∞ ) and let f (x) = x−1, then
‖f ‖2
2 =
∫∞
0
x−2 < ∞ by the p test,
‖f ‖1 =
∫∞
0
x−1 → ∞ by the p test.
2. ∃f ∈ L∞ (X) \ L2(X) when m(X) = ∞ :
Take X = R and f (x) = 1 . then
‖f ‖∞ = 1
‖f ‖2
2 =
∫
R
1 → ∞ .
3. L2(X) ⊆ L1(X) = ⇒ m(X) < ∞ :
4

Let f = χX , by assumption we can find a constant M such that ‖χX ‖2 ≤ M ‖χX ‖1.
Then pick a sequence of sets Ek ↗ X such that m(Ek) < ∞ for all k, χEk ↗ χX , and thus
‖χEk ‖p ≤ M ‖χE‖p. By the lemma, ‖χEk ‖p = m(Ek)1/p, so we have
‖χEk ‖2 ≤ M ‖χEk ‖1 =⇒ ‖χEk ‖2
‖χEk ‖1
≤ M
=⇒ m(Ek)1/2
m(Ek) ≤ M
=⇒ m(Ek)−1/2 ≤ M
=⇒ m(Ek) ≤ M 2 < ∞ .
and by continuity of measure, we have limK m(Ek) = m(X) ≤ M 2 < ∞ .
2.2 Part b
1. L1(X)⋂L∞ (X) ⊂ L2(X):
Let f ∈ L1(X)⋂L∞ (X) and M := ‖f ‖∞ , then
‖f ‖2
2 =
∫
X
|f |2 =
∫
X
|f ||f | ≤
∫
X
M |f |= M
∫
|f |:= ‖f ‖∞ ‖f ‖1 < ∞ . (1)
The inclusion is strict, since we know from above that there is a function in L2(X) that is not in
L∞ (X).
Note that taking square roots in (1) immediately yields
‖f ‖L2(X) ≤ ‖f ‖1/2
L1(X)‖f ‖1/2
L∞ (X).
2. L2(X) ⊂ L1(X) + L∞ (X):
Let f ∈ L2(X), then write S = {x ϶ |f (x)| ≥1} and f = χSf + χScf := g + h.
Since x ≥ 1 = ⇒ x2 ≥ x, we have
‖g‖2
1 =
∫
X
|g|=
∫
S
|f | ≤
∫
S
|f |2 ≤
∫
X
|f |2 = ‖f ‖2
2 < ∞ ,
and so g ∈ L1(X).
To see that h ∈ L∞ (X), we just note that h is bounded by 1 by construction, and so ‖h‖∞ ≤ 1 < ∞ .
3 Problem 3
For notational convenience, it suﬀices to prove this for ℓp(N), where we re-index each sequence in
ℓp(Z) using a bijection Z → N.
Note: this technically reorders all sums appearing, but since we are assuming absolute conver-
gence everywhere, this can be done. One can also just replace ∑m
j=n |aj|p with∑
n≤|j|≤m |aj|p
in what follows.
5

1. ℓ1(N) ⊂ ℓ2(N):
Suppose∑
j |a|j < ∞ , then its tails go to zero, so choose N large enough so that
j ≥ N =⇒ | aj|< 1.
But then
j ≥ N =⇒ | aj|2 < |aj|,
and
∑
j
|aj|2 =
N∑
j=1
|aj|2 +
∞∑
j=N +1
|aj|2
≤
N∑
j=1
|aj|2 +
∞∑
j=N +1
|aj|
≤ M +
∞∑
j=N +1
|aj|
≤ M +
∞∑
j=1
|aj|
< ∞ .
where we just note that the first portion of the sum is a finite sum of finite numbers and thus
bounded.
To see that the inclusion is strict, take a :=
{
j−1}∞
j=1; then ‖a‖2 < ∞ by the p-test by ‖a‖1 = ∞
since it yields the harmonic series.
2. ℓ2(N) ⊂ ℓ∞ (N):
This follows from the contrapositive: if a is a sequence with unbounded terms, then ‖a‖2 =∑|aj|2
can not be finite, since convergence would require that |aj|2 → 0 and thus |aj| → 0.
To see that the inclusion is strict, take a = {1}∞
j=1. Then ‖a‖∞ = 1 , but the corresponding sum
does not converge.
3. ‖a‖2 ≤ ‖a‖1:
Let M = ‖a‖1, then
‖a‖2
2 ≤ ‖a‖2
1 ⇐ ⇒ ‖a‖2
2
M 2 ≤ 1 ⇐ ⇒
∑
j
⏐⏐⏐⏐
aj
M
⏐⏐⏐⏐
2
≤ 1.
But then we can use the fact that
⏐⏐⏐⏐
aj
M
⏐⏐⏐⏐≤ 1 = ⇒
⏐⏐⏐⏐
aj
M
⏐⏐⏐⏐
2
≤
⏐⏐⏐⏐
aj
M
⏐⏐⏐⏐
6

to obtain
∑
j
⏐⏐⏐⏐
aj
M
⏐⏐⏐⏐
2
≤
∑
j
⏐⏐⏐⏐
aj
M
⏐⏐⏐⏐= 1
M
∑
j
|aj|:= 1.
4. ‖a‖∞ ≤ ‖a‖2:
This follows from the fact that, we have
‖a‖2
∞ :=
(
sup
j
|aj|
) 2
= sup
j
|aj|2 ≤
∑
j
|aj|2 = ‖a‖2
2
and taking square roots yields the desired inequality.
Note: the middle inequality follows from the fact that the supremum S is the least upper
bound of all of the aj, so for all j, we have aj + ε > S for every ε > 0. But in particular,
ak + aj > a j for any pair aj, ak where ak ⁄= 0, so ak + aj > S and thus so is the entire sum.
4 Problem 4
4.1 Part a
Let {fk} be a Cauchy sequence, then ‖fk − fj‖u → 0. Define a candidate limit by fixing x, then
using the fact that |fj(x) − fk(x)| → 0 as a Cauchy sequence in R, which converges to some f (x).
We want to show that and ‖fn − f ‖u → 0 and f ∈ C([0, 1]).
This is immediate though, since fn → f uniformly by construction, and the uniform limit of
continuous functions is continuous.
4.2 Part b
It suﬀices to produce a Cauchy sequence of continuous functions fk such that ‖fj − fj‖1 → 0 but
if we define f (x) := lim fk(x), we have either ‖f ‖1 = ∞ or f is not continuous.
To this end, take fk(x) = xk for k = 1, 2, · · ·, ∞ .
Then pointwise we have
fk →
{
0 x ∈ [0, 1)
1 x = 1 ,
which has a clear discontinuity, but
‖fk − fj‖1 :=
∫1
0
xk − xj = 1
k + 1 − 1
j + 1 → 0.
7

5 Problem 5
5.1 Part a
⇐ = : It suﬀices to show that the map
H ↠ ℓ2(N)
x ↦→ {⟨x, un⟩}∞
n=1 := {an}∞
n=1
is a surjection, and for every a ∈ ℓ2(N), we can pull back to some x ∈ H such that ‖x‖H = ‖a‖ℓ2(N).
Following the proof in Neil’s notes, let a ∈ ℓ2(N) be given by a = {aj}, and define SN =∑N
n=1 anun.
We then have
‖SN − SM ‖H =
‖‖‖‖‖‖
N∑
n=M +1
anun
‖‖‖‖‖‖
H
=
N∑
n=M +1
‖anun‖H by Pythagoras, since the un are orthogonal
=
N∑
n=M +1
|an|C ‖un‖H
=
N∑
n=M +1
|an|C since the un are orthonormal
→ 0 as N, M → ∞ ,
which goes to zero because it is the tail of a convergent sum in R.
Since H is complete, every Cauchy sequence converges, and in particular SN → x ∈ H for some x.
We now have
|⟨x, un⟩|= |⟨x − SN + SN , un⟩| ∀n, N
= |⟨x − SN , un⟩+ ⟨SN , un⟩| ∀n, N
≤ ‖x − SN ‖H ‖un‖H + |⟨SN , un⟩| ∀n, N by Cauchy-Schwartz
= ‖x − SN ‖H + |⟨SN , un⟩| ∀n, N
= ‖x − SN ‖H + |an| ∀N ≥ n
→ 0 + |an| as N → ∞ ,
where we just note that
⟨SN , un⟩=
⟨N∑
j=1
ajuj, un
⟩
=
N∑
j=1
aj⟨uj, un⟩= an ⇐ ⇒ N ≥ n
8

since ⟨uj, un⟩= δj,n and so the an term is extracted iff un actually appears as a summand.
We thus have
⟨x, un⟩= |an| ∀ n,
and since {un} is a basis, we can apply Parseval’s identity to obtain
‖x‖2
H =
∞∑
n=1
|⟨x, un⟩|:=
∞∑
n=1
|an|.
=⇒ : Given a vector x =∑
n anun, we can immediately note that both ‖x‖H < ∞ and ⟨x, un⟩=
an. Since {un} being a basis is equivalent to Parseval’s identity holding, we immediately obtain
∞∑
n=1
|an|=
∞∑
n=1
|⟨x, un⟩|= ‖x‖2
H < ∞ .
5.2 Part b
In both cases, suppose such a linear functional exists.
1. Using part (a), we know that H is isometrically isomorphic to ℓ2(N), and thus H ∨
f ∼=
(ℓ2(N))∨ ∼=d ℓ2(N).
Note: this follows since ℓp(N)∨ ∼= ℓq(N) where p, q are Holder conjugates.
But then, since L ∈ H ∨, under the isometry f it maps to the functional
Lℓ : ℓ2(Z) → C
a = {an} ↦→
∑
n∈N
ann−1,
which under the identification of dual spaces g identifies Lℓ with the vector b :=
{
n−1}
n∈N.
Most importantly, these are all isometries, so we have the equalities
‖L‖H = ‖Lℓ‖ℓ2(N)∨ = ‖b‖ℓ2(N),
so it suﬀices to compute the ℓ2 norm of the sequence bn = 1
n . To this end, we have
‖b‖2
ℓ2(N) =
∑
n
⏐⏐⏐⏐
1
n
⏐⏐⏐⏐
2
=
∑
n
1
n2
= π2
6 ,
which shows that ‖L‖H = π/
√
6.
9

2. Using the same argument, we obtain b =
{
n−1/2
}
n∈N
, and thus
‖L‖2
H = ‖b‖2
ℓ2(N) =
∑
n
⏐⏐⏐n−1/2
⏐⏐⏐
2
→ ∞ .
which shows that L is unbounded, and thus can not be a continuous linear functional.
6 Problem 6
We can use the fact that Λp ∈ (Lp)∨ ∼= Lq, where this is an isometric isomorphism given by the
map
I : Lq → (Lp)∨
g ↦→(f ↦→
∫
f g).
Under this identification, for any Λ ∈ (Lp)∨, to any Λ ∈ (Lp)∨ we can associate a g ∈ Lq, where we
have
‖Λ‖(Lp)∨ = ‖g‖Lq .
In this case, we can identify Λp = I(g), where g(x) = x2 and we can verify that g ∈ Lq by computing
its norm:
‖g‖q
Lq =
∫1
0
(x2)q dx
= x2q+1
2q + 1
⏐⏐⏐⏐⏐
1
0
= 1
2q + 1
= p − 1
3p − 1 < ∞ ,
where we identify q = p
p−1 , and note that this is finite for all 1 ≤ p ≤ ∞ since it limits to 1
3 .
But then
‖Λp‖(Lp)∨ = ‖g‖Lq =
( p − 1
3p − 1
) 1
q
=
( p − 1
3p − 1
) p−1
p
,
which shows that Λp is bounded and thus a continuous linear functional.
10

