
##

import pandas as pd
from githubdata import GithubData

repo_url = 'https://github.com/imahdimir/d-Ticker-2-BaseTicker-map'
btic_repo_url = 'https://github.com/imahdimir/d-uniq-BaseTickers'

btic = 'BaseTicker'
tick = 'Ticker'

def main() :


  pass

  ##
  map_repo = GithubData(repo_url)
  map_repo.clone_overwrite_last_version()
  ##
  fpn = map_repo.data_fps[0]
  df = pd.read_parquet(fpn)
  df = df.reset_index()
  ##
  df = df[[tick, btic]]
  ##
  df = df.drop_duplicates()
  ##
  df = df.sort_values([btic, tick])
  ##

  btic_repo = GithubData(btic_repo_url)
  btic_repo.clone_overwrite_last_version()
  ##
  bdfpn = btic_repo.data_fps[0]
  bdf = pd.read_parquet(bdfpn)
  bdf = bdf.reset_index()
  ##
  assert df[btic].isin(bdf[btic]).all(), 'some basetickers are not in ref basetickers data'
  ##

  df = df.set_index(tick)
  ##
  df.to_parquet(fpn)
  ##
  commit_msg = 'gov'
  map_repo.commit_and_push_to_github_data_target(commit_msg)
  ##

  btic_repo.rmdir()
  map_repo.rmdir()

  ##


  ##


##
# noinspection PyUnreachableCode
if False :

  pass

  ##


  ##

##