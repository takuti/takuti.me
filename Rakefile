desc "Generate public/ as production content (specifying baseUrl), and sync them to the remote server"
task :deploy do
  system "direnv allow ."

  base_url = ENV["HUGO_BASE_URL"]
  system "gulp && hugo --baseUrl='#{base_url}'"

  program = ENV["RSYNC_PROGRAM"]
  port = ENV["RSYNC_DEST_PORT"]
  user = ENV["RSYNC_USER"]
  host = ENV["RSYNC_HOST"]
  dest = ENV["RSYNC_DEST"]
  system "rsync --rsync-path=\"#{program}\" public/ -avz -e \"ssh -p #{port}\" --delete #{user}@#{host}:#{dest}"
end

task default: :deploy