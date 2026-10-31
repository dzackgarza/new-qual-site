---
schema: qual/card@1
id: P-UCTOP290-S11-5
kind: problem
title: Tor and Ext for rational and torsion abelian groups
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: >-
    Read sheet 11, Problem 5 in the extraction and PDF page image.
    The sheet refers to a prior table but does not print it; the
    card makes the standard cyclic-group cases and new rational
    cases explicit.
---

::: {.problem}
Extend the table of values of
$\Tor_1^{\ZZ}(A,B)$ and $\Ext^1_{\ZZ}(A,B)$
to the cases where $A$ and $B$ may be $\QQ$ and $\QQ/\ZZ$.
Give the values for $A,B$ among
$\ZZ$, $\ZZ/n$, $\QQ$, and $\QQ/\ZZ$, with positive integers
$m,n$ used for the cyclic entries.
:::

::: {.solution}

Put $d=\gcd(m,n)$ and
$\widehat{\ZZ}=\varprojlim_k\ZZ/k$.
With rows indexed by $A$ and columns by $B$, the Tor table is
$$
\begin{array}{c c c c c}
\Tor_1^{\ZZ}(A,B)&\ZZ&\ZZ/m&\QQ&\QQ/\ZZ\\
\ZZ&0&0&0&0\\
\ZZ/n&0&\ZZ/d&0&\ZZ/n\\
\QQ&0&0&0&0\\
\QQ/\ZZ&0&\ZZ/m&0&\QQ/\ZZ
\end{array}
$$
and the Ext table is
$$
\begin{array}{c c c c c}
\Ext^1_{\ZZ}(A,B)&\ZZ&\ZZ/m&\QQ&\QQ/\ZZ\\
\ZZ&0&0&0&0\\
\ZZ/n&\ZZ/n&\ZZ/d&0&0\\
\QQ&\widehat{\ZZ}/\ZZ&0&0&0\\
\QQ/\ZZ&\widehat{\ZZ}&\ZZ/m&0&0.
\end{array}
$$

For Tor, $\ZZ$ and $\QQ$ are flat, so their rows vanish.
The resolution
$0\to\ZZ\xrightarrow{n}\ZZ\to\ZZ/n\to0$
gives
$$
\Tor_1^{\ZZ}(\ZZ/n,B)=B[n].
$$
The exact sequence
$0\to\ZZ\to\QQ\to\QQ/\ZZ\to0$
gives
$$
\Tor_1^{\ZZ}(\QQ/\ZZ,B)
=\ker(B\to\QQ\otimes B),
$$
the torsion subgroup of $B$. These formulas give every Tor
entry.

For Ext, the free row vanishes and the same cyclic resolution
gives $\Ext^1_{\ZZ}(\ZZ/n,B)=B/nB$.
The groups $\QQ$ and $\QQ/\ZZ$ are divisible, hence injective
as $\ZZ$-modules, so their Ext columns vanish.

It remains to explain the entries with $B=\ZZ$ and
$A=\QQ$ or $\QQ/\ZZ$. Apply
$\Hom_{\ZZ}(\QQ/\ZZ,-)$ to
$0\to\ZZ\to\QQ\to\QQ/\ZZ\to0$.
Since $\Hom(\QQ/\ZZ,\QQ)=0$ and $\QQ$ is injective,
$$
\Ext^1_{\ZZ}(\QQ/\ZZ,\ZZ)
\cong\Hom_{\ZZ}(\QQ/\ZZ,\QQ/\ZZ)
\cong\widehat{\ZZ}.
$$
The last isomorphism follows by writing
$\QQ/\ZZ$ as the direct sum of its Prüfer $p$-groups, whose
endomorphism rings are $\ZZ_p$.

Now apply $\Hom_{\ZZ}(-,\ZZ)$ to
$0\to\ZZ\to\QQ\to\QQ/\ZZ\to0$.
Because $\Hom(\QQ,\ZZ)=0$ and
$\Ext^2_{\ZZ}(-,\ZZ)=0$, the resulting exact sequence is
$$
0\longrightarrow\ZZ\longrightarrow\widehat{\ZZ}
\longrightarrow\Ext^1_{\ZZ}(\QQ,\ZZ)
\longrightarrow0.
$$
Thus $\Ext^1_{\ZZ}(\QQ,\ZZ)\cong\widehat{\ZZ}/\ZZ$.

Finally, apply $\Hom_{\ZZ}(\QQ,-)$ and
$\Hom_{\ZZ}(\QQ/\ZZ,-)$ to
$0\to\ZZ\xrightarrow{m}\ZZ\to\ZZ/m\to0$.
The group $\widehat{\ZZ}/\ZZ$ is divisible: every residue
class modulo $m$ in $\widehat{\ZZ}$ has an integer
representative. Hence multiplication by $m$ on it is
surjective, and $\Ext^1_{\ZZ}(\QQ,\ZZ/m)=0$.
Also
$\widehat{\ZZ}/m\widehat{\ZZ}\cong\ZZ/m$,
so $\Ext^1_{\ZZ}(\QQ/\ZZ,\ZZ/m)\cong\ZZ/m$.

:::
