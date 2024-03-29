local v, b, bands = ...

local br = b / bands
if v < 0 then
  return '0,0,0,0'
elseif br < 0.5 then
  -- 255,  0,  0,... @ br = 0.167
  -- 255,255,  0,... @ br = 0.333
  --   0,255,  0,... @ br = 0.5
  return ((br - 0.5) * -1530)..','..((br - 0.167) * 1530)..',0,'..(v^3 * 255)
else
  --   0,255,255,... @ br = 0.667
  --   0,  0,255,... @ br = 0.833
  -- 255,  0,255,... @ br = 1
  return ((br - 0.833) * 1530)..','..((br - 0.667) * -1530)..','..((br - 0.5) * 1530)..','..(v^3 * 255)
end
