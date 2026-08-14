---
schema: qual/card@1
id: P-KPCIE
kind: problem
title: "Let $x_0 = a, x_1 = b$, and set $x_n \\definedas {x_{n-1} + x_{n-2} \\over 2} \\quad n\\geq 2$ Show that $\\theset{x_n}$ is a Cauchy sequence and find its\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - sequences-of-numbers
  - completeness
  - convergence
relations: []
review: draft
---
:::{.problem title="?"}
Let $x_0 = a, x_1 = b$, and set
\[  
x_n \definedas {x_{n-1} + x_{n-2} \over 2} \quad n\geq 2
.\]

Show that $\theset{x_n}$ is a Cauchy sequence and find its limit in terms of $a$ and $b$.

:::

:::{.solution}
With some substitution, one can compute
\[
\abs{x_n - x_{n-1}}
= \abs{{1\over 2} x_{n-1} + {1\over 2} x_{n-2} - x_{n-1}}
= {1\over 2} \abs{x_{n-1} - x_{n-2}}
,\]
which holds for all $n$.
This is enough to show that the sequence is contractive, i.e. 
\[
\abs{x_n - x_{n-1}} = c \abs{x_{n-1} - x_{n-2}} && c\in (0, 1)
.\]

Apply this recursively yields
\[
\abs{x_n - x_{n-1}} = \qty{1\over 2}^{n-1} \abs{b-a} \convergesto{n\to\infty} 0
,\]
since $\abs{b-a}$ is a constant.
So in fact $x_n$ is convergent and thus Cauchy convergent.

Note: to compare $\abs{x_i - x_j}$ directly, assume $i>j$ and apply the above estimate $i-j+1$ on $\abs{x_i - x_{i-1}}, \abs{x_{i-1} - x_{i-2}}, \cdots$ to reduce to this case.
This yields something like
\[
\abs{x_i - x_j} = \qty{1\over 2}^{i-j+1}\abs{x_{j} - x_{j-1}} = \qty{1\over 2}^{i-j+1} \qty{1\over 2}^{j-1} \abs{b-a}\to 0
.\]
One could equivalently use the triangle inequality and a partial geometric sum to write
\[
\abs{x_i - x_j} \leq \sum_{j\leq k \leq i-1} \abs{x_{k+1} - x_{k}} \implies \abs{x_i - x_j} \leq c^j\qty{1\over 1-c}\abs{b-a}
.\]


Computing its limit: the usual trick of setting $L \da \lim x_n = \lim x_{n-1} = \lim x_{n-2}$ only yields $L = {L + L \over 2}$ here, and thus no information.
Instead assume $x_n = r^n$ is geometric, then
\[
2x_n - x_{n-1} - x_{n-2} = 0 \implies 2r^n - r^{n-1} - r^{n-2} = 0 \implies 2r^2 - r - 1 = 0 \iff (2r+1)(r-1) = 0 \implies r = -1/2, 1
.\]
Write a general solution as 
\[
x_n = c_1 (-1/2)^n + c_2 (1)^n = c_1 (-1/2)^n + c_2
,\]
and solve for initial conditions:
\[
x_0: \quad a &= c_1 + c_2 \\
x_1: \quad b &= (-1/2)c_1 + c_2 \\ \\
\implies
\matt 1 1 {-1/2} 1
\begin{bmatrix}
c_1  
\\
c_2 
\end{bmatrix} &=
\begin{bmatrix}
a  
\\
b 
\end{bmatrix} \\
\implies 
\begin{bmatrix}
c_1  
\\
c_2 
\end{bmatrix} &=
{1\over 1 + (1/2)}
\matt 1 {-1} {1/2} 1
\begin{bmatrix}
a  
\\
b 
\end{bmatrix} 
\\
&=
\qty{1\over 3}
\matt 2 {-2} {1} 2
\begin{bmatrix}
a  
\\
b 
\end{bmatrix} \\
&=
\qty{1\over 3}
\begin{bmatrix}
2a-2b
\\
a+b
\end{bmatrix} 
.\]

So the general solution is
\[
x_n = {2\over 3}(a-b) \qty{-1\over 2}^n + {1\over 3}(a+b)\convergesto{n\to \infty} \qty{1\over 3}(a+b)
.\]
:::

