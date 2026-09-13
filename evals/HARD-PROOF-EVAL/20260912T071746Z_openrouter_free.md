# Eval: openrouter/free

- Run timestamp (UTC): 20260912T071746Z

- Model timestamp (UTC): 20260912T071845Z

- Model: `openrouter/free`

- Provider: `openrouter`

- Success: True

- Usage: {"prompt_tokens": 3740, "completion_tokens": 8000, "total_tokens": 11740, "cost": 0, "is_byok": false, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "cost_details": {"upstream_inference_cost": 0, "upstream_inference_prompt_cost": 0, "upstream_inference_completions_cost": 0}, "completion_tokens_details": {"reasoning_tokens": 4967, "image_tokens": 0, "audio_tokens": 0}}

- Problem source: `HARD-PROOF-EVAL.md` verbatim (Koebe-Bieberbach)

- Prompt length: 8891 chars

* * *

## Chain-of-Thought (reasoning)

Let me work through each part (a) through (g) carefully and completely.

## Part (a)

We need to show that without further restrictions on $f$ (beyond holomorphicity on $\mathbb{D}$ and $f(0) = 0$), there is no $r > 0$ such that $D_r(0) \subseteq f(\mathbb{D})$ for all such $f$.

The hint suggests finding $f_n$ with $f_n(0) = 0$ and $1/n \notin f_n(\mathbb{D})$.

Take $f_n(z) = z/n$.
Then:

- $f_n(0) = 0$ ✓

- $f_n(\mathbb{D}) = \{z/n : |z| < 1\} = D_{1/n}(0)$, the open disk of radius $1/n$ centered at 0.

- $1/n \notin D_{1/n}(0)$ since $|1/n| = 1/n$ and the disk is open (points have modulus strictly less than $1/n$).

So $1/n \notin f_n(\mathbb{D})$.

$f_n'(0) = 1/n \to 0$ as $n \to \infty$.

For any $r > 0$, choose $n$ large enough so that $1/n < r$.
Then $1/n \in D_r(0)$ but $1/n \notin f_n(\mathbb{D})$, so $D_r(0) \not\subseteq f_n(\mathbb{D})$.

## Part (b)

Now assume $f'(0) = 1$.
Consider $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1)$ for $\epsilon > 0$.

- $f_\epsilon(0) = \epsilon(e^0 - 1) = 0$ ✓

- $f_\epsilon'(z) = \epsilon \cdot (1/\epsilon) e^{z/\epsilon} = e^{z/\epsilon}$, so $f_\epsilon'(0) = 1$ ✓

- $f_\epsilon$ is holomorphic on all of $\mathbb{C}$, hence on $\mathbb{D}$.

The image: $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1)$.
Since $e^{z/\epsilon} \neq 0$ for all $z \in \mathbb{C}$, we have $f_\epsilon(z) \neq \epsilon(0 - 1) = -\epsilon$.

So $-\epsilon \notin f_\epsilon(\mathbb{D})$.

For any $r > 0$, choose $\epsilon < r$.
Then $|-\epsilon| = \epsilon < r$, so $-\epsilon \in D_r(0)$, but $-\epsilon \notin f_\epsilon(\mathbb{D})$.
Hence $D_r(0) \not\subseteq f_\epsilon(\mathbb{D})$.

## Part (c)

Let $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots$ be analytic and injective for $0 < |z| < 1$.

We need to show $\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$.

**Proof using the area theorem:**

For $0 < \rho < 1$, consider the image of the annulus $\rho < |z| < 1$ under $h$.
Actually, let's consider $h$ on the circle $|z| = \rho$.

The boundary of $h(\{|z| = \rho\})$ is the curve $h(\rho e^{i\theta})$ for $\theta \in [0, 2\pi)$.
Since $h$ is injective on the punctured disk, this curve is a Jordan curve enclosing a region.

The area enclosed by the image of $|z| = \rho$ under $h$ can be computed as:

$$A(\rho) = \frac{1}{2i} \oint_{|z|=\rho} \overline{h(z)} h'(z) \, dz$$

Let $z = \rho e^{i\theta}$, so $dz = i\rho e^{i\theta} d\theta$.

$h(z) = z^{-1} + c_0 + c_1 z + c_2 z^2 + \cdots$ $h'(z) = -z^{-2} + c_1 + 2c_2 z + 3c_3 z^2 + \cdots$

$\overline{h(z)} = \bar{z}^{-1} + \bar{c}_0 + \bar{c}_1 \bar{z} + \bar{c}_2 \bar{z}^2 + \cdots$

On $|z| = \rho$: $\bar{z} = \rho^2/z$, so $\bar{z}^{-1} = z/\rho^2$ and $\bar{z}^k = \rho^{2k}/z^k$.

$$\overline{h(z)} = \frac{z}{\rho^2} + \bar{c}_0 + \frac{\bar{c}_1 \rho^2}{z} + \frac{\bar{c}_2 \rho^4}{z^2} + \cdots$$

Now: $$\overline{h(z)} h'(z) = \left(\frac{z}{\rho^2} + \bar{c}_0 + \frac{\bar{c}_1 \rho^2}{z} + \frac{\bar{c}_2 \rho^4}{z^2} + \cdots\right)\left(-\frac{1}{z^2} + c_1 + 2c_2 z + 3c_3 z^2 + \cdots\right)$$

The area formula gives: $$A(\rho) = \frac{1}{2i} \oint_{|z|=\rho} \overline{h(z)} h'(z) \, dz$$

We need the coefficient of $z^{-1}$ in $\overline{h(z)} h'(z)$ (since $\oint z^{-1} dz = 2\pi i$, and the area is $\pi$ times the coefficient of $z^{-1}$... let me be more careful).

Actually, the area enclosed is: $$A(\rho) = \frac{1}{2i} \oint \bar{h} h' dz = \frac{1}{2i} \int_0^{2\pi} \overline{h(\rho e^{i\theta})} h'(\rho e^{i\theta}) i\rho e^{i\theta} d\theta$$

Let me use the standard result.
The area of the region bounded by the curve $w = h(\rho e^{i\theta})$ is:

$$A(\rho) = \pi \left(\frac{1}{\rho^2} - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n}\right)$$

Wait, let me derive this more carefully.

The area of the complement of $h(D_\rho(0) \setminus \{0\})$ — actually, let me think about what area we're computing.

For the standard area theorem: Consider $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots$ injective on $0 < |z| < 1$.

The image of the circle $|z| = \rho$ (for $0 < \rho < 1$) is a Jordan curve.
The area of the region enclosed by this curve (counted with multiplicity) is:

$$A(\rho) = \frac{1}{2i} \oint_{|z|=\rho} \overline{h(z)} h'(z) dz$$

Let me compute this.
With $z = \rho e^{i\theta}$:

$h(z) = z^{-1} + \sum_{n=0}^{\infty} c_n z^n$ $h'(z) = -z^{-2} + \sum_{n=1}^{\infty} n c_n z^{n-1}$

$\overline{h(z)} = \bar{z}^{-1} + \sum_{n=0}^{\infty} \bar{c}_n \bar{z}^n = \frac{z}{\rho^2} + \sum_{n=0}^{\infty} \bar{c}_n \frac{\rho^{2n}}{z^n}$

(using $\bar{z} = \rho^2/z$ on $|z| = \rho$)

So: $$\overline{h(z)} h'(z) = \left(\frac{z}{\rho^2} + \sum_{m=0}^{\infty} \bar{c}_m \frac{\rho^{2m}}{z^m}\right)\left(-\frac{1}{z^2} + \sum_{k=1}^{\infty} k c_k z^{k-1}\right)$$

The area is: $$A(\rho) = \frac{1}{2i} \oint_{|z|=\rho} \overline{h(z)} h'(z) dz = \pi \cdot [\text{coefficient of } z^{-1} \text{ in } \overline{h(z)} h'(z)]$$

Wait, $\frac{1}{2i} \oint z^n dz = \frac{1}{2i} \cdot 2\pi i \cdot \delta_{n,-1} = \pi \delta_{n,-1}$.

So $A(\rho) = \pi \cdot [\text{coefficient of } z^{-1} \text{ in } \overline{h(z)} h'(z)]$.

Let me find the coefficient of $z^{-1}$ in $\overline{h(z)} h'(z)$.

From $\frac{z}{\rho^2} \cdot (- \frac{1}{z^2})$: this gives $-\frac{1}{\rho^2} z^{-1}$.
Coefficient: $-1/\rho^2$.

From $\frac{z}{\rho^2} \cdot kc_k z^{k-1}$: this gives $\frac{k c_k}{\rho^2} z^k$.
For $z^{-1}$ we need $k = -1$, impossible.
So no contribution.

From $\bar{c}_m \frac{\rho^{2m}}{z^m} \cdot (-\frac{1}{z^2})$: this gives $-\bar{c}_m \rho^{2m} z^{-(m+2)}$.
For $z^{-1}$ we need $m+2 = 1$, i.e., $m = -1$.
Impossible since $m \geq 0$.

From $\bar{c}_m \frac{\rho^{2m}}{z^m} \cdot k c_k z^{k-1}$: this gives $k \bar{c}_m c_k \rho^{2m} z^{k-1-m}$.
For $z^{-1}$ we need $k - 1 - m = -1$, i.e., $k = m$.
Since $k \geq 1$ and $m \geq 0$, we need $m = k \geq 1$.

So the contribution is $\sum_{k=1}^{\infty} k |c_k|^2 \rho^{2k}$.

Therefore: $$A(\rho) = \pi\left(-\frac{1}{\rho^2} + \sum_{k=1}^{\infty} k|c_k|^2 \rho^{2k}\right)$$

Hmm, but this should be the area enclosed, which should be positive.
Let me reconsider.

Actually, the issue is the orientation.
For $h(z) = 1/z + \cdots$, as $z$ traverses $|z| = \rho$ counterclockwise, $h(z)$ traverses its image... let me think about the winding.

Actually, the standard area theorem states that the area of the complement of the image domain (i.e., the area outside the image of the annulus) is:

$$\text{Area}(\mathbb{C} \setminus h(\{|z| < \rho\} \setminus \{0\})) = \pi\left(\frac{1}{\rho^2} - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n}\right)$$

And this must be $\geq 0$, which gives $\sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} \leq \frac{1}{\rho^2}$.

Wait, but the problem says to compute the area of the complement of $h(D_\rho(0) \setminus \{0\})$ and let $\rho \to 1$.

Actually, let me reconsider.
The complement of $h(D_\rho(0) \setminus \{0\})$ — this is the set of points not in the image of the punctured disk of radius $\rho$.
Since $h$ maps the annulus $\rho < |z| < 1$ injectively to some domain, and also maps $|z| < \rho$ (punctured) injectively...

Hmm, let me think about this differently.
The standard approach:

For $0 < \rho < 1$, consider the image of the circle $|z| = \rho$ under $h$.
This is a Jordan curve $\Gamma_\rho$.
The interior of $\Gamma_\rho$ is the image $h(\{|z| < \rho\} \setminus \{0\})$ (by the argument principle / injectivity).

The area of the interior is: $$\text{Area}(h(\{|z| < \rho\} \setminus \{0\})) = \pi\left(\sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} - \frac{1}{\rho^2}\right)$$

Wait, this would be negative for small $\rho$, which doesn't make sense for an area.

Let me redo the computation more carefully.
The signed area enclosed by the curve $w(\theta) = h(\rho e^{i\theta})$ is:

$$A = \frac{1}{2i} \int_0^{2\pi} \overline{w(\theta)} w'(\theta) d\theta$$

where $w(\theta) = h(\rho e^{i\theta})$ and $w'(\theta) = h'(\rho e^{i\theta}) \cdot i\rho e^{i\theta}$.

So $A = \frac{1}{2i} \int_0^{2\pi} \overline{h(\rho e^{i\theta})} h'(\rho e^{i\theta}) i\rho e^{i\theta} d\theta = \frac{1}{2} \int_0^{2\pi} \overline{h} h' \rho e^{i\theta} d\theta$

Alternatively, in complex form: $$A = \frac{1}{2i} \oint_{|z|=\rho} \overline{h(z)} h'(z) dz$$

Let me recompute.
On $|z| = \rho$, with $z = \rho e^{i\theta}$:

$h(z) = z^{-1} + c_0 + c_1 z + c_2 z^2 + \cdots$

$\overline{h(z)} = \overline{z}^{-1} + \bar{c}_0 + \bar{c}_1 \bar{z} + \bar{c}_2 \bar{z}^2 + \cdots$

On $|z| = \rho$: $\bar{z} = \rho^2/z$, so $\bar{z}^{-1} = z/\rho^2$.

$\overline{h(z)} = z/\rho^2 + \bar{c}_0 + \bar{c}_1 \rho^2/z + \bar{c}_2 \rho^4/z^2 + \cdots$

$h'(z) = -1/z^2 + c_1 + 2c_2 z + 3c_3 z^2 + \cdots$

Product $\overline{h(z)} \cdot h'(z)$:

The $z^{-1}$ coefficient:

- From $(z/\rho^2) \times (-1/z^2) = -1/(\rho^2 z)$: coefficient $-1/\rho^2$.

- From $(\bar{c}_m \rho^{2m}/z^m) \times (k c_k z^{k-1})$ where $k-m = -1$, i.e., $m = k+1$: but $m \geq 0$ and $k \geq 1$, so $m \geq 2$.
  Wait, we need the power of $z$ to be $-1$: $k - 1 - m = -1$, so $k = m$.
  With $k \geq 1, m \geq 0$: $m = k \geq 1$.
  Contribution: $k \bar{c}_k c_k \rho^{2k} = k|c_k|^2 \rho^{2k}$.

So the coefficient of $z^{-1}$ in $\overline{h(z)} h'(z)$ is $-1/\rho^2 + \sum_{k=1}^{\infty} k|c_k|^2 \rho^{2k}$.

Therefore: $$A(\rho) = \frac{1}{2i} \oint_{|z|=\rho} \overline{h(z)} h'(z) dz = \pi \left(-\frac{1}{\rho^2} + \sum_{k=1}^{\infty} k|c_k|^2 \rho^{2k}\right)$$

Now, for small $\rho$, the term $-1/\rho^2$ dominates, so $A(\rho) < 0$.
This means the curve is traversed clockwise (negative orientation), so the actual enclosed area is:

$$|A(\rho)| = \pi \left(\frac{1}{\rho^2} - \sum_{k=1}^{\infty} k|c_k|^2 \rho^{2k}\right)$$

The complement of $h(D_\rho(0) \setminus \{0\})$ — since $h$ maps the punctured disk injectively, the image $h(D_\rho(0) \setminus \{0\})$ is a domain whose boundary is $\Gamma_\rho$.
The complement of this domain in $\mathbb{C}$ has area:

Actually, I think the problem is asking for the area of $\mathbb{C} \setminus h(D_\rho(0) \setminus \{0\})$.
Since $h(D_\rho(0) \setminus \{0\})$ is the interior of $\Gamma_\rho$ (for small enough $\rho$), the complement is the exterior, which has infinite area.
That doesn't work either.

Let me reconsider.
Perhaps the problem means: the area of the complement of the image within some bounded region, or perhaps it's the area formula applied differently.

Actually, I think the standard approach for the area theorem is:

The area of the image $h(\{|z| = \rho\})$ counted with multiplicity gives us:

The signed area enclosed by the image curve is $\pi(-1/\rho^2 + \sum n|c_n|^2 \rho^{2n})$, which is negative for small $\rho$.
The negative sign indicates the curve is traversed clockwise.
The actual area enclosed is $\pi(1/\rho^2 - \sum n|c_n|^2 \rho^{2n})$.

Since $h$ is injective, this area is non-negative (it's the area of a genuine region).
So:

$$\pi\left(\frac{1}{\rho^2} - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n}\right) \geq 0$$

This gives $\sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} \leq \frac{1}{\rho^2}$.

As $\rho \to 1^-$: $\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$.

This is the desired result.

Actually wait, I need to be more careful about what "complement" means.
Let me re-read the hint: "Calculate the area of the complement of $h(D_\rho(0) \setminus \{0\})$ where $0 < \rho < 1$."

I think this means: $h$ maps the annulus $\{0 < |z| < \rho\}$ (or $\{0 < |z| < 1\}$ restricted to $|z| < \rho$) to some domain.
The complement of this image domain...

Actually, I think the correct interpretation is: Consider the image of $\{z : 0 < |z| < \rho\}$ under $h$.
This is a simply connected domain (since $h$ is injective there).
Its complement in $\hat{\mathbb{C}}$ (the Riemann sphere) has area $4\pi - \text{area of image}$... no, that's not right either.

Let me just use the standard area theorem approach.
The key computation is:

For the Jordan curve $\Gamma_\rho = h(\{|z| = \rho\})$, the area enclosed (which equals the area of $h(\{|z| < \rho\} \setminus \{0\})$ by injectivity and the argument principle) is:

$$\text{Area} = \pi\left(\frac{1}{\rho^2} - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n}\right) \geq 0$$

The non-negativity follows because this is the area of a genuine region (the image of a domain under an injective map).

Therefore $\sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} \leq 1/\rho^2$ for all $0 < \rho < 1$.

Taking $\rho \to 1^-$ (by monotone convergence or just termwise limit since all terms are positive):

$$\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$$

## Part (d)

Given $f(z) = z + a_2 z^2 + a_3 z^3 + \cdots$ injective in $\mathbb{D}$ with $f(0) = 0$, $f'(0) = 1$.

**Step 1:** $f(z)/z = 1 + a_2 z + a_3 z^2 + \cdots$ is holomorphic in $\mathbb{D}$.

$f(z)/z$ is nonzero in $\mathbb{D}$: At $z = 0$, $f(z)/z \to f'(0) = 1 \neq 0$.
For $z \neq 0$, if $f(z)/z = 0$ then $f(z) = 0 = f(0)$, contradicting injectivity.

**Step 2:** Since $f(z)/z$ is holomorphic and nowhere vanishing on the simply connected domain $\mathbb{D}$, it has a holomorphic square root $\psi(z)$ with $\psi(0) = 1$ (normalizing the branch).

**Step 3:** Define $g(z) = z\psi(z^2)$.
Then: $$g(z)^2 = z^2 \psi(z^2)^2 = z^2 \cdot \frac{f(z^2)}{z^2} = f(z^2)$$

**Step 4:** $g(0) = 0$ and $g'(0) = \psi(0) = 1$.

**Step 5:** $g$ is injective.

First, note that $g(-z) = -z\psi((-z)^2) = -z\psi(z^2) = -g(z)$, so $g$ is odd.

If $g(z_1) = g(z_2)$, then $g(z_1)^2 = g(z_2)^2$, so $f(z_1^2) = f(z_2^2)$.
Since $f$ is injective, $z_1^2 = z_2^2$, meaning $z_1 = \pm z_2$.

If $z_1 = -z_2$, then $g(z_1) = g(-z_2) = -g(z_2)$.
But $g(z_1) = g(z_2)$, so $g(z_2) = -g(z_2)$, implying $g(z_2) = 0$.
Since $g(z) = z\psi(z^2)$ and $\psi(z^2) \neq 0$ (because $\psi(0) = 1$ and $\psi$ is continuous, and actually $\psi(z^2) = \sqrt{f(z^2)/z^2}$ which is nonzero since $f$ is injective), we get $z_2 = 0$, hence $z_1 = 0 = z_2$.

So $z_1 = z_2$, and $g$ is injective.

## Part (e)

We have $g(z) = z\psi(z^2)$ where $\psi(z) = \sqrt{f(z)/z}$ with $\psi(0) = 1$.

**Step 1:** Expand $g$.
Since $\psi(z) = 1 + \frac{a_2}{2}z + \frac{1}{2}(a_3 - \frac{a_2^2}{4})z^2 + \cdots$ (from squaring $\psi^2 = f(z)/z = 1 + a_2 z + a_3 z^2 + \cdots$):

Wait, let me be more careful.
$\psi(z)^2 = f(z)/z = 1 + a_2 z + a_3 z^2 + \cdots$

If $\psi(z) = 1 + b_1 z + b_2 z^2 + \cdots$, then: $\psi(z)^2 = 1 + 2b_1 z + (b_1^2 + 2b_2) z^2 + \cdots$

So $2b_1 = a_2$, giving $b_1 = a_2/2$.

Then $g(z) = z\psi(z^2) = z(1 + b_1 z^2 + b_2 z^4 + \cdots) = z + b_1 z^3 + b_2 z^5 + \cdots$

So $g(z) = z + \frac{a_2}{2} z^3 + \cdots$ (only odd powers).

**Step 2:** Consider $1/g(z)$.
Since $g$ has a simple zero at 0: $$\frac{1}{g(z)} = \frac{1}{z} + d_0 + d_1 z + d_2 z^2 + \cdots$$

Since $g$ is odd ($g(z) = z + c_3 z^3 + c_5 z^5 + \cdots$), $1/g$ is also odd (since $1/g(-z) = 1/(-g(z)) = -1/g(z)$). So $d_0 = 0$, $d_2 = 0$, etc. Only odd powers appear.

$1/g(z) = 1/z + d_1 z + d_3 z^3 + \cdots$

From $g(z) = z + \frac{a_2}{2}z^3 + \cdots$: $$\frac{1}{g(z)} = \frac{1}{z(1 + \frac{a_2}{2}z^2 + \cdots)} = \frac{1}{z}(1 - \frac{a_2}{2}z^2 + \cdots) = \frac{1}{z} - \frac{a_2}{2}z + \cdots$$

So $d_1 = -a_2/2$.

**Step 3:** Apply part (c) to $1/g(z)$.
The function $g$ satisfies the hypotheses of the Koebe theorem (injective, $g(0) = 0$, $g'(0) = 1$), so $1/g$ has the form $1/z + d_0 + d_1 z + \cdots$ with $d_0 = 0$ and is injective on $\mathbb{D} \setminus \{0\}$ (actually on $0 < |z| < 1$, since $g$ maps $\mathbb{D}$ injectively and $g(0) = 0$, so $1/g$ is injective on $\mathbb{D} \setminus \{0\}$).

Wait, actually $1/g$ is defined and injective on $\mathbb{D} \setminus \{0\}$ since $g$ is injective on $\mathbb{D}$ and $g(0) = 0$.

But we need $1/g$ to be injective on $0 < |z| < 1$.
Since $g$ is injective on $\mathbb{D}$ and $g(z) \neq 0$ for $z \neq 0$ (because $g$ is injective and $g(0) = 0$), $1/g$ is indeed injective on $\mathbb{D} \setminus \{0\}$.

By part (c) applied to $h(z) = 1/g(z) = 1/z + d_1 z + \cdots$ (with $c_0 = d_0 = 0$, $c_1 = d_1$, etc.):

$$\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$$

In particular, $1 \cdot |d_1|^2 \leq 1$, so $|d_1| \leq 1$.

Since $d_1 = -a_2/2$, we get $|a_2|/2 \leq 1$, i.e., $|a_2| \leq 2$.

**Equality case:** $|a_2| = 2$ iff $|d_1| = 1$ iff equality holds in part (c).

Equality in the area theorem (part c) means that $\sum_{n=1}^{\infty} n|c_n|^2 = 1$ with all the constraint concentrated on $n=1$ (since $|c_1| = 1$ already uses up the full budget).
So $c_n = 0$ for all $n \geq 2$, meaning $1/g(z) = 1/z + e^{i\theta} z$ for some $\theta$.

Then $g(z) = \frac{z}{1 + e^{i\theta} z^2}$, and: $$f(z^2) = g(z)^2 = \frac{z^2}{(1 + e^{i\theta} z^2)^2}$$

Setting $w = z^2$: $f(w) = \frac{w}{(1 + e^{i\theta} w)^2}$.

So $f(z) = \frac{z}{(1 + e^{i\theta} z)^2}$.

## Part (f)

Let $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots$ be injective on $\mathbb{D}$ (actually on $0 < |z| < 1$, but let's say it extends to be injective on $\mathbb{D} \setminus \{0\}$) and avoids values $z_1$ and $z_2$.

Consider $\phi_j(z) = \frac{1}{h(z) - z_j}$ for $j = 1, 2$.

Since $h$ avoids $z_j$, $h(z) - z_j \neq 0$ for all $z \in \mathbb{D} \setminus \{0\}$.
Also, $h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + \cdots$ has a simple pole at 0.

So $\phi_j(z)$ is holomorphic and nonzero on $\mathbb{D} \setminus \{0\}$, with a simple zero at 0 (since $h(z) - z_j \sim 1/z$ near 0, so $\phi_j(z) \sim z$ near 0).

Wait, let me reconsider.
$h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + \cdots$.
Near $z = 0$, $h(z) - z_j \approx 1/z$, so $\phi_j(z) = 1/(h(z) - z_j) \approx z$ near 0.

So $\phi_j$ has a removable singularity at 0 with $\phi_j(0) = 0$, and $\phi_j'(0) = 1$.

Is $\phi_j$ injective?
If $\phi_j(z_1) = \phi_j(z_2)$, then $h(z_1) - z_j = h(z_2) - z_j$, so $h(z_1) = h(z_2)$.
Since $h$ is injective, $z_1 = z_2$.
Yes, $\phi_j$ is injective.

So $\phi_j$ satisfies the hypotheses of the theorem (injective, $\phi_j(0) = 0$, $\phi_j'(0) = 1$).

Now, $\phi_j(z) = \frac{1}{h(z) - z_j} = \frac{1}{1/z + (c_0 - z_j) + c_1 z + \cdots} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$

So $\phi_j(z) = z \cdot \frac{1}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots} = z(1 - (c_0 - z_j)z + \cdots) = z - (c_0 - z_j)z^2 + \cdots$

So $\phi_j(z) = z + (\text{something})z^2 + \cdots$

The coefficient of $z^2$ in $\phi_j$ is $-(c_0 - z_j) = z_j - c_0$.

By part (e), $|\text{coefficient of } z^2| \leq 2$, so $|z_j - c_0| \leq 2$ for each $j$.

Therefore: $|z_1 - z_2| = |(z_1 - c_0) - (z_2 - c_0)| \leq |z_1 - c_0| + |z_2 - c_0| \leq 2 + 2 = 4$.

## Part (g)

Let $f : \mathbb{D} \to \mathbb{C}$ be injective with $f(0) = 0$ and $f'(0) = 1$.
We want to show $D_{1/4}(0) \subseteq f(\mathbb{D})$.

**Proof by contradiction:** Suppose there exists $w$ with $|w| < 1/4$ such that $w \notin f(\mathbb{D})$.

Since $f$ is injective and $f(0) = 0$, we have $f(z) \neq 0$ for all $z \neq 0$ in $\mathbb{D}$.
So $0 \notin f(\mathbb{D} \setminus \{0\})$.

Consider $h(z) = 1/f(z)$, defined on $\mathbb{D} \setminus \{0\}$.

- $h$ has a simple pole at 0 (since $f$ has a simple zero at 0).

- $h$ is injective on $\mathbb{D} \setminus \{0\}$ (since $f$ is injective and the map $w \mapsto 1/w$ is injective on $\mathbb{C} \setminus \{0\}$).

- $h$ avoids the value 0 (since $1/f(z) = 0$ has no solution).

- $h$ avoids the value $1/w$ (since $f$ avoids $w$).

So $h$ is injective on $0 < |z| < 1$ with Laurent expansion $h(z) = 1/z + c_0 + c_1 z + \cdots$ and avoids $z_1 = 0$ and $z_2 = 1/w$.

By part (f): $|z_1 - z_2| \leq 4$, i.e., $|0 - 1/w| \leq 4$, i.e., $1/|w| \leq 4$, i.e., $|w| \geq 1/4$.

This contradicts $|w| < 1/4$.

Therefore, $D_{1/

* * *

## Model Solution

None

* * *

## Reasoning Details (raw)

```json
[
  {
    "type": "reasoning.text",
    "text": "Let me work through each part (a) through (g) carefully and completely.\n\n## Part (a)\n\nWe need to show that without further restrictions on $f$ (beyond holomorphicity on $\\mathbb{D}$ and $f(0) = 0$), there is no $r > 0$ such that $D_r(0) \\subseteq f(\\mathbb{D})$ for all such $f$.\n\nThe hint suggests finding $f_n$ with $f_n(0) = 0$ and $1/n \\notin f_n(\\mathbb{D})$.\n\nTake $f_n(z) = z/n$. Then:\n- $f_n(0) = 0$ \u2713\n- $f_n(\\mathbb{D}) = \\{z/n : |z| < 1\\} = D_{1/n}(0)$, the open disk of radius $1/n$ centered at 0.\n- $1/n \\notin D_{1/n}(0)$ since $|1/n| = 1/n$ and the disk is open (points have modulus strictly less than $1/n$).\n\nSo $1/n \\notin f_n(\\mathbb{D})$.\n\n$f_n'(0) = 1/n \\to 0$ as $n \\to \\infty$.\n\nFor any $r > 0$, choose $n$ large enough so that $1/n < r$. Then $1/n \\in D_r(0)$ but $1/n \\notin f_n(\\mathbb{D})$, so $D_r(0) \\not\\subseteq f_n(\\mathbb{D})$.\n\n## Part (b)\n\nNow assume $f'(0) = 1$. Consider $f_\\epsilon(z) = \\epsilon(e^{z/\\epsilon} - 1)$ for $\\epsilon > 0$.\n\n- $f_\\epsilon(0) = \\epsilon(e^0 - 1) = 0$ \u2713\n- $f_\\epsilon'(z) = \\epsilon \\cdot (1/\\epsilon) e^{z/\\epsilon} = e^{z/\\epsilon}$, so $f_\\epsilon'(0) = 1$ \u2713\n- $f_\\epsilon$ is holomorphic on all of $\\mathbb{C}$, hence on $\\mathbb{D}$.\n\nThe image: $f_\\epsilon(z) = \\epsilon(e^{z/\\epsilon} - 1)$. Since $e^{z/\\epsilon} \\neq 0$ for all $z \\in \\mathbb{C}$, we have $f_\\epsilon(z) \\neq \\epsilon(0 - 1) = -\\epsilon$.\n\nSo $-\\epsilon \\notin f_\\epsilon(\\mathbb{D})$.\n\nFor any $r > 0$, choose $\\epsilon < r$. Then $|-\\epsilon| = \\epsilon < r$, so $-\\epsilon \\in D_r(0)$, but $-\\epsilon \\notin f_\\epsilon(\\mathbb{D})$. Hence $D_r(0) \\not\\subseteq f_\\epsilon(\\mathbb{D})$.\n\n## Part (c)\n\nLet $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ be analytic and injective for $0 < |z| < 1$.\n\nWe need to show $\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$.\n\n**Proof using the area theorem:**\n\nFor $0 < \\rho < 1$, consider the image of the annulus $\\rho < |z| < 1$ under $h$. Actually, let's consider $h$ on the circle $|z| = \\rho$.\n\nThe boundary of $h(\\{|z| = \\rho\\})$ is the curve $h(\\rho e^{i\\theta})$ for $\\theta \\in [0, 2\\pi)$. Since $h$ is injective on the punctured disk, this curve is a Jordan curve enclosing a region.\n\nThe area enclosed by the image of $|z| = \\rho$ under $h$ can be computed as:\n\n$$A(\\rho) = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) \\, dz$$\n\nLet $z = \\rho e^{i\\theta}$, so $dz = i\\rho e^{i\\theta} d\\theta$.\n\n$h(z) = z^{-1} + c_0 + c_1 z + c_2 z^2 + \\cdots$\n$h'(z) = -z^{-2} + c_1 + 2c_2 z + 3c_3 z^2 + \\cdots$\n\n$\\overline{h(z)} = \\bar{z}^{-1} + \\bar{c}_0 + \\bar{c}_1 \\bar{z} + \\bar{c}_2 \\bar{z}^2 + \\cdots$\n\nOn $|z| = \\rho$: $\\bar{z} = \\rho^2/z$, so $\\bar{z}^{-1} = z/\\rho^2$ and $\\bar{z}^k = \\rho^{2k}/z^k$.\n\n$$\\overline{h(z)} = \\frac{z}{\\rho^2} + \\bar{c}_0 + \\frac{\\bar{c}_1 \\rho^2}{z} + \\frac{\\bar{c}_2 \\rho^4}{z^2} + \\cdots$$\n\nNow:\n$$\\overline{h(z)} h'(z) = \\left(\\frac{z}{\\rho^2} + \\bar{c}_0 + \\frac{\\bar{c}_1 \\rho^2}{z} + \\frac{\\bar{c}_2 \\rho^4}{z^2} + \\cdots\\right)\\left(-\\frac{1}{z^2} + c_1 + 2c_2 z + 3c_3 z^2 + \\cdots\\right)$$\n\nThe area formula gives:\n$$A(\\rho) = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) \\, dz$$\n\nWe need the coefficient of $z^{-1}$ in $\\overline{h(z)} h'(z)$ (since $\\oint z^{-1} dz = 2\\pi i$, and the area is $\\pi$ times the coefficient of $z^{-1}$... let me be more careful).\n\nActually, the area enclosed is:\n$$A(\\rho) = \\frac{1}{2i} \\oint \\bar{h} h' dz = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{h(\\rho e^{i\\theta})} h'(\\rho e^{i\\theta}) i\\rho e^{i\\theta} d\\theta$$\n\nLet me use the standard result. The area of the region bounded by the curve $w = h(\\rho e^{i\\theta})$ is:\n\n$$A(\\rho) = \\pi \\left(\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right)$$\n\nWait, let me derive this more carefully.\n\nThe area of the complement of $h(D_\\rho(0) \\setminus \\{0\\})$ \u2014 actually, let me think about what area we're computing.\n\nFor the standard area theorem: Consider $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ injective on $0 < |z| < 1$.\n\nThe image of the circle $|z| = \\rho$ (for $0 < \\rho < 1$) is a Jordan curve. The area of the region enclosed by this curve (counted with multiplicity) is:\n\n$$A(\\rho) = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) dz$$\n\nLet me compute this. With $z = \\rho e^{i\\theta}$:\n\n$h(z) = z^{-1} + \\sum_{n=0}^{\\infty} c_n z^n$\n$h'(z) = -z^{-2} + \\sum_{n=1}^{\\infty} n c_n z^{n-1}$\n\n$\\overline{h(z)} = \\bar{z}^{-1} + \\sum_{n=0}^{\\infty} \\bar{c}_n \\bar{z}^n = \\frac{z}{\\rho^2} + \\sum_{n=0}^{\\infty} \\bar{c}_n \\frac{\\rho^{2n}}{z^n}$\n\n(using $\\bar{z} = \\rho^2/z$ on $|z| = \\rho$)\n\nSo:\n$$\\overline{h(z)} h'(z) = \\left(\\frac{z}{\\rho^2} + \\sum_{m=0}^{\\infty} \\bar{c}_m \\frac{\\rho^{2m}}{z^m}\\right)\\left(-\\frac{1}{z^2} + \\sum_{k=1}^{\\infty} k c_k z^{k-1}\\right)$$\n\nThe area is:\n$$A(\\rho) = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) dz = \\pi \\cdot [\\text{coefficient of } z^{-1} \\text{ in } \\overline{h(z)} h'(z)]$$\n\nWait, $\\frac{1}{2i} \\oint z^n dz = \\frac{1}{2i} \\cdot 2\\pi i \\cdot \\delta_{n,-1} = \\pi \\delta_{n,-1}$.\n\nSo $A(\\rho) = \\pi \\cdot [\\text{coefficient of } z^{-1} \\text{ in } \\overline{h(z)} h'(z)]$.\n\nLet me find the coefficient of $z^{-1}$ in $\\overline{h(z)} h'(z)$.\n\nFrom $\\frac{z}{\\rho^2} \\cdot (- \\frac{1}{z^2})$: this gives $-\\frac{1}{\\rho^2} z^{-1}$. Coefficient: $-1/\\rho^2$.\n\nFrom $\\frac{z}{\\rho^2} \\cdot kc_k z^{k-1}$: this gives $\\frac{k c_k}{\\rho^2} z^k$. For $z^{-1}$ we need $k = -1$, impossible. So no contribution.\n\nFrom $\\bar{c}_m \\frac{\\rho^{2m}}{z^m} \\cdot (-\\frac{1}{z^2})$: this gives $-\\bar{c}_m \\rho^{2m} z^{-(m+2)}$. For $z^{-1}$ we need $m+2 = 1$, i.e., $m = -1$. Impossible since $m \\geq 0$.\n\nFrom $\\bar{c}_m \\frac{\\rho^{2m}}{z^m} \\cdot k c_k z^{k-1}$: this gives $k \\bar{c}_m c_k \\rho^{2m} z^{k-1-m}$. For $z^{-1}$ we need $k - 1 - m = -1$, i.e., $k = m$. Since $k \\geq 1$ and $m \\geq 0$, we need $m = k \\geq 1$.\n\nSo the contribution is $\\sum_{k=1}^{\\infty} k |c_k|^2 \\rho^{2k}$.\n\nTherefore:\n$$A(\\rho) = \\pi\\left(-\\frac{1}{\\rho^2} + \\sum_{k=1}^{\\infty} k|c_k|^2 \\rho^{2k}\\right)$$\n\nHmm, but this should be the area enclosed, which should be positive. Let me reconsider.\n\nActually, the issue is the orientation. For $h(z) = 1/z + \\cdots$, as $z$ traverses $|z| = \\rho$ counterclockwise, $h(z)$ traverses its image... let me think about the winding.\n\nActually, the standard area theorem states that the area of the complement of the image domain (i.e., the area outside the image of the annulus) is:\n\n$$\\text{Area}(\\mathbb{C} \\setminus h(\\{|z| < \\rho\\} \\setminus \\{0\\})) = \\pi\\left(\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right)$$\n\nAnd this must be $\\geq 0$, which gives $\\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\leq \\frac{1}{\\rho^2}$.\n\nWait, but the problem says to compute the area of the complement of $h(D_\\rho(0) \\setminus \\{0\\})$ and let $\\rho \\to 1$.\n\nActually, let me reconsider. The complement of $h(D_\\rho(0) \\setminus \\{0\\})$ \u2014 this is the set of points not in the image of the punctured disk of radius $\\rho$. Since $h$ maps the annulus $\\rho < |z| < 1$ injectively to some domain, and also maps $|z| < \\rho$ (punctured) injectively...\n\nHmm, let me think about this differently. The standard approach:\n\nFor $0 < \\rho < 1$, consider the image of the circle $|z| = \\rho$ under $h$. This is a Jordan curve $\\Gamma_\\rho$. The interior of $\\Gamma_\\rho$ is the image $h(\\{|z| < \\rho\\} \\setminus \\{0\\})$ (by the argument principle / injectivity).\n\nThe area of the interior is:\n$$\\text{Area}(h(\\{|z| < \\rho\\} \\setminus \\{0\\})) = \\pi\\left(\\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} - \\frac{1}{\\rho^2}\\right)$$\n\nWait, this would be negative for small $\\rho$, which doesn't make sense for an area.\n\nLet me redo the computation more carefully. The signed area enclosed by the curve $w(\\theta) = h(\\rho e^{i\\theta})$ is:\n\n$$A = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{w(\\theta)} w'(\\theta) d\\theta$$\n\nwhere $w(\\theta) = h(\\rho e^{i\\theta})$ and $w'(\\theta) = h'(\\rho e^{i\\theta}) \\cdot i\\rho e^{i\\theta}$.\n\nSo $A = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{h(\\rho e^{i\\theta})} h'(\\rho e^{i\\theta}) i\\rho e^{i\\theta} d\\theta = \\frac{1}{2} \\int_0^{2\\pi} \\overline{h} h' \\rho e^{i\\theta} d\\theta$\n\nAlternatively, in complex form:\n$$A = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) dz$$\n\nLet me recompute. On $|z| = \\rho$, with $z = \\rho e^{i\\theta}$:\n\n$h(z) = z^{-1} + c_0 + c_1 z + c_2 z^2 + \\cdots$\n\n$\\overline{h(z)} = \\overline{z}^{-1} + \\bar{c}_0 + \\bar{c}_1 \\bar{z} + \\bar{c}_2 \\bar{z}^2 + \\cdots$\n\nOn $|z| = \\rho$: $\\bar{z} = \\rho^2/z$, so $\\bar{z}^{-1} = z/\\rho^2$.\n\n$\\overline{h(z)} = z/\\rho^2 + \\bar{c}_0 + \\bar{c}_1 \\rho^2/z + \\bar{c}_2 \\rho^4/z^2 + \\cdots$\n\n$h'(z) = -1/z^2 + c_1 + 2c_2 z + 3c_3 z^2 + \\cdots$\n\nProduct $\\overline{h(z)} \\cdot h'(z)$:\n\nThe $z^{-1}$ coefficient:\n- From $(z/\\rho^2) \\times (-1/z^2) = -1/(\\rho^2 z)$: coefficient $-1/\\rho^2$.\n- From $(\\bar{c}_m \\rho^{2m}/z^m) \\times (k c_k z^{k-1})$ where $k-m = -1$, i.e., $m = k+1$: but $m \\geq 0$ and $k \\geq 1$, so $m \\geq 2$. Wait, we need the power of $z$ to be $-1$: $k - 1 - m = -1$, so $k = m$. With $k \\geq 1, m \\geq 0$: $m = k \\geq 1$. Contribution: $k \\bar{c}_k c_k \\rho^{2k} = k|c_k|^2 \\rho^{2k}$.\n\nSo the coefficient of $z^{-1}$ in $\\overline{h(z)} h'(z)$ is $-1/\\rho^2 + \\sum_{k=1}^{\\infty} k|c_k|^2 \\rho^{2k}$.\n\nTherefore:\n$$A(\\rho) = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) dz = \\pi \\left(-\\frac{1}{\\rho^2} + \\sum_{k=1}^{\\infty} k|c_k|^2 \\rho^{2k}\\right)$$\n\nNow, for small $\\rho$, the term $-1/\\rho^2$ dominates, so $A(\\rho) < 0$. This means the curve is traversed clockwise (negative orientation), so the actual enclosed area is:\n\n$$|A(\\rho)| = \\pi \\left(\\frac{1}{\\rho^2} - \\sum_{k=1}^{\\infty} k|c_k|^2 \\rho^{2k}\\right)$$\n\nThe complement of $h(D_\\rho(0) \\setminus \\{0\\})$ \u2014 since $h$ maps the punctured disk injectively, the image $h(D_\\rho(0) \\setminus \\{0\\})$ is a domain whose boundary is $\\Gamma_\\rho$. The complement of this domain in $\\mathbb{C}$ has area:\n\nActually, I think the problem is asking for the area of $\\mathbb{C} \\setminus h(D_\\rho(0) \\setminus \\{0\\})$. Since $h(D_\\rho(0) \\setminus \\{0\\})$ is the interior of $\\Gamma_\\rho$ (for small enough $\\rho$), the complement is the exterior, which has infinite area. That doesn't work either.\n\nLet me reconsider. Perhaps the problem means: the area of the complement of the image within some bounded region, or perhaps it's the area formula applied differently.\n\nActually, I think the standard approach for the area theorem is:\n\nThe area of the image $h(\\{|z| = \\rho\\})$ counted with multiplicity gives us:\n\nThe signed area enclosed by the image curve is $\\pi(-1/\\rho^2 + \\sum n|c_n|^2 \\rho^{2n})$, which is negative for small $\\rho$. The negative sign indicates the curve is traversed clockwise. The actual area enclosed is $\\pi(1/\\rho^2 - \\sum n|c_n|^2 \\rho^{2n})$.\n\nSince $h$ is injective, this area is non-negative (it's the area of a genuine region). So:\n\n$$\\pi\\left(\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right) \\geq 0$$\n\nThis gives $\\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\leq \\frac{1}{\\rho^2}$.\n\nAs $\\rho \\to 1^-$: $\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$.\n\nThis is the desired result.\n\nActually wait, I need to be more careful about what \"complement\" means. Let me re-read the hint: \"Calculate the area of the complement of $h(D_\\rho(0) \\setminus \\{0\\})$ where $0 < \\rho < 1$.\"\n\nI think this means: $h$ maps the annulus $\\{0 < |z| < \\rho\\}$ (or $\\{0 < |z| < 1\\}$ restricted to $|z| < \\rho$) to some domain. The complement of this image domain...\n\nActually, I think the correct interpretation is: Consider the image of $\\{z : 0 < |z| < \\rho\\}$ under $h$. This is a simply connected domain (since $h$ is injective there). Its complement in $\\hat{\\mathbb{C}}$ (the Riemann sphere) has area $4\\pi - \\text{area of image}$... no, that's not right either.\n\nLet me just use the standard area theorem approach. The key computation is:\n\nFor the Jordan curve $\\Gamma_\\rho = h(\\{|z| = \\rho\\})$, the area enclosed (which equals the area of $h(\\{|z| < \\rho\\} \\setminus \\{0\\})$ by injectivity and the argument principle) is:\n\n$$\\text{Area} = \\pi\\left(\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right) \\geq 0$$\n\nThe non-negativity follows because this is the area of a genuine region (the image of a domain under an injective map).\n\nTherefore $\\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\leq 1/\\rho^2$ for all $0 < \\rho < 1$.\n\nTaking $\\rho \\to 1^-$ (by monotone convergence or just termwise limit since all terms are positive):\n\n$$\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$$\n\n## Part (d)\n\nGiven $f(z) = z + a_2 z^2 + a_3 z^3 + \\cdots$ injective in $\\mathbb{D}$ with $f(0) = 0$, $f'(0) = 1$.\n\n**Step 1:** $f(z)/z = 1 + a_2 z + a_3 z^2 + \\cdots$ is holomorphic in $\\mathbb{D}$.\n\n$f(z)/z$ is nonzero in $\\mathbb{D}$: At $z = 0$, $f(z)/z \\to f'(0) = 1 \\neq 0$. For $z \\neq 0$, if $f(z)/z = 0$ then $f(z) = 0 = f(0)$, contradicting injectivity.\n\n**Step 2:** Since $f(z)/z$ is holomorphic and nowhere vanishing on the simply connected domain $\\mathbb{D}$, it has a holomorphic square root $\\psi(z)$ with $\\psi(0) = 1$ (normalizing the branch).\n\n**Step 3:** Define $g(z) = z\\psi(z^2)$. Then:\n$$g(z)^2 = z^2 \\psi(z^2)^2 = z^2 \\cdot \\frac{f(z^2)}{z^2} = f(z^2)$$\n\n**Step 4:** $g(0) = 0$ and $g'(0) = \\psi(0) = 1$.\n\n**Step 5:** $g$ is injective. \n\nFirst, note that $g(-z) = -z\\psi((-z)^2) = -z\\psi(z^2) = -g(z)$, so $g$ is odd.\n\nIf $g(z_1) = g(z_2)$, then $g(z_1)^2 = g(z_2)^2$, so $f(z_1^2) = f(z_2^2)$. Since $f$ is injective, $z_1^2 = z_2^2$, meaning $z_1 = \\pm z_2$.\n\nIf $z_1 = -z_2$, then $g(z_1) = g(-z_2) = -g(z_2)$. But $g(z_1) = g(z_2)$, so $g(z_2) = -g(z_2)$, implying $g(z_2) = 0$. Since $g(z) = z\\psi(z^2)$ and $\\psi(z^2) \\neq 0$ (because $\\psi(0) = 1$ and $\\psi$ is continuous, and actually $\\psi(z^2) = \\sqrt{f(z^2)/z^2}$ which is nonzero since $f$ is injective), we get $z_2 = 0$, hence $z_1 = 0 = z_2$.\n\nSo $z_1 = z_2$, and $g$ is injective.\n\n## Part (e)\n\nWe have $g(z) = z\\psi(z^2)$ where $\\psi(z) = \\sqrt{f(z)/z}$ with $\\psi(0) = 1$.\n\n**Step 1:** Expand $g$. Since $\\psi(z) = 1 + \\frac{a_2}{2}z + \\frac{1}{2}(a_3 - \\frac{a_2^2}{4})z^2 + \\cdots$ (from squaring $\\psi^2 = f(z)/z = 1 + a_2 z + a_3 z^2 + \\cdots$):\n\nWait, let me be more careful. $\\psi(z)^2 = f(z)/z = 1 + a_2 z + a_3 z^2 + \\cdots$\n\nIf $\\psi(z) = 1 + b_1 z + b_2 z^2 + \\cdots$, then:\n$\\psi(z)^2 = 1 + 2b_1 z + (b_1^2 + 2b_2) z^2 + \\cdots$\n\nSo $2b_1 = a_2$, giving $b_1 = a_2/2$.\n\nThen $g(z) = z\\psi(z^2) = z(1 + b_1 z^2 + b_2 z^4 + \\cdots) = z + b_1 z^3 + b_2 z^5 + \\cdots$\n\nSo $g(z) = z + \\frac{a_2}{2} z^3 + \\cdots$ (only odd powers).\n\n**Step 2:** Consider $1/g(z)$. Since $g$ has a simple zero at 0:\n$$\\frac{1}{g(z)} = \\frac{1}{z} + d_0 + d_1 z + d_2 z^2 + \\cdots$$\n\nSince $g$ is odd ($g(z) = z + c_3 z^3 + c_5 z^5 + \\cdots$), $1/g$ is also odd (since $1/g(-z) = 1/(-g(z)) = -1/g(z)$). So $d_0 = 0$, $d_2 = 0$, etc. Only odd powers appear.\n\n$1/g(z) = 1/z + d_1 z + d_3 z^3 + \\cdots$\n\nFrom $g(z) = z + \\frac{a_2}{2}z^3 + \\cdots$:\n$$\\frac{1}{g(z)} = \\frac{1}{z(1 + \\frac{a_2}{2}z^2 + \\cdots)} = \\frac{1}{z}(1 - \\frac{a_2}{2}z^2 + \\cdots) = \\frac{1}{z} - \\frac{a_2}{2}z + \\cdots$$\n\nSo $d_1 = -a_2/2$.\n\n**Step 3:** Apply part (c) to $1/g(z)$. The function $g$ satisfies the hypotheses of the Koebe theorem (injective, $g(0) = 0$, $g'(0) = 1$), so $1/g$ has the form $1/z + d_0 + d_1 z + \\cdots$ with $d_0 = 0$ and is injective on $\\mathbb{D} \\setminus \\{0\\}$ (actually on $0 < |z| < 1$, since $g$ maps $\\mathbb{D}$ injectively and $g(0) = 0$, so $1/g$ is injective on $\\mathbb{D} \\setminus \\{0\\}$).\n\nWait, actually $1/g$ is defined and injective on $\\mathbb{D} \\setminus \\{0\\}$ since $g$ is injective on $\\mathbb{D}$ and $g(0) = 0$.\n\nBut we need $1/g$ to be injective on $0 < |z| < 1$. Since $g$ is injective on $\\mathbb{D}$ and $g(z) \\neq 0$ for $z \\neq 0$ (because $g$ is injective and $g(0) = 0$), $1/g$ is indeed injective on $\\mathbb{D} \\setminus \\{0\\}$.\n\nBy part (c) applied to $h(z) = 1/g(z) = 1/z + d_1 z + \\cdots$ (with $c_0 = d_0 = 0$, $c_1 = d_1$, etc.):\n\n$$\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$$\n\nIn particular, $1 \\cdot |d_1|^2 \\leq 1$, so $|d_1| \\leq 1$.\n\nSince $d_1 = -a_2/2$, we get $|a_2|/2 \\leq 1$, i.e., $|a_2| \\leq 2$.\n\n**Equality case:** $|a_2| = 2$ iff $|d_1| = 1$ iff equality holds in part (c).\n\nEquality in the area theorem (part c) means that $\\sum_{n=1}^{\\infty} n|c_n|^2 = 1$ with all the constraint concentrated on $n=1$ (since $|c_1| = 1$ already uses up the full budget). So $c_n = 0$ for all $n \\geq 2$, meaning $1/g(z) = 1/z + e^{i\\theta} z$ for some $\\theta$.\n\nThen $g(z) = \\frac{z}{1 + e^{i\\theta} z^2}$, and:\n$$f(z^2) = g(z)^2 = \\frac{z^2}{(1 + e^{i\\theta} z^2)^2}$$\n\nSetting $w = z^2$: $f(w) = \\frac{w}{(1 + e^{i\\theta} w)^2}$.\n\nSo $f(z) = \\frac{z}{(1 + e^{i\\theta} z)^2}$.\n\n## Part (f)\n\nLet $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ be injective on $\\mathbb{D}$ (actually on $0 < |z| < 1$, but let's say it extends to be injective on $\\mathbb{D} \\setminus \\{0\\}$) and avoids values $z_1$ and $z_2$.\n\nConsider $\\phi_j(z) = \\frac{1}{h(z) - z_j}$ for $j = 1, 2$.\n\nSince $h$ avoids $z_j$, $h(z) - z_j \\neq 0$ for all $z \\in \\mathbb{D} \\setminus \\{0\\}$. Also, $h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + \\cdots$ has a simple pole at 0.\n\nSo $\\phi_j(z)$ is holomorphic and nonzero on $\\mathbb{D} \\setminus \\{0\\}$, with a simple zero at 0 (since $h(z) - z_j \\sim 1/z$ near 0, so $\\phi_j(z) \\sim z$ near 0).\n\nWait, let me reconsider. $h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + \\cdots$. Near $z = 0$, $h(z) - z_j \\approx 1/z$, so $\\phi_j(z) = 1/(h(z) - z_j) \\approx z$ near 0.\n\nSo $\\phi_j$ has a removable singularity at 0 with $\\phi_j(0) = 0$, and $\\phi_j'(0) = 1$.\n\nIs $\\phi_j$ injective? If $\\phi_j(z_1) = \\phi_j(z_2)$, then $h(z_1) - z_j = h(z_2) - z_j$, so $h(z_1) = h(z_2)$. Since $h$ is injective, $z_1 = z_2$. Yes, $\\phi_j$ is injective.\n\nSo $\\phi_j$ satisfies the hypotheses of the theorem (injective, $\\phi_j(0) = 0$, $\\phi_j'(0) = 1$).\n\nNow, $\\phi_j(z) = \\frac{1}{h(z) - z_j} = \\frac{1}{1/z + (c_0 - z_j) + c_1 z + \\cdots} = \\frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \\cdots}$\n\nSo $\\phi_j(z) = z \\cdot \\frac{1}{1 + (c_0 - z_j)z + c_1 z^2 + \\cdots} = z(1 - (c_0 - z_j)z + \\cdots) = z - (c_0 - z_j)z^2 + \\cdots$\n\nSo $\\phi_j(z) = z + (\\text{something})z^2 + \\cdots$\n\nThe coefficient of $z^2$ in $\\phi_j$ is $-(c_0 - z_j) = z_j - c_0$.\n\nBy part (e), $|\\text{coefficient of } z^2| \\leq 2$, so $|z_j - c_0| \\leq 2$ for each $j$.\n\nTherefore: $|z_1 - z_2| = |(z_1 - c_0) - (z_2 - c_0)| \\leq |z_1 - c_0| + |z_2 - c_0| \\leq 2 + 2 = 4$.\n\n## Part (g)\n\nLet $f : \\mathbb{D} \\to \\mathbb{C}$ be injective with $f(0) = 0$ and $f'(0) = 1$. We want to show $D_{1/4}(0) \\subseteq f(\\mathbb{D})$.\n\n**Proof by contradiction:** Suppose there exists $w$ with $|w| < 1/4$ such that $w \\notin f(\\mathbb{D})$.\n\nSince $f$ is injective and $f(0) = 0$, we have $f(z) \\neq 0$ for all $z \\neq 0$ in $\\mathbb{D}$. So $0 \\notin f(\\mathbb{D} \\setminus \\{0\\})$.\n\nConsider $h(z) = 1/f(z)$, defined on $\\mathbb{D} \\setminus \\{0\\}$. \n\n- $h$ has a simple pole at 0 (since $f$ has a simple zero at 0).\n- $h$ is injective on $\\mathbb{D} \\setminus \\{0\\}$ (since $f$ is injective and the map $w \\mapsto 1/w$ is injective on $\\mathbb{C} \\setminus \\{0\\}$).\n- $h$ avoids the value 0 (since $1/f(z) = 0$ has no solution).\n- $h$ avoids the value $1/w$ (since $f$ avoids $w$).\n\nSo $h$ is injective on $0 < |z| < 1$ with Laurent expansion $h(z) = 1/z + c_0 + c_1 z + \\cdots$ and avoids $z_1 = 0$ and $z_2 = 1/w$.\n\nBy part (f): $|z_1 - z_2| \\leq 4$, i.e., $|0 - 1/w| \\leq 4$, i.e., $1/|w| \\leq 4$, i.e., $|w| \\geq 1/4$.\n\nThis contradicts $|w| < 1/4$.\n\nTherefore, $D_{1/",
    "format": "unknown",
    "index": 0
  }
]
```

* * *

## Raw Response (truncated)

```json
{
  "id": "gen-1789197466-Ekte5modxlYNNn44s5Z6",
  "object": "chat.completion",
  "created": 1789197466,
  "model": "inclusionai/ling-3.0-flash-vl:free",
  "provider": "Novita",
  "system_fingerprint": null,
  "service_tier": null,
  "choices": [
    {
      "index": 0,
      "logprobs": null,
      "finish_reason": "length",
      "native_finish_reason": "length",
      "message": {
        "role": "assistant",
        "content": null,
        "refusal": null,
        "reasoning": "Let me work through each part (a) through (g) carefully and completely.\n\n## Part (a)\n\nWe need to show that without further restrictions on $f$ (beyond holomorphicity on $\\mathbb{D}$ and $f(0) = 0$), there is no $r > 0$ such that $D_r(0) \\subseteq f(\\mathbb{D})$ for all such $f$.\n\nThe hint suggests finding $f_n$ with $f_n(0) = 0$ and $1/n \\notin f_n(\\mathbb{D})$.\n\nTake $f_n(z) = z/n$. Then:\n- $f_n(0) = 0$ \u2713\n- $f_n(\\mathbb{D}) = \\{z/n : |z| < 1\\} = D_{1/n}(0)$, the open disk of radius $1/n$ centered at 0.\n- $1/n \\notin D_{1/n}(0)$ since $|1/n| = 1/n$ and the disk is open (points have modulus strictly less than $1/n$).\n\nSo $1/n \\notin f_n(\\mathbb{D})$.\n\n$f_n'(0) = 1/n \\to 0$ as $n \\to \\infty$.\n\nFor any $r > 0$, choose $n$ large enough so that $1/n < r$. Then $1/n \\in D_r(0)$ but $1/n \\notin f_n(\\mathbb{D})$, so $D_r(0) \\not\\subseteq f_n(\\mathbb{D})$.\n\n## Part (b)\n\nNow assume $f'(0) = 1$. Consider $f_\\epsilon(z) = \\epsilon(e^{z/\\epsilon} - 1)$ for $\\epsilon > 0$.\n\n- $f_\\epsilon(0) = \\epsilon(e^0 - 1) = 0$ \u2713\n- $f_\\epsilon'(z) = \\epsilon \\cdot (1/\\epsilon) e^{z/\\epsilon} = e^{z/\\epsilon}$, so $f_\\epsilon'(0) = 1$ \u2713\n- $f_\\epsilon$ is holomorphic on all of $\\mathbb{C}$, hence on $\\mathbb{D}$.\n\nThe image: $f_\\epsilon(z) = \\epsilon(e^{z/\\epsilon} - 1)$. Since $e^{z/\\epsilon} \\neq 0$ for all $z \\in \\mathbb{C}$, we have $f_\\epsilon(z) \\neq \\epsilon(0 - 1) = -\\epsilon$.\n\nSo $-\\epsilon \\notin f_\\epsilon(\\mathbb{D})$.\n\nFor any $r > 0$, choose $\\epsilon < r$. Then $|-\\epsilon| = \\epsilon < r$, so $-\\epsilon \\in D_r(0)$, but $-\\epsilon \\notin f_\\epsilon(\\mathbb{D})$. Hence $D_r(0) \\not\\subseteq f_\\epsilon(\\mathbb{D})$.\n\n## Part (c)\n\nLet $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ be analytic and injective for $0 < |z| < 1$.\n\nWe need to show $\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$.\n\n**Proof using the area theorem:**\n\nFor $0 < \\rho < 1$, consider the image of the annulus $\\rho < |z| < 1$ under $h$. Actually, let's consider $h$ on the circle $|z| = \\rho$.\n\nThe boundary of $h(\\{|z| = \\rho\\})$ is the curve $h(\\rho e^{i\\theta})$ for $\\theta \\in [0, 2\\pi)$. Since $h$ is injective on the punctured disk, this curve is a Jordan curve enclosing a region.\n\nThe area enclosed by the image of $|z| = \\rho$ under $h$ can be computed as:\n\n$$A(\\rho) = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) \\, dz$$\n\nLet $z = \\rho e^{i\\theta}$, so $dz = i\\rho e^{i\\theta} d\\theta$.\n\n$h(z) = z^{-1} + c_0 + c_1 z + c_2 z^2 + \\cdots$\n$h'(z) = -z^{-2} + c_1 + 2c_2 z + 3c_3 z^2 + \\cdots$\n\n$\\overline{h(z)} = \\bar{z}^{-1} + \\bar{c}_0 + \\bar{c}_1 \\bar{z} + \\bar{c}_2 \\bar{z}^2 + \\cdots$\n\nOn $|z| = \\rho$: $\\bar{z} = \\rho^2/z$, so $\\bar{z}^{-1} = z/\\rho^2$ and $\\bar{z}^k = \\rho^{2k}/z^k$.\n\n$$\\overline{h(z)} = \\frac{z}{\\rho^2} + \\bar{c}_0 + \\frac{\\bar{c}_1 \\rho^2}{z} + \\frac{\\bar{c}_2 \\rho^4}{z^2} + \\cdots$$\n\nNow:\n$$\\overline{h(z)} h'(z) = \\left(\\frac{z}{\\rho^2} + \\bar{c}_0 + \\frac{\\bar{c}_1 \\rho^2}{z} + \\frac{\\bar{c}_2 \\rho^4}{z^2} + \\cdots\\right)\\left(-\\frac{1}{z^2} + c_1 + 2c_2 z + 3c_3 z^2 + \\cdots\\right)$$\n\nThe area formula gives:\n$$A(\\rho) = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) \\, dz$$\n\nWe need the coefficient of $z^{-1}$ in $\\overline{h(z)} h'(z)$ (since $\\oint z^{-1} dz = 2\\pi i$, and the area is $\\pi$ times the coefficient of $z^{-1}$... let me be more careful).\n\nActually, the area enclosed is:\n$$A(\\rho) = \\frac{1}{2i} \\oint \\bar{h} h' dz = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{h(\\rho e^{i\\theta})} h'(\\rho e^{i\\theta}) i\\rho e^{i\\theta} d\\theta$$\n\nLet me use the standard result. The area of the region bounded by the curve $w = h(\\rho e^{i\\theta})$ is:\n\n$$A(\\rho) = \\pi \\left(\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right)$$\n\nWait, let me derive this more carefully.\n\nThe area of the complement of $h(D_\\rho(0) \\setminus \\{0\\})$ \u2014 actually, let me think about what area we're computing.\n\nFor the standard area theorem: Consider $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ injective on $0 < |z| < 1$.\n\nThe image of the circle $|z| = \\rho$ (for $0 < \\rho < 1$) is a Jordan curve. The area of the region enclosed by this curve (counted with multiplicity) is:\n\n$$A(\\rho) = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) dz$$\n\nLet me compute this. With $z = \\rho e^{i\\theta}$:\n\n$h(z) = z^{-1} + \\sum_{n=0}^{\\infty} c_n z^n$\n$h'(z) = -z^{-2} + \\sum_{n=1}^{\\infty} n c_n z^{n-1}$\n\n$\\overline{h(z)} = \\bar{z}^{-1} + \\sum_{n=0}^{\\infty} \\bar{c}_n \\bar{z}^n = \\frac{z}{\\rho^2} + \\sum_{n=0}^{\\infty} \\bar{c}_n \\frac{\\rho^{2n}}{z^n}$\n\n(using $\\bar{z} = \\rho^2/z$ on $|z| = \\rho$)\n\nSo:\n$$\\overline{h(z)} h'(z) = \\left(\\frac{z}{\\rho^2} + \\sum_{m=0}^{\\infty} \\bar{c}_m \\frac{\\rho^{2m}}{z^m}\\right)\\left(-\\frac{1}{z^2} + \\sum_{k=1}^{\\infty} k c_k z^{k-1}\\right)$$\n\nThe area is:\n$$A(\\rho) = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) dz = \\pi \\cdot [\\text{coefficient of } z^{-1} \\text{ in } \\overline{h(z)} h'(z)]$$\n\nWait, $\\frac{1}{2i} \\oint z^n dz = \\frac{1}{2i} \\cdot 2\\pi i \\cdot \\delta_{n,-1} = \\pi \\delta_{n,-1}$.\n\nSo $A(\\rho) = \\pi \\cdot [\\text{coefficient of } z^{-1} \\text{ in } \\overline{h(z)} h'(z)]$.\n\nLet me find the coefficient of $z^{-1}$ in $\\overline{h(z)} h'(z)$.\n\nFrom $\\frac{z}{\\rho^2} \\cdot (- \\frac{1}{z^2})$: this gives $-\\frac{1}{\\rho^2} z^{-1}$. Coefficient: $-1/\\rho^2$.\n\nFrom $\\frac{z}{\\rho^2} \\cdot kc_k z^{k-1}$: this gives $\\frac{k c_k}{\\rho^2} z^k$. For $z^{-1}$ we need $k = -1$, impossible. So no contribution.\n\nFrom $\\bar{c}_m \\frac{\\rho^{2m}}{z^m} \\cdot (-\\frac{1}{z^2})$: this gives $-\\bar{c}_m \\rho^{2m} z^{-(m+2)}$. For $z^{-1}$ we need $m+2 = 1$, i.e., $m = -1$. Impossible since $m \\geq 0$.\n\nFrom $\\bar{c}_m \\frac{\\rho^{2m}}{z^m} \\cdot k c_k z^{k-1}$: this gives $k \\bar{c}_m c_k \\rho^{2m} z^{k-1-m}$. For $z^{-1}$ we need $k - 1 - m = -1$, i.e., $k = m$. Since $k \\geq 1$ and $m \\geq 0$, we need $m = k \\geq 1$.\n\nSo the contribution is $\\sum_{k=1}^{\\infty} k |c_k|^2 \\rho^{2k}$.\n\nTherefore:\n$$A(\\rho) = \\pi\\left(-\\frac{1}{\\rho^2} + \\sum_{k=1}^{\\infty} k|c_k|^2 \\rho^{2k}\\right)$$\n\nHmm, but this should be the area enclosed, which should be positive. Let me reconsider.\n\nActually, the issue is the orientation. For $h(z) = 1/z + \\cdots$, as $z$ traverses $|z| = \\rho$ counterclockwise, $h(z)$ traverses its image... let me think about the winding.\n\nActually, the standard area theorem states that the area of the complement of the image domain (i.e., the area outside the image of the annulus) is:\n\n$$\\text{Area}(\\mathbb{C} \\setminus h(\\{|z| < \\rho\\} \\setminus \\{0\\})) = \\pi\\left(\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right)$$\n\nAnd this must be $\\geq 0$, which gives $\\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\leq \\frac{1}{\\rho^2}$.\n\nWait, but the problem says to compute the area of the complement of $h(D_\\rho(0) \\setminus \\{0\\})$ and let $\\rho \\to 1$.\n\nActually, let me reconsider. The complement of $h(D_\\rho(0) \\setminus \\{0\\})$ \u2014 this is the set of points not in the image of the punctured disk of radius $\\rho$. Since $h$ maps the annulus $\\rho < |z| < 1$ injectively to some domain, and also maps $|z| < \\rho$ (p
```
