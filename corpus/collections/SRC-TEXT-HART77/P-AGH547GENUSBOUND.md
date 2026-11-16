---
schema: qual/card@1
id: P-AGH547GENUSBOUND
kind: problem
title: Maximal arithmetic genus of a divisor of given degree on a cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Adjunction
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.7, the retained Egbert calculation, the cubic-surface
    blowup/anticanonical description, V.1.9 Hodge index, and the ample-line-
    bundle/Bertini inputs. The retained source passes to a standard-form
    coordinate calculation; the sharp bound is more directly obtained from
    H=-K_S, H^2=3, Hodge index D^2<=d^2/3, and the parity
    D^2 congruent d mod 2 forced by adjunction. The maximizing numerical
    classes are mH for d=3m, mH+L for d=3m+1, and mH+Q for d=3m+2,
    where L is a line and Q=H-L is a smooth residual conic. Their required
    linear systems are shown below to contain smooth irreducible members
    without using the later V.4.8 classification.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete Hodge/parity bound and all three sharpness families.
    Tightened the conic construction to use a base-point-free residual
    subpencil rather than claiming completeness, and used the standard
    Bertini irreducibility theorem for the base-point-free birational system
    |H+L|. Verified the low-degree cases d=1,2,3 separately within the same
    line/conic/hyperplane construction.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published-solution pass for issue #121. Read the printed exercise in
    Hartshorne, Algebraic Geometry (1977), V.4.7, printed p. 407 (text
    version tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed
    p. N is PDF p. N+15), with Proposition 4.8, printed pp. 401-402, and
    Corollary 4.13, printed p. 406. Read at the cited place: National Taiwan
    University Algebraic Geometry II (2020 Spring), Chapter V §4 Exercise 7
    by Yi-Tsung Wang, printed pp. 16-17, text version
    tmp/sources/ntu-ag2-chapter5.md, and the same two pages of the PDF,
    where the extracted text loses the signs of two displays. Checked: the
    equivalence the source asserts between its two displayed inequalities
    (substituting 3a = d + sum b_i), which holds with the correct adjunction
    formula 2p_a(D)-2 = a^2-sum b_i^2-d and fails by 2 with the formula as
    printed; its two inequalities, which are (1/2)(sum b_i-2d)^2 >= 0 and
    Cauchy-Schwarz 6 sum b_i^2 >= (sum b_i)^2; and the degree, self-
    intersection and arithmetic genus of every class it lists. Defect found
    in the source: in the d = 2 mod 3 family the multiplicities are
    interchanged, so the printed vector has degree d+2 and not d, while the
    vector with (d+1)/3 on e_1,...,e_4 and (d-2)/3 on e_5,e_6 has degree d
    and the genus the source reports; the card displays the latter and says
    so. Also found: the source asserts attainment by an irreducible
    nonsingular curve without argument, and records d = 4 as unknown. Not
    checked: no source outside this one was read for this card.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the published argument transcribed, each step naming
    its source with its printed page; the card's earlier Hodge-index and
    Bertini construction, which was not a transcription, is replaced by it.
    Steps intersection-data, reduction-to-self-intersection,
    hodge-inequality, genus-bound, extremal-classes and small-degrees are the
    source's pages 16-17; step nonsingular-members supplies the step from a
    class to a curve in it from the book's Corollary 4.13(a),(b), printed
    p. 406, which the source does not supply, and names d = 4 as the case
    where it fails.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the card beside the source. Recomputed, for each family, the
    degree 3a-sum b_i, the self-intersection a^2-sum b_i^2 and
    p_a = (D^2-d)/2+1, and checked the equality with the bound in the
    residue class of each; checked the bound's integrality step in the
    residues 1 and 2 modulo 3; checked the hypotheses of (4.13)(a) for each
    of the classes used, which hold for d > 4 in the second family, d > 2 in
    the third and all d > 0 in the first, and separately at d = 5; checked
    that the d = 4 class of the second family has D.F_56 = 0, so that
    (4.13) does not apply to it. Not reviewed and not supplied: no proof
    that the maximum at d = 4 is achieved, and none was added; the
    2026-11-16 COMPLAINTS record names that case.
---

::: {.problem}
If $D$ is any divisor of degree $d$ on the cubic surface (4.7.3), show that
$$
p_a(D) \leqslant \begin{cases}\frac{1}{6}(d-1)(d-2) & \text{if } d \equiv 1,2\, (\bmod 3) \\ \frac{1}{6}(d-1)(d-2)+\frac{2}{3} & \text{if } d \equiv 0\, (\bmod 3)\end{cases}
$$
Show furthermore that for every $d>0$, this maximum is achieved by some irreducible nonsingular curve.
:::

::: {.solution}

The bound and the classes attaining it are transcribed from the National Taiwan University
*Algebraic Geometry II*, 2020 Spring, Chapter V §4, Exercise 7, by Yi-Tsung Wang, printed
pp. 16--17 (text version `tmp/sources/ntu-ag2-chapter5.md`), and the step from a class to a curve in
it is the book's Corollary 4.13(b), printed p. 406. The intersection-theoretic data of a class
$a\ell-\sum_ib_ie_i$ is the book's Proposition 4.8, printed p. 401.

::: pf

::: {.pf-step #intersection-data}
For a divisor class
$$
D\sim a\ell-\sum_{i=1}^6b_ie_i
$$
on the cubic surface $X$,
$$
d=\deg D=3a-\sum_ib_i,
\qquad
D^2=a^2-\sum_ib_i^2,
\qquad
D\cdot K_X=-d,
\qquad
p_a(D)=\tfrac12(D^2-d)+1 .
$$

::: pf-proof
These are items (c), (d), (e), (f) and (g) of Proposition 4.8 of the book, printed p. 401: the
degree is $D\cdot h=d$, the self-intersection is $a^2-\sum_ib_i^2$ because $\ell^2=1$ and
$e_i^2=-1$ with all other pairings zero, $D\cdot K_X=-D\cdot h=-d$, and (g) is
$2p_a(D)-2=D\cdot(D+K_X)$, that is, $p_a(D)=\frac12(a^2-\sum_ib_i^2-d)+1$. The source states the
first three and then writes "$2p_a(D)=D^2+D\cdot K=a^2-\sum b_i^2-\deg D$", which drops the
$-2$ of the adjunction formula; the inequality it goes on to prove is the one obtained from the
correct $2p_a(D)-2=a^2-\sum_ib_i^2-d$.
:::

:::

::: {.pf-step #reduction-to-self-intersection}
The genus bound of the exercise is equivalent to
$$
a^2-\sum_i b_i^2\le\frac{d^2}{3}.
$$

::: pf-proof
By step [](#intersection-data){.pf-ref},
$$
p_a(D)\le\tfrac16(d-1)(d-2)+\tfrac23
\iff
2p_a(D)-2\le\tfrac{d^2-3d}{3}
\iff
a^2-\sum_ib_i^2\le\tfrac{d^2}{3},
$$
using $a^2-\sum b_i^2-d=2p_a(D)-2$ and $(d-1)(d-2)=d^2-3d+2$. This is the source's reduction:
it says that to prove $p_a(D)\le\frac16(d-1)(d-2)+\frac23$ it suffices to prove
$(d+\sum b_i)^2-9\sum b_i^2-9d\le 3d^2-9d$, which is $a^2-\sum b_i^2\le d^2/3$ after
substituting $3a=d+\sum b_i$.
:::

:::

::: {.pf-step #hodge-inequality}
$$
2d\sum_ib_i+\Bigl(\sum_ib_i\Bigr)^2-9\sum_ib_i^2\le 2d^2 .
$$

::: pf-proof
The source's two inequalities, both for arbitrary reals:
$$
2d^2\ge 2d\sum_ib_i-\tfrac12\Bigl(\sum_ib_i\Bigr)^2,
$$
which is $\frac12\bigl(\sum b_i-2d\bigr)^2\ge0$, and
$$
2d\sum_ib_i-\tfrac12\Bigl(\sum_ib_i\Bigr)^2
\ge
2d\sum_ib_i+\Bigl(\sum_ib_i\Bigr)^2-9\sum_ib_i^2,
$$
which is $9\sum b_i^2-\frac32(\sum b_i)^2\ge0$, that is
$6\sum_ib_i^2\ge(\sum_ib_i)^2$, Cauchy--Schwarz for six numbers, the inequality the source cites.
Combining the two gives the displayed inequality.
:::

:::

::: {.pf-step #genus-bound}
For every divisor $D$ of degree $d$ on the cubic surface,
$$
p_a(D)\le
\begin{cases}
\tfrac16(d-1)(d-2)+\tfrac23, & d\equiv0\pmod3,\\
\tfrac16(d-1)(d-2), & d\equiv1,2\pmod3 .
\end{cases}
$$

::: pf-proof
Steps [](#reduction-to-self-intersection){.pf-ref} and [](#hodge-inequality){.pf-ref} give
$a^2-\sum b_i^2\le d^2/3$, hence
$p_a(D)\le\frac16(d^2-3d+6)=\frac16(d-1)(d-2)+\frac23$. If $d\equiv1$ or $2$ modulo $3$, then
$(d-1)(d-2)$ is divisible by $3$ and by $2$, so $\frac16(d-1)(d-2)$ is an integer, and since
$p_a(D)$ is an integer the bound sharpens to $p_a(D)\le\frac16(d-1)(d-2)$. This is the source's
argument in the two residues, and it proves the first display of the exercise.
:::

:::

::: {.pf-step #extremal-classes}
For each of the following classes the degree is $d$ and $p_a$ equals the bound of step
[](#genus-bound){.pf-ref}:
$$
d\equiv0:\quad D=d\ell-\tfrac d3\sum_{i=1}^6e_i ,
$$
$$
d\equiv1,\ d>4:\quad
D=d\ell-\tfrac{d-1}{3}(e_1+e_2+e_3+e_4)-\tfrac{d+2}{3}(e_5+e_6),
$$
$$
d\equiv2,\ d>5:\quad
D=d\ell-\tfrac{d+1}{3}(e_1+e_2+e_3+e_4)-\tfrac{d-2}{3}(e_5+e_6),
$$
$$
d=5:\quad D=4\ell-2e_1-e_2-e_3-e_4-e_5-e_6 .
$$

::: pf-proof
In each case $a=d$ and $\sum_ib_i=2d$, so $d=\deg D$ by step [](#intersection-data){.pf-ref}.
For the first, $\sum_ib_i^2=6(d/3)^2=2d^2/3$, so
$D^2=d^2-2d^2/3=d^2/3$ and $p_a(D)=\frac12(d^2/3-d)+1=\frac16(d-1)(d-2)+\frac23$, equality in
step [](#genus-bound){.pf-ref}. For the second, with $k=\frac{d-1}{3}$,
$\sum_ib_i^2=4k^2+2(k+1)^2=6k^2+4k+2$ and $d=3k+1$, so
$D^2=d^2-6k^2-4k-2=\frac{d^2-4}{3}$ and
$p_a(D)=\frac12\left(\frac{d^2-4}{3}-d\right)+1=\frac16(d-1)(d-2)$. For the third the same
computation with $k=\frac{d-2}{3}$ and $d=3k+2$ gives $D^2=\frac{d^2-4}{3}$ and
$p_a(D)=\frac16(d-1)(d-2)$. For $d=5$ the class has
$\sum_ib_i^2=4+5=9$ and $D^2=16-9=7$, so $p_a(D)=\frac12(7-5)+1=2=\frac16\cdot4\cdot3$.

The source prints the third family with the multiplicities the other way round,
$\frac{d-2}{3}$ on $e_1,\ldots,e_4$ and $\frac{d+1}{3}$ on $e_5,e_6$; for that vector
$\sum_ib_i=2d-2$ and the degree is $3d-(2d-2)=d+2$, with $d=3m+2$, so its stated "$\deg D=d$"
fails there. The vector displayed above is the one for which the degree and the value of $p_a$ the
source reports both hold.
:::

:::

::: {.pf-step #small-degrees}
For $d=1$ and $d=2$ the bound is attained by a line and by a conic; for $d=4$ the second family of
step [](#extremal-classes){.pf-ref} gives a class of degree $4$ with $p_a=1$.

::: pf-proof
A line has $d=1$, $D^2=-1$ and $p_a=0=\frac16\cdot0\cdot(-1)$; a conic has $d=2$, $D^2=0$ and
$p_a=0=\frac16\cdot1\cdot0$; both are nonsingular irreducible curves, and these are the source's
"for $d=1$ and $2$, a line and a conic achieve the maximum, respectively". At $d=4$ the second
family of step [](#extremal-classes){.pf-ref} reads $D=4\ell-(e_1+e_2+e_3+e_4)-2(e_5+e_6)$, of
degree $4$ and $p_a=1$, the maximum of step [](#genus-bound){.pf-ref} for $d\equiv1\pmod3$. The
source excludes $d=4$ from that family, writes "For $d=4$, I don't know", and states its conclusion
as holding for every $d>0$ "possibly except $d=4$".
:::

:::

::: {.pf-step #nonsingular-members}
For every $d>0$ with $d\ne4$, the class of step [](#extremal-classes){.pf-ref} of degree $d$
contains an irreducible nonsingular curve; hence the maximum of the exercise is attained for those
$d$.

::: pf-proof
Apply (4.13)(a) of the book, printed p. 406: $D$ is ample exactly when $b_i>0$ for each $i$,
$a>b_i+b_j$ for each $i,j$, and $2a>\sum_{i\ne j}b_i$ for each $j$. For the classes of step
[](#extremal-classes){.pf-ref} one has $a=d$ and $\sum_ib_i=2d$, so the last condition reads
$2d>2d-b_j$, which holds; the middle one reads $d>b_i+b_j$, and for the largest pairs it is
$d>\frac{2(d+2)}{3}$, that is $d>4$, in the second family, $d>\frac{2(d+1)}{3}$, that is $d>2$, in
the third, and $d>\frac{2d}{3}$, that is $d>0$, in the first; and $b_i>0$ holds because
$d>0$ in the first family, $d>1$ in the second and $d>2$ in the third. The exceptions $d=1,2$ are
the line and the conic of step [](#small-degrees){.pf-ref}, and $d=5$ is the fourth class of step
[](#extremal-classes){.pf-ref}, for which $b_1=2$ and the remaining $b_i$ equal $1$, so
$a=4>b_i+b_j$ holds, since the largest pair sum is $3$, and
$2a=8>6=\sum_ib_i-1\ge\sum_{i\ne j}b_i$. By Corollary 4.13(b) of the book,
printed p. 406, every divisor class satisfying those conditions contains an irreducible nonsingular
curve. Hence the maximum is attained for each of those $d$. At $d=4$ the class of step
[](#small-degrees){.pf-ref} has $D\cdot F_{56}=4-2-2=0$ for the line $F_{56}$, so it is not ample
and (4.13) does not apply to it.
:::

:::

::: {.pf-step #conclusion}
The bound of the exercise holds for every divisor of degree $d$, and the maximum is achieved by an
irreducible nonsingular curve for every $d>0$ with $d\ne4$; the case $d=4$ is not covered by the
sources.

::: pf-proof
The bound is step [](#genus-bound){.pf-ref}. The attainment is step [](#nonsingular-members){.pf-ref}
for $d\ne4$, and step [](#small-degrees){.pf-ref} records what the source says of $d=4$, namely that
it does not know. No argument for $d=4$ is given on this card.
:::

:::

::: pf-qed
Steps [](#intersection-data){.pf-ref}, [](#reduction-to-self-intersection){.pf-ref},
[](#hodge-inequality){.pf-ref} and [](#genus-bound){.pf-ref} prove the bound;
steps [](#extremal-classes){.pf-ref}, [](#small-degrees){.pf-ref} and
[](#nonsingular-members){.pf-ref} prove the attainment of the bound, except at $d=4$.
:::

:::
:::

::: {.remark title="Published solution"}
National Taiwan University, *Algebraic Geometry II* (2020 Spring, Chin-Lung Wang), Chapter V §4,
Exercise 7, by Yi-Tsung Wang, printed pp. 16--17, text version
`tmp/sources/ntu-ag2-chapter5.md`. The source computes $2p_a(D)$ from $D^2+D\cdot K$, remarks that
the inequality is Cauchy--Schwarz, and sharpens the bound in the residues $1,2$ modulo $3$ by
integrality, which is steps [](#intersection-data){.pf-ref}--[](#genus-bound){.pf-ref}; it then
lists the extremal classes of step [](#extremal-classes){.pf-ref} and the small cases of step
[](#small-degrees){.pf-ref}. Three points of the printed text are not reproduced: it writes
$2p_a(D)=D^2+D\cdot K$ for $2p_a(D)-2=D\cdot(D+K)$; the multiplicities in its $d\equiv2$ family are
interchanged, so that family as printed has degree $d+2$; and it asserts that each listed class is
achieved by an irreducible nonsingular curve without giving a curve or a reference, admits
$d=4$ as unknown ("For $d=4$, I don't know"), and states only that the maximum is achieved for
every $d>0$ possibly except $d=4$. Step [](#nonsingular-members){.pf-ref} supplies the missing
argument from the book's Corollary 4.13(b), printed p. 406, and fails exactly at $d=4$, where the
maximising class has $D\cdot L=0$ for one of the 27 lines and so is not ample.
:::
