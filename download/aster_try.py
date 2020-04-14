import landsatxplore.api

# Initialize a new API instance and get an access key
api = landsatxplore.api.API('student_boku', 'boku_vfegis_2019')

# Request
scenes = api.search(
    dataset='ASTER_L1T',
    latitude=46.982292,
    longitude=-101.53849,
    start_date='2010-01-01',
    end_date='2019-01-01',
    max_cloud_cover=10)

print('{} scenes found.'.format(len(scenes)))

for scene in scenes:
    print(scene['acquisitionDate'])

api.logout()