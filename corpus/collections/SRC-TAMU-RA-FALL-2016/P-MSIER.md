---
schema: qual/card@1
id: P-MSIER
kind: problem
title: Pointwise convergence versus convergence in measure on a finite measure space
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Measure Theory
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Let $(\Omega,\mathcal{A},\mu)$ be a finite measure space and $(f_n)$ be a sequence of measurable functions on $\Omega$ that converges pointwise to zero.
Prove that $(f_n)$ converges in measure to zero.
Show that the converse is false for $[0,1]$ with Lebesgue measure.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/a16.pdf` and no solutions sheet accompanies it, so the argument and the counterexample below are the card's own. The first part is proved directly from the dominated convergence theorem, which is available because the measure is finite; the card's earlier route through Egoroff's theorem is also correct and is noted at the end of that step. The second part verifies the counterexample, which the earlier version only named.

Throughout, $(\Omega,\mathcal{A},\mu)$ is a finite measure space, $\mu(\Omega)<\infty$, each $f_{n}$ is measurable, and $f_{n}\to0$ pointwise. For $\varepsilon>0$ put $A_{n}\coloneqq\theset{x\in\Omega\mid\abs{f_{n}(x)}\geq\varepsilon}$, so that $f_{n}\to0$ in measure means $\mu(A_{n})\to0$ for every $\varepsilon>0$.

::: pf

::: {.pf-step #in-measure}
$f_{n}\to0$ in measure.

:::: pf-proof

::: {.pf-step #setwise}
For fixed $\varepsilon>0$, the characteristic functions $\chi_{A_{n}}$ tend to $0$ at every point.

::: pf-proof
Let $x\in\Omega$. Since $f_{n}(x)\to0$, there is $N$ with $\abs{f_{n}(x)}<\varepsilon$ for all $n\geq N$, and then $x\notin A_{n}$ for those $n$; so $\chi_{A_{n}}(x)=0$ eventually and the sequence tends to $0$.
:::

:::

::: {.pf-step #dominated}
$\mu(A_{n})=\int_{\Omega}\chi_{A_{n}}\,d\mu\to0$.

::: pf-proof
Each $\chi_{A_{n}}$ is measurable and $\abs{\chi_{A_{n}}}\leq1$, and the constant function $1$ is integrable because $\mu(\Omega)<\infty$ — this is where finiteness of the measure is used. By step [](#setwise){.pf-ref} the sequence tends to $0$ pointwise, so the dominated convergence theorem gives $\int_{\Omega}\chi_{A_{n}}\,d\mu\to\int_{\Omega}0\,d\mu=0$.
:::

:::

::: {.pf-step}
The conclusion follows.

::: pf-proof
$\mu(A_{n})=\int\chi_{A_{n}}d\mu\to0$ by step [](#dominated){.pf-ref}, and $\varepsilon>0$ was arbitrary, which is the definition of convergence in measure. Alternatively, Egoroff's theorem applies to this finite measure space and gives, for each $\delta>0$, a set $E$ with $\mu(E)<\delta$ off which the convergence is uniform, so that $A_{n}\subset E$ for all large $n$ and hence $\mu(A_{n})<\delta$.
:::

:::

::::

:::

::: {.pf-step #enumeration}
On $[0,1]$ with Lebesgue measure, put $f_{n}\coloneqq\chi_{I_{n}}$ where $n=2^{k}+j$ with $0\leq j<2^{k}$ and $I_{n}\coloneqq\big[j/2^{k},(j+1)/2^{k}\big]$. This is a well-defined sequence of measurable functions on $[0,1]$.

::: pf-proof
Every positive integer $n$ lies in exactly one interval $[2^{k},2^{k+1})$ of integers, namely with $k$ the unique integer such that $2^{k}\leq n<2^{k+1}$, and then $j\coloneqq n-2^{k}$ satisfies $0\leq j<2^{k}$. So the assignment $n\mapsto(k,j)$ is well defined and each $I_{n}$ is a closed interval contained in $[0,1]$, whose characteristic function is measurable.
:::

:::

::: {.pf-step #measure-convergence}
$f_{n}\to0$ in measure on $[0,1]$.

:::: pf-proof

::: {.pf-step #level-set}
For $0<\varepsilon<1$ the set where $\abs{f_{n}}\geq\varepsilon$ is $I_{n}$, of measure $2^{-k}$.

::: pf-proof
$\abs{f_{n}}$ takes only the values $0$ and $1$, so for $0<\varepsilon<1$ the level set $\theset{\abs{f_{n}}\geq\varepsilon}$ is exactly $\theset{f_{n}=1}=I_{n}$, whose Lebesgue measure is $(j+1)/2^{k}-j/2^{k}=2^{-k}$.
:::

:::

::: {.pf-step}
$\mu\big(\theset{\abs{f_{n}}\geq\varepsilon}\big)\to0$ as $n\to\infty$.

::: pf-proof
By step [](#level-set){.pf-ref} the measure is $2^{-k}$, where $k=k(n)$ tends to infinity with $n$ because $n\geq2^{k}$; hence $2^{-k}\to0$. For $\varepsilon\geq1$ the level set is empty and the measure is $0$ throughout.
:::

:::

::::

:::

::: pf-step
Therefore the converse fails: $f_{n}$ does not converge pointwise to $0$ on $[0,1]$.

::: pf-proof
Fix any $x\in[0,1]$. For every $k\geq1$ there is exactly one $j$ with $0\leq j<2^{k}$ and $j/2^{k}\leq x<(j+1)/2^{k}$, and for that $j$ the point $x$ lies in $I_{n}$ with $n=2^{k}+j$, so $f_{n}(x)=1$. (For $x=1$ the same holds, with $j=2^{k}-1$.) Hence the subsequence $f_{2^{k}+j_{k}}(x)=1$ does not tend to $0$, and $f_{n}(x)$ has no limit at any point of $[0,1]$. So the sequence converges in measure, by step [](#measure-convergence){.pf-ref}, but not pointwise, which is the required counterexample to the converse.
:::

:::

:::

:::
