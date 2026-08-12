---
schema: qual/card@1
id: P-YJFBZ
kind: problem
title: "For each $n\\in \\ZZ^{\\geq 1}$, let $P_n(z) = 1 + z + {1\\over 2!} z^2 + \\cdots + {1\\over n!}z^n$ Show that for sufficiently large $n$, the\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
For each $n\in \ZZ^{\geq 1}$, let
\[
P_n(z) = 1 + z + {1\over 2!} z^2 + \cdots + {1\over n!}z^n
.\]
Show that for sufficiently large $n$, the polynomial $P_n$ has no zeros in $\abs{z} < 10$, while the polynomial $P_n(z) - 1$ has precisely 3 zeros there.
:::

:::{.solution}
More is true: this will hold for any disc of arbitrary radius $R$, with $n$ depending on $R$.
Fix $R$, then use that $P_n(z) \convergesto{n\to\infty} e^z$ uniformly on the compact disc $\abs{z} \leq R$.
Consequently, setting $g_n(z) \da {P_n(z)\over e^z}$, we have $g_n(z) \to 1$ uniformly on this disc, for any $\eps> 0$ this can be used to produce an $n\gg 1$ such that $\abs{ g_n(z) - 1 } < \eps$ for all $\abs{z} \leq R$.

So take $\eps \da 1$ and define $h(z) \da 1$, then for $\abs{z} = R$
\[
\abs{g_n(z) - 1} < 1 = \abs{h(z)}
,\]
so by Rouché,
\[
0 = \size Z_{h} = \size Z_{h + (g_n - 1)} = \size Z_{g_n}
,\]
since $h$ has no zeros at all.
Take $R=10$ to get the stated result.

For $P_n(z) - 1$, note that $e^z-1=0$ has three solutions in $\abs{z} < 10$, namely $z=0, \pm 2\pi i$.
We similarly have $P_n(z)-1\to e^z-1$ uniformly, so on a disc of radius $R$ choose $n$ large enough so that
\[
\abs{{P_n(z) -1 \over e^z - 1} - 1} &< 1 \\
\implies \abs{ (P_n(z) - 1) - (e^z-1) \over e^z-1} &< 1 \\
\implies \abs{ (P_n(z) - 1) - (e^z-1)} &< \abs{e^z-1} \\
\da \abs{m(z)} &< \abs{M(z)}
,\]
so 
\[
3 = \size Z_M = \size Z_{M+m} = \size Z_{P_n - 1}
.\]
:::

