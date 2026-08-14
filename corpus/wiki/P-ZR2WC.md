---
schema: qual/card@1
id: P-ZR2WC
kind: problem
title: "- Definition of uniform convergence:"
classification:
  areas:
  - prelim
  topics:
  - uniform-convergence
  - riemann-integrability
relations: []
review: draft
---
4. 
   - Definition of uniform convergence:
  $$
  \theset{f_n}_{i=1}^\infty\rightrightarrows f \text{ on } X  \iff \forall \varepsilon > 0,~ \exists N(\varepsilon) \suchthat n\geq N(\varepsilon) \implies \forall x \in X,~ \abs{f_n(x) - f(x)} < \varepsilon
  $$
    - **Theorem** (Riemann-Lebesgue): A bounded function on a compact set is integrable iff its set of discontinuities has measure zero.

    - **Theorem**: 
  $$
  f_n \rightrightarrows f \implies \lim_{n\to\infty} \int_X f_n(x) ~dx = \int_X  \lim_{n\to\infty} f_n(x) ~dx = \int_X f(x) ~dx
  $$
    - *Proof* (Pugh 218): 
    
      - We first show $f$ is integrable. Fix $f_n$; by the Riemann-Lebesgue theorem, since $f_n$ is integrable, it is bounded and discontinuous only at finitely many points $Z_n$, and thus bounded and continuous on $[a,b] - Z_n$ where $\mu(Z_n) = 0.$ 
      
        Let $Z = \union_n Z_n$, which is a countable union of countable sets and thus countable, so $\mu(Z) = 0$. A uniform limit of continuous functions is continuous, so $\lim f_n = f$ is a continuous function on $S = [a,b] - Z$. 
      
        Since $f$ is a uniform limit of bounded functions, it is bounded, and since $f$ is both bounded and continuous off of a null set, it is integrable. 
  
      - We now show $\int f_n \rightrightarrows \int f$. Let $C_b(X, \RR) = \theset{f:X \to \RR \suchthat f\text{ is bounded }}$, which is a complete normed space under the norm $\norm{f}_\infty = \displaystyle\sup_{x\in X}\theset{\abs{f(x)}}$ which induces the metric 
      $$d(f,g) = \norm{f-g}_\infty = \sup_{x\in X}\theset{\abs{f(x) - g(x)}}.$$

      - Now $f_n \rightrightarrows f \iff \norm{f-f_n}_\infty \to 0$, so we can thus compute
      $$\begin{align*}
      \abs{\int_a^b f(x)~dx - \int_a^b f_n(x)~dx} 
      &= \abs{\int_a^b f(x) - f_n(x)~dx} \\
      &\leq \int_a^b \abs{f(x) - f_n(x)}~dx \\
      &\leq \norm{f-f_n}_\infty \abs{b-a}
       \to ~0 \abs{b-a} = 0.
      \end{align*}$$

      Applying this to $f = 0$, we have $f_n \rightrightarrows 0 \implies \int f_n \rightrightarrows \int 0 = 0$. $\qed$

