---
schema: qual/card@1
id: P-ZJVTY
kind: problem
title: "The claim is that every element in $M \\definedas R^n/\\im A$ is torsio\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

The claim is that every element in $M \definedas R^n/\im A$ is torsion $\iff$ the matrix rank of $A$ is exactly $n \iff$ the Smith normal form of $A$ has exactly $n$ nonzero invariant factors.

To see that this is the case, we can apply the structure theorem for finitely-generated modules over a PID. This gives us
$$
M \cong F \oplus \bigoplus R/(r_i)
$$

where $F$ is free of finite rank, $R/(r_i)$ is cyclic torsion, and $r_i \divides r_{i+1} \divides \cdots$ are the invariant factors of $M$.

We thus have
$$
M \cong R^n/\im A \cong F \oplus \bigoplus R/(r_i),
$$

which will be pure torsion if and only if $F = 0$.

But if we compute the smith normal for of $A$, we obtain
$$
SNF(A) = 
\left[ \begin{array}{rrrrrr}
 d_1 & 0 & \cdots & 0 & \cdots & 0 \\
0 & d_2 & \cdot & 0 & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots & \cdots & 0\\
0 & 0 & \cdots & d_n & \cdots & 0
\end{array}\right]
$$

where $d_1 \divides d_2 \divides \cdots \divides d_n$, and thus
\[
\begin{align*}
\im A \cong \im SNF(A) &\cong d_1 R \oplus d_2 R \oplus \cdots \oplus d_n R \\  \\
\implies M = R^n/\im A &\cong \frac{R^n}{d_1 R \oplus d_2 R \oplus \cdots d_n R} \\ \\
&\cong R/(d_1) \oplus R/(d_2) \cdots \oplus R/(d_n)
\end{align*}
\]

where $R/(d_i)$ is a cyclic torsion module precisely when $d_i \neq 0$.
If instead some $d_i = 0$, we then have $R/(d_i) \cong R$, which is a free $R\dash$module, yielding non-torsion elements in $M$.

But $\det(A) = \det(SNF(A)) = \prod_{i=1}^n d_i$, and so if $d_i=0$ for some $i$ iff $\det A = 0$ iff $\rank A < n$.
