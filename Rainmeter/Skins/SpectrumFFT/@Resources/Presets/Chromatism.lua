local v = ...

if v < 0 then
  return '0,0,0,0'
elseif v < 0.6 then
  --   0,127,255 @ 0.2
  --   0,255,255 @ 0.4
  -- 255,255,255 @ 0.6
  return ((v - 0.4) * 1275)..','..(v * 638)..','..(v * 1275)..','..(v * 1275)
else
  -- 255,255,  0 @ 0.6
  -- 255,  0,  0 @ 0.9
  return '255,'..((v - 0.9) * -850)..',0'
end