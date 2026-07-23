---
schema: qual/card@1
id: P-CWZF3
kind: problem
title: "We want to show that if $(p) \\normal R$ is a prime ideal then $R/(p)$\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
We want to show that if $(p) \normal R$ is a prime ideal then $R/(p)$ is a field, so we'll proceed by letting $x + (p) \in R/(p)$ be arbitrary where $x\not \in (p)$ and producing a multiplicative inverse.

Since $R$ is a principal ideal domain, prime ideals are maximal, so $(p)$ is maximal.
Then $x\in R \setminus (p)$, so define
$$
I \definedas \theset{p + rx \suchthat p\in (p), r\in R} \normal R,
$$

which is an ideal in $R$.

In particular, since $x\not\in (p)$, we have a strict containment $(p) < I$, but since $(p)$ was maximal this forces $I = R$.

Then $1 \in I$, so there exists some $p, r$ such that $p + rx = 1$, i.e. $rx - 1 \in (p)$.

But then

$$
r + (p) \cdot x + (p) = rx + (p) = 1 + (p),
$$

which says that $(x + (p))\inv = r + (p)$ in $R/(p)$.

## Part (b)

Images and kernels of module homomorphisms are always submodules, so define
\[
\begin{align*}
\phi: A \to A \\
x \mapsto px
.\end{align*}
\]

This is a module homomorphism, and
\[
\begin{align*}
\im \phi &\definedas \theset{px \suchthat x \in A} \definedas pA,\\
\ker \phi &\definedas \theset{a\in A \suchthat pA = 0} \definedas A[p]
.\end{align*}
\]

## Part (c)

Since $R/(p)$ is a field, we just need to show that $A/pA \actson R/(p)$ defines a module.

$r\cdot(x + y) = rx + ry$:
\[
\begin{align*}
r + (p) \actson x + pA \oplus y + pA &\definedas r + (p) \actson x + y + pA \\
&\definedas r(x+y) + pA \\
&= rx + ry + pA \\
&\definedas rx + pA \oplus ry + pA \\
&\definedas r\actson x + pA \oplus r \actson y + pA
.\end{align*}
\]

$(r + s)\cdot x = rx + sx$:
\[
\begin{align*}
r + (p) \oplus s + (p) \actson x + pA &\definedas
r + s + (p) \actson x + pA \\
&\definedas (r+s)x + pA \\
&= rx + sx + pA \\
&\definedas rx + pA \oplus sx + pA \\
&\definedas r+(p) \actson x + pA \oplus s+(p) \actson x + pA
.\end{align*}
\]

$rs\cdot x = r\cdot (s\cdot x)$:
\[
\begin{align*}
r+ (p) \cdot s + (p) \actson  x + pA &\definedas rs + (p) \actson x + pA \\
&= rsx + pA \\
&\definedas r + (p) \actson sx + pA \\
&\definedas r + (p) \actson s + (p) \actson x + pA
.\end{align*}
\]

$1\cdot x = x$:
\[
\begin{align*}
1_R + (p) \actson x + pA &= 1_R x + pA = x + pA
.\end{align*}
\]

## Part (d)
Similarly, since $R/(p)$ is a field, it suffices to show that $R/(p)\actson A[p]$ defines a module.

$r\cdot(x + y) = rx + ry$:
\[
\begin{align*}
r + (p) \actson (a + a') &\definedas r(a + a') \\
&= ra + ra' \\
&= r\actson a + r\actson a'
.\end{align*}
\]
$(r + s)\cdot x = rx + sx$:
\[
\begin{align*}
r + s + (p) \actson a &= (r+s)a \\
&= ra + sa \\
&= r\actson a + s\actson a
.\end{align*}
\]

$rs\cdot x = r\cdot (s\cdot x)$:
\[
\begin{align*}
rs + (p) \actson a &= rsa \\
&= r \actson sa \\
&= r \actson s \actson a
.\end{align*}
\]
$1\cdot x = x$:
\[
\begin{align*}
1_R + (p) \actson a &= 1a = a
.\end{align*}
\]

