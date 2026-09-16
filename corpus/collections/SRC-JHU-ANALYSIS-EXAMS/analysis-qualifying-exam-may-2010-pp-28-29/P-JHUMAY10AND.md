---
schema: qual/card@1
id: P-JHUMAY10AND
kind: problem
title: "Harmonic conjugate on the exterior of the unit disk up to a logarithmic term"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the exterior-disk domain and the real logarithmic correction with May 2010 problem 4 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved reality of the Laurent residue from the exact real differential dh, canceled that residue with a real logarithmic correction, and justified convergence of the termwise Laurent primitive on compact annuli."
---

::: {.problem}
4. Let h be a harmonic function on the domain

$$
U : = \left\{ z \in \mathbb { C } : | z | > 1 \right\} .
$$

Show that there exists a constant $c \in \mathbb { R }$ and a holomorphic function $f$ on $U$ such that $\mathrm { R e } f ( z ) = h ( z ) + c \log | z |$ for all $z \in U$
:::

::: solution
<1>1. The holomorphic gradient of $h$ has a real residue on the exterior annulus.

::: proof
Write $z=x+iy$ and put $q(z)=h_x(z)-ih_y(z)$. The
Cauchy–Riemann equations for $q$ are precisely
$h_{xx}=-h_{yy}$ and $h_{xy}=h_{yx}$, so harmonicity
makes $q$ holomorphic on $U$. Its Laurent expansion is
$$
q(z)=\sum_{n\in\mathbb Z}a_nz^n\qquad(1<|z|<\infty)
$$
[@SS03]. For any $r>1$, its residue coefficient is
$$
a_{-1}=\frac1{2\pi i}\int_{|z|=r}q(z)\,dz.
$$
Along a curve one has
$$
q(z)\,dz=(h_x\,dx+h_y\,dy)
+i(h_x\,dy-h_y\,dx).
$$
The real part is $dh$, whose integral over the closed
circle is zero. Thus the integral is purely imaginary,
and $a_{-1}$ is real. Denote this real number by $a$.
:::

<1>2. Subtracting $a/z$ gives a holomorphic gradient with a single-valued primitive.

::: proof
Set $c=-a$. The function $q+c/z=q-a/z$ has no
$z^{-1}$ term. Define
$$
F(z)=\sum_{\substack{n\in\mathbb Z\\n\ne-1}}
\frac{a_n}{n+1}z^{n+1}.
$$
To justify this definition, fix $1<r\leq|z|\leq R<\infty$
and choose $1<s<r\leq R<T$. If $M_t=\max_{|z|=t}|q(z)|$,
the Laurent coefficient formula gives
$|a_n|\leq M_T T^{-n}$ for $n\geq0$, and
$|a_{-k}|\leq M_s s^k$ for $k\geq1$ [@SS03].
The positive-power part of the proposed primitive is
therefore bounded termwise by $M_T R(R/T)^n$.
For $k\geq2$, its negative-power terms have modulus at most
$M_s r(s/r)^k$. Both are summable geometric bounds,
uniform on the chosen compact annulus. The same coefficient
bounds give uniform convergence of the differentiated
series there. Termwise differentiation is consequently
valid, and $F$ is holomorphic with
$$
F'(z)=q(z)-a/z.
$$
The integer powers make $F$ single-valued on all of $U$;
no logarithm branch is assumed.
:::

<1>3. An additive real constant makes the real part equal to the required function.

::: proof
Put $H(z)=h(z)+c\log|z|$. On $U$,
$$
(\log|z|)_x-i(\log|z|)_y
=\frac{x-iy}{x^2+y^2}=\frac1z.
$$
Hence $H_x-iH_y=q+c/z=F'$. For holomorphic $F$,
this means that $\operatorname{Re}F$ and $H$ have the
same real gradient. Their difference is locally constant,
and $U$ is connected, so it equals one real constant $d$.
Then $f=F-d$ is holomorphic on $U$ and satisfies
$$
\operatorname{Re}f=h+c\log|z|,
\qquad
c=-\frac1{2\pi i}\int_{|z|=r}(h_x-ih_y)\,dz\in\mathbb R.
$$
This is the asserted representation.
:::
:::
