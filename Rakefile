task :env do
  system "direnv allow ."
end

task :generate do
  base_url = ENV["HUGO_BASE_URL"]
  system "gulp && hugo --baseUrl='#{base_url}'"
end

task :deploy do
  program = ENV["RSYNC_PROGRAM"]
  port = ENV["RSYNC_DEST_PORT"]
  user = ENV["RSYNC_USER"]
  host = ENV["RSYNC_HOST"]
  dest = ENV["RSYNC_DEST"]
  system "rsync --exclude=\".well-known\" --rsync-path=\"#{program}\" public/ -avz -e \"ssh -p #{port}\" --delete #{user}@#{host}:#{dest}"
end

task default: [ :env, :generate, :deploy ]
