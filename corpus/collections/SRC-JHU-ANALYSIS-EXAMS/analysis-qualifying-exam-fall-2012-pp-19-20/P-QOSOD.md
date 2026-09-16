---
schema: qual/card@1
id: P-QOSOD
kind: problem
title: "Maximal derivative of a disk self-map at an interior point"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Disc Automorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the evaluation point, prescribed value and request for every extremizer with Fall 2012 problem 3 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the normalization derivatives, the numerical maximum, both directions of the equality case and the nonvanishing denominator of every displayed extremizer."
---

::: {.problem}
Let $D=\{z\in\mathbb C:|z|<1\}$. What is the maximum
possible value of $|f'(1/2)|$ for a holomorphic function
$f:D\to D$ satisfying $f(1/2)=3/4$? Find all such
functions that attain this maximum.
:::

::: {.solution}
The maximum is $\boxed{7/12}$. Every extremizer, and no
other function, has the form
$$
\boxed{f_\lambda(z)=
\frac{\frac34+\lambda\frac{z-1/2}{1-z/2}}
{1+\frac34\lambda\frac{z-1/2}{1-z/2}},
\qquad |\lambda|=1.}
$$

<1>1. Disk automorphisms reduce the derivative estimate to the origin.

::: {.proof}
For $c\in D$, set
$$
\phi_c(z)=\frac{z-c}{1-\overline c z},
\qquad \phi_c^{-1}(w)=\frac{w+c}{1+\overline c w}.
$$
Their denominators are nonzero on $D$, substitution shows
they are inverses, and
$$
1-|\phi_c(z)|^2=
\frac{(1-|c|^2)(1-|z|^2)}{|1-\overline c z|^2}>0.
$$
The inverse is $\phi_{-c}$, so it also maps $D$ into itself.
Thus these are disk automorphisms.

Put $a=1/2$, $b=3/4$, and
$G=\phi_b\circ f\circ\phi_a^{-1}$. Then $G:D\to D$
is holomorphic with $G(0)=0$. Direct differentiation gives
$$
\phi_b'(b)=\frac1{1-b^2},\qquad
(\phi_a^{-1})'(0)=1-a^2,
$$
and hence
$$
G'(0)=\frac{1-a^2}{1-b^2}f'(a)=\frac{12}{7}f'(1/2).
$$
Schwarz's lemma gives $|G'(0)|\leq1$ [@SS03]. Therefore
$|f'(1/2)|\leq7/12$.
:::

<1>2. Equality holds exactly for the displayed functions.

::: {.proof}
Schwarz's lemma also gives $|G(w)|\leq|w|$. Thus
$H(w)=G(w)/w$ extends holomorphically across zero, with
$H(0)=G'(0)$, and satisfies $|H|\leq1$ on $D$.
If $|f'(1/2)|=7/12$, then $|H(0)|=1$. The maximum
modulus principle forces $H\equiv\lambda$ for some
$|\lambda|=1$ [@SS03]. Thus $G(w)=\lambda w$, and
undoing the two automorphisms gives exactly
$f=\phi_b^{-1}\circ(\lambda\phi_a)$, the stated formula.

Conversely, for every $|\lambda|=1$ this composition is
a holomorphic disk automorphism, sends $a$ to $b$, and
has $G'(0)=\lambda$. The derivative calculation in
step <1>1 therefore gives $|f_\lambda'(1/2)|=7/12$.
The explicit denominator cannot vanish since
$|\frac34\lambda\phi_a(z)|<3/4$ on $D$.
This proves attainment and exhausts all equality cases.
:::
:::
