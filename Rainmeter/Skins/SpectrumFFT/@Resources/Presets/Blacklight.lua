local v = ...

if v < 0 then
  return '0,0,0,0'
else
  --   0,  0,255 @ 0.5
  -- 150, 42,255 @ 1
  return ((v - 0.5) * 300)..','..((v - 0.5) * 84)..','..(v * 510)..','..(v * 510)
end
