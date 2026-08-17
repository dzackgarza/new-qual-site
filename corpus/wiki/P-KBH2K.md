---
schema: qual/card@1
id: P-KBH2K
kind: problem
title: "Let $\\{a_n\\}_{n=1}^\\infty$ be a sequence of real numbers. Prove that if $\\displaystyle\\lim_{n\\to \\infty } a_n = 0$, then $\\lim _{n \\rightarrow \\infty} \\frac{a_{1}+\\cdots+a_{n}}{n}=0$\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - series-of-numbers
  - limits
relations: []
review: draft
solved: true
---
Let $\{a_n\}_{n=1}^\infty$ be a sequence of real numbers.

a.
Prove that if $\displaystyle\lim_{n\to \infty } a_n = 0$, then 
\[
\lim _{n \rightarrow \infty} \frac{a_{1}+\cdots+a_{n}}{n}=0
\]

b.
Prove that if $\displaystyle\sum_{n=1}^{\infty} \frac{a_{n}}{n}$ converges, then 
\[
\lim _{n \rightarrow \infty} \frac{a_{1}+\cdots+a_{n}}{n}=0
\]

:::{.solution}
\envlist

:::{.concept}
\envlist
- Cesaro mean/summation. 
- Break series apart into pieces that can be handled separately.
- Idea: once $N$ is large enough, $a_k \approx S$, and all smaller terms will die off as $N\to \infty$.
  - See [this MSE answer](https://math.stackexchange.com/questions/514802/convergence-of-series-implies-convergence-of-cesaro-mean).
:::

:::{.proof title="of a"}
\envlist

- Prove a stronger result: 
\[
a_k \to S \implies S_N\definedas \frac 1 N \sum_{k=1}^N a_k \to S
.\]

- For any $\eps> 0$, use convergence $a_k \to S$: choose (and fix) $M = M(\eps)$ large enough such that 
\[
k\geq M+1 \implies \abs{a_k - S} < \varepsilon
.\]

- With $M$ fixed, choose $N = N(M, \eps)$ large enough so that ${1\over N} \sum_{k=1}^{M} \abs{a_k - S} < \eps$.

- Then
\[
\left|\left(\frac{1}{N} \sum_{k=1}^{N} a_{k}\right)-S\right| 
&= {1\over N} \abs{ \qty{\sum_{k=1}^N a_k} - NS  } \\
&= {1\over N} \abs{ \qty{\sum_{k=1}^N a_k} - \sum_{k=1}^N S  } \\
&=\frac{1}{N}\left|\sum_{k=1}^{N}\left(a_{k}-S\right)\right| \\
&\leq \frac{1}{N} \sum_{k=1}^{N}\left|a_{k}-S\right| \\
&= {1\over N} \sum_{k=1}^{M} \abs{a_k - S} + \sum_{k=M+1}^N \abs{a_k - S} \\
&\leq {1\over N} \sum_{k=1}^{M} \abs{a_k - S} + \sum_{k=M+1}^N {\eps } \quad \text{since } a_k \to S\\
&= {1\over N} \sum_{k=1}^{M} \abs{a_k - S} + (N - M){\eps } \\
&\leq \eps + (N(M, \eps) - M(\eps))\eps
.\]

:::

:::{.remark}
Revisit, not so clear that the last line can be made smaller than $\eps$, since $M, N$ both depend on $\eps$...
:::
#todo

:::{.proof title="of b"}
\envlist

- Define
\[
\Gamma_n \definedas \sum_{k=n}^\infty \frac{a_k}{k}
.\]

- $\Gamma_1 = \sum_{k=1}^n \frac{ a_k } k$ is the original series and each $\Gamma_n$ is a tail of $\Gamma_1$, so by assumption $\Gamma_n \converges{n\to\infty}\to 0$.

- Compute
\[
\frac 1 n \sum_{k=1}^n a_k 
&= \frac 1 n (\Gamma_1 + \Gamma_2 + \cdots + \Gamma_{n} \mathbf{- \Gamma_{n+1}}) \\
.\]

- This comes from consider the following summation:
\begin{tikzcd}[row sep=small, column sep=small]
\Gamma_1:&\arrow[dash, ddddd]   & a_1 & + \frac{a_2}{2} & + \frac{a_3}{3} & + \cdots &     &                                    &          &  &  &  \\
\Gamma_2:                                                       &               &     & \frac{a_2}{2}   & + \frac{a_3}{3} & + \cdots &     &                                    &          &  &  &  \\
\Gamma_3:                                                       &               &     &                 & \frac{a_3}{3}   & + \cdots &     &                                    &          &  &  &  \\
 \arrow[dash, rrrrrrrrrr] &&&&&&&&&&{}&   \\
\sum_{i=1}^n \Gamma_i:                                          &               & a_1 & +a_2            & +a_3            & + \cdots & a_n & + \frac{a_{n+1}}{n+1}              & + \cdots &  &  &  \\
& {}               &     &                 &                 &          &     &   &          &  &  & 
\end{tikzcd}

- Use part (a): since $\Gamma_n \converges{n\to\infty}\to 0$, we have ${1\over n} \sum_{k=1}^n \Gamma_k \converges{n\to\infty}\to 0$.
- Also a minor check: $\Gamma_n \to 0 \implies {1\over n}\Gamma_n \to 0$.
- Then
\[
\frac 1 n \sum_{k=1}^n a_k 
&= \frac 1 n (\Gamma_1 + \Gamma_2 + \cdots + \Gamma_{n} \mathbf{- \Gamma_{n+1}}) \\
&= \qty{ {1\over n } \sum_{k=0}^n \Gamma_k } - \qty{{1\over n}\Gamma_{n+1} } \\
&\converges{n\to\infty}\to 0
.\]

:::

:::
