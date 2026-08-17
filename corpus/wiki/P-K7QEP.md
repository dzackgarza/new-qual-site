---
schema: qual/card@1
id: P-K7QEP
kind: problem
title: $L^2([0,1])$ is dense in $L^1([0,1])$, and Riesz representation for $L^1([0,1])$
classification:
  areas:
  - real-analysis
  topics:
  - riesz-representation
  - lp-spaces
  - density
relations: []
review: draft
solved: true
---
a.
Show that $L^2([0, 1]) ⊆ L^1([0, 1])$ and argue that $L^2([0, 1])$ in fact forms a dense subset of $L^1([0, 1])$.

b.
Let $Λ$ be a continuous linear functional on $L^1([0, 1])$.
  
Prove the Riesz Representation Theorem for $L^1([0, 1])$ by following the steps below:

i. Establish the existence of a function $g ∈ L^2([0, 1])$ which represents $Λ$ in the sense that
  \[
  Λ(f ) = f (x)g(x) dx \text{ for all } f ∈ L^2([0, 1]).
  \]

  > Hint: You may use, without proof, the Riesz Representation Theorem for $L^2([0, 1])$.

ii. Argue that the $g$ obtained above must in fact belong to $L^∞([0, 1])$ and represent $Λ$ in the sense that
  \[
  \Lambda(f)=\int_{0}^{1} f(x) \overline{g(x)} d x \quad \text { for all } f \in L^{1}([0,1])
  \]
  with
  \[
  \|g\|_{L^{\infty}([0,1])} = \|\Lambda\|_{L^{1}([0,1])\dual}
  \]

:::{.concept}
\envlist

- Holders' inequality: $\norm{fg}_1 \leq \norm{f}_p \norm{f}_q$
- Riesz Representation for $L^2$: If $\Lambda \in (L^2)\dual$ then there exists a unique $g\in L^2$ such that $\Lambda(f) = \int fg$.
- $\norm{f}_{L^\infty(X)} \definedas \inf \theset{t\geq 0 \suchthat \abs{f(x)} \leq t \text{ almost everywhere} }$.
- **Lemma**:  $m(X) < \infty \implies L^p(X) \subset L^2(X)$.

  :::{.proof}
  - Write Holder's inequality as $\norm{fg}_1 \leq \norm{f}_a \norm{g}_b$ where $\frac 1 a + \frac 1 b = 1$, then
  \[
  \norm{f}_p^p = \norm{\abs f^p}_1 \leq \norm{\abs f^p}_a ~\norm{1}_b
  .\]

  - Now take $a = \frac 2 p$ and this reduces to 
  \[
  \norm{f}_p^p &\leq \norm{f}_2^p ~m(X)^{\frac 1 b} \\
  \implies \norm{f}_p &\leq \norm{f}_2 \cdot O(m(X)) < \infty
  .\]
  :::
:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- Note $X = [0, 1] \implies m(X) = 1$.
- By Holder's inequality with $p=q=2$, 
\[
\norm{f}_1 = \norm{f\cdot 1}_1 \leq \norm{f}_2 \cdot \norm{1}_2 = \norm{f}_2 \cdot m(X)^{\frac 1 2} = \norm{f}_2,
\]

- Thus $L^2(X) \subseteq L^1(X)$ 
- Since they share a common dense subset (simple functions), $L^2$ is dense in $L^1$ 

:::

Let $\Lambda \in L^1(X)\dual$ be arbitrary.

:::{.proof title="of b, Existence of $g$ representing $\Lambda$"}
Let $f\in L^2\subseteq L^1$ be arbitrary.

Claim: $\Lambda\in L^1(X)\dual \implies \Lambda \in L^2(X)\dual$.

- Suffices to show that $\norm{\Gamma}_{L^2(X)\dual} \definedas \sup_{\norm{f}_2 = 1} \abs{\Gamma(f)} < \infty$, since bounded implies continuous.

- By the lemma, $\norm{f}_1 \leq C\norm{f}_2$ for some constant $C \approx m(X)$.

- Note $$\norm{\Lambda}_{L^1(X)\dual} \definedas \displaystyle\sup_{\norm{f}_1 = 1} \abs{\Lambda(f)}$$

- Define $\hat f = {f\over \norm{f}_1}$ so $\norm{\hat f}_1 = 1$

- Since $\norm{\Lambda}_{1\dual}$ is a supremum over *all* $f \in L^1(X)$ with $\norm{f}_1 =1$, 
\[
\abs{\Lambda(\hat f)} \leq \norm{\Lambda}_{(L^1(X))\dual}
,\]

- Then
\[
\frac{\abs{\Lambda(f)}}{\norm{f}_1} &= \abs{\Lambda(\hat f)} \leq \norm{\Lambda}_{L^1(X)\dual} \\
\implies \abs{\Lambda(f)} 
&\leq \norm{\Lambda}_{1\dual} \cdot \norm{f}_1 \\
&\leq \norm{\Lambda}_{1\dual} \cdot C \norm{f}_2 < \infty \quad\text{by assumption}
,\]

- So $\Lambda \in (L^2)\dual$.

Now apply Riesz Representation for $L^2$: there is a $g \in L^2$ such that $$f\in L^2 \implies \Lambda(f) = \inner{f}{g} \definedas \int_0^1 f(x) \bar{g(x)}\, dx.$$

:::

:::{.proof title="of b, $g$ is in $L^\infty$"}
\envlist

- It suffices to show $\norm{g}_{L^\infty(X)} < \infty$.
- Since we're assuming $\norm{\Gamma}_{L^1(X)\dual} < \infty$, it suffices to show the stated equality. 
:::{.remark}
Is this assumed..? Or did we show it..?
:::

- Claim: $\norm{\Lambda}_{L^1(X)\dual} =\norm{g}_{L^\infty(X)}$
  - The result will follow since $\Lambda$ was assumed to be in $L^1(X)\dual$, so $\norm{\Lambda}_{L^1(X)\dual} < \infty$.
  - $\leq$: 
  \[
  \norm{\Lambda}_{L^1(X)\dual} 
  &= \sup_{\norm{f}_1 = 1} \abs{\Lambda(f)} \\
&= \sup_{\norm{f}_1 = 1} \abs{\int_X f \bar g} \quad\text{by (i)}\\
  &= \sup_{\norm{f}_1 = 1} \int_X \abs{f \bar g} \\
  &\definedas \sup_{\norm{f}_1 = 1} \norm{fg}_1 \\
  &\leq \sup_{\norm{f}_1 = 1} \norm{f}_1 \norm{g}_\infty \quad\text{by Holder with } p=1,q=\infty\\
  &= \norm{g}_\infty
  ,\]

  - $\geq$:

    - Suppose toward a contradiction that $\norm{g}_\infty > \norm{\Lambda}_{1\dual}$.

    - Then there exists some $E\subseteq X$ with $m(E) > 0$ such that $$x\in E \implies \abs{g(x)} > \norm{\Lambda}_{L^1(X)\dual}.$$

    - Define 
    \[
    h = \frac{1}{m(E)} \frac{\overline{g}}{\abs g} \chi_E
    .\]
  
    - Note $\norm{h}_{L^1(X)} = 1$.
    
    - Then
    \[
    \Lambda(h) &= \int_X hg \\
    &\definedas \int_X \frac{1}{m(E)} \frac{g \overline g}{\abs g} \chi_E \\
    &= \frac{1}{m(E)} \int_E \abs{g} \\
    &\geq \frac{1}{m(E)} \norm{g}_\infty m(E) \\
    &= \norm{g}_\infty \\
    &> \norm{\Lambda}_{L^1(X)\dual}
    ,\]
      a contradiction since $\norm{\Lambda}_{L^1(X)\dual}$ is the supremum over all $h_\alpha$ with $\norm{h_\alpha}_{L^1(X)} = 1$.

:::

:::

