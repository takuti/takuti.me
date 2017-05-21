task :generate do
  system "gulp && hugo"
end

task :publish do
  system "cd public && git add . && git cm -m 'Update' && git push origin master"
end

task default: [ :generate ]
