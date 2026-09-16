---
schema: qual/card@1
id: E-SMI-8000E-FEI
kind: problem
title: Irreducibility and splitting fields of three polynomials
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all three polynomials and all requested splitting-field questions with Smith 8000 Fall 2006 final part I."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Determined the Galois groups C3, S5, and C7 semidirect C6, the splitting-field degrees and real/solvable status, and classified every intermediate field normal over Q via the corresponding normal subgroups."
---

::: {.exercise}
Do all parts.
For each of the following polynomials over $\mathbb{Q}$:

(a) Prove the polynomial is irreducible over $\mathbb{Q}$.

(b) Say as much as you can about the splitting field $E$: the degree over $\mathbb{Q}$, whether or not it is a solvable extension, whether it is contained in $\mathbb{R}$, and compute the Galois group as well as you can.

(c) Say whatever you can about those intermediate fields between $E$ and $\mathbb{Q}$ which are normal over $\mathbb{Q}$.

(i) $X^3 - 3X + 1$

(ii) $X^5 - 20X + 4$

(iii) $X^7 - 2$
:::

::: {.solution}
We treat the three polynomials separately.

## (i) $f(X)=X^3-3X+1$

<1>1. The cubic is irreducible over $\mathbb Q$.
::: {.proof}
By the rational-root theorem, any rational root of the monic polynomial $f$
must be $\pm1$. But
$$
f(1)=-1,
\qquad
f(-1)=3.
$$
Thus $f$ has no rational root. A reducible cubic over a field has a linear
factor, so
$$
\boxed{f\text{ is irreducible over }\mathbb Q.}
$$
:::

<1>2. All three roots are real, and the discriminant is a square.
::: {.proof}
The derivative is
$$
f'(x)=3(x^2-1).
$$
Thus $f$ is increasing on $(-\infty,-1)$, decreasing on $(-1,1)$, and
increasing on $(1,\infty)$. Moreover
$$
f(-1)=3>0,
\qquad
f(1)=-1<0,
$$
while
$$
f(x)\to-\infty\quad(x\to-\infty),
\qquad
f(x)\to\infty\quad(x\to\infty).
$$
Hence there is exactly one root in each of the three monotonicity intervals,
so all three roots are real.

For a depressed cubic $X^3+pX+q$, the discriminant is
$$
-4p^3-27q^2.
$$
Here $p=-3$ and $q=1$, so
$$
\Delta_f=-4(-3)^3-27=108-27=81=9^2.
$$
:::

<1>3. The splitting field has degree $3$ and Galois group $C_3$.
::: {.proof}
Because $f$ is irreducible of degree three, its Galois group is a transitive
subgroup of $S_3$. The discriminant is a square in $\mathbb Q$, so the
Galois group lies in $A_3$. The only transitive subgroup of $A_3$ is $A_3$
itself. Therefore
$$
\boxed{\operatorname{Gal}(E/\mathbb Q)\cong A_3\cong C_3.}
$$
Consequently
$$
\boxed{[E:\mathbb Q]=3.}
$$
In particular the degree-three root field of any root already equals the
splitting field.

Since all roots are real,
$$
\boxed{E\subseteq\mathbb R.}
$$
The group $C_3$ is abelian, hence solvable, so this Galois extension is
solvable and the polynomial is solvable by radicals.
:::

<1>4. There are no nontrivial proper intermediate fields, hence no nontrivial proper normal ones.
::: {.proof}
The Galois group $C_3$ has only the subgroups
$$
1
\quad\text{and}\quad
C_3.
$$
By the Galois correspondence the only intermediate fields are
$$
E
\quad\text{and}\quad
\mathbb Q.
$$
Both are of course normal over $\mathbb Q$.
:::

## (ii) $g(X)=X^5-20X+4$

<1>5. The quintic is irreducible over $\mathbb Q$.
::: {.proof}
Translate the variable by one:
$$
\begin{aligned}
g(X+1)
&=(X+1)^5-20(X+1)+4\\
&=X^5+5X^4+10X^3+10X^2-15X-15.
\end{aligned}
$$
Every nonleading coefficient is divisible by $5$, while the constant term
$-15$ is not divisible by $25$. Eisenstein's criterion at $5$ therefore
shows that $g(X+1)$ is irreducible over $\mathbb Q$. Translation by one is an
automorphism of $\mathbb Q[X]$, so
$$
\boxed{g\text{ is irreducible over }\mathbb Q.}
$$
:::

<1>6. The polynomial has exactly three real roots.
::: {.proof}
We have
$$
g'(x)=5x^4-20=5(x^4-4).
$$
Thus $g'$ is positive for $|x|>\sqrt2$ and negative for
$|x|<\sqrt2$. The two critical values are
$$
g(-\sqrt2)=4+16\sqrt2>0
$$
and
$$
g(\sqrt2)=4-16\sqrt2<0.
$$
Together with the limits at $\pm\infty$, the monotonicity intervals show that
$g$ has exactly one real root in each of
$$
(-\infty,-\sqrt2),
\qquad
(-\sqrt2,\sqrt2),
\qquad
(\sqrt2,\infty).
$$
Hence it has exactly three real roots and one nonreal conjugate pair.
:::

<1>7. The Galois group is $S_5$.
::: {.proof}
Irreducibility makes the Galois group
$$
G\le S_5
$$
transitive on the five roots. Therefore
$$
5\mid |G|,
$$
so Cauchy's theorem gives an element of order $5$, necessarily a $5$-cycle.

Complex conjugation acts on the roots. By step <1>6 it fixes the three real
roots and swaps the two nonreal roots, so its action is a transposition.
Thus $G$ contains both a $5$-cycle and a transposition.

Conjugating the transposition by powers of the $5$-cycle gives
transpositions along the edges of a connected graph on the five roots. Edge
transpositions of a connected graph generate the full symmetric group.
Therefore
$$
\boxed{G=S_5.}
$$
Consequently
$$
\boxed{[E:\mathbb Q]=|S_5|=120.}
$$
:::

<1>8. This splitting field is neither real nor solvable.
::: {.proof}
The splitting field contains the nonreal roots from step <1>6, so
$$
\boxed{E\not\subseteq\mathbb R.}
$$

The group $S_5$ is not solvable because it contains the nonabelian simple
normal subgroup $A_5$. Indeed, the commutator subgroup of the nonabelian
simple group $A_5$ is a nontrivial normal subgroup, hence equals $A_5$
itself, so the derived series of $A_5$ never reaches the identity. Also
$$
S_5/A_5\cong C_2.
$$
Hence
$$
\boxed{E/\mathbb Q\text{ is not a solvable Galois extension},}
$$
and the quintic is not solvable by radicals.
:::

<1>9. The only intermediate fields normal over $\mathbb Q$ are $\mathbb Q$, the quadratic discriminant field, and $E$.
::: {.proof}
The normal subgroups of $S_5$ are
$$
1,
\qquad
A_5,
\qquad
S_5.
$$
Indeed, if $N\trianglelefteq S_5$, then
$N\cap A_5\trianglelefteq A_5$. Simplicity of $A_5$ gives
$N\cap A_5=1$ or $A_5$. In the second case $N=A_5$ or $S_5$; in the first,
$N$ injects into $S_5/A_5\cong C_2$, and a nontrivial normal subgroup of
order two would be central, impossible because $Z(S_5)=1$.

Thus the normal intermediate fields are
$$
E,
\qquad
E^{A_5},
\qquad
\mathbb Q.
$$
The middle field is generated by the square root of the discriminant. A
direct discriminant computation for $X^5+aX+b$ gives
$$
\Delta=5^5b^4+4^4a^5,
$$
so here
$$
\Delta_g
=5^5\cdot4^4+4^4(-20)^5
=-818400000
=-2^8\cdot3\cdot5^5\cdot11\cdot31.
$$
Its square class is $-5115$, hence
$$
\boxed{E^{A_5}=\mathbb Q(\sqrt{-5115}).}
$$
:::

## (iii) $h(X)=X^7-2$

<1>10. The polynomial is irreducible over $\mathbb Q$.
::: {.proof}
All nonleading coefficients of
$$
X^7-2
$$
are divisible by $2$, and its constant term is not divisible by $4$.
Eisenstein's criterion at $2$ gives
$$
\boxed{X^7-2\text{ irreducible over }\mathbb Q.}
$$
:::

<1>11. Describe the splitting field and compute its degree.
::: {.proof}
Let
$$
\alpha=2^{1/7}>0
$$
and let $\zeta=\zeta_7$ be a primitive seventh root of unity. The seven roots
are
$$
\alpha,\zeta\alpha,\ldots,\zeta^6\alpha,
$$
so the splitting field is
$$
E=\mathbb Q(\alpha,\zeta).
$$

Eisenstein gives
$$
[\mathbb Q(\alpha):\mathbb Q]=7,
$$
while cyclotomic theory gives
$$
[\mathbb Q(\zeta):\mathbb Q]=\varphi(7)=6.
$$
The degree of their intersection divides both $7$ and $6$, hence
$$
\mathbb Q(\alpha)\cap\mathbb Q(\zeta)=\mathbb Q.
$$
Therefore
$$
\boxed{[E:\mathbb Q]=7\cdot6=42.}
$$
:::

<1>12. The Galois group is the faithful semidirect product $C_7\rtimes C_6$.
::: {.proof}
Define
$$
\sigma(\alpha)=\zeta\alpha,
\qquad
\sigma(\zeta)=\zeta.
$$
Then $\sigma$ has order $7$.

Since the two subfields in step <1>11 have trivial intersection, the
automorphism of $\mathbb Q(\zeta)$ defined by
$$
\zeta\longmapsto\zeta^3
$$
extends while fixing $\alpha$. Thus there is an automorphism $\tau$ with
$$
\tau(\alpha)=\alpha,
\qquad
\tau(\zeta)=\zeta^3.
$$
Because $3$ has order $6$ modulo $7$, the automorphism $\tau$ has order $6$.
Moreover
$$
\tau\sigma\tau^{-1}=\sigma^3.
$$

The $42$ elements
$$
\sigma^i\tau^j,
\qquad
0\le i<7,
\quad
0\le j<6,
$$
are distinct. Since the splitting field has degree $42$, they exhaust its
Galois group. Hence
$$
\boxed{
\operatorname{Gal}(E/\mathbb Q)
\cong C_7\rtimes C_6,}
$$
where a generator of $C_6$ acts on $C_7$ by multiplication by $3$ modulo
$7$.
:::

<1>13. The extension is solvable but not contained in $\mathbb R$.
::: {.proof}
The normal subgroup
$$
\langle\sigma\rangle\cong C_7
$$
has quotient $C_6$. Both are abelian, so the Galois group is solvable; in
fact its commutator subgroup is contained in $C_7$. Hence
$$
\boxed{E/\mathbb Q\text{ is solvable},}
$$
and $X^7-2$ is solvable by radicals.

On the other hand, $E$ contains the nonreal primitive seventh root of unity
$\zeta$, so
$$
\boxed{E\not\subseteq\mathbb R.}
$$
:::

<1>14. Classify all intermediate fields normal over $\mathbb Q$.
::: {.proof}
Put
$$
N=\langle\sigma\rangle\cong C_7.
$$
Then
$$
G/N\cong C_6.
$$
We first classify the normal subgroups of $G$.

If $K\trianglelefteq G$, then
$$
K\cap N\trianglelefteq N.
$$
Since $|N|=7$ is prime,
$$
K\cap N=1
\quad\text{or}\quad
N.
$$
If $K\cap N=1$, then for $k\in K$ and $n\in N$ the commutator
$[k,n]$ lies in both $K$ and $N$, hence is trivial. Thus $K$ centralizes
$N$. The action of $C_6$ on $N$ is faithful, so
$$
C_G(N)=N.
$$
Therefore $K\le N$, and the trivial intersection forces $K=1$.

If $N\le K$, then $K/N$ is a subgroup of the cyclic group $G/N\cong C_6$.
Conversely, the inverse image of every subgroup of the abelian quotient
$C_6$ is normal. Hence the normal subgroups are precisely
$$
1,
\quad
N,
\quad
N\rtimes C_2,
\quad
N\rtimes C_3,
\quad
G.
$$

Their fixed fields are therefore exactly the intermediate fields normal over
$\mathbb Q$. They may be identified inside the cyclotomic subfield
$$
E^N=\mathbb Q(\zeta_7).
$$
Thus the complete list is
$$
\boxed{
\begin{aligned}
&E,\\
&\mathbb Q(\zeta_7),\\
&\mathbb Q(\zeta_7+\zeta_7^{-1}),\\
&\mathbb Q(\sqrt{-7}),\\
&\mathbb Q.
\end{aligned}}
$$
The degrees over $\mathbb Q$ are respectively
$$
42,\ 6,\ 3,\ 2,\ 1.
$$
The cubic field is the maximal real subfield of $\mathbb Q(\zeta_7)$, fixed
by complex conjugation, and $\mathbb Q(\sqrt{-7})$ is its unique quadratic
subfield.
:::
:::
