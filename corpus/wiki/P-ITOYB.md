---
schema: qual/card@1
id: P-ITOYB
kind: problem
title: "Similarly, since $R/(p)$ is a field, it suffices to show that $R/(p)\\actson A[p]$\u2026"
classification:
  areas:
  - algebra
  topics:
  - modules
  - torsion
  - fields
relations: []
review: draft
---

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
