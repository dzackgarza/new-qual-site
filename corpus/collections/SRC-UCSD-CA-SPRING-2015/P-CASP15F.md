---
schema: qual/card@1
id: P-CASP15F
kind: problem
title: "Sum of zeros minus poles of an elliptic function in a fundamental parallelogram"
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Residue Theorem
  - Periodic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/complex-15.pdf, problem 6 (10 pts):
    "Let f(z) be an elliptic function with periods omega_1, omega_2. Assume that f(z) has no zeros
    or poles on the boundary of P, where P := {z = s_1 omega_1 + s_2 omega_2 | 0 < s_1, s_2 < 1} and
    let a_1, ..., a_m denote the zeros and b_1, ..., b_n the poles of f(z) in P (each repeated
    according to multiplicity). State and prove a theorem regarding sum a_j - sum b_k." The card's
    statement is that problem verbatim.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked each pair of opposite sides:
    substituting z = w + omega_2 on the side at s_2 = 1, using that f'/f is elliptic, and taking
    account of the reversed orientation gives -omega_2 times the integral over the side at
    s_2 = 0, and symmetrically +omega_1 times the integral over the side at s_1 = 0; the relative
    sign is now explained rather than asserted. Checked the residue of z f'/f at a zero of
    multiplicity nu, which is nu a, and at a pole of order mu, which is -mu b. Added the reason each
    of the two remaining integrals divided by 2 pi i is an integer: the endpoints of each side
    differ by a period, so the image under f is a closed curve and the integral is its winding
    number. No retained published solution covers this problem.
---

::: {.problem}
Let $f(z)$ be an elliptic function with periods $\omega_1, \omega_2$.
Assume that $f(z)$ has no zeros or poles on $\partial P$, where
$$
P := \{z = s_1 \omega_1 + s_2 \omega_2 \mid 0 < s_1, s_2 < 1\}
$$
and let $a_1, a_2, \ldots, a_m$ denote the zeros and $b_1, b_2, \ldots, b_n$ the poles of $f(z)$ in $P$ (each repeated according to multiplicity).
State and prove a theorem regarding $\sum_{j=1}^m a_j - \sum_{k=1}^n b_k$.
:::

::: {.solution}
This is Problem 6 of the UCSD complex-analysis qualifying exam of Spring 2015 (`assets/attachments/complex-15.pdf`, 10 points). No published solution set is transcribed: the argument is the card's own, and it is the standard argument-principle and residue-theorem proof that the zeros and poles of an elliptic function agree in number and in sum modulo the period lattice.

::: pf

::: {.pf-step #statement}
Let $f$ be elliptic with periods $\omega_{1},\omega_{2}$, with no zeros or poles on $\partial P$, $P=\theset{s_{1}\omega_{1}+s_{2}\omega_{2}\mid0<s_{1},s_{2}<1}$, zeros $a_{1},\dots,a_{m}$ and poles $b_{1},\dots,b_{n}$ in $P$ listed with multiplicity. Then $m=n$ and
$$\sum_{j=1}^{m}a_{j}-\sum_{k=1}^{n}b_{k}\in\Lambda=\ZZ\omega_{1}+\ZZ\omega_{2}.$$

::: pf-proof
This is the theorem the exercise asks to state and prove; it says that the zeros and the poles of an elliptic function are congruent modulo the period lattice, both in number and in sum. The two parts are proved in steps [](#count){.pf-ref} and [](#conclusion){.pf-ref}.
:::
:::

::: {.pf-step #count}
$m=n$.

::: pf-proof
The argument principle applied to $f$ on the boundary of the parallelogram $P$ gives
$$\frac{1}{2\pi i}\int_{\partial P}\frac{f'}{f}\,dz=m-n,$$
since $f$ has no zeros or poles on $\partial P$. The function $f'/f$ is elliptic with the periods $\omega_{1},\omega_{2}$, so its integrals over two opposite sides of $P$, which correspond under translation by one of the periods, cancel; hence the integral over $\partial P$ is $0$ and $m=n$.
:::
:::

::: {.pf-step #residue}
$\sum_{j}a_{j}-\sum_{k}b_{k}=\frac{1}{2\pi i}\int_{\partial P}z\frac{f'(z)}{f(z)}\,dz$.

::: pf-proof
The only singularities of $z f'/f$ inside $P$ are at the zeros and poles of $f$. At a zero $a$ of multiplicity $\nu$ one has $f'/f=\nu/(z-a)+$ holomorphic, so the residue of $z f'/f$ at $a$ is $\nu a$. At a pole $b$ of order $\mu$ one has $f'/f=-\mu/(z-b)+$ holomorphic, so the residue there is $-\mu b$. The residue theorem sums these, and the sum over zeros and poles counted with multiplicity is $\sum_{j}a_{j}-\sum_{k}b_{k}$.
:::
:::

::: {.pf-step #pairone}
The two sides of $\partial P$ parallel to $\omega_{1}$ together contribute $-\omega_{2}\int_{\gamma_{1}}\frac{f'}{f}\,dz$, where $\gamma_{1}$ is the side from $0$ to $\omega_{1}$.

::: pf-proof
Let $\gamma_{1}$ be the side $s_{2}=0$ and $\gamma_{1}+\omega_{2}$ the side $s_{2}=1$, the latter traversed in the direction opposite to $\gamma_{1}$ in the positive traversal of $\partial P$. Substituting $z=w+\omega_{2}$ on the second and using $f'(w+\omega_{2})/f(w+\omega_{2})=f'(w)/f(w)$, the two contributions add to
$$\int_{\gamma_{1}}z\frac{f'}{f}\,dz-\int_{\gamma_{1}}(w+\omega_{2})\frac{f'(w)}{f(w)}\,dw=-\omega_{2}\int_{\gamma_{1}}\frac{f'}{f}\,dz.$$
:::
:::

::: {.pf-step #pairtwo}
The two sides parallel to $\omega_{2}$ together contribute $\omega_{1}\int_{\gamma_{2}}\frac{f'}{f}\,dz$, where $\gamma_{2}$ is the side from $0$ to $\omega_{2}$.

::: pf-proof
The same computation with the roles of $\omega_{1}$ and $\omega_{2}$ interchanged: the side at $s_{1}=1$ is the translate by $\omega_{1}$ of the side $\gamma_{2}$ at $s_{1}=0$, traversed oppositely, so the pair contributes $\omega_{1}\int_{\gamma_{2}}f'/f\,dz$, the sign being opposite to the previous case because of the orientation of the boundary.
:::
:::

::: {.pf-step #conclusion}
$\sum_{j}a_{j}-\sum_{k}b_{k}=N_{1}\omega_{1}+N_{2}\omega_{2}$ with $N_{1},N_{2}\in\ZZ$.

::: pf-proof
By steps [](#residue){.pf-ref}, [](#pairone){.pf-ref} and [](#pairtwo){.pf-ref},
$$\sum_{j}a_{j}-\sum_{k}b_{k}=\frac{1}{2\pi i}\left(\omega_{1}\int_{\gamma_{2}}\frac{f'}{f}\,dz-\omega_{2}\int_{\gamma_{1}}\frac{f'}{f}\,dz\right).$$
Each $\frac{1}{2\pi i}\int_{\gamma_{i}}f'/f\,dz$ is an integer: $f$ is meromorphic, and along $\gamma_{1}$ the values at the two endpoints agree because $\omega_{1}$ is a period, so $f\circ\gamma_{1}$ is a closed curve and the integral computes its winding number about $0$; the same holds for $\gamma_{2}$ with the period $\omega_{2}$. So the difference is $N_{1}\omega_{1}+N_{2}\omega_{2}$ with $N_{1},N_{2}\in\ZZ$.
:::
:::
:::

:::
