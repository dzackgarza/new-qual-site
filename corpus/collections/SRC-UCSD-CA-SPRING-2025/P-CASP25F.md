---
schema: qual/card@1
id: P-CASP25F
kind: problem
title: "Three-circles type theorem for holomorphic functions vanishing only at 0"
classification:
  areas:
  - complex-analysis
  topics:
  - Hadamard Three-Circles Theorem
  - Harmonic Functions
  - Maximum Principle
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f : \DD \to \CC$ be holomorphic and assume $f(z) \neq 0$ for $z \neq 0$.
For $0 \leq r < 1$, let $M(r) = \max_{\abs{z}=r} \abs{f(z)}$.

(i) Show that the function $h_s(z) = s \log \abs{z} + \log \abs{f(z)}$ is harmonic in $\DD \setminus \{0\}$ for all $s \in \RR$.

(ii) Show that there exists $s \in \RR$ such that $\max_{\abs{z}=\frac{1}{2}} h_s(z) = \max_{\abs{z}=\frac{1}{8}} h_s(z)$.

(iii) Show that $M\!\left(\frac{1}{4}\right)^2 \leq M\!\left(\frac{1}{2}\right) M\!\left(\frac{1}{8}\right)$.

(iv) Show that equality holds if and only if $f(z) = az^n$ for some $a \in \CC$ and some integer $n \geq 0$.
:::

::: {.solution}
(i) On $\DD\setminus\{0\}$ the function $f$ has no zeros, so
$\log\abs{f}$ is harmonic there. Since $\log\abs{z}$ is also harmonic on the punctured
disk,
$$
h_s(z)=s\log\abs{z}+\log\abs{f(z)}
$$
is harmonic for every real $s$.

(ii) On the circle $\abs{z}=r$,
$$
\max h_s=s\log r+\log M(r).
$$
Thus we need
$$
s\log\frac12+\log M(1/2)
=s\log\frac18+\log M(1/8).
$$
Since $\log(1/2)\ne\log(1/8)$, this determines a real $s$ uniquely.

(iii) Fix this value of $s$. By the maximum principle for the harmonic
function $h_s$ on the annulus $1/8<\abs{z}<1/2$, its maximum on the intermediate
circle $\abs{z}=1/4$ is at most the common maximum on the two boundary circles:
$$
s\log\frac14+\log M(1/4)
\le s\log\frac12+\log M(1/2).
$$
Using
$$
2\log\frac14=\log\frac12+\log\frac18
$$
and the defining equality for $s$, we obtain
$$
2\log M(1/4)
\le \log M(1/2)+\log M(1/8).
$$
Exponentiating gives
$$
\boxed{M(1/4)^2\le M(1/2)M(1/8).}
$$

(iv) If $f(z)=az^n$, then $M(r)=\abs{a}r^n$, so equality is immediate.

Conversely suppose equality holds. Then the inequality in the maximum
principle above is equality at some point on the interior circle $\abs{z}=1/4$.
Hence $h_s$ attains its maximum in the annulus and is therefore constant
there. Let $n$ be the order of the zero of $f$ at $0$ (possibly $n=0$), and
write
$$
f(z)=z^n g(z),
$$
where $g$ is holomorphic and nowhere zero on $\DD$. Then
$$
h_s(z)=(s+n)\log\abs{z}+\log\abs{g(z)}.
$$
Since this is constant on an annulus and $\log\abs{g}$ extends harmonically across
$0$, necessarily $s+n=0$ and $\log\abs{g}$ is constant. A holomorphic function of
constant modulus is constant, so $g\equiv a$. Therefore
$$
f(z)=az^n.
$$
:::
