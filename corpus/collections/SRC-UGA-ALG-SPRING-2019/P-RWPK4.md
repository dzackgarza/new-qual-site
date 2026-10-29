---
schema: qual/card@1
id: P-RWPK4
kind: problem
title: Jordan form over $\QQ$ and $\FF_p$ of the $p\times p$ matrix with zeros on
  the diagonal and ones elsewhere
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Characteristic
relations: []
review: draft
---
::: {.problem}
Let $p$ be a prime number, and let $A \in M_p(F)$ be the $p \times p$ matrix with $0$ on the main diagonal and $1$ in all off-diagonal entries:
$$
A = \begin{pmatrix}
0 & 1 & 1 & \cdots & 1 \\
1 & 0 & 1 & \cdots & 1 \\
1 & 1 & 0 & \cdots & 1 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & 1 & 1 & \cdots & 0
\end{pmatrix}.
$$
Determine the Jordan Canonical Form (JCF) of $A$ and an explicit change-of-basis matrix $P$ putting $A$ in Jordan canonical form:

(a) When $F = \QQ$,

(b) When $F = \FF_p$.
:::

::: {.solution}

::: pf

::: pf-step

If $J_p$ is the all-ones matrix, then $A=J_p-I_p$.

::: pf-proof

::: pf-step

Let $J_p \in M_p(F)$ denote the $p \times p$ all-ones matrix ($J_{i, j} = 1$ for all $1 \le i, j \le p$).

:::

::: pf-step

Then $A = J_p - I_p$.

:::

::: pf-step

For any scalar $\mu \in F$ and vector $v \in F^p$:
    $$J_p v = \mu v \iff A v = (J_p - I_p) v = (\mu - 1) v.$$

:::

::: pf-step

Thus the eigenvalues of $A$ are $\lambda = \mu - 1$, where $\mu$ is an eigenvalue of $J_p$, and the corresponding eigenspaces are identical.

:::

:::

:::

::: pf-step

Over $\QQ$, the matrix $A$ is diagonalizable with eigenvalues $p-1$ and $-1$ of multiplicities $1$ and $p-1$, respectively.

::: pf-proof

::: pf-step

Spectrum of $J_p$:
        - For the vector $v_1 = (1, 1, \dots, 1)^t \in \QQ^p$, $J_p v_1 = p v_1$, so $\mu_1 = p$ is an eigenvalue of $J_p$.
        - For each $i \in \{1, \dots, p-1\}$, let $u_i = e_1 - e_{i+1} = (1, 0, \dots, -1, \dots, 0)^t$. Since the sum of entries of $u_i$ is $1 - 1 = 0$, $J_p u_i = 0 = 0 \cdot u_i$.
        - The $p-1$ vectors $\{u_1, \dots, u_{p-1}\}$ are linearly independent: if $\sum_{i=1}^{p-1} c_i u_i = 0$, the $(i+1)$-st component is $-c_i = 0$ for each $i$.
        - Thus $\mu_0 = 0$ is an eigenvalue of $J_p$ with geometric multiplicity $p - 1$.

:::

::: pf-step

Eigenvalues and eigenspaces of $A$:
        - The eigenvalue $\mu_1 = p$ corresponds to $\lambda_1 = p - 1$ for $A$ with eigenvector $v_1$.
        - The eigenvalue $\mu_0 = 0$ corresponds to $\lambda_0 = -1$ for $A$ with $(p-1)$-dimensional eigenspace spanned by $\{u_1, \dots, u_{p-1}\}$.

:::

::: pf-step

Diagonalizability:
        - The sum of geometric multiplicities is $1 + (p - 1) = p = \dim \QQ^p$.
        - Therefore $A$ is diagonalizable over $\QQ$, so its JCF is diagonal:
        $$J_{\QQ}(A) = \operatorname{diag}(p - 1, -1, -1, \dots, -1).$$

:::

::: pf-step

Transformation matrix $P$:

:::

- Define $P \in \operatorname{GL}_p(\QQ)$ with columns given by the eigenbasis:
$$P = \begin{pmatrix} v_1 & u_1 & u_2 & \cdots & u_{p-1} \end{pmatrix} = \begin{pmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & -1 & 0 & \cdots & 0 \\
1 & 0 & -1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & 0 & 0 & \cdots & -1
\end{pmatrix}.$$
- Then $P^{-1} A P = J_{\QQ}(A)$.

:::

:::

::: pf-step

Over $\FF_p$, the nilpotent part $A+I_p$ has square zero and rank one.

::: pf-proof

::: pf-step

Characteristic polynomial over $\FF_p$:
        - In $\FF_p$, $p - 1 \equiv -1 \pmod p$.
        - Thus $\chi_A(x) = (x - (p - 1))(x + 1)^{p-1} \equiv (x + 1)^p \pmod p$.
        - The only eigenvalue of $A$ in $\FF_p$ is $\lambda = -1$, with algebraic multiplicity $p$.

:::

::: pf-step

Nilpotent part $N = A - (-1) I_p = A + I_p = J_p$:
        - Over $\FF_p$, $N^2 = J_p^2 = p J_p \equiv 0 \in M_p(\FF_p)$.
        - Since $J_p \ne 0$, the minimal polynomial of $A$ is $m_A(x) = (x + 1)^2$.
        - Thus the largest Jordan block has size 2.

:::

::: pf-step

Geometric multiplicity:
        - All rows of $J_p$ are identical and non-zero, so $\operatorname{rank}(J_p) = 1$.
        - By Rank-Nullity, $\dim \ker(A + I_p) = \dim \ker(J_p) = p - 1$.
        - There are exactly $p - 1$ Jordan blocks for $\lambda = -1$.

:::

::: pf-step

Jordan block structure:
        - Since the partition of $p$ into $p - 1$ parts with largest part 2 is uniquely $2 + 1 + 1 + \dots + 1$, the JCF over $\FF_p$ consists of one $2 \times 2$ block and $p - 2$ blocks of size $1 \times 1$:
        $$J_{\FF_p}(A) = \begin{pmatrix}
        -1 & 1 & 0 & \cdots & 0 \\
        0 & -1 & 0 & \cdots & 0 \\
        0 & 0 & -1 & \cdots & 0 \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & 0 & \cdots & -1
        \end{pmatrix}.$$

:::

::: pf-step

Jordan basis and matrix $P$:

:::

- Choose the generalized eigenvector $w = e_1 = (1, 0, 0, \dots, 0)^t \in \FF_p^p$.
- Apply $A + I = J_p$:
$$(A + I) w = J_p e_1 = (1, 1, \dots, 1)^t = v_1.$$
- Since $(A + I) v_1 = J_p v_1 = p v_1 \equiv 0$, the pair $\{v_1, w\}$ forms a Jordan chain of length 2:
$$A v_1 = -v_1, \qquad A w = v_1 - w.$$
- For the remaining $p - 2$ blocks of size 1, choose eigenvectors $u_1, \dots, u_{p-2}$ where $u_i = e_1 - e_{i+1}$.
- These $p$ vectors $\{v_1, w, u_1, u_2, \dots, u_{p-2}\}$ form a basis of $\FF_p^p$.
- Setting $P = \begin{pmatrix} v_1 & w & u_1 & u_2 & \cdots & u_{p-2} \end{pmatrix} \in \operatorname{GL}_p(\FF_p)$ satisfies $P^{-1} A P = J_{\FF_p}(A)$.

:::

:::

::: pf-qed

Over $\QQ$, $A$ is diagonalizable with eigenvalues $p-1$ (mult 1) and $-1$ (mult $p-1$). Over $\FF_p$, $A$ has one Jordan block of size 2 and $p-2$ Jordan blocks of size 1 for eigenvalue $-1$.

:::

:::

:::
