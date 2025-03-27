# Simple Capture
### Dificulty: Simple

```
FROM: SecurityAdmin@Allsafe.com
TO: IncidentResponse@Allsafe.com

MESSAGE:

I hope you're having a good day. We've got some news regarding the latest breach of our client's company, "EvilCorp." As you may be aware, a group calling themselves "TheBringesOfJustice" struck their systems, and as part of our investigation, we're trying to figure out how much data they stole.

It was brought to our attention by one of our best cryptographers that the system they utilized was called `Asem.rb`, a form of rather primitive asymmetrical encryption, originally made by a researcher calling themselves "M1tsuStr1k3r." We believe that you may have some luck analyzing the provided captures/logs and help us understand the range of the attack.

Consider taking a look at the attachments provided by our cryptographers, as we believe they might be useful.

Thank you, and the best of lucks.
- AllSafe : Security Admin

```


## Asem.rb
```ruby
require("openssl")
class Asem
  def self.e(msg, k, p: false)
    k, p_ = k.split(":").map(&:to_i)
    b = msg.bytes
    c = b.map { |x| x * k % p_ } 
    d = c.pack("Q*").force_encoding("UTF-8")
    d = d.unpack1("H*") if p
    d
  end

  def self.d(msg, k, p: false)
    k, p_ = k.split(":").map(&:to_i)
    f = p ? [msg].pack("H*").unpack("Q*") : msg.unpack("Q*")
    i = g(OpenSSL::BN.new(2).mod_exp(k, OpenSSL::BN.new(p_)).to_i, p_)
    r = f.map { |x| x * i % p_ }
    r.pack("C*")
  end

  def self.g(a, m)
    m0, x0, x1 = m, 0, 1
    return 0 if m == 1
    while a > 1
      q = a / m
      m, a = a % m, m
      x0, x1 = x1 - q * x0, x0
    end
    x1 += m0 if x1.negative?
    x1
  end
end
```

## Key exchange
```
# Structure
000.000.000.00 -- hex-payload -- 000.000.000.00
[---SENDER---] 00ff00ff00ff00ff [---RECIEVER---]
```
[Capture file](files/keyexchange.log)
